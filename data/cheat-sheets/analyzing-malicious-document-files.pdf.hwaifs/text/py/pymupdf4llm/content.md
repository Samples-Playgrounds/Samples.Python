# **ANALYZING MALICIOUS DOCUMENTS**

This cheat sheet outlines tips and tools for analyzing
malicious documents, such as Microsoft Office, RTF,
and PDF files.


**General Approach to Document Analysis**


1. Examine the document for anomalies, such as

risky tags, scripts, and embedded artifacts.


2. Locate embedded code, such as shellcode,

macros, JavaScript, or other suspicious objects.


3. Extract suspicious code or objects from the file.


4. If relevant, deobfuscate and examine macros,

JavaScript, or other embedded code.


5. If relevant, emulate, disassemble and/or debug

shellcode that you extracted from the document.


6. Understand the next steps in the infection chain.


**Microsoft Office Format Notes**
Binary Microsoft Office document files (.doc, .xls,
etc.) use the OLE2 (a.k.a. Structured Storage) format.


SRP streams in OLE2 documents sometimes store a
[cached version of earlier VBA macro code.](https://www.sans.org/blog/srp-streams-in-ms-office-documents-reveal-earlier-versions-of-malicious-macros/)


OOXML document files (.docx, .xlsm, etc.) supported
by Microsoft Office are compressed zip archives.


VBA macros in OOXML documents are stored inside
an OLE2 binary file, which is within the zip archive.


Excel supports XLM macros that are embedded as
formulas in sheets without the OLE2 binary file.
RTF documents don’t support macros but can contain
malicious embedded files and objects.
**Useful MS Office File Analysis Commands**



/XObject can embed an image for phishing.


Be mindful of obfuscation with hex codes, such as
[/JavaScript vs. /J#61vaScript. (See examples.)](https://blog.didierstevens.com/2008/04/29/pdf-let-me-count-the-ways/)
**Useful PDF File Analysis Commands**


```
oledump.py
file.xls -i

oledump.py
file.xls -s 3 -v

```


List all OLE2 streams present
in _file.xls_ .


Extract VBA source code
from stream _3_ in _file.xls_ .



`[xmldump.py pretty](https://blog.didierstevens.com/2018/01/15/update-xmldump-py-version-0-0-2/)` Format XML file supplied via
STDIN for easier analysis.



Display risky keywords present in
file _file.pdf_ .


Show stats about keywords. Add
“-O” to include object streams.


Display contents of object _id_ . Add
“ `-d` ” to dump object’s stream.


Display objects that
reference object _id_ .


```
oledump.py file.xls -p
plugin_http_heuristics

```


Find obfuscated URLs
in _file.xls_ macros.


```
pdfid.py
file.pdf -n

pdf-parser.py
file.pdf -a

pdf-parser.py
file.pdf -o id

pdf-parser.py
file.pdf -r id

```

```
vmonkey
file.doc

evilclippy -uu
file.ppt

```


Emulate the execution of macros
in file.doc to analyze them.


Remove the password prompt
from macros in _file.ppt_ .


```
msoffcrypto-tool

infile.docm
outfile.docm -p

pcodedmp
file.doc

pcode2code
file.doc

rtfobj.py
file.rtf

rtfdump.py
file.rtf

rtfdump.py
file.rtf -O

```


Decrypt _outfile.docm_ using
specified password to create
_outfile.docm_ .


Disassemble VBA-stomped
p-code macro from _file.doc_ .


Decompile VBA-stomped
p-code macro from _file.doc_ .


Extract objects embedded
into RTF _file.rtf_ .


List groups and structure of
RTF file _file.rtf_ .


Examine objects in RTF file
_file.rtf_ .


```
qpdf --password=pass
--decrypt infile.pdf
outfile.pdf

```


Decrypt _infile.pdf_ using
password _pass_ to create
_outfile.pdf_ .



**Shellcode and Other Analysis Commands**


```
xorsearch -W
-d 3 file.bin

```


Locate shellcode patterns inside
the binary file _file.bin_ .


```
scdbgc /f
file.bin

runsc32 -f
file.bin -n

```


Emulate execution of shellcode in
_file.bin_ . Use “ `/off` ” to specify offset.


Execute shellcode in _file.bin_ to
observe behavior in an isolated lab.



List Base64-encoded strings
present in file _file.txt_ .


Convert numbers that represent
characters in _file_ to a string.



**Additional Document Analysis Tools**

[SpiderMonkey, cscript, and box-js help deobfuscate](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey)
JavaScript that you extract from document files.


Use the debugger built into Microsoft Office to
deobfuscate macros in an isolated lab.


[Use AMSIScriptContentRetrieval.ps1 to observe](https://gist.githubusercontent.com/mattifestation/e179218d88b5f100b0edecdec453d9be/raw/2329bda456b5b8e2f973cc5dc026b6fc221dad79/AMSIScriptContentRetrieval.ps1)
Microsoft Office execute macros in an isolated lab.


[Some automated analysis sandboxes can analyze](https://zeltser.com/automated-malware-analysis/)
aspects of malicious document files.


[REMnux distro includes many of the free document](https://remnux.org/)
analysis tools mentioned above.


```
base64dump.py
file.txt

numbers-tostring.py file

```

```
rtfdump.py file.rtf
-s 5 -H -d

xlmdeobfuscator
--file file.xlsm

```


Extract hex contents from
group in RTF file _file.rtf_ .


Deobfuscate XLM (Excel 4)
macros in _file.xlsm_ .



**Risky PDF Keywords**
/OpenAction and /AA specify the script or action to
run automatically.


/JavaScript, /JS, /AcroForm, and /XFA can specify
JavaScript to run.


/URI accesses a URL, perhaps for phishing.


/SubmitForm and /GoToR can send data to URL.


/ObjStm can hide objects inside an object stream.


```
zipdump.py
file.pptx

zipdump.py
file.pptx -s 3 -d

```


Examine contents of OOXML
file _file.pptx_ .


Extract file with index _3_ from
_file.pptx_ to STDOUT.



`[olevba](https://github.com/decalage2/oletools/wiki/olevba)` _`file.xlsm`_ Locate and extract macros
from _file.xlsm_ .



Authored by Lenny Zeltser with feedback from Pedro Bueno and Didier Stevens. Malicious document analysis and related topics are covered in the SANS Institute course
FOR610: Reverse-Engineering Malware, which Lenny co-authored. Creative Commons v3 “Attribution” License for this cheat sheet version 4.1. More at zeltser.com/cheat-sheets.


