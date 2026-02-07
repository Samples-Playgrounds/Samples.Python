/negationslash

/negationslash

/negationslash

| Theoretical Computer Science Cheat Sheet   | Theoretical Computer Science Cheat Sheet                                                         | Theoretical Computer Science Cheat Sheet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Theoretical Computer Science Cheat Sheet   |
|--------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Definitions                                | Definitions                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                            |
| f ( n ) = O ( g ( n ))                     | iff ∃ positive c,n 0 such that 0 ≤ f ( n ) ≤ cg ( n ) ∀ n ≥ n 0 .                                | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| f ( n ) = Ω( g ( n ))                      | iff ∃ positive c,n 0 such that f ( n ) ≥ cg ( n ) ≥ 0 ∀ n ≥ n 0 .                                | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| f ( n ) = Θ( g ( n ))                      | iff f ( n ) = O ( g ( n )) and f ( n ) = Ω( g ( n )).                                            | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| f ( n ) = o ( g ( n ))                     | iff lim n →∞ f ( n ) /g ( n ) = 0.                                                               | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| lim n →∞ a n = a                           | iff ∀ /epsilon1 > 0, ∃ n 0 such that &#124; a n - a &#124; < /epsilon1 , ∀ n ≥ n 0 .             | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| sup S                                      | least b ∈ R such that b ≥ s , ∀ s ∈ S .                                                          | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| inf S                                      | greatest b ∈ R such that b ≤ s , ∀ s ∈ S .                                                       | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| lim inf n →∞ a n                           | lim n →∞ inf { a i &#124; i ≥ n, i ∈ N } .                                                       | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| lim sup n →∞ a n                           | lim n →∞ sup { a i &#124; i ≥ n, i ∈ N } .                                                       | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| ( n k )                                    | Combinations: Size k sub- sets of a size n set.                                                  | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| [ n k ]                                    | Stirling numbers (1st kind): Arrangements of an n ele- ment set into k cycles.                   | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| { n k }                                    | Stirling numbers (2nd kind): Partitions of an n element set into k non-empty sets.               | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| 〈 n k 〉                                    | 1st order Eulerian numbers: Permutations π 1 π 2 . . .π n on { 1 , 2 , . . .,n } with k ascents. | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| n k 〉                                      | 2nd order Eulerian numbers.                                                                      | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |
| 〈 〈 〉 C n                                  | Catalan Numbers: Binary trees with n +1 vertices.                                                | Series n ∑ i =1 i = n ( n +1) 2 , n ∑ i =1 i 2 = n ( n +1)(2 n +1) 6 , n ∑ i =1 i 3 = n 2 ( n +1) 2 4 . In general: n ∑ i =1 i m = 1 m +1 [ ( n +1) m +1 - 1 - n ∑ i =1 ( ( i +1) m +1 - i m +1 - ( m +1) i m ) ] n - 1 ∑ i =1 i m = 1 m +1 m ∑ k =0 ( m +1 k ) B k n m +1 - k . Geometric series: n ∑ i =0 c i = c n +1 - 1 c - 1 , c = 1 , ∞ ∑ i =0 c i = 1 1 - c , ∞ ∑ i =1 c i = c 1 - c , &#124; c &#124; < 1 , n ∑ i =0 ic i = nc n +2 - ( n +1) c n +1 + c ( c - 1) 2 , c = 1 , ∞ ∑ i =0 ic i = c (1 - c ) 2 , &#124; c &#124; < 1 Harmonic series: H n = n ∑ i =1 1 i , n ∑ i =1 iH i = n ( n +1) 2 H n - n ( n - 1) 4 . n ∑ i =1 H i = ( n +1) H n - n, n ∑ i =1 ( i m ) H i = ( n +1 m +1 )( H n +1 - 1 m +1 ) . 1. ( n k ) = n ! ( n - k )! k ! , 2. n ∑ k =0 ( n k ) = 2 n , 3. ( n k ) = ( n n - k ) , 4. ( n k ) = n k ( n - 1 k - 1 ) , 5. ( n k ) = ( n - 1 k ) + ( n - 1 k - 1 ) , 6. ( n m )( m k ) = ( n k )( n - k m - k ) , 7. n ∑ k =0 ( r + k k ) = ( r + n +1 n ) , 8. n ∑ k =0 ( k m ) = ( n +1 m +1 ) , 9. n ∑ k =0 ( r k )( s n - k ) = ( r + s n ) , 10. ( n k ) = ( - 1) k ( k - n - 1 k ) , 11. { n 1 } = { n n } = 1 , 12. { n 2 } = 2 n - 1 - 1 , 13. { n k } = k { n - 1 k } + { n - 1 k - 1 } , - 1)! H n - 1 , 16. [ n n ] = 1 , 17. [ n k ] ≥ { n k } , n } = [ n ] = ( n ) , 20. n ∑ [ n ] = n ! , 21. C = 1 ( 2 n ) , |                                            |

Master method:

<!-- formula-not-decoded -->

If ∃ /epsilon1 &gt; 0 such that f ( n ) = O ( n log b a -/epsilon1 ) then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If ∃ /epsilon1 &gt; 0 such that f ( n ) = Ω( n log b a + /epsilon1 ), and ∃ c &lt; 1 such that af ( n/b ) ≤ cf ( n ) for large n , then

<!-- formula-not-decoded -->

Substitution (example): Consider the following recurrence

<!-- formula-not-decoded -->

Note that T i is always a power of two. Let t i = log 2 T i . Then we have

<!-- formula-not-decoded -->

Let u i = t i / 2 i . Dividing both sides of the previous equation by 2 i +1 we get

<!-- formula-not-decoded -->

Substituting we find

<!-- formula-not-decoded -->

which is simply u i = i/ 2. So we find that T i has the closed form T i = 2 i 2 i -1 . Summing factors (example): Consider the following recurrence

<!-- formula-not-decoded -->

Rewrite so that all terms involving T are on the left side

<!-- formula-not-decoded -->

Now expand the recurrence, and choose a factor which makes the left side 'telescope'

## Identities Cont.

<!-- formula-not-decoded -->

## Recurrences

<!-- formula-not-decoded -->

Let m = log 2 n . Summing the left side we get T ( n ) -3 m T (1) = T ( n ) -3 m = T ( n ) -n k where k = log 2 3 ≈ 1 . 58496. Summing the right side we get

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and so T ( n ) = 3 n k -2 n . Full history recurrences can often be changed to limited history ones (example): Consider

<!-- formula-not-decoded -->

Note that

<!-- formula-not-decoded -->

Subtracting we find

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Trees

Every tree with n vertices has n -1 edges.

Kraft inequality: If the depths of the leaves of a binary tree are d 1 , . . . , d n :

<!-- formula-not-decoded -->

and equality holds only if every internal node has 2 sons.

Generating functions:

1. Multiply both sides of the equation by x i .
2. Sum both sides over all i for which the equation is valid.
3. Choose a generating function G ( x ). Usually G ( x ) = ∞ i =0 x i g i .
4. ∑ 3. Rewrite the equation in terms of the generating function G ( x ).
4. Solve for G ( x ).
5. The coefficient of x i in G ( x ) is g i . Example:

<!-- formula-not-decoded -->

Multiply and sum:

<!-- formula-not-decoded -->

We choose G ( x ) = ∑ i ≥ 0 x i g i . Rewrite in terms of G ( x ):

<!-- formula-not-decoded -->

Simplify:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solve for G ( x ):

Expand this using partial fractions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

| Theoretical Computer Science Cheat Sheet                        | Theoretical Computer Science Cheat Sheet                        | Theoretical Computer Science Cheat Sheet                        | Theoretical Computer Science Cheat Sheet                          | Theoretical Computer Science Cheat Sheet                                           |
|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| π ≈ 3 . 14159, e ≈ 2 . 71828, γ ≈ 0 . 57721, φ = 1+ √ 5 2 ≈ 1 . | π ≈ 3 . 14159, e ≈ 2 . 71828, γ ≈ 0 . 57721, φ = 1+ √ 5 2 ≈ 1 . | π ≈ 3 . 14159, e ≈ 2 . 71828, γ ≈ 0 . 57721, φ = 1+ √ 5 2 ≈ 1 . | π ≈ 3 . 14159, e ≈ 2 . 71828, γ ≈ 0 . 57721, φ = 1+ √ 5 2 ≈ 1 .   | 61803, ˆ φ = 1 - √ 5 2 ≈ - . 61803                                                 |
| i                                                               | 2 i                                                             | p i                                                             | General                                                           | Probability                                                                        |
| 1                                                               | 2                                                               | 2                                                               | Bernoulli Numbers ( B i = 0, odd i = 1):                          | Continuous distributions: If                                                       |
| 2                                                               | 4                                                               | 3                                                               | B 0 = 1, B 1 = - 1 , B 2 = 1 , B 4 = - 1 ,                        | b                                                                                  |
| 3                                                               | 8                                                               | 5                                                               | 2 6 30 B 6 = 1 42 , B 8 = - 1 30 , B 10 = 5 66 .                  | Pr[ a < X < b ] = ∫ a p ( x ) dx,                                                  |
| 4                                                               | 16                                                              | 7                                                               | Change of base, quadratic formula:                                | then p is the probability density function of                                      |
| 5                                                               | 32                                                              | 11                                                              | log a x - b ± √ b 2 - 4 ac .                                      | X . If Pr[ X < a ] = P ( a ) ,                                                     |
| 6                                                               | 64                                                              | 13                                                              | log b x = log a b , 2 a                                           | then P is the distribution function of X . If                                      |
| 7                                                               | 128                                                             | 17                                                              | Euler's number e :                                                | P and p both exist then                                                            |
| 8                                                               | 256                                                             | 19                                                              | e = 1+ 1 2 + 1 6 + 1 24 + 1 120 + · · ·                           | P ( a ) = a p ( x                                                                  |
| 9                                                               | 512                                                             | 23                                                              | lim 1+ x n = e x .                                                | ∫ -∞ ) dx.                                                                         |
| 10                                                              | 1,024                                                           | 29                                                              | n →∞ ( n ) 1 n 1 n +1                                             | Expectation: If X is discrete                                                      |
| 11                                                              | 2,048                                                           | 31                                                              | ( 1+ n ) < e < ( 1+ n ) .                                         | E[ g ( X )] = g ( x ) Pr[ X = x ] .                                                |
| 12                                                              | 4,096                                                           | 37                                                              | 1+ 1 n n = e - e 2 n + 11 e 24 n 2 - O ( 1 n 3 ) .                | ∑ x                                                                                |
| 13                                                              | 8,192                                                           | 41                                                              | ( ) Harmonic numbers:                                             | If X continuous then ∞                                                             |
| 14                                                              | 16,384                                                          | 43                                                              | 1, 3 , 11 , 25 , 137 , 49 , 363 140 , 761 280 , 7129 2520 , . . . | E[ g ( X )] = ∫ g ( x ) p ( x ) dx = ∫ ∞ -∞ g ( x ) dP ( x ) .                     |
| 15                                                              | 32,768                                                          | 47                                                              | 2 6 12 60 20                                                      | -∞ Variance, standard deviation:                                                   |
| 16                                                              | 65,536                                                          | 53                                                              | ln n<H n < ln n +1 ,                                              | VAR[ X ] = E[ X 2 ] - E[ X ] 2 ,                                                   |
| 17                                                              | 131,072                                                         | 59                                                              | 1                                                                 | σ = VAR[ X ] .                                                                     |
| 18                                                              | 262,144                                                         | 61                                                              | H n = ln n + γ + O ( n ) .                                        | √ For events A and B :                                                             |
| 19                                                              | 524,288                                                         | 67                                                              | Factorial, Stirling's approximation:                              | Pr[ A ∨ B ] = Pr[ A ] +Pr[ B ] - Pr[ A ∧ B ]                                       |
| 20                                                              | 1,048,576                                                       | 71                                                              | 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, . . .                 | Pr[ A ∧ B ] = Pr[ A ] · Pr[ B ] ,                                                  |
| 21                                                              | 2,097,152                                                       | 73                                                              | n                                                                 | iff A and B are independent.                                                       |
| 22                                                              | 4,194,304                                                       | 79                                                              | n ! = √ 2 πn ( n e ) ( 1+Θ ( 1 n )) .                             | A B ] = Pr[ A ∧ B ] ]                                                              |
| 23                                                              | 8,388,608                                                       | 83                                                              | Ackermann's function and inverse:                                 | Pr[ &#124; Pr[ B                                                                   |
|                                                                 |                                                                 | 89                                                              | 2 j i = 1                                                         | For random variables X and Y :                                                     |
| 24 25                                                           | 16,777,216 33,554,432                                           | 97                                                              | a ( i, j ) =   a ( i - 1 , 2) j = 1                             | E[ X · Y ] = E[ X ] · E[ Y ] ,                                                     |
| 26                                                              | 67,108,864                                                      | 101                                                             | a ( i - 1 ,a ( i, j - 1)) i, j ≥ 2 i } .                          | if X and Y are independent. ,                                                      |
| 27                                                              | 134,217,728                                                     | 103                                                             |  α ( i ) = min { j &#124; a ( j, j ) ≥                           | E[ X + Y ] = E[ X ] +E[ Y ] ] .                                                    |
| 28                                                              | 268,435,456                                                     | 107                                                             | Binomial distribution:                                            | E[ cX ] = c E[ X                                                                   |
| 29                                                              | 536,870,912                                                     | 109                                                             | Pr[ X = k ] = ( n k ) p k q n - k , q = 1 - p,                    | Bayes' theorem:                                                                    |
| 30                                                              | 1,073,741,824                                                   | 113                                                             | n n                                                               | Pr[ A i &#124; B ] = Pr[ B &#124; A i ] Pr[ A i ] n Pr[ A j ] Pr[ B &#124; A j ] . |
| 31                                                              | 2,147,483,648                                                   | 127                                                             | E[ X ] = k ( ) p k q n - k = np.                                  | ∑ j =1 Inclusion-exclusion:                                                        |
| 32                                                              | 4,294,967,296                                                   | 131                                                             | ∑ k =1 k                                                          | n n                                                                                |
| Pascal's Triangle                                               | Pascal's Triangle                                               | Pascal's Triangle                                               | Poisson distribution: λ k                                         | Pr [ ∨ X i ] = ∑ Pr[ X i ]+                                                        |
| 1                                                               | 1                                                               | 1                                                               | Pr[ X = k ] = e - λ k ! , E[ X ] = λ.                             | i =1 i =1 n k                                                                      |
| 1 1                                                             | 1 1                                                             | 1 1                                                             | Normal (Gaussian) distribution:                                   | ∑ ( - 1) k +1 ∑ Pr [ ∧ X i j ] .                                                   |
| 1 2 1                                                           | 1 2 1                                                           | 1 2 1                                                           | p ( x ) = 1 e - ( x - µ ) 2 / 2 σ 2 , E[ X ] = µ.                 | k =2 i i < ··· <i k j =1 Moment inequalities:                                      |
|                                                                 |                                                                 |                                                                 | √ 2 πσ                                                            |                                                                                    |
| 1 3 3 1                                                         | 1 3 3 1                                                         | 1 3 3 1                                                         | The 'coupon collector': We are given a                            | Pr &#124; X &#124; ≥ λ E[ X ] ≤ 1 ,                                                |
| 1 4 6 4 1                                                       | 1 4 6 4 1                                                       | 1 4 6 4 1                                                       | random coupon each day, and there are n                           | [ ] λ 1                                                                            |
| 1 5 10 10 5 1                                                   | 1 5 10 10 5 1                                                   | 1 5 10 10 5 1                                                   | different types of coupons. The distribu-                         | Pr X - E[ X ] ≥ λ · σ ≤ λ 2 .                                                      |
| 1 6 15 20 15 6 1                                                | 1 6 15 20 15 6 1                                                | 1 6 15 20 15 6 1                                                | tion of coupons is uniform. The expected                          | [ ∣ ∣ ∣ ∣ ] Geometric distribution:                                                |
| 1 7 21 35 35 21 7 1 1                                           | 8 28 56 70 56 28                                                | 1                                                               | number of days to pass before we to col- lect all n types is      | Pr[ X = k ] = pq k - 1 , q = 1 - p,                                                |
| 1 9 36 84 126 126 84 36 9 1                                     | 1 9 36 84 126 126 84 36 9 1                                     | 1 9 36 84 126 126 84 36 9 1                                     | nH .                                                              | X ] = ∞ kpq k - 1 = 1 .                                                            |
| 1 10 45                                                         | 120 210 252 210                                                 | 120 45 10                                                       | n                                                                 | E[ ∑ p                                                                             |

tan

a

+

B

cos

a

sec

## Theoretical Computer Science Cheat Sheet

## Trigonometry

<!-- image -->

Pythagorean theorem:

C

=

2

Definitions:

sin csc

a

a

A

=

A/C,

=

C/A,

a

2

.

=

=

=

cot

a

sin

a

A

cos

a

=

B ,

B/C,

C/B,

=

Area, radius of inscribed circle:

1

2

A

AB

+

B

+

AB,

Identities:

sin

x

=

tan

1

csc

1

x

cot

x

=

,

,

x

2

x

= sec

1 + tan sin

x

= cos cos

cot

x

x

2

(

π

2

-

=

-

=

cos(

x,

x

π

cot(

,

-

)

x

)

,

B

A .

a

cos sin

a

=

x

=

C .

cos

2

1

sec

x

,

2

x

= 1

x

sin

+cos

2

= csc

x

1 + cot sin

x

= sin(

tan

x

= cot

π

-

,

)

x

-

csc

x

= cot sin( x ± y ) = sin x cos y ± cos x sin y,

cos( x ± y ) = cos x cos y ∓ sin x sin y,

<!-- formula-not-decoded -->

,

2

x,

π

-

(

x

2

π

2

x

-

)

x

-

cot

2 tan

,

)

x

2

<!-- formula-not-decoded -->

sin 2

cos

x

x,

= 2 sin

x

cos 2

2

= cos

x

cos 2

x

tan 2

x

sin(

= 1

=

x

x

-

-

sin

2

2

2 sin

2 tan x,

x

1

+

tan

y

2

) sin(

x

-

-

x

,

y

cos(

) cos(

x

+

y

x

) = sin

-

Euler's equation:

e

ix

= cos v2.02

x

sin 2

cos 2

x

x

cos 2

cot 2

x

-

x

2

y

=

y, sin

-

y.

) = cos

2

x

2

2

sin

+

i

sin x,

e

iπ

=

-

c

1994 by Steve Seiden sseiden@acm.org

©

http://www.csc.lsu.edu/~seiden

=

1 + tan

2

= 2 cos

x

1

-

2

x

-

=

tan

2

1 + tan

2

x

cot

2 cot

-

1

.

x

x,

,

x,

x

,

1

,

x

x

,

1

,

## Matrices

/negationslash

Multiplication:

<!-- formula-not-decoded -->

Determinants: det A = 0 iff A is non-singular.

det det

A

A

=

= det

n

·

∑

·

sign(

π

i

=1

3 determinant:

∏

∣

∣

∣

×

×

2 and 3

2

∣

b

a

c

∣

d

e

f

∣

∣

h

i

g

∣

∣

Permanents:

Definitions:

e

e

x

b

a

∣

∣

ad

=

∣

=

∣

c

g

∣

∣

∣

∣

∣

∣

∣

=

∣

∣

perm

-

h

-

∣

∣

c

f

∣

aei

∣

∣

-

∣

=

det

A

π

a

)

bc,

∣

+

bfg ceg

a

∣

∣

-

d

B, i,π

i

(

c

f

∣

+

cdh fha

∣

n

∑

∏

∣

∣

-

a

(

i,π

∣

)

)

.

+

i

ibd.

.

i

A

π

=1

i

## Hyperbolic Functions

-

e

-

x

e

x

2

e

+

x

sinh tanh

x

x

=

=

sech

x

-

1

cosh

e

e

x

x

=

Identities:

2

-

sinh

x

cosh

2

coth

x

cosh(

-

-

sinh(

-

-

,

x

2

2

csch

x

x

) = cosh

x

+

cosh(

x

sinh 2

x

x

,

= 1

,

= 1

cosh

x

csch

x

=

=

coth

x

=

+

e

-

1

2

sinh

1

x

tanh

2

tanh

,

x,

y

) = sinh

x

+

x

cosh2

x

cosh

y

cosh

y

x

cosh

) = cosh

= 2 sinh cosh

x

2

= cosh

x

+sinh

(cosh

x

x

+sinh

2

x

=

∣

a

∣

∣

∣

d

x

,

.

x

x

+sech sinh(

-

tanh(

2

x

-

) =

-

x

+cosh

y

x,

2

+sinh

e

n

)

,

x

= cosh

x

2 sinh

-

x

2

,

x

= cosh

1

θ sin θ cos θ tan θ

0

0

1

0

π

√

√

6

π

4

π

3

π

2

1

2

2

√

2

3

√

2

1

3

2

2

√

2

1

2

0

3

3

1

3

√

∞

) =

x

+sinh x,

cosh

x

-

nx

+sinh

2

x

2

x

,

x

= 1

b

e

∣

∣

∣

∣

,

sinh

-

tanh sinh

y, sinh

sinh y,

x

=

nx,

e

n

∈

x, x,

-

x

,

Z

,

2 cosh

= cosh

x

+1

. . . in mathematics you don't understand things, you just get used to them.

- J. von Neumann

.

,

b

e

d

B

2

More Trig.

C

b

h

a

A c B Law of cosines: c 2 = a 2 + b 2 -2 ab cos C. Area:

A

=

hc,

=

1

2

1

2

c

sin ab

2

=

C, sin

sin

A

2 sin

C

Heron's formula:

A

a

b

√

s

s

s

=

s

s

a

s

b

+

b

a, b,

=

=

=

1

·

·

·

2

(

s

s

s

a

-

-

-

c

=

c.

s

More identities:

sin

-

cos tan

cot sin

cos tan

sin

x

cos

1

2

x

2

x

2

x

2

x

x

x

x

√

=

=

=

=

=

=

=

=

=

=

=

=

2

1 + cos

2

1

cos

√

1 + cos

1

-

-

x

cos sin

x

,

sin

x

1 + cos

x

,

√

1 + cos

1

cos

1 + cos

x

-

sin

x

sin

1

e

ix

e

ix

-

i

,

x

-

x

cos

-

-

e

2

i

+

e

2

e

ix

e

ix

e

-

+

2

,

ix ix

,

e

e

ix

-

i

e

2

ix

=

sinh

-

-

ix

-

1

+1

ix

i

,

cos

x

= cosh ix,

tan x = tanh ix i .

ix

,

-

+

c

√

B

s

)

.

c

,

,

x

,

x

x

x

x

x

,

,

,

,

,

## Theoretical Computer Science Cheat Sheet

## Number Theory

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

/negationslash

<!-- formula-not-decoded -->

if m i and m j are relatively prime for i = j . Euler's function: φ ( x ) is the number of positive integers less than x relatively prime to x . If ∏ n i =1 p e i i is the prime factorization of x then n

Euler's theorem: If a and b are relatively prime then

<!-- formula-not-decoded -->

Fermat's theorem:

<!-- formula-not-decoded -->

The Euclidean algorithm: if a &gt; b are integers then

<!-- formula-not-decoded -->

If ∏ n i =1 p e i i is the prime factorization of x then

<!-- formula-not-decoded -->

Perfect Numbers: x is an even perfect number iff x = 2 n -1 (2 n -1) and 2 n -1 is prime.

Wilson's theorem:

n

is a prime iff

<!-- formula-not-decoded -->

M¨ obius inversion:

1

= 1.

i

if

µ

(

i

) =









If



0

(

if

i

is not square-free.

-

1)

r

if

i

is the product of

r

distinct primes.

<!-- formula-not-decoded -->

then

<!-- formula-not-decoded -->

Prime numbers:

p n = n ln n + n ln ln n n + n ln ln n

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Graph Theory

## Definitions:

Loop

An edge connecting a ver- tex to itself.

## Directed Simple

Each edge has a direction. Graph with no loops or multi-edges.

Walk

A sequence v 0 e 1 v 1 . . . e /lscript v /lscript .

Trail

Awalk with distinct edges.

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

Hamiltonian

Graph with a cycle visiting each vertex exactly once.

Cut

A set of edges whose re- moval increases the num- ber of components.

Cut-set A minimal cut.

Cut edge

A size 1 cut.

k-Connected vertices.

A graph connected with the removal of any k - 1

k-Tough

∀ S ⊆ V, S = ∅ we have k · c ( G - S ) ≤ | S | .

k-Regular

A graph where all vertices

have degree k .

k-Factor

A k -regular spanning subgraph.

Matching

A set of edges, no two of which are adjacent.

Clique

A set of vertices, all of which are adjacent.

Ind. set

A set of vertices, none of which are adjacent.

Vertex cover A set of vertices which cover all edges.

Planar graph A graph which can be em- beded in the plane.

Plane graph An embedding of a planar graph.

$$∑ v ∈ V deg( v ) = 2 m.$$

/negationslash

<!-- formula-not-decoded -->

Any planar graph has a vertex with degree ≤ 5.

## Notation:

E

(

G

)

Edge set

V ( G ) Vertex set

c ( G ) Number of components

G [ S ] Induced subgraph

deg( v ) Degree of v

∆( G ) Maximum degree

δ ( G ) Minimum degree

χ ( G ) Chromatic number

χ E ( G ) Edge chromatic number

G c Complement graph

K n Complete graph

K n 1 ,n 2 Complete bipartite graph

r( k, /lscript ) Ramsey number

## Geometry

Projective coordinates: triples ( x, y, z ), not all x , y and z zero.

(

) = (

cx, cy, cz x, y, z

)

## Cartesian Projective

(

∀

x, y

(

x, y,

1)

)

y

m,

(

, b

1

=

mx

+

b

)

(1

x = c -Distance formula, L p and L ∞ metric:

)

,

c

,

0

-

<!-- formula-not-decoded -->

Area of triangle ( x 0 , y 0 ), ( x 1 , y 1 ) and ( x 2 , y 2 ):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

∣ ∣ Angle formed by three points:

<!-- image -->

Line through two points ( x 0 , y 0 ) and ( x 1 , y 1 ):

<!-- formula-not-decoded -->

∣ ∣ ∣ Area of circle, volume of sphere:

<!-- formula-not-decoded -->

If I have seen farther than others, it is because I have stood on the shoulders of giants.

- Issac Newton

c

/negationslash

= 0

.

(

x

π

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Brouncker's continued fraction expansion:

Gregrory's series:

<!-- formula-not-decoded -->

Newton's series:

<!-- formula-not-decoded -->

Sharp's series:

<!-- formula-not-decoded -->

Euler's series:

<!-- formula-not-decoded -->

## Partial Fractions

Let N ( x ) and D ( x ) be polynomial functions of x . We can break down N ( x ) /D ( x ) using partial fraction expansion. First, if the degree of N is greater than or equal to the degree of D , divide N by D , obtaining

<!-- formula-not-decoded -->

where the degree of N ′ is less than that of D . Second, factor D ( x ). Use the following rules: For a non-repeated factor:

N

-

(

a

x

)

A

)

D

(

x

)

=

x

-

a

where

+

<!-- formula-not-decoded -->

For a repeated factor:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

.

The reasonable man adapts himself to the world; the unreasonable persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable. - George Bernard Shaw

N

′

D

(

(

x

x

)

)

,

## Theoretical Computer Science Cheat Sheet

## Calculus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Derivatives:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Integrals:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

/negationslash

/negationslash

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- image -->

Expansions:

<!-- formula-not-decoded -->

## Escher's Knot

<!-- image -->

## Stieltjes Integration

<!-- formula-not-decoded -->

If the integrals involved exist, and F possesses a derivative F ′ at every point in [ a, b ] then

<!-- formula-not-decoded -->

00 47 18 76 29 93 85 34 61 52 86 11 57 28 70 39 94 45 02 63 95 80 22 67 38 71 49 56 13 04 59 96 81 33 07 48 72 60 24 15 73 69 90 82 44 17 58 01 35 26 68 74 09 91 83 55 27 12 46 30 37 08 75 19 92 84 66 23 50 41 14 25 36 40 51 62 03 77 88 99 21 32 43 54 65 06 10 89 97 78 42 53 64 05 16 20 31 98 79 87

The Fibonacci number system: Every integer n has a unique representation

<!-- formula-not-decoded -->

## Fibonacci Numbers

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Cramer's Rule

If we have equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

Let A = ( a i,j ) and B be the column matrix ( b i ). Then there is a unique solution iff det A = 0. Let A i be A with column i replaced by B . Then x i = det A i det A .

Improvement makes strait roads, but the crooked roads without Improvement, are roads of Genius.

- William Blake (The Marriage of Heaven and Hell)

## Theoretical Computer Science Cheat Sheet

## Series