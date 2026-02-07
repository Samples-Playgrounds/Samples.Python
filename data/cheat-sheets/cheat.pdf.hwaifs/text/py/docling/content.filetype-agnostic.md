C"T- n(n+1)

n(nt 1)(2n + 1)

n-(nt1)

ncT-

- n+1)c"++c nn - 1)

y

(c -1)2

(2n)-

2n

Definitions

Theoretical Computer Science Cheat Sheet

Series

| Theoretical Computer Science Cheat Sheet iff 3 positive c, no such that   | Theoretical Computer Science Cheat Sheet iff 3 positive c, no such that                         | Theoretical Computer Science Cheat Sheet iff 3 positive c, no such that                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Theoretical Computer Science Cheat Sheet iff 3 positive c, no such that   |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Definitions                                                               | Definitions                                                                                     | Series                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Series                                                                    |
| f(n) = O(g(n))  f(n) = 1(9(n))                                            | iff ∃ positive c, n0 such that 0 ≤ f(n) ≤ cg(n) ∀n ≥ n0 .                                       | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| f(n) = Ω(g(n))  f(n) = 0(9(n))                                            | iff ∃ positive c, n0 such that f(n) ≥ cg(n) ≥ 0 ∀n ≥ n0 .                                       | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| f(n) = Θ(g(n))  f(n) = 019(n)) n →∞0                                      | iff f(n) =  O(g(n)) and f(n) = Ω(g(n)).                                                         | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| f(n) = o(g(n))                                                            | iff lim n→∞  f(n)/g(n) = 0.                                                                     | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| lim n→∞ a n  =  a  inf S                                                  | iff ∀ǫ >  0, ∃n0  such that &#124;a n  −  a &#124; < ǫ ,  ∀n ≥ n0 .                             | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| sup S                                                                     | least b ∈ R such that b ≥ s , ∀s ∈ S .                                                          | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| inf S  lim sup an n ›∞0                                                   | greatest b ∈ R such that b ≤ s ,  ∀s ∈ S .                                                      | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| lim inf n→∞ a n                                                           | lim n→∞ inf{ai&#124; i ≥ n, i ∈ N} .                                                            | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| lim sup n→∞ a n                                                           | lim n→∞ sup{ai&#124; i ≥ n, i ∈ N} .                                                            | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| n k                                                                      | Combinations: Size k sub sets of a size n set.                                                 | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
|   n k                                                                   | Stirling numbers (1st kind): Arrangements of an n  ele ment set into k cycles.                 | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
|   n k                                                                    | Stirling numbers (2nd kind): Partitions of an n  element set into k non-empty sets.             | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| n k                                                                       | 1st order Eulerian numbers: Permutations π 1π2 . . . πn  on {1 ,  2, . . . , n} with k ascents. | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| n k                                                                       | 2nd order Eulerian numbers.                                                                     | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |
| Cn  Cn  14.                                                               | Catalan Numbers: Binary trees with n + 1 vertices.                                              | X n i=1 i = n (n + 1) 2 , X n i=1 i 2  = n (n + 1)(2n + 1) 6 , X n i=1 i 3  = n 2 (n + 1) 2 4 . In general: X n i=1 i m  = 1 m + 1  (n + 1) m+1  −  1  − X n i=1 (i + 1) m+1  −  i m+1  −  (m + 1)i m   n X − 1 i=1 i m  = 1 m + 1 X m k=0  m + 1 k  Bkn m+1−k . Geometric series: X n i=0 c i  = c n+1  −  1 c  −  1 , c 6= 1 , X ∞ i=0 c i  = 1 1  −  c , X ∞ i=1 c i  = c 1  −  c ,  &#124;c&#124; < 1 , X n i=0 ic i  = nc n+2  −  (n + 1)c n+1  + c (c  − 1) 2 , c 6= 1 , X ∞ i=0 ic i  = c (1 −  c) 2 ,  &#124;c&#124; < 1 Harmonic series: Hn  Hn  = X n i=1 1 i , X n i=1 iHi  Hi  = n (n + 1) 2 Hn  Hn  − n (n  − 1) 4 . X n i=1 Hi  Hi  = (n + 1)Hn  Hn  −  n,  X n i=1  i m  Hi  =  n + 1 m + 1  Hn Hn+1  − 1 m + 1  . 1.   n k  = n ! (n  − k)!k! ,  2.  X n k=0  n k  = 2 n ,  3.   n k  =  n n  −  k  , 4.   n k  = n k  n  −  1 k  −  1  ,  5.   n k  =  n  −  1 k  +  n  −  1 k  −  1  , 6.   n m  m k  =  n k  n  −  k m  −  k  ,  7.  X n k=0  r + k k  =  r + n + 1 n  , 8.  X n k=0  k m  =  n + 1 m + 1  ,  9.  X n k=0  r k   s n  −  k  =  r + s n  , 10.   n k  = (−1) k  k  −  n  −  1 k  ,  11.   n 1  =  n n  = 1 , 12.   n 2  = 2 n − 1  −  1 ,  13.   n k  = k  n  −  1 k  +  n  −  1 k  −  1  , − 1)!Hn Hn − 1,  16.   n n  = 1 ,  17.   n k  ≥  n k  , n  =  n  =  n  20.  X n  n  =  n! 21. Cn  1  2n  In general: 1 | n°(n + 1)?.                                                               |

i

(- 1

G (x) - 90

- 2х

-

5it1 = 21 +7

л - nt1

<!-- formula-not-decoded -->

T(n)=aT (n/b) + f(n), a ≥1,6 &gt; 1

If Je &gt; 0 such that f(n) = O(nogba-e)

Master method:

<!-- formula-not-decoded -->

If ∃ǫ &gt; 0 such that f(n) = O(n
logb a − ǫ ) then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If ∃ǫ &gt; 0 such that f(n) = Ω(n
logb a+ǫ ), and ∃c &lt; 1 such that af(n/b) ≤ cf(n) for large n, then

<!-- formula-not-decoded -->

Substitution (example): Consider the following recurrence

<!-- formula-not-decoded -->

Note that Ti Ti is always a power of two. Let t i = log 2 Ti Ti . Then we have

<!-- formula-not-decoded -->

Let u i = ti/2 i . Dividing both sides of the previous equation by 2 i+1 we get

<!-- formula-not-decoded -->

Substituting we find

<!-- formula-not-decoded -->

which is simply ui = i/2. So we find that Ti Ti has the closed form Ti Ti = 2 i2 i − 1 . Summing factors (example): Consider the following recurrence

<!-- formula-not-decoded -->

Rewrite so that all terms involving T are on the left side scope"

<!-- formula-not-decoded -->

Now expand the recurrence, and choose a factor which makes the left side "telescope"

Theoretical Computer Science Cheat Sheet

Identities Cont.

## Identities Cont.

## Recurrences

<!-- formula-not-decoded -->

Let m = log 2 n. Summing the left side we get T (n) − 3 m T (1) = T (n) − 3 m = T (n) − n k where k = log 2 3 ≈ 1 . 58496. Summing the right side we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

i-1

and so T (n) = 3n k − 2n. Full history recurrences can often be changed to limited history ones (example): Consider

<!-- formula-not-decoded -->

Note that

<!-- formula-not-decoded -->

j=0

j=0

Subtracting we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

tion by x^

Generating functions:

1. Multiply both sides of the equation by x i .
2. Sum both sides over all i for which the equation is valid.
3. Choose a generating function G(x). Usually G(x) = P ∞ i=0 x i gi .
3. Rewrite the equation in terms of the generating function G(x).
4. Solve for G(x).
5. The coefficient of x i in G(x) is gi . Example:

i20

<!-- formula-not-decoded -->

Multiply and sum:

<!-- formula-not-decoded -->

We choose G(x) = P i≥0 x i gi. Rewrite in terms of G(x):

<!-- formula-not-decoded -->

Simplify:

<!-- formula-not-decoded -->

Solve for G(x):

<!-- formula-not-decoded -->

Expand this using partial fractions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

+

HIN

Trees

Every tree with n vertices has n - 1

edges.

## Trees

Every tree with n vertices has n − 1 edges.

Kraft inequality: If the depths of the leaves of a binary tree are d 1 , . . . , d n :

<!-- formula-not-decoded -->

and equality holds only if every internal node has 2 sons.

„Vv\_

loga x lle

Pr B Ai Pr Ail

2n

-½, Bz = E,

+1)"

+")'

49

363

20'

140'

280, 2520%

-e

38 =- 30, B10

-b+V62-1ac

+021+*+9+9+

Pr|Bl

2T0

2al

T ~ 3.14159,

7129

Theoretical Computer Science Cheat Sheet e ~ 2.71828,

y ~ 0.57721,

ф= 1y ~ 1.61803,

| Theoretical Computer Science Cheat Sheet Probability                      | Theoretical Computer Science Cheat Sheet Probability                      | Theoretical Computer Science Cheat Sheet Probability                      | Theoretical Computer Science Cheat Sheet Probability                      | Theoretical Computer Science Cheat Sheet Probability               |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------|
| π ≈ 3 . 14159,  e ≈ 2 . 71828,  γ ≈ 0 . 57721,  φ = 1+√ 5 2  ≈ 1 . 1 2 2 | π ≈ 3 . 14159,  e ≈ 2 . 71828,  γ ≈ 0 . 57721,  φ = 1+√ 5 2  ≈ 1 . 1 2 2 | π ≈ 3 . 14159,  e ≈ 2 . 71828,  γ ≈ 0 . 57721,  φ = 1+√ 5 2  ≈ 1 . 1 2 2 | π ≈ 3 . 14159,  e ≈ 2 . 71828,  γ ≈ 0 . 57721,  φ = 1+√ 5 2  ≈ 1 . 1 2 2 | 61803,  φ ˆ  = 1 − √ 5 2  ≈ − . 61803                             |
| i                                                                         | 2 i  8                                                                    | pi  5                                                                     | General                                                                   | Probability                                                        |
| 1  3 4                                                                    | 2                                                                         | 2  7                                                                      | Bernoulli Numbers (Bi = 0, odd i 6= 1):                                   | Continuous distributions: If                                       |
| 2  5                                                                      | 4                                                                         | 3 11                                                                      | B 0  = 1, B1  =  − 1 2 ,  B 2  =  1 6 ,  B 4  =  −  1 30 ,              | b                                                                  |
| 3  6                                                                      | 8                                                                         | 5                                                                         | B 6  =  1 42 ,  B 8  =  −  1 30 ,  B 10  =  5 66  .                       | Pr[a < X < b] =  Z  a Z  a p(x) dx,                              |
| 4  7                                                                      | 16                                                                        | 7                                                                         | Change of base, quadratic formula:                                        | then p is the probability density function of                      |
| 5  8                                                                      | 32                                                                        | 11                                                                        | log a  x − b ± √ b 2  −  4ac                                           | X. If Pr[X < a] = P(a)                                             |
| 6  9                                                                      | 64                                                                        | 13                                                                        | log b  x  = log a b , 2a . =e".                                           | , then P is the distribution function of X. If                     |
| 7                                                                         | 128                                                                       | 17                                                                        | Euler’s number e:                                                         | P and p both exist then                                            |
| 8                                                                         | 256                                                                       | 19                                                                        | e = 1 +  1 2  + 1 6  + 1 24  + 1 120  + · · ·                             | P(a) =  Z  − a                                                    |
| 9                                                                         | 512                                                                       | 23                                                                        | lim  1 + x  n =  e x .                                                 | Z  −∞ p(x) dx.                                                    |
| 10                                                                        | 1,024                                                                     | 29                                                                        | n→∞  n 1 n 1 n+1                                                          | Expectation: If X is discrete                                      |
| 11                                                                        | 2,048                                                                     | 31                                                                        | 1 +  n  < e <  1 +  n  .                                                | E[g(X)] = X g(x) Pr[X =  x] .                                      |
| 12                                                                        | 4,096                                                                     | 37                                                                        | 1 +  1 n  n =  e  − e 2n + 11e 24n2 −  O  1 n 3  .                     | x                                                                  |
| 13                                                                        | 8,192                                                                     | 41                                                                        | Harmonic numbers:                                                         | If X continuous then ∞ ∞                                           |
| 14                                                                        | 16,384                                                                    | 43                                                                        | 1,  3 11 25 137 49 363 140 , 761 280 , 7129 2520 , . . .                  | E[g(X)] =  Z  − Z  −∞ g(x)p(x) dx = Z  − Z  −∞ g(x) dP(x) .    |
| 15                                                                        | 32,768                                                                    | 47                                                                        | 2 , 6 , 12 , 60  , 20 ,                                                  | Variance, standard deviation:                                      |
| 16                                                                        | 65,536                                                                    | 53                                                                        | ln n < Hn  Hn  < ln n + 1 ,                                               | VAR[X] = E[X 2 ] − E[X] 2 ,                                        |
| 17                                                                        | 131,072                                                                   | 59                                                                        | Hn  1                                                                     | σ  = p VAR[X] .                                                   |
| 18                                                                        | 262,144                                                                   | 61                                                                        | Hn  = ln n + γ + O  n  .                                                | For events A and B:                                                |
| 19                                                                        | 524,288                                                                   | 67                                                                        | Factorial, Stirling’s approximation:                                      | Pr[A ∨ B] = Pr[A] + Pr[B] − Pr[A ∧ B]                              |
| 20                                                                        | 1,048,576                                                                 | 71                                                                        | 1, 2, 6, 24, 120, 720, 5040, 40320, 362880,  . . .                        | Pr[A ∧ B] = Pr[A] · Pr[B] ,                                        |
| 21                                                                        | 2,097,152                                                                 | 73                                                                        | n                                                                         | iff A and B are independent.                                       |
| 22                                                                        | 4,194,304                                                                 | 79                                                                        | n ! = √ 2πn  n e   1 + Θ 1 n  .                                   | Pr[A&#124;B] =  Pr[A ∧ B]                                          |
| 23                                                                        | 8,388,608                                                                 | 83                                                                        | Ackermann’s function and inverse:                                         | Pr[B]                                                              |
|                                                                           |                                                                           | 89                                                                        |   2 j i = 1                                                           | For random variables X and Y :                                     |
| 24  25                                                                    | 16,777,216  33,554,432                                                    | 97                                                                        | a (i, j) =    a (i  −  1 ,  2)  j = 1                                | E[X · Y ] = E[X] · E[Y ] ,                                         |
| 26                                                                        | 67,108,864                                                                | 101                                                                       |   a (i  −  1, a(i, j − 1))  i, j ≥ 2                                   | if X and Y are independent.                                        |
| 27                                                                        | 134,217,728                                                               | 103                                                                       | α (i) = min{j &#124; a(j, j) ≥ i} .                                       | E[X + Y ] = E[X] + E[Y ] ,                                         |
| 28                                                                        | 268,435,456                                                               | 107                                                                       | Binomial distribution:                                                    | E[cX] = c E[X] .                                                   |
| 29                                                                        | 536,870,912                                                               | 109                                                                       | Pr[X = k] =   n k  p k q n − k , q = 1  − p,                           | Bayes’ theorem:                                                    |
| 30                                                                        | 1,073,741,824                                                             | 113                                                                       | n n −                                                                     | Pr[Ai&#124;B] =  Pr[B&#124;Ai] Pr[Ai] P n Pr[Aj ] Pr[B&#124;Aj ] . |
| 31                                                                        | 2,147,483,648                                                             | 127                                                                       | E[X] = X k   p k q n k  =  np.                                         | j=1  Inclusion-exclusion:                                          |
| 32                                                                        | 4,294,967,296                                                             | 131                                                                       | k=1 k                                                                     | n n                                                                |
| Pascal’s Triangle                                                         | Pascal’s Triangle                                                         | Pascal’s Triangle                                                         | Poisson distribution: λ k                                                 | Pr  h _ X i i = X Pr[Xi] + j=1                                   |
| 1                                                                         | 1                                                                         | 1                                                                         | Pr[X = k] =  e λ k! ,  E[X] = λ.                                          | i=1 i=1 n k                                                        |
| 1 1                                                                       | 1 1                                                                       | 1 1                                                                       | Normal (Gaussian) distribution:                                           | X (−1) k+1  X Pr  h ^ X ij i .                                     |
| 1 2 1                                                                     | 1 2 1                                                                     | 1 2 1                                                                     | p(x) =  1 e − (x−µ) 2 /2σ 2 E[X] = µ.                                     | k=2 ii<···<ik j=1 Moment inequalities:                             |
|                                                                           |                                                                           |                                                                           | √ 2πσ ,                                                                  |                                                                    |
| 1 3 3 1                                                                   | 1 3 3 1                                                                   | 1 3 3 1                                                                   | The “coupon collector”: We are given a                                    | Pr   &#124;X&#124; ≥ λE[X]  ≤ 1 ,                             |
| 1 4 6 4 1 1 5 10 10 5 1                                                   | 1 4 6 4 1 1 5 10 10 5 1                                                   | 1 4 6 4 1 1 5 10 10 5 1                                                   | random coupon each day, and there are n                                   | λ 1                                                                |
|                                                                           |                                                                           |                                                                           | different types of coupons. The distribu                                 | Pr  h X  − E[X]   ≥ λ ·  σ i ≤ λ2 .                       |
| 1 6 15 20 15 6 1                                                          | 1 6 15 20 15 6 1                                                          | 1 6 15 20 15 6 1                                                          | tion of coupons is uniform. The expected                                  | Geometric distribution:                                            |
| 1 7 21 35 35 21 7 1                                                       | 1 8 28 56 70 56 28 8 1                                                    | 1 7 21 35 35 21 7 1                                                       | number of days to pass before we to col lect all n types is              | Pr[X = k] = pq k − 1 , q = 1  − p,                                 |
| 1 9 36 84 126 126 84 36 9 1                                               | 1 9 36 84 126 126 84 36 9 1                                               | 1 9 36 84 126 126 84 36 9 1                                               | nHn                                                                       | ∞ kpq k − 1  = 1 .                                                 |
|                                                                           |                                                                           |                                                                           | Hn.                                                                       | E[X] = X p                                                         |

761

in cos a

sın a

1 - cOSx

SIn X

2 tan x sinh ıx

tanh ix

OS

A

=

- e

AB

=

tanx = tany

1+ cosx cot x cot y F 1

оx + 0-x '

sinh p cot. p

cosh p'

- 1 ) 7

in

=

=

COS a

8/0

1\_ tan2 n'

fal

1Itanptann'

2

2

sins sin a.

cot r - cot u

›| t tan a

,

A

+ B

2

2

cot a =

cos a

=

cos a sec a

AB

cot a cos a

(0,1)

Multiplication:

## Theoretical Computer Science Cheat Sheet

## Trigonometry

A

C

Definitions:

(cos 0, sin 0)

<!-- image -->

Pythagorean theorem:

C

Definitions:

sin a

A

=

= A/C, csc a

=

C/A, sin a

=

A

=

B

Area, radius of inscribed circle:

sin x =

AB,

CSCx'

Identities:

1

sin x

=

csc x

1

cot x

,

1 + tan

2

x = sec sin x = cos

π

−

2

cos x

=

−

cos(π

cot x

2

x,

x



−

−

=

−

,

,

x)

,

AB

1

2

COS X =

A + B + C

.

B

A

.

1

secx'

sin x + cos x = 1,

1

cos x

=

sin

2

x + cos sec x

2

x = 1

1 + cot

2

x = csc

,

2

x, sin x = sin(π

−

tan x = cot cot(π

x)

csc x = cot sin(x ± y) = sin x cos y ± cos x sin y,

cos(x ± y) = cos x cos y ∓ sin x sin y,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

sin 2x = 2 sin x cos x, cos 2x = cos

x

sin tan 2x =

cos 2x = 1

tan 2x

=

1

2

−

2 sin x,

2 tan x

2

−

tan sin(x + y) sin(x

,

x

− y) = sin

2

cos(x + y) cos(x

− y) = cos

Euler’s equation:

e

= cos x + isin x, e cos 2x

cot 2x sin

sin iπ

=

=

y,

2

y.

=

sin 2x

π

2

−

2

x)

,

x



−

,

cot x,

2 tan x

1 + tan? x'

2 tan x

=

1 + tan

2

cos 2x = 2 cos

x

cot 2x

1

2

−

2

−

tan

1 + tan

2

cot

x

2

−

2 cotx

−

v2.02 c 1994 by Steve Seiden sseiden@acm.org

http://www.csc.lsu.edu/~seiden

1

2

−

−

ix

2

−

2

x,

x

2

=

C=A•B,

Multiplication:

<!-- formula-not-decoded -->

Determinants: det A 6= 0 iff A is non-singular.

det A

det A =

B = det A

n

X

Y

sign(π)ai,π(i)

π

i=1

2 × 2 and 3 × 3 determinant:

d

= 9

f

a b

9

e

h

a b c d e f

=

g h i

Permanents:

Definitions:

sinh x =

Definitions:

e

x

sinh x tanh x

=

=

=

cosh x

e

e

sech x

Identities:

cosh sinh

−

2

−

e

+ e

x

x

1

,

x = 1

2

x

−

coth

2

2

2

x

−

csch x = 1

cosh(−x) = cosh x, cosh x

csch x

a

perm A =
X

=

−

ceg

−

e f d f

c d

- h

=

ad b c

g

bc,

h

aei + bfg + cdh

−

fha − ibd.

n

Y

i,π(i)

.

π

i=1

## Hyperbolic Functions

=

esch x

−

−

−

x

x

x

x

-,

+ e

−

x

2

1

sinh x

,

coth x

=

=

=

tanh x

.

sinh(-x) = - sinhx, tanh

2

2

x

+ sech x = 1

,

sinh(−x) = − sinh x, tanh(−x) = − tanh x,

sinh(x + y) = sinh x cosh y + cosh x sinh y, cosh(x + y) = cosh x cosh y + sinh x sinh y,

sinh 2x = 2 sinh x cosh x, cosh 2x = cosh

+ sinh

2

x

cosh x + sinh x

=

(cosh x + sinh x)

n

2 sinh

= cosh x

x

2

2

e

x, coshx - sinhx = e-",

2

nEZ, cosh x

sinh x

x

,

−

=

e

= cosh nx + sinh nx, n ∈ Z

1

,

2 cosh

= cosh x + 1

,

3

θ sin θ cos θ tan θ

0 0 1 0

π

√
3

√
3

1

6

π

4

π

3

π

2

1

2

√
2

2

√
3

2

√
2

2

1

2

2

1 0

00

3

1

√
3

∞

2

x

−

x

1

a c

2

·

·

det B,

## Matrices

k=1

= B/C,

= C/B, cos a

=

tan x

=

,

Trigonometry

x

2

x

.

Theoretical Computer Science Cheat Sheet

Matrices

=

sin a

.

x

1

x

x

1

,

,

,

,

,

N/=

e

,

,

,

,

−

e

−

2

. . . in mathematics you don't understand things, you just get used to them.

– J. von Neumann

.

+ i a b

d e

,

,

.

More Trig.

More Trig.

C

Law of cosines:

B

b

a

h

A c B Law of cosines: c 2 = a 2 +b 2 − 2ab cos C. Area:

c sin A sin B

A =

hc,

1

2

1

2

c

ab sin C,

2

sin A sin B

a

=

=

2 sin C

Heron’s formula:

Sa =s - a,

A =
√
s

sb

·

·

·

a

s

s

(a + b + c)

s

sb

1

=

=

=

2

s

s

−

a,

−

b,

s

−

c

=

c.

s

2

More identities:

r

−

1

sin tan 2

cos tan

cot 5

cot

2

=

sin x =

=

COS X

sin x cos x

tan x sin x

=

sin x cos x

=

=

=

=

x

2

x

2

x

2

=

=

=

x

=

r

r

2

1 + cos x

2

1

cos x

−

1 + cos x

1

−

cos x sin x

sin x

1 + cos x

,

r

1 + cos x

1

cos x

−

1 + cos x sin x

sin x

−

cos x ix

ix

i

1

e

e

=

-i

=

−

=

=

i

−

ix

−

e

2i

+ e

−

2

e

e

e

ix

e

−

ix

+ e

2ix ix

,

−

−

−

1

+ 1

,

−

i

e

2ix sinh ix

~.

cos x

= cosh ix, tan x = tanh ix i .

,

=

s

,

,

,

.

c,

,

,

,

,

,

ix ix ,

,

C2T1

- 1

TIC:

In In n

2.n

• n•

\_ (X1, У1) • (X2, Уг)

n: - 1

Theoretical Computer Science Cheat Sheet

/(r.-p)2 + (11-10)2

I Pi

Pilo

(=):

Number Theory

The Chinese remainder theorem: There ex-

Definitions:

Graph Theory

Notation:

## Theoretical Computer Science Cheat Sheet

ists a number C such that:

## Number Theory

E(G)

tex to itself.

The Chinese remainder theorem: There exists a number C such that:

C ≡ r 1 mod m 1

.

.

.

.

.

.

.

.

.

C ≡ r n mod m n

if m i and m j are relatively prime for i 6= j . Euler's function: φ(x) is the number of positive integers less than x relatively prime to x. If Q n i=1 p ei i is the prime factorization of x then

n

<!-- formula-not-decoded -->

Euler's theorem: If a and b are relatively prime then

<!-- formula-not-decoded -->

Fermat’s theorem:

<!-- formula-not-decoded -->

The Euclidean algorithm: if a &gt; b are integers then

<!-- formula-not-decoded -->

If Q n i=1 p ei i is the prime factorization of x then

<!-- formula-not-decoded -->

Perfect Numbers: x is an even perfect number iff x = 2 n − 1 (2 n − 1) and 2 n − 1 is prime.

Wilson’s theorem: n is a prime iff u(i) =

<!-- formula-not-decoded -->

M¨obius inversion:




1 if i = 1.

If

µ(i) =

If then

<!-- formula-not-decoded -->

0 if i is not square-free.

(−1)

if i is the product of

r

r

distinct primes.

<!-- formula-not-decoded -->

In Inn

Inn

Prime numbers:

pn = n ln n + n ln ln n − n + n ln ln n ln n

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->












Edge set

## Graph Theory

## Definitions:

Loop

An edge connecting a ver- tex to itself.

## Directed Simple

Each edge has a direction. Graph with no loops or multi-edges.

Walk

A sequence v0e1v1 . . . eℓvℓ .

Trail

A walk with distinct edges.

Path

A trail with distinct vertices.

Connected

A graph where there exists a path between any two vertices.

Component

A maximal connected subgraph.

Tree

A connected acyclic graph.

Free tree

A tree with no root.

DAG

Directed acyclic graph.

Eulerian

Graph with a trail visiting each edge exactly once.

Hamiltonian Graph with a cycle visiting each vertex exactly once.

Cut

A set of edges whose re- moval increases the num- ber of components.

Cut-set

A minimal cut.

Cut edge

A size 1 cut.

k-Connected A graph connected with the removal of any k − 1 vertices. k-Regular

k-Tough

∀S ⊆ V, S 6= ∅ we have k · c (G − S) ≤ |S| .

k-Regular

A graph where all vertices have degree k .

k-Factor

A k-regular spanning subgraph.

Matching

A set of edges, no two of which are adjacent.

Clique

A set of vertices, all of which are adjacent.

Ind. set

A set of vertices, none of which are adjacent.

Vertex cover A set of vertices which cover all edges.

Planar graph A graph which can be em- beded in the plane.

Plane graph An embedding of a planar graph.

$$X v∈V deg(v) = 2m.$$

If G is planar then n − m + f = 2, so

$$f ≤ 2n$$

$$− 4, m ≤ 3n − 6 .$$

Each edge has a direction.

A

Tree

Any planar graph has a vertex with degree ≤ 5.

Vertex set

## Notation:

E(G) Edge set

V (G) Vertex set

c (G) Number of components

G[S] Induced subgraph

deg(v) Degree of v

∆(G) Maximum degree

δ(G) Minimum degree

χ(G) Chromatic number

χE(G) Edge chromatic number

G c Complement graph

Kn Kn Complete graph

Kn Kn1,n2 Complete bipartite graph

r (k, ℓ) Ramsey number

## Geometry

Projective coordinates: triples (x, y, z), not all x , y and z zero.

(x, y, z) = (cx, cy, cz)

∀c 6= 0

## Cartesian Projective

(x, y) (x, y, 1)

y

=

(m, −1, b)

mx + b

x

(1

)

=

−

,

,

0

c

c

Distance formula, L p and L ∞ metric:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Area of triangle (x0, y0), (x1, y1) and (x2, y2):

<!-- formula-not-decoded -->

Angle formed by three points:

<!-- image -->

Line through two points (x0, y0) and (x1, y1):

<!-- formula-not-decoded -->

Area of circle, volume of sphere:

<!-- formula-not-decoded -->

If I have seen farther than others, it is because I have stood on the shoulders of giants.

– Issac Newton

.

•

•

•

+

du du

du du

du du

du

1

1

1

d arctan u)

d(arcsec u)

-1

du+)

d(c)

d(cu)

d (cosh u)

(n quIsp d(UV)

d (U")

(n500)0

(nue1)p d (sin u)

d (CSC U)

d (arcsın u)

d (cot u)

d seC u)

a (tanh u)

du d (coth u)

d sech u)

du d (csch u)

d(arcsinh u)

(X) N

(X)

d(arctanhu)

d arcsech u)

N (X)

N()

du du

(X) N

•

d(e)

•

•

•

-n.

•

v-di in " di

in * +

•

1

33.7t du

1

du du

du du

du du

=

-1

dr''

d(u/v)

1

1.3.3.5.5.7..

dr dr

dr

3

=

= c-

32

+

=

dr'

=

dr

=

1 p2

- de dr

dr

32

" (đi) - u (đx)

2+

/-„2 dx'

/1+72 dx'

2+

dx dx

dx dx

2+z7

Wallis' identity:

7 = 2.

2•2.4.4.6.6..

1.3.3.5.5.7..

π

<!-- formula-not-decoded -->

Brouncker’s continued fraction expansion:

<!-- formula-not-decoded -->

Gregrory’s series:

<!-- formula-not-decoded -->

Newton’s series:

<!-- formula-not-decoded -->

Sharp’s series:

<!-- formula-not-decoded -->

Euler’s series:

<!-- formula-not-decoded -->

## Partial Fractions

Let N(x) and D(x) be polynomial functions of x. We can break down N(x)/D(x) using partial fraction expansion. First, if the degree of N is greater than or equal to the degree of D, divide N by D, obtaining

<!-- formula-not-decoded -->

where the degree of N ′ is less than that of D. Second, factor D(x). Use the following rules: For a non-repeated factor:

N(x)

−

(x where

N (x)

(x-a)mD(x)

(x)

N

′

D(x)

,

N' (x)

D(x)

<!-- formula-not-decoded -->

For a repeated factor:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

.

The reasonable man adapts himself to the world; the unreasonable persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable. – George Bernard Shaw

A

=

a)D(x)

+

x

−

a

Theoretical Computer Science Cheat Sheet

Calculus du

Derivatives:

## Theoretical Computer Science Cheat Sheet

1. - dx

= C- dx

Derivatives:

4.

dx

7.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

9.

11.

<!-- formula-not-decoded -->

13.

= tan u sec u•

du

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

21.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

25.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

29.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Integrals:

<!-- formula-not-decoded -->

, n‡ -1,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

2.

dix

## Calculus

du/v)

v(d) - u (do)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

d(uv)

du dx

dx

= U

d(ecu)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

10.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

14.

<!-- formula-not-decoded -->

20.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

26.

<!-- formula-not-decoded -->

32.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

du sh

sh - sh

- 100

sin cOs"- - x sin x

tan x sec"- cot X CSC"-

un dx

X COS X

n- 1

n - 1

n - 2

n - 2

dx a + x

dx ax

2 (30x - Za) (a + bx) - x dx

x' dx

a

+.

+

&gt;

in

(5

in

%

=-In

d

2

a

in in X

- U

n. - 1

+

n. - 1

n. - 1l

+

n. - 1

н|*

HIN

н|*

1/22 1 2

hadi hadi

0 |8

a

1/p212

ccosh * +1

a2 → x2

= §Va-x2+3a a '

a '

Va? - x'

eresin a, a &gt; 0,

p2 - 02

Va+brd:

ax? + bx

а + bx '

1562

=dx, xVa + bx

va + bx

1/2-p2

• 0x = - ș (02 - x2)3/2, vaz -x==-àIn

Va? - x?

Va? -x2

a, a+ va? + x?

1/72 + 2 d

1

Theoretical Computer Science Cheat Sheet

Calculus Cont.

Va + bx n.

+ bx dx =

n.

a + Vaz - x2

Vat bx-va a+ Vaz -x?

Va + x?

Vx2 -a2

:

<!-- formula-not-decoded -->

• d.

dx = 2va + bx +

=-§Va-x2+Șa

= ‡ Ş|

In

-- In

In a &gt; 0,

+

x dx

2

2ax +b xp

in -

- 2ах - b dx

bx + 2c a.

In(ax)

a

=

a

(X"):

nxn-1

= a in

-"

x1

-X)=

x-=

-C

4ac - 62

Aac - 62'

Vavaxe+bx+c.

Var2 + bx + c

х dx

= 22+1

2 1 2 d

Ix'

n).

xT =

1)=

1)=",

= X =,

-a v62 - 4ac

m+I'

xvax? + bx + c

Ix/62 - 4ac'

-x)"

Vax2 + bx + c x3

Theoretical Computer Science Cheat Sheet dx

2a

Var2 + bx + c'

Calculus Cont.

Finite Calculus

1)-n

<!-- formula-not-decoded -->

x≥ + x-

23 + 3x2+ x-

Vax? +bx +c

a

+

(X -

K.z"

1

Bix

- X

a) -

+11

1

1

ai-1

1

3

Hi-1x

21

-f

-x'

[)

-A

U0 -

ил -

(1 - p)2

„x÷ +

+ Ex

„x÷ +

x÷ +

+÷x°

x= +

x÷+

x‡ +

(2i)1'

+ =x

+*(n-1x ex -

VI-4x

1 -p

2 X-

4

1

V1 - 4x

<!-- image -->

Taylor's series:

In -

+

+

MIN

1100

Theoretical Computer Science Cheat Sheet

Series

Ordinary power series:

n!x

- 12- (2- - 1) B2ix---

4(2)

5(х-1)

2-" -- B2n

-1 (4-2) B2ix"

-n n(2i - 1)!

(42)!

1 - x

(2i)!

м) 2

zel

(2n)!

4 x

X'

1 - VI-x

Expansions:

Expansions:

<!-- formula-not-decoded -->

## Cramer’s Rule

If we have equations:

<!-- formula-not-decoded -->

Let A = (ai,j ) and B be the column matrix (bi). Then there is a unique solution iff det A 6= 0. Let Ai be A with column i replaced by B. Then xi = det A i det A .

- William Blake (The Marriage of Heaven and Hell)

Improvement makes strait roads, but the crooked roads without Improvement, are roads of Genius.

– William Blake (The Marriage of Heaven and Hell)

Escher's Knot

## Escher’s Knot

<!-- image -->

If G is continuous in the interval [a, b] and F is nondecreasing then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If the integrals involved exist, and F possesses a derivative F ′ at every point in [a, b] then Fibonacci Numbers

00

86

95

59

21

47

11

80

96

<!-- formula-not-decoded -->

18

57

22

81

76

28

67

33

29

70

38

07

93

39

71

48

72

60

24

15

00 47 18 76 29 93 85 34 61 52 86 11 57 28 70 39 94 45 02 63 95 80 22 67 38 71 49 56 13 04 59 96 81 33 07 48 72 60 24 15 73 69 90 82 44 17 58 01 35 26 68 74 09 91 83 55 27 12 46 30 37 08 75 19 92 84 66 23 50 41 14 25 36 40 51 62 03 77 88 99 21 32 43 54 65 06 10 89 97 78 42 53 64 05 16 20 31 98 79 87

The Fibonacci number system: Every integer n has a unique representation

<!-- formula-not-decoded -->

## Fibonacci Numbers

Fi = Fi-1+Fi-2,

Fo = F1 = 1,

<!-- formula-not-decoded -->

Theoretical Computer Science Cheat Sheet

Series

## Theoretical Computer Science Cheat Sheet

## Series

•n/