|    |     |                             |               |                         |        |    |
|---:|:----|:----------------------------|:--------------|:------------------------|:-------|:---|
|  0 | ;   | Program.Scan(System.String, | nan           | Int32,                  | Int32) |    |
|  1 | nan | sub                         | rsp,28        | nan                     | nan    |    |
|  2 | nan | cmp                         | r8d,r9d       | nan                     | nan    |    |
|  3 | nan | jge                         | short M00_L01 | nan                     | nan    |    |
|  4 | nan | mov                         | eax,[rdx+8]   | nan                     | nan    |    |
|  5 | nan | M00_L00:                    | nan           | nan                     | nan    |    |
|  6 | nan | cmp                         | r8d,eax       | nan                     | nan    |    |
|  7 | nan | jae                         | short M00_L02 | nan                     | nan    |    |
|  8 | nan | inc                         | r8d           | nan                     | nan    |    |
|  9 | nan | cmp                         | r8d,r9d       | nan                     | nan    |    |
| 10 | nan | jl                          | short M00_L00 | nan                     | nan    |    |
| 11 | nan | M00_L01:                    | nan           | nan                     | nan    |    |
| 12 | nan | add                         | rsp,28        | nan                     | nan    |    |
| 13 | nan | ret                         | nan           | nan                     | nan    |    |
| 14 | nan | M00_L02:                    | nan           | nan                     | nan    |    |
| 15 | nan | call                        | nan           | CORINFO_HELP_RNGCHKFAIL | nan    |    |
| 16 | nan | int                         | 3             | nan                     | nan    |    |
| 17 | ;   | Total bytes of              | code 36       | nan                     | nan    |    |