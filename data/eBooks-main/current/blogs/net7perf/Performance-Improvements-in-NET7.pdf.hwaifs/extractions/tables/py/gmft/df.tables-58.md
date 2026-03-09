|    |     |             |                                           |    |
|---:|:----|:------------|:------------------------------------------|:---|
|  0 | ;   | nan         | Program.Scan(System.ReadOnlySpan`1<Char>) |    |
|  1 | nan | mov         | rax,[rdx]                                 |    |
|  2 | nan | mov         | edx,[rdx+8]                               |    |
|  3 | nan | xor         | ecx,ecx                                   |    |
|  4 | nan | test        | edx,edx                                   |    |
|  5 | nan | jle         | short M00_L01                             |    |
|  6 | nan | M00_L00:    | nan                                       |    |
|  7 | nan | mov         | r8d,ecx                                   |    |
|  8 | nan | movsx       | r8,word ptr [rax+r8*2]                    |    |
|  9 | nan | inc         | ecx                                       |    |
| 10 | nan | cmp         | ecx,edx                                   |    |
| 11 | nan | jl          | short M00_L00                             |    |
| 12 | nan | M00_L01:    | nan                                       |    |
| 13 | nan | ret         | nan                                       |    |
| 14 | ;   | Total bytes | of code 27                                |    |