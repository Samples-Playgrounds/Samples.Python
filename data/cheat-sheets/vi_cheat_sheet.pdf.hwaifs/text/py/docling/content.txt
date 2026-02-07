## vi  Editor  'Cheat  Sheet'

## VI  'Cheat' Sheet ACNS Bulletin ED-03

February 1995

Invoking vi:

vi filename [count][command]

Format of vi commands:

(count repeats the effect of the command)

## Command  mode  versus  input  mode

:wq :q! ZZ :sh Vi starts in command mode. The positioning commands operate only while vi is in command mode. You switch vi to input mode by entering any one of several vi input commands. (See next section.) Once in input mode, any character you type is taken to be text and is added to the file. You cannot execute any commands until you exit input mode. To exit input mode, press the escape ( Esc ) key.

## Input  commands (end  with  Esc)

| File management   | commands                       |
|-------------------|--------------------------------|
| :w name           | Write edit buffer to file name |
| :wq vi            | Write to file and quit         |
| :q! com-          | Quit without saving changes    |
| ZZ charac-        | Same as :wq                    |
| :sh file.         | Execute shell commands         |

## Window  motions

| a       | Append after cursor       |
|---------|---------------------------|
| i       | Insert before cursor      |
| o       | Open line below           |
| O       | Open line above           |
| :r file | Insert file after current |

Any of these commands leaves vi in input mode until you press Esc . Pressing the RETURN key will not take you out of input mode.

## Change  commands  (Input  mode)

| cw   | Change word (Esc)                    |
|------|--------------------------------------|
| cc   | Change line (Esc) - blanks line      |
| c$   | Change to end of line                |
| r c  | Replace character with c             |
| R    | Replace (Esc) - typeover             |
| s    | Substitute (Esc) - 1 char with       |
| S    | Substitute (Esc) - Rest of line text |
| .    | Repeat last change                   |

## Changes  during  insert  mode

Back to beginning of insert

| <ctrl>h   | Back one character   |
|-----------|----------------------|
| <ctrl>w   | Back one word        |
| <ctrl>u   | Back to beginning of |

| <ctrl>d     | Scroll down (half a screen)                  |
|-------------|----------------------------------------------|
| <ctrl>u     | Scroll up (half a screen)                    |
| <ctrl>f     | Page forward                                 |
| <ctrl>b     | Page backward                                |
| /string     | Search forward                               |
| ?string     | Search backward                              |
| <ctrl>l     | Redraw screen                                |
| <ctrl>g you | Display current line number file information |
| n           | Repeat search                                |
| N           | Repeat search reverse                        |
| G           | Go to last line                              |
| n G         | Go to line n                                 |
| : n         | Go to line n                                 |
| z<CR>       | Reposition window: cursor at top             |
| z.          | Reposition window: cursor in                 |
| z-          | Reposition window: cursor at                 |

## Cursor  motions

H

Upper left corner (home)

M

L

h

j

k

^

$

l

w

b

f

c

;

Middle line

Lower left corner

Back a character

Down a line

Up a line

Beginning of line

End of line

Forward a character

One word forward

Back one word

Find

c

Repeat find (find next

c

)

## Deletion  commands

dd  or n dd

Delete n lines to general buffer

dw

Delete word to general buffer

d n w

Delete n words

d)

Delete to end of sentence

db

Delete previous word

D

Delete to end of line

x

Delete character

## Recovering  deletions

p

Put general buffer after cursor

P

Put general buffer before cursor

## Undo  commands

u

Undo last change

U

Undo all changes on line

## Rearrangement  commands

## Move text  from  file old to  file new

vi old

' a 10yy

yank 10 lines to buffer a

:w

write work buffer

:e new

edit new file

' a p

put text from a after cursor

:30,60w new

Write lines 30 to 60 in file new

## Regular  expressions  (search  strings)

^

Matches beginning of line

$

Matches end of line

.

Matches any single character

*

Matches any previous character

.*

Matches any character

## Search  and  replace  commands

## Syntax:

```
:[address]s/old_text/new_text/
```

Yank (copy) line to general buffer

## Address components:

.

Current line

A line that contains "string"

| n               | Line number n        |
|-----------------|----------------------|
| .+ m            | Current line plus m  |
| $               | Last line            |
| /string/        | A line that contains |
| %               | Entire file          |
| [addr1],[addr2] | Specifies a range    |

## Examples:

yy or Y

' z 6yy

Yank 6 lines to buffer z

yw

Yank word to general buffer

' a 9dd

Delete 9 lines to buffer a

' A 9dd

Delete 9 lines; Append to buffer a

' a p

Put text from buffer a after cursor

p

Put general buffer after cursor

P

Put general buffer before cursor Join lines

J

## Parameters

:set list

Show invisible characters

:set nolist

Don't show invisible characters

:set number

Show line numbers Don't show line numbers

:set nonumber

:set autoindent

Indent after carriage return Turn off autoindent

:set noautoindent

:set showmatch

Show matching sets of parentheses as they are typed Turn off showmatch

:set noshowmatch

:set showmode :set noshowmode

:set all

Show values of all possible parameters

The following example replaces only the first occurrence of Banana with Kumquat in each of 11 lines starting with the current line (.) and continuing for the 10 that follow (.+10).

```
:.,.+10s/Banana/Kumquat
```

The following example replaces every occurrence (caused by the g at the end of the command) of apple with pear.

```
:%s/apple/pear/g
```

The following example removes the last character from every line in the file. Use it if every line in the file with ^M as the result of a file transfer. Execute it when the cursor is on the first line of the file.

```
:%s/.$//
```

Display mode on last line of screen Turn off showmode