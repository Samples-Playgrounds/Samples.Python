|    |     |                                          |                                                                       |
|---:|:----|:-----------------------------------------|:----------------------------------------------------------------------|
|  0 | nan | C5F877                                   | vzeroupper                                                            |
|  1 | nan | G_M000_IG02:                             | ;; offset=0003H                                                       |
|  2 | nan | C5F91001                                 | vmovupd xmm0, xmmword ptr [rcx]                                       |
|  3 | nan | C5F9D7C0                                 | vpmovmskb eax, xmm0                                                   |
|  4 | nan | G_M000_IG03:                             | ;; offset=000BH                                                       |
|  5 | nan | C3                                       | ret                                                                   |
|  6 | ;   | Total bytes of code 12                   | nan                                                                   |
|  7 | ;   | Assembly listing for G_M000_IG01: C5F877 | method Program:WithVector(Vector128`1):int ;; offset=0000H vzeroupper |