|    |     |                             |                         |        |    |
|---:|:----|:----------------------------|:------------------------|:-------|:---|
|  0 | ;   | Program.Scan(System.String, | Int32,                  | Int32) |    |
|  1 | nan | sub                         | rsp,28                  | nan    |    |
|  2 | nan | cmp                         | r8d,r9d                 | nan    |    |
|  3 | nan | jge                         | short M00_L01           | nan    |    |
|  4 | nan | mov                         | eax,[rdx+8]             | nan    |    |
|  5 | nan | M00_L00:                    | nan                     | nan    |    |
|  6 | nan | cmp                         | r8d,eax                 | nan    |    |
|  7 | nan | jae                         | short M00_L02           | nan    |    |
|  8 | nan | inc                         | r8d                     | nan    |    |
|  9 | nan | cmp                         | r8d,r9d                 | nan    |    |
| 10 | nan | jl                          | short M00_L00           | nan    |    |
| 11 | nan | M00_L01:                    | nan                     | nan    |    |
| 12 | nan | add                         | rsp,28                  | nan    |    |
| 13 | nan | ret                         | nan                     | nan    |    |
| 14 | nan | M00_L02:                    | nan                     | nan    |    |
| 15 | nan | call                        | CORINFO_HELP_RNGCHKFAIL | nan    |    |
| 16 | nan | int                         | 3                       | nan    |    |
| 17 | ;   | Total bytes of              | code 36                 | nan    |    |