# vi Editor “Cheat Sheet”



VI “Cheat” Sheet
ACNS Bulletin ED–03
_February 1995_



Invoking vi: vi _filename_
Format of vi commands: _[count][command]_ (count repeats the effect of the command)



~~Command mode versus input mode~~


Vi starts in command mode. The positioning commands
operate only while vi is in command mode. You switch vi
to input mode by entering any one of several vi input commands. (See next section.) Once in input mode, any character you type is taken to be text and is added to the file. You
cannot execute any commands until you exit input mode.
To exit input mode, press the escape ( **`Esc`** ) key.

~~Input commands~~ ~~(end with Esc)~~

a Append after cursor
i Insert before cursor

 - Open line below
O Open line above
:r _file_ Insert _file_ after current line

Any of these commands leaves vi in input mode until you
press **`Esc`** . Pressing the **`RETURN`** key will not take you out
of input mode.

~~Change commands (Input mode)~~

cw Change word (Esc)
cc Change line (Esc) - blanks line
c$ Change to end of line
r _c_ Replace character with _c_
R Replace (Esc) - typeover
s Substitute (Esc) - 1 char with string
S Substitute (Esc) - Rest of line with
text
## . Repeat last change

~~Changes during insert mode~~

<ctrl>h Back one character
<ctrl>w Back one word
<ctrl>u Back to beginning of insert



~~File management commands~~

:w _name_ Write edit buffer to file _name_
:wq Write to file and quit
:q! Quit without saving changes
ZZ Same as :wq
:sh Execute shell commands (<ctrl>d)

~~Window motions~~

<ctrl>d Scroll down (half a screen)
<ctrl>u Scroll up (half a screen)
<ctrl>f Page forward
<ctrl>b Page backward
/string Search forward
?string Search backward
<ctrl>l Redraw screen
<ctrl>g Display current line number and
file information
n Repeat search
N Repeat search reverse
G Go to last line
_n_ G Go to line _n_
: _n_ Go to line _n_
z<CR> Reposition window: cursor at top
z. Reposition window: cursor in middle
z- Reposition window: cursor at bottom

~~Cursor motions~~

H Upper left corner (home)
M Middle line
L Lower left corner
h Back a character
j Down a line
k Up a line
^ Beginning of line
$ End of line
l Forward a character
w One word forward
b Back one word
f _c_ Find _c_
; Repeat find (find next _c_ )


~~Deletion commands~~

dd or _n_ dd Delete _n_ lines to general buffer
dw Delete word to general buffer
d _n_ w Delete _n_ words
d) Delete to end of sentence
db Delete previous word
D Delete to end of line
x Delete character

~~Recovering deletions~~

p Put general buffer after cursor
P Put general buffer before cursor

~~Undo commands~~

u Undo last change
U Undo all changes on line

~~Rearrangement commands~~

yy or Y Yank (copy) line to general buffer
“ _z_ 6yy Yank 6 lines to buffer _z_
yw Yank word to general buffer
“ _a_ 9dd Delete 9 lines to buffer _a_
“ _A_ 9dd Delete 9 lines; Append to buffer _a_
“ _a_ p Put text from buffer _a_ after cursor
p Put general buffer after cursor
P Put general buffer before cursor
J Join lines

~~Parameters~~

:set list Show invisible characters
:set nolist Don’t show invisible characters

:set number Show line numbers
:set nonumber Don’t show line numbers

:set autoindent Indent after carriage return
:set noautoindent Turn off autoindent
:set showmatch Show matching sets of
parentheses as they are typed
:set noshowmatch Turn off showmatch

:set showmode Display mode on last line of screen
:set noshowmode Turn off showmode

:set all Show values of all possible
parameters



~~Move text from file~~ ~~_old_~~ ~~to file~~ ~~_new_~~

vi _old_
“ _a_ 10yy yank 10 lines to buffer _a_
:w write work buffer
:e _new_ edit new file
“ _a_ p put text from _a_ after cursor
:30,60w _new_ Write lines 30 to 60 in file _new_

~~Regular expressions (search strings)~~

^ Matches beginning of line
$ Matches end of line
. Matches any single character

 - Matches any previous character
.* Matches any character

~~Search and replace commands~~


Syntax:
```
  :[address]s/old_text/new_text/

```

Address components:
. Current line
n Line number n
.+m Current line plus m lines
$ Last line
/string/ A line that contains "string"
% Entire file

[addr1],[addr2] Specifies a range


Examples:

The following example replaces only the **first** occurrence of Banana with Kumquat in each of 11 lines
starting with the current line (.) and continuing for the
10 that follow (.+10).
```
  :.,.+10s/Banana/Kumquat

```

The following example replaces **every** occurrence
(caused by the `g` at the end of the command) of
`apple` with `pear.`
```
  :%s/apple/pear/g

```

The following example removes the last character from
every line in the file. Use it if every line in the file ends
with `^M` as the result of a file transfer. Execute it
when the cursor is on the first line of the file.
```
  :%s/.$//

```

