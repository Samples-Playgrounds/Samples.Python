|    | ;        | Program.Compute()   |                              |
|---:|:---------|:--------------------|:-----------------------------|
|  0 | nan      | push r15            | nan                          |
|  1 | nan      | push r14            | nan                          |
|  2 | nan      | push r12            | nan                          |
|  3 | nan      | push rdi            | nan                          |
|  4 | nan      | push rsi            | nan                          |
|  5 | nan      | push rbp            | nan                          |
|  6 | nan      | push rbx            | nan                          |
|  7 | nan      | sub rsp,20          | nan                          |
|  8 | nan      | xor esi,esi         | nan                          |
|  9 | M00_L00: | nan                 | nan                          |
| 10 | nan      | xor edi,edi         | nan                          |
| 11 | nan      | imul                | ebx,esi,3E8                  |
| 12 | M00_L01: | nan                 | nan                          |
| 13 | nan      | xor ebp,ebp         | nan                          |
| 14 | nan      | imul                | r14d,edi,64                  |
| 15 | nan      | add r14d,ebx        | nan                          |
| 16 | M00_L02: | nan                 | nan                          |
| 17 | nan      | xor                 | r15d,r15d                    |
| 18 | nan      | lea                 | ecx,[rbp+rbp*4]              |
| 19 | nan      | lea                 | r12d,[r14+rcx*2]             |
| 20 | M00_L03: | nan                 | nan                          |
| 21 | nan      | lea                 | ecx,[r12+r15]                |
| 22 | nan      | call qword          | ptr [Program.Process(Int32)] |
| 23 | nan      | inc r15d            | nan                          |
| 24 | nan      | cmp r15d,0A         | nan                          |
| 25 | nan      | jl short            | M00_L03                      |
| 26 | nan      | inc ebp             | nan                          |
| 27 | nan      | cmp ebp,0A          | nan                          |
| 28 | nan      | jl short            | M00_L02                      |
| 29 | nan      | inc edi             | nan                          |
| 30 | nan      | cmp edi,0A          | nan                          |
| 31 | nan      | jl short            | M00_L01                      |
| 32 | nan      | inc esi             | nan                          |
| 33 | nan      | cmp esi,0A          | nan                          |
| 34 | nan      | jl short            | M00_L00                      |
| 35 | nan      | add rsp,20          | nan                          |
| 36 | nan      | pop rbx             | nan                          |
| 37 | nan      | pop rbp             | nan                          |
| 38 | nan      | pop rsi             | nan                          |
| 39 | nan      | pop rdi             | nan                          |
| 40 | nan      | pop r12             | nan                          |
| 41 | nan      | pop r14             | nan                          |
| 42 | nan      | pop r15             | nan                          |
| 43 | nan      | ret                 | nan                          |
| 44 | ; Total  | bytes of code 99    | nan                          |