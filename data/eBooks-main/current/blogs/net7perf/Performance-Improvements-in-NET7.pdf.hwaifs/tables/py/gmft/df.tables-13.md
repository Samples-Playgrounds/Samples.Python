|    |              |                |       |                                |
|---:|:-------------|:---------------|:------|:-------------------------------|
|  0 | G_M000_IG02: | nan            | ;;    | offset=0004H                   |
|  1 | nan          | 33D2           | xor   | edx, edx                       |
|  2 | nan          | 4885C9         | test  | rcx, rcx                       |
|  3 | nan          | 742A           | je    | SHORT G_M000_IG05              |
|  4 | nan          | 448B4108       | mov   | r8d, dword ptr [rcx+08H]       |
|  5 | nan          | 4181F845230100 | cmp   | r8d, 0x12345                   |
|  6 | nan          | 7C1D           | jl    | SHORT G_M000_IG05              |
|  7 | nan          | 4183C0D6       | add   | r8d, -42                       |
|  8 | nan          | 0F1F4000       | align | [4 bytes for IG03]             |
|  9 | G_M000_IG03: | nan            | ;;    | offset=0020H                   |
| 10 | nan          | 8BC2           | mov   | eax, edx                       |
| 11 | nan          | 4439448110     | cmp   | dword ptr [rcx+4*rax+10H], r8d |
| 12 | nan          | 7433           | je    | SHORT G_M000_IG08              |
| 13 | nan          | FFC2           | inc   | edx                            |
| 14 | nan          | 81FA45230100   | cmp   | edx, 0x12345                   |
| 15 | nan          | 7CED           | jl    | SHORT G_M000_IG03              |