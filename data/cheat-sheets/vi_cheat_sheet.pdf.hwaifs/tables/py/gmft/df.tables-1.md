|    | Deletion          | commands                            |
|---:|:------------------|:------------------------------------|
|  0 | dd or ndd         | Delete n lines to general buffer    |
|  1 | dw                | Delete word to general buffer       |
|  2 | dnw               | Delete n words                      |
|  3 | d)                | Delete to end of sentence           |
|  4 | db                | Delete previous word                |
|  5 | D                 | Delete to end of line               |
|  6 | x                 | Delete character                    |
|  7 | Recovering        | deletions                           |
|  8 | p                 | Put general buffer after cursor     |
|  9 | P                 | Put general buffer before cursor    |
| 10 | Undo commands     | nan                                 |
| 11 | u                 | Undo last change                    |
| 12 | U                 | Undo all changes on line            |
| 13 | Rearrangement     | commands                            |
| 14 | yy or Y           | Yank (copy) line to general buffer  |
| 15 | “z6yy             | Yank 6 lines to buffer z            |
| 16 | yw                | Yank word to general buffer         |
| 17 | “a9dd             | Delete 9 lines to buffer a          |
| 18 | “A9dd             | Delete 9 lines; Append to buffer a  |
| 19 | “ap               | Put text from buffer a after cursor |
| 20 | p                 | Put general buffer after cursor     |
| 21 | P                 | Put general buffer before cursor    |
| 22 | J                 | Join lines                          |
| 23 | Parameters        | nan                                 |
| 24 | :set list         | Show invisible characters           |
| 25 | :set nolist       | Don’t show invisible characters     |
| 26 | :set number       | Show line numbers                   |
| 27 | :set nonumber     | Don’t show line numbers             |
| 28 | :set autoindent   | Indent after carriage return        |
| 29 | :set noautoindent | Turn off autoindent                 |
| 30 | :set showmatch    | Show matching sets of               |
| 31 | nan               | parentheses as they are typed       |
| 32 | :set noshowmatch  | Turn off showmatch                  |
| 33 | :set showmode     | Display mode on last line of screen |
| 34 | :set noshowmode   | Turn off showmode                   |
| 35 | :set all          | Show values of all possible         |
| 36 | nan               | parameters                          |