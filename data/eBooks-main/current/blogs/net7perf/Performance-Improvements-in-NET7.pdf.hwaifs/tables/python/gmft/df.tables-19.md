|    | ;        | Program.Compute()   |                              |
|---:|:---------|:--------------------|:-----------------------------|
|  0 |          | push r15            |                              |
|  1 |          | push r14            |                              |
|  2 |          | push r12            |                              |
|  3 |          | push rdi            |                              |
|  4 |          | push rsi            |                              |
|  5 |          | push rbp            |                              |
|  6 |          | push rbx            |                              |
|  7 |          | sub rsp,20          |                              |
|  8 |          | xor esi,esi         |                              |
|  9 | M00_L00: |                     |                              |
| 10 |          | xor edi,edi         |                              |
| 11 |          | imul                | ebx,esi,3E8                  |
| 12 | M00_L01: |                     |                              |
| 13 |          | xor ebp,ebp         |                              |
| 14 |          | imul                | r14d,edi,64                  |
| 15 |          | add r14d,ebx        |                              |
| 16 | M00_L02: |                     |                              |
| 17 |          | xor                 | r15d,r15d                    |
| 18 |          | lea                 | ecx,[rbp+rbp*4]              |
| 19 |          | lea                 | r12d,[r14+rcx*2]             |
| 20 | M00_L03: |                     |                              |
| 21 |          | lea                 | ecx,[r12+r15]                |
| 22 |          | call qword          | ptr [Program.Process(Int32)] |
| 23 |          | inc r15d            |                              |
| 24 |          | cmp r15d,0A         |                              |
| 25 |          | jl short            | M00_L03                      |
| 26 |          | inc ebp             |                              |
| 27 |          | cmp ebp,0A          |                              |
| 28 |          | jl short            | M00_L02                      |
| 29 |          | inc edi             |                              |
| 30 |          | cmp edi,0A          |                              |
| 31 |          | jl short            | M00_L01                      |
| 32 |          | inc esi             |                              |
| 33 |          | cmp esi,0A          |                              |
| 34 |          | jl short            | M00_L00                      |
| 35 |          | add rsp,20          |                              |
| 36 |          | pop rbx             |                              |
| 37 |          | pop rbp             |                              |
| 38 |          | pop rsi             |                              |
| 39 |          | pop rdi             |                              |
| 40 |          | pop r12             |                              |
| 41 |          | pop r14             |                              |
| 42 |          | pop r15             |                              |
| 43 |          | ret                 |                              |
| 44 | ; Total  | bytes of code 99    |                              |