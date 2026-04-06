|    | 0       | 1                                   |
|---:|:--------|:------------------------------------|
|  0 | yy or Y | Yank (copy) line to general buffer  |
|  1 | ' z 6yy | Yank 6 lines to buffer z            |
|  2 | yw      | Yank word to general buffer         |
|  3 | ' a 9dd | Delete 9 lines to buffer a          |
|  4 | ' A 9dd | Delete 9 lines; Append to buffer a  |
|  5 | ' a p   | Put text from buffer a after cursor |
|  6 | p       | Put general buffer after cursor     |
|  7 | P       | Put general buffer before cursor    |
|  8 | J       | Join lines                          |