|    |                      |      |    |                             |
|---:|:---------------------|:-----|:---|:----------------------------|
|  0 | G_M000_IG04:         | ;;   |    | offset=003BH                |
|  1 | 48B9D820801A24020000 | mov  |    | rcx, 0x2241A8020D8          |
|  2 | 488B09               | mov  |    | rcx, gword ptr [rcx]        |
|  3 | FF1572CD0D00         | call |    | [Console:WriteLine(String)] |
|  4 | EBE7                 | jmp  |    | SHORT G_M000_IG03           |