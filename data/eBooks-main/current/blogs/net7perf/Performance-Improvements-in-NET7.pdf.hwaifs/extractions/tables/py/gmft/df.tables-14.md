|    | G_M000_IG01:   |                      |    | ;;   | offset=0000H                  |
|---:|:---------------|:---------------------|:---|:-----|:------------------------------|
|  0 | nan            | 57                   |    | push | rdi                           |
|  1 | nan            | 56                   |    | push | rsi                           |
|  2 | nan            | 4883EC28             |    | sub  | rsp, 40                       |
|  3 | nan            | 488BF1               |    | mov  | rsi, rcx                      |
|  4 | G_M000_IG02:   | nan                  |    | ;;   | offset=0009H                  |
|  5 | nan            | 33FF                 |    | xor  | edi, edi                      |
|  6 | nan            | 4885F6               |    | test | rsi, rsi                      |
|  7 | nan            | 742B                 |    | je   | SHORT G_M000_IG05             |
|  8 | nan            | 48B9982DD43CFC7F0000 |    | mov  | rcx, 0x7FFC3CD42D98           |
|  9 | nan            | 48390E               |    | cmp  | qword ptr [rsi], rcx          |
| 10 | nan            | 751C                 |    | jne  | SHORT G_M000_IG05             |
| 11 | G_M000_IG03:   | nan                  |    | ;;   | offset=001FH                  |
| 12 | nan            | 48B9282040F948020000 |    | mov  | rcx, 0x248F9402028            |
| 13 | nan            | 488B09               |    | mov  | rcx, gword ptr [rcx]          |
| 14 | nan            | FF1526A80D00         |    | call | [Console:Write(String)]       |
| 15 | nan            | FFC7                 |    | inc  | edi                           |
| 16 | nan            | 83FF7B               |    | cmp  | edi, 123                      |
| 17 | nan            | 7CE6                 |    | jl   | SHORT G_M000_IG03             |
| 18 | G_M000_IG04:   | nan                  |    | ;;   | offset=0039H                  |
| 19 | nan            | EB29                 |    | jmp  | SHORT G_M000_IG07             |
| 20 | G_M000_IG05:   | nan                  |    | ;;   | offset=003BH                  |
| 21 | nan            | 48B9982DD43CFC7F0000 |    | mov  | rcx, 0x7FFC3CD42D98           |
| 22 | nan            | 48390E               |    | cmp  | qword ptr [rsi], rcx          |
| 23 | nan            | 7521                 |    | jne  | SHORT G_M000_IG08             |
| 24 | nan            | 48B9282040F948020000 |    | mov  | rcx, 0x248F9402028            |
| 25 | nan            | 488B09               |    | mov  | rcx, gword ptr [rcx]          |
| 26 | nan            | FF15FBA70D00         |    | call | [Console:Write(String)]       |
| 27 | G_M000_IG06:   | nan                  |    | ;;   | offset=005DH                  |
| 28 | nan            | FFC7                 |    | inc  | edi                           |
| 29 | nan            | 83FF7B               |    | cmp  | edi, 123                      |
| 30 | nan            | 7CD7                 |    | jl   | SHORT G_M000_IG05             |
| 31 | G_M000_IG07:   | nan                  |    | ;;   | offset=0064H                  |
| 32 | nan            | 4883C428             |    | add  | rsp, 40                       |
| 33 | nan            | 5E                   |    | pop  | rsi                           |
| 34 | nan            | 5F                   |    | pop  | rdi                           |
| 35 | nan            | C3                   |    | ret  | nan                           |
| 36 | G_M000_IG08:   | nan                  |    | ;;   | offset=006BH                  |
| 37 | nan            | 488BCE               |    | mov  | rcx, rsi                      |
| 38 | nan            | 8BD7                 |    | mov  | edx, edi                      |
| 39 | nan            | 49BB1000AA3CFC7F0000 |    | mov  | r11, 0x7FFC3CAA0010           |
| 40 | nan            | 41FF13               |    | call | [r11]IPrinter:Print(int):this |
| 41 | nan            | EBDE                 |    | jmp  | SHORT G_M000_IG06             |
| 42 | ; Total        | bytes of code 127    |    | nan  | nan                           |