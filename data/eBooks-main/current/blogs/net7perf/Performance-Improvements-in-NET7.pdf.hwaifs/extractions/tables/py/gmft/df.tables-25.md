|    |     |                           |     |                                        |
|---:|:----|:--------------------------|:----|:---------------------------------------|
|  0 | ;   | Program.IsValueType() sub | nan | nan                                    |
|  1 | nan | mov                       | nan | rsp,28 rcx,offset MT_System.Int32      |
|  2 | nan | call                      | nan | CORINFO_HELP_TYPEHANDLE_TO_RUNTIMETYPE |
|  3 | nan | mov                       | nan | rcx,rax                                |
|  4 | nan | mov                       | nan | rax,[7FFCA47C9560]                     |
|  5 | nan | cmp                       | nan | [rcx],ecx                              |
|  6 | nan | add                       | nan | rsp,28                                 |
|  7 | nan | jmp                       | nan | rax                                    |
|  8 | ;   | Total bytes               | of  | code 38                                |