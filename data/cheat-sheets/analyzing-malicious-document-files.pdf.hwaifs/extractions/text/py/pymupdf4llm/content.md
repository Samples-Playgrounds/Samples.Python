## **ANALYZING MALICIOUS DOCUMENTS** 

This cheat sheet outlines tips and tools for analyzing malicious documents, such as Microsoft Office, RTF, and PDF files. 

## **General Approach to Document Analysis** 

1. Examine the document for anomalies, such as risky tags, scripts, and embedded artifacts. 

2. Locate embedded code, such as shellcode, macros, JavaScript, or other suspicious objects. 

3. Extract suspicious code or objects from the file. 

4. If relevant, deobfuscate and examine macros, JavaScript, or other embedded code. 

5. If relevant, emulate, disassemble and/or debug shellcode that you extracted from the document. 

6. Understand the next steps in the infection chain. 

## **Microsoft Office Format Notes** 

Binary Microsoft Office document files (.doc, .xls, etc.) use the OLE2 (a.k.a. Structured Storage) format. SRP streams in OLE2 documents sometimes store a cached version of earlier VBA macro code. 

OOXML document files (.docx, .xlsm, etc.) supported by Microsoft Office are compressed zip archives. 

VBA macros in OOXML documents are stored inside an OLE2 binary file, which is within the zip archive. 

Excel supports XLM macros that are embedded as formulas in sheets without the OLE2 binary file. 

RTF documents don’t support macros but can contain malicious embedded files and objects. 

## **Useful MS Office File Analysis Commands** 

|`zipdump.py`|Examine contents of OOXML|
|---|---|
|_`file.pptx`_<br>`zipdump.py`|file_file.pptx_.<br>Extract file with index_3_from|
|_`file.pptx -s 3 -d`_<br>`olevba`_`file.xlsm`_|_file.pptx_to STDOUT.<br>Locate and extract macros|
||from_file.xlsm_.|



List all OLE2 streams present in _file.xls_ . 

## `oledump.py` 

```
file.xls -i
```

Extract VBA source code from stream _3_ in _file.xls_ . 

```
oledump.py
file.xls -s 3 -v
```

`xmldump.py pretty` Format XML file supplied via STDIN for easier analysis. 

`oledump.py` _`file.xls`_ `-p` Find obfuscated URLs `plugin_http_heuristics` in _file.xls_ macros. 

`vmonkey` Emulate the execution of macros _`file.doc`_ in file.doc to analyze them. 

Remove the password prompt from macros in _file.ppt_ . 

```
evilclippy -uu
file.ppt
```

Decrypt _outfile.docm_ using specified password to create _outfile.docm_ . 

`msoffcrypto-tool` Decrypt _outfile.docm_ using _`infile.docm`_ specified password to create _`outfile.docm -p` outfile.docm_ . `pcodedmp` Disassemble VBA-stomped _`file.doc`_ p-code macro from _file.doc_ . 

Decompile VBA-stomped p-code macro from _file.doc_ . Extract objects embedded into RTF _file.rtf_ . 

```
pcode2code
file.doc
```

`rtfobj.py` Extract objects embedded _`file.rtf`_ into RTF _file.rtf_ . `rtfdump.py` List groups and structure of _`file.rtf`_ RTF file _file.rtf_ . `rtfdump.py` Examine objects in RTF file _`file.rtf`_ `-O` _file.rtf_ . 

Examine objects in RTF file _file.rtf_ . 

`rtfdump.py` _`file.rtf`_ Extract hex contents from `-s` _`5`_ `-H -d` group in RTF file _file.rtf_ . `xlmdeobfuscator` Deobfuscate XLM (Excel 4) `--file` _`file.xlsm`_ macros in _file.xlsm_ . 

## **Risky PDF Keywords** 

/OpenAction and /AA specify the script or action to run automatically. 

/JavaScript, /JS, /AcroForm, and /XFA can specify JavaScript to run. 

/URI accesses a URL, perhaps for phishing. 

/SubmitForm and /GoToR can send data to URL. /ObjStm can hide objects inside an object stream. 

/XObject can embed an image for phishing. 

Be mindful of obfuscation with hex codes, such as /JavaScript vs. /J#61vaScript. (See examples.) 

## **Useful PDF File Analysis Commands** 

`pdfid.py` Display risky keywords present in _`file.pdf`_ `-n` file _file.pdf_ . `- pdf parser.py` Show stats about keywords. Add _`file.pdf`_ `-a` “-O” to include object streams. `pdf-parser.py` Display contents of object _id_ . Add _`file.pdf`_ `-o` _`id`_ “ `-d` ” to dump object’s stream. `pdf-parser.py` Display objects that _`file.pdf`_ `-r` _`id`_ reference object _id_ . _`qpdf --password=pass`_ Decrypt _infile.pdf_ using _`--decrypt infile.pdf`_ password _pass_ to create _`outfile.pdf` outfile.pdf_ . **Shellcode and Other Analysis Commands** `xorsearch -W` Locate shellcode patterns inside `-d 3` _`file.bin`_ the binary file _file.bin_ . `scdbgc /f` Emulate execution of shellcode in _`file.bin` file.bin_ . Use “ `/off` ” to specify offset. `runsc32 -f` Execute shellcode in _file.bin_ to _`file.bin`_ `-n` observe behavior in an isolated lab. `base64dump.py` List Base64-encoded strings _`file.txt`_ present in file _file.txt_ . `numbers-to-` Convert numbers that represent `string.py` _`file`_ characters in _file_ to a string. 

## **Shellcode and Other Analysis Commands** 

## **Additional Document Analysis Tools** 

SpiderMonkey, cscript, and box-js help deobfuscate JavaScript that you extract from document files. 

Use the debugger built into Microsoft Office to deobfuscate macros in an isolated lab. 

Use AMSIScriptContentRetrieval.ps1 to observe Microsoft Office execute macros in an isolated lab. 

Some automated analysis sandboxes can analyze aspects of malicious document files. 

REMnux distro includes many of the free document analysis tools mentioned above. 

Authored by Lenny Zeltser with feedback from Pedro Bueno and Didier Stevens. Malicious document analysis and related topics are covered in the SANS Institute course FOR610: Reverse-Engineering Malware, which Lenny co-authored. Creative Commons v3 “Attribution” License for this cheat sheet version 4.1. More at zeltser.com/cheat-sheets. 

