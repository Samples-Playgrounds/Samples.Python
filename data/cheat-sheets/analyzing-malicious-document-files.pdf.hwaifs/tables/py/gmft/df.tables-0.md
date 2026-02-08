|    | and    | PDF files.                                    |                                                         | file.xls                                  |
|---:|:-------|:----------------------------------------------|:--------------------------------------------------------|:------------------------------------------|
|  0 | nan    | General Approach                              | to Document Analysis                                    | xmldump.py                                |
|  1 | 1.     | Examine the document risky tags, scripts,     | for anomalies, such as and embedded artifacts.          | oledump.py                                |
|  2 | 2.     | Locate embedded macros, JavaScript,           | code, such as shellcode, or other suspicious objects.   | plugin_http_heuristics vmonkey            |
|  3 | 3.     | Extract suspicious                            | code or objects from the file.                          | file.doc                                  |
|  4 | 4.     | If relevant, deobfuscate JavaScript, or other | and examine macros, embedded code.                      | evilclippy file.ppt                       |
|  5 | 5.     | If relevant, emulate, shellcode that you      | disassemble and/or debug extracted from the document.   | msoffcrypto-tool infile.docm outfile.docm |
|  6 | 6.     | Understand the                                | next steps in the infection chain.                      | pcodedmp                                  |
|  7 | nan    | Microsoft Office                              | Format Notes                                            | file.doc                                  |
|  8 | etc.)  | Binary Microsoft Office use the OLE2 (a.k.a.  | document files (.doc, .xls, Structured Storage) format. | pcode2code file.doc                       |
|  9 | SRP    | streams in OLE2 cached version of earlier     | documents sometimes store a VBA macro code.             | rtfobj.py file.rtf                        |
| 10 | by     | OOXML document files Microsoft Office are     | (.docx, .xlsm, etc.) supported compressed zip archives. | rtfdump.py file.rtf                       |
| 11 | VBA an | macros in OOXML OLE2 binary file, which       | documents are stored inside is within the zip archive.  | rtfdump.py file.rtf                       |
| 12 | Excel  | supports XLM formulas in sheets without       | macros that are embedded as the OLE2 binary file.       | rtfdump.py -s 5 -H                        |
| 13 | RTF    | documents don’t malicious embedded            | support macros but can contain files and objects.       | xlmdeobfuscator --file file.xlsm          |
| 14 | nan    | Useful MS Office                              | File Analysis Commands                                  | Risky PDF                                 |
| 15 | nan    | zipdump.py file.pptx                          | Examine contents of OOXML file file.pptx.               | /OpenAction run automatically.            |
| 16 | nan    | zipdump.py file.pptx -s 3 -d                  | Extract file with index 3 from file.pptx to STDOUT.     | /JavaScript, JavaScript to                |
| 17 | nan    | olevba file.xlsm                              | Locate and extract macros                               | /URI accesses                             |
| 18 | nan    | nan                                           | from file.xlsm.                                         | /SubmitForm                               |