|    | push          | r14                    |
|---:|:--------------|:-----------------------|
|  0 | push          | rdi                    |
|  1 | push          | rsi                    |
|  2 | push          | rbp                    |
|  3 | push          | rbx                    |
|  4 | sub           | rsp,20                 |
|  5 | xor           | esi,esi                |
|  6 | M00_L00:      | nan                    |
|  7 | xor           | edi,edi                |
|  8 | M00_L01:      | nan                    |
|  9 | xor           | ebx,ebx                |
| 10 | M00_L02:      | nan                    |
| 11 | xor           | ebp,ebp                |
| 12 | imul          | ecx,esi,3E8            |
| 13 | imul          | eax,edi,64             |
| 14 | add           | ecx,eax                |
| 15 | lea           | eax,[rbx+rbx*4]        |
| 16 | lea           | r14d,[rcx+rax*2]       |
| 17 | M00_L03:      | nan                    |
| 18 | lea           | ecx,[r14+rbp]          |
| 19 | call          | Program.Process(Int32) |
| 20 | inc           | ebp                    |
| 21 | cmp           | ebp,0A                 |
| 22 | jl            | short M00_L03          |
| 23 | inc           | ebx                    |
| 24 | cmp           | ebx,0A                 |
| 25 | jl            | short M00_L02          |
| 26 | inc           | edi                    |
| 27 | cmp           | edi,0A                 |
| 28 | jl            | short M00_L01          |
| 29 | inc           | esi                    |
| 30 | cmp           | esi,0A                 |
| 31 | jl            | short M00_L00          |
| 32 | add           | rsp,20                 |
| 33 | pop           | rbx                    |
| 34 | pop           | rbp                    |
| 35 | pop           | rsi                    |
| 36 | pop           | rdi                    |
| 37 | pop           | r14                    |
| 38 | ret           | nan                    |
| 39 | ; Total bytes | of code 84             |