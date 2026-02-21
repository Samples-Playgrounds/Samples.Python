|    |              |            |     |                               |
|---:|:-------------|:-----------|:----|:------------------------------|
|  0 | G_M000_IG05: | nan        | ;;  | offset=0034H                  |
|  1 | nan          | 3B4108     | cmp | eax, dword ptr [rcx+08H]      |
|  2 | nan          | 7323       | jae | SHORT G_M000_IG10             |
|  3 | nan          | 8BD0       | mov | edx, eax                      |
|  4 | nan          | 837C91102A | cmp | dword ptr [rcx+4*rdx+10H], 42 |
|  5 | nan          | 7410       | je  | SHORT G_M000_IG08             |
|  6 | nan          | FFC0       | inc | eax                           |
|  7 | nan          | 3D45230100 | cmp | eax, 0x12345                  |
|  8 | nan          | 7CE9       | jl  | SHORT G_M000_IG05             |