# **ANALYZING MALICIOUS DOCUMENTS**

This cheat sheet outlines tips and tools for analyzing malicious documents, such as Microsoft Office, RTF, and PDF files.

## **General Approach to Document Analysis**

- 1. Examine the document for anomalies, such as risky tags, scripts, and embedded artifacts.
- 2. Locate embedded code, such as shellcode, macros, JavaScript, or other suspicious objects.
- 3. Extract suspicious code or objects from the file.
- 4. If relevant, deobfuscate and examine macros, JavaScript, or other embedded code.
- 5. If relevant, emulate, disassemble and/or debug shellcode that you extracted from the document.
- 6. Understand the next steps in the infection chain.

#### **Microsoft Office Format Notes**

Binary Microsoft Office document files (.doc, .xls, etc.) use the OLE2 (a.k.a. Structured Storage) format.

SRP streams in OLE2 documents sometimes store a cached version of [earlier VBA macro code.](https://www.sans.org/blog/srp-streams-in-ms-office-documents-reveal-earlier-versions-of-malicious-macros/)

OOXML document files (.docx, .xlsm, etc.) supported by Microsoft Office are compressed zip archives.

VBA macros in OOXML documents are stored inside an OLE2 binary file, which is within the zip archive.

Excel supports XLM macros that are embedded as formulas in sheets without the OLE2 binary file.

RTF documents don't support macros but can contain malicious embedded files and objects.

### **Useful MS Office File Analysis Commands**

| zipdump.py<br>file.pptx         | Examine<br>contents of OOXML<br>file file.pptx.              |
|---------------------------------|--------------------------------------------------------------|
| zipdump.py<br>file.pptx -s 3 -d | Extract file with index 3<br>from<br>file.pptx<br>to STDOUT. |
| olevba<br>file.xlsm             | Locate and extract macros<br>from file.xlsm.                 |

| List all OLE2 streams present<br>Extract VBA source code<br>in file.xls.<br>Format XML file supplied via<br>STDIN for easier analysis.<br>Find obfuscated URLs<br>macros.<br>Emulate the execution of macros |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                              |
|                                                                                                                                                                                                              |
|                                                                                                                                                                                                              |
|                                                                                                                                                                                                              |
| in file.doc to analyze them.                                                                                                                                                                                 |
| Remove the password prompt<br>from macros in file.ppt.                                                                                                                                                       |
| Decrypt outfile.docm<br>using<br>specified password<br>to create                                                                                                                                             |
| Disassemble VBA-stomped<br>p-code macro from file.doc.                                                                                                                                                       |
| Decompile VBA-stomped<br>p-code macro from file.doc.                                                                                                                                                         |
| Extract objects embedded                                                                                                                                                                                     |
| List groups and structure of                                                                                                                                                                                 |
| Examine objects in RTF file                                                                                                                                                                                  |
| Extract hex contents from<br>group in RTF file file.rtf.                                                                                                                                                     |
| Deobfuscate XLM (Excel 4)<br>macros in file.xlsm.                                                                                                                                                            |
|                                                                                                                                                                                                              |

#### **Risky PDF Keywords**

/OpenAction and /AA specify the script or action to run automatically.

/JavaScript, /JS, /AcroForm, and /XFA can specify JavaScript to run.

/URI accesses a URL, perhaps for phishing.

/SubmitForm and /GoToR can send data to URL.

/ObjStm can hide objects inside an object stream.

/XObject can embed an image for phishing. Be mindful of obfuscation with hex codes, such as /JavaScript vs. /J#61vaScript. [\(See examples.](https://blog.didierstevens.com/2008/04/29/pdf-let-me-count-the-ways/))

## **Useful PDF File Analysis Commands**

| pdfid.py<br>file.pdf<br>-n                                 | Display risky keywords present in<br>file<br>file.pdf.                    |
|------------------------------------------------------------|---------------------------------------------------------------------------|
| pdf-parser.py<br>file.pdf<br>-a                            | Show stats<br>about keywords. Add<br>"-O"<br>to include object streams.   |
| pdf-parser.py<br>file.pdf -o<br>id                         | Display contents of object id. Add<br>"-d" to dump<br>object's stream.    |
| pdf-parser.py<br>file.pdf -r<br>id                         | Display objects that<br>reference object id.                              |
| qpdf<br>password=pass<br>decrypt infile.pdf<br>outfile.pdf | Decrypt infile.pdf<br>using<br>password pass<br>to create<br>outfile.pdf. |

## **Shellcode and Other Analysis Commands**

| xorsearch<br>-W<br>-d 3 file.bin | Locate shellcode patterns inside<br>the binary file file.bin.               |
|----------------------------------|-----------------------------------------------------------------------------|
| scdbgc                           | Emulate execution of shellcode in                                           |
| /f                               | file.bin.                                                                   |
| file.bin                         | Use "/off" to specify offset.                                               |
| runsc32<br>-f<br>file.bin<br>-n  | Execute shellcode in file.bin<br>to<br>observe behavior in an isolated lab. |
| base64dump.py                    | List Base64-encoded strings                                                 |
| file.txt                         | present in file file.txt.                                                   |
| numbers-to                       | Convert numbers that represent                                              |
| string.py                        | characters in file                                                          |
| file                             | to a string.                                                                |

## **Additional Document Analysis Tools**

[SpiderMonkey,](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey) [cscript,](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cscript) and [box-js](https://github.com/CapacitorSet/box-js) help deobfuscate JavaScript that you extract from document files.

Use the debugger built into Microsoft Office to deobfuscate macros in an isolated lab.

Use [AMSIScriptContentRetrieval.ps1](https://gist.githubusercontent.com/mattifestation/e179218d88b5f100b0edecdec453d9be/raw/2329bda456b5b8e2f973cc5dc026b6fc221dad79/AMSIScriptContentRetrieval.ps1) to observe Microsoft Office execute macros in an isolated lab.

Som[e automated analysis](https://zeltser.com/automated-malware-analysis/) sandboxes can analyze aspects of malicious document files.

[REMnux](https://remnux.org/) distro includes many of the free document analysis tools mentioned above.

Authored by Lenny Zeltser with feedback from Pedro Bueno and Didier Stevens. Malicious document analysis and related topics are covered in the SANS Institute course FOR610: Reverse-Engineering Malware, which Lenny co-authored. Creative Commons v3 "Attribution" License for this cheat sheet version 4.1. More at zeltser.com/cheat-sheets.