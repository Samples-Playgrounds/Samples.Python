Theoretical Computer Science Cheat Sheet


Definitions Series



f (n) = O(g(n)) iff ∃ positive c, n0 such that
0 f (n) cg(n) n n0.
≤ ≤ ∀ ≥

f (n) = Ω(g(n)) iff ∃ positive c, n0 such that
f (n) cg(n) 0 n n0.
≥ ≥ ∀ ≥

f (n) = Θ(g(n)) iff f (n) = O(g(n)) and
f (n) = Ω(g(n)).


f (n) = o(g(n)) iff limn→∞ f (n)/g(n) = 0.

lim iff ǫ > 0, n0 such that
n→∞ [a][n][ =][ a] an ∀ a < ǫ, ∃n n0.
|                 - | ∀ ≥

sup S least b ∈ R such that b ≥ s,
∀s ∈ S.

inf S greatest b ∈ R such that b ≤
s, ∀s ∈ S.

lim inf lim
n→∞ [a][n] n→∞ [inf][{][a][i][ |][ i][ ≥] [n, i][ ∈] [N][}][.]



Hn =



�n



i = [n][(][n][ + 1)]

2

i=1



�n



�n



,
2



i [2] = [n][(][n][ + 1)(2][n][ + 1)]

6

i=1



,
6





i [3] = [n][2][(][n][ + 1)][2]

4

i=1



.
4



In general:
�n

1
i [m] =
m + 1
i=1



In general:
�n




(n + 1) [m][+1] - 1 −



�n




(i + 1) [m][+1] i [m][+1] (m + 1)i [m][��]

    -    


i=1



n�−1 1

i [m] =
m + 1
i=1



n�−1



�m


k=0




m + 1
k




Bkn [m][+1][−][k] .



Geometric series:
�n [n][+1]



�n

c [i] = [c][n][+1][ −] [1]

c 1

i=0 


�∞



�∞



c
c [i] = c < 1,
1 c [,] | |
i=1 


�∞



1
c [i] =
1 c [,]
i=0 


�n

ic [i] = [nc][n][+2][ −] [(][n][ + 1)][c][n][+1][ +][ c]

(c 1) [2]

i=0 


�n



, c = 1,
c 1 ̸
 


c
ic [i] = c < 1.
(1 c) [2][,] | |
i=0 


Harmonic series:



, c = 1,
(c 1) [2] ̸
 



[ + 1)]

Hn
2 - [n][(][n][ −] 4 [1)]



�n



iHi = [n][(][n][ + 1)]

2

i=1



.
4



��
1
Hn+1
    - m + 1




.



�n


i=1



1

i [,]



1



lim sup lim
n→∞ [a][n] n→∞ [sup][{][a][i][ |][ i][ ≥] [n, i][ ∈] [N][}][.]




i
m




- n + 1
Hi =
m + 1



�n


i=1




 - n
k



k Combinations: Size k sub
sets of a size n set.

- nk Stirling numbers (1st kind):



�n

i=1 Hi = (n + 1)Hn − n,




 n
1.
k

 n
4.
k

 n
6.
m




n!
= 2.
(n k)!k! [,]

- - − 



= [n]




n − 1

- k −�1



�n




n
k




- n
= 2 [n], 3.
k




, 7.



k=0



�n




- n
k



Stirling numbers (1st kind):
Arrangements of an n element set into k cycles.



��
m
k



k Stirling numbers (2nd kind):

Partitions of an n element
set into k non-empty sets.

- nk 1st order Eulerian numbers:



8.



k




- k=0 n
, 5.
k



��
n − k
m − k




, 9.



�n




- n
=

 - �n − k

1 n 1

+  
 - k − 1




- n 1
= k




r + k
k



��
s
n� − k�




- n
=
k




- k=0 n
, 11.
1



k=0




- r + n + 1
=
n




- n
=
n




= 1,




,

,

,


,



k 1st order Eulerian numbers:

Permutations π1π2 . . . πn on
{1, 2, . . ., n} with k ascents.
�� ��
nk 2nd order Eulerian numbers.



�n



k=0




k
m




- k n 1
= ( 1) [k]  -  
  - k




r
k



k=0




- n + 1
=
m + 1




- r + s
=
n




,



2nd order Eulerian numbers.



k=0�

n
10.
k

  n
12.
2




- n 1
+  k 1

 -  - −�



Cn Catalan Numbers: Binary
trees with n + 1 vertices.




- n
= 2 [n][−][1] 1, 13.

   - k




  n
14.
1

  n
18.
k

  n
22.
0

  0
25.
k




- n
= (n 1)!, 15.
   - 2




- n
= (n − 1)!Hn−1, 16. n




- n 1
= k  k




- n
≥ k




- n 1
= (n 1)     - k




- n
, 19.
n 1

  -  - −�




- n
, 24.
k




- n
=
2




, 20.



k=0




 - n
= 1, 17.
k




1
= n!, 21. Cn =
n + 1




2n
n




,

,

,

,

,



�n




- n
=
n 1

- 



- n
= 1, 23.
k




- n 1
+ k − 1




- n
=
n 1 k

 -  - −  



- n
=
n 1

     - −



�k=0 n 1
= (k + 1)  k




- n 1
+ (n k)     - k 1

    -    



n
k




- - 1 if k = 0, n
= 26.
0 otherwise 1




- n + 1
= 3 [n] (n + 1)2 [n] +

  - 2




=



k=0




- n
= 2 [n] n 1, 27.

  -   - 2




n + 1
k




- n
(m + 1 k) [n] ( 1) [k], 30. m!
    -     - m



�� ��
n
= 1, 33.
n




=



k=0




n
k

�n



��
x + k
n



�m



�n



28. x [n] =



�n




n
k



��
k
n − m




  n
31.
m

��
n
34.
k



�k=0
=



�� ��
n 1
= (k + 1)  k




=




- n
, 29.
m



��
, 35.




n
k



k=0



��
n − k
m



�n




- ��
n
( 1) [n][−][k][−][m] k!, 32.

 - 0



�� ��
n 1
+ (2n 1 k)      -    - k 1
         



=



�n



��
= 0 for n ̸= 0,



��
= [(2][n][)][n]



��
n
k




  x
36.
x − n



�n


k=0



��
n
k



���
x + n − 1 − k
2n




- n + 1
, 37.
m + 1





 =


k




- ��
n k
k m



k=0



k=0




k
m




(m + 1) [n][−][k],



,
2 [n]


Theoretical Computer Science Cheat Sheet





 =




 =



���
x + k
2n




(−1) [m][−][k],




,




  n + 1
38.
m + 1





 =



��
k
m




=




- k=0 k=0 n
( 1) [n][−][k], 41.

 - m




n [n][−][k] = n!



Identities Cont. Trees



k=0



�n



�n




- x
, 39.

    -    - x − n



�n



��
n
k



��
k
m




n
k



��
k + 1
m + 1




k
m



1
k!




k
m




  n
40.
m





 =



k



k



�m 
n + k
k
k
k=0



k=0




- m + n + 1
, 43.
m




- k=0
n + 1
k + 1



k=0




,



�k
n
k




=



�m



�m 
n + k
k(n + k)
k
k=0



�m





 =



k




=




- k=0
(−1) [m][−][k], for n ≥ m,




  m + n + 1
42.
m




  n
44.
m





 =



�k

 =



��
k
m




- n
( 1) [m][−][k], 45. (n m)!

 - - m



��
m + n
n + k



k



��
k
m




m − n
m + k



��
m + n
n + k




- k
n + 1
k + 1




 n + 1
k + 1


 =




  n
46.

  - n − m
n
48.
ℓ + m



k



��
m + k
k



��k
ℓ + m
ℓ



Every tree with n
vertices has n − 1
edges.


Kraft inequality: If the depths
of the leaves of
a binary tree are
d1, . . ., dn:
�n

2 [−][d][i] ≤ 1,
i=1


and equality holds
only if every internal node has 2
sons.



k




m − n
m + k


 =





 =



�� k
ℓ + m
ℓ



k



��
n − k
m



��
n
k




- - k
n
, 47.

- n −� m




- n
, 49.
ℓ + m



k



k



��
n − k
m



��
m + k
k



��
n
k




,

.




k
ℓ




k
ℓ



Recurrences



Master method:
T (n) = aT (n/b) + f (n), a ≥ 1, b > 1

If ∃ǫ > 0 such that f (n) = O(n [log][b][ a][−][ǫ] )
then
T (n) = Θ(n [log][b][ a] ).


If f (n) = Θ(n [log][b][ a] ) then
T (n) = Θ(n [log][b][ a] log2 n).

If ∃ǫ > 0 such that f (n) = Ω(n [log][b][ a][+][ǫ] ),
and ∃c < 1 such that af (n/b) ≤ cf (n)
for large n, then
T (n) = Θ(f (n)).


Substitution (example): Consider the
following recurrence
Ti+1 = 2 [2][i]    - Ti [2][,] T1 = 2.

Note that Ti is always a power of two.
Let ti = log2 Ti. Then we have
ti+1 = 2 [i] + 2ti, t1 = 1.

Let ui = ti/2 [i] . Dividing both sides of
the previous equation by 2 [i][+1] we get
ti+1 2 [i]
2 [i][+1][ =] 2 [i][+1][ +][ t] 2 [i][i][ .]



and so T (n) = 3n [k] - 2n. Full history recurrences can often be changed to limited
history ones (example): Consider




 -  1�T (n) − 3T (n/2) = n




 -  3 T (n/2) − 3T (n/4) = n/2



... ... ...




             3 [log][2][ n][−][1][�] T (2) 3T (1) = 2
      


Let m = log2 n. Summing the left side
we get T (n) − 3 [m] T (1) = T (n) − 3 [m] =
T (n) − n [k] where k = log2 3 ≈ 1.58496.
Summing the right side we get
m�−1 n m�−1     -     


Generating functions:
1. Multiply both sides of the equation by x [i] .
2. Sum both sides over all i for
which the equation is valid.
3. Choose a generating function
G(x). Usually G(x) = [�][∞] i=0 [x][i][g][i][.]
3. Rewrite the equation in terms of
the generating function G(x).
4. Solve for G(x).
5. The coefficient of x [i] in G(x) is gi.
Example:
gi+1 = 2gi + 1, g0 = 0.



m�−1



3 �i

2 .



i=0




3



i=0



n
2 [i][ 3][i][ =][ n]



Let c = [3]



2 [. Then we have]







x [i] .
i≥0



Multiply and sum:

 



- 
gi+1x [i] =
i≥0 i≥0




- 
2gix [i] +
i≥0 i≥0



n



m�−1 - cm 1

c [i] = n   
c 1

i=0 


m�−1



c − 1



= 2n(c [log][2][ n] - 1)



= 2n(c [(][k][−][1) log][c][ n] - 1)



We choose G(x) = [�] i 0 [x][i][g][i][. Rewrite]
≥
in terms of G(x):

    
G(x) g0
     - = 2G(x) + x [i] .




   
) g0
 - = 2G(x) +

x



x [i] .
i≥0



= 2n [k] - 2n,



(x) 1

= 2G(x) +
x 1 x [.]
        


2 [i]

2 [i][+1][ +][ t] 2 [i]



2 [i][ .]



Simplify:
G(x)



Substituting we find
ui+1 = 2 [1] [+][ u][i]



2 [,]



Solve for G(x):
x
G(x) =
(1 x)(1 2x) [.]
        -        


2 [1] [+][ u][i][,] u1 = [1] 2



�i−1

Tj, T0 = 1.
j=0



which is simply ui = i/2. So we find
that Ti has the closed form Ti = 2 [i][2][i][−][1] .
Summing factors (example): Consider
the following recurrence
T (n) = 3T (n/2) + n, T (1) = 1.


Rewrite so that all terms involving T
are on the left side
T (n) − 3T (n/2) = n.

Now expand the recurrence, and choose
a factor which makes the left side “telescope”



Ti = 1 +


Note that



Expand this using partial fractions:




   2 1
G(x) = x
1 2x 1 x

   - [−]   










Ti+1 = 1 +


Subtracting we find



�i

Tj.
j=0



x [i]
i≥0











 2



= x




 =



(2 [i][+1]  - 1)x [i][+1] .
i≥0



Ti+1 − Ti = 1 +


= Ti.



�i

Tj 1
j=0 - 


�i−1

Tj
j=0



�i−1




- 
2 [i] x [i]  i≥0 i≥0



And so Ti+1 = 2Ti = 2 [i][+1] .



So gi = 2 [i] - 1.


Theoretical Computer Science Cheat Sheet



2√5 1.61803, φˆ = [1][−] 2√
≈



√
π 3.14159, e 2.71828, γ 0.57721, φ = [1+] 2
≈ ≈ ≈



2 5 .61803
≈−



i 2 [i] pi General Probability



1 2 2 Bernoulli Numbers (Bi = 0, odd i ̸= 1):

2 4 3 B0 = 1, B1 = − 2 [1] [,][ B][2][ =][ 1] 6 [,][ B][4][ =][ −] 30 [1] [,]



Continuous distributions: If



p(x) dx,
a



2 4 3


3 8 5
4 16 7



2 [,][ B][2][ =][ 1] 6

[1]



6 [,][ B][4][ =][ −] 30 [1]



= 1,B6 = B4211 = [,][ B] - [8][ =] 2 [,][ −][ B][2] 30 [1][ =][,][ B][ 1] 6 [10][,][ B][ =][4][ =] 665 [ −][.] 30 [,]



then p is the probability density function of
X. If
Pr[X < a] = P (a),
then P is the distribution function of X. If
P and p both exist then




       - b
Pr[a < X < b] =



5
30 [1] [,][ B][10][ =] 66 [.]



Change of base, quadratic formula:



b [2] 4ac

 - .
2a



5 32 11
6 64 13


7 128 17
8 256 19


9 512 23
10 1,024 29


11 2,048 31
12 4,096 37


13 8,192 41
14 16,384 43


15 32,768 47


16 65,536 53
17 131,072 59


18 262,144 61
19 524,288 67


20 1,048,576 71
21 2,097,152 73


22 4,194,304 79
23 8,388,608 83


24 16,777,216 89
25 33,554,432 97


26 67,108,864 101
27 134,217,728 103



logb x = [log][a][ x]



α(i) = min{j | a(j, j) ≥ i}.




[log][a][ x] −b ± √

loga b [,] 2



Euler’s number e:



e = 1 + [1]




[1]

2 [+][ 1] 6




[ 1] 6 [+][ 1]




[ 1] 24 [+] 1201 [+][ · · ·]

 



   - a
P (a) =



p(x) dx.
−∞




    - �n

lim 1 + [x] = e [x] .

�1 +n→∞ [1] �n < e <n �1 + [1] �n



lim
n→∞




1 + [x]



n



�1 + n [1] �n < e < �1 + n [1] �n+1� .

 - �n e
1 + [1] = e

[+ 11][e]

[O]



n [1] �n < e < �1 + n [1]



Expectation: If X is discrete



If X continuous then




  E[g(X)] =



g(x) Pr[X = x].

x



�n e
n [1] = e − 2n




   
[e] 1

24n [2][ −] [O] n [3]



e

2n [+ 11] 24n [e]



n [3]




.



g(x) dP (x).
−∞



Harmonic numbers:



1, [3]



6 [,][ 25] 12




[3]

2 [,][ 11] 6



12 [,][ 137] 60



60 [,][ 49] 20



20 [,][ 363] 140



140 [,][ 761] 280



280 [,][ 7129] 2520



2520 [, . . .]




     ∞
E[g(X)] =



Variance, standard deviation:
VAR[X] = E[�X [2] ] − E[X] [2],




       
∞ ∞

g(x)p(x) dx =
−∞ −∞



ln n < Hn < ln n + 1,




 σ =




      1
Hn = ln n + γ + O



n




.



Factorial, Stirling’s approximation:


1, 2, 6, 24, 120, 720, 5040, 40320, 362880, . . .



σ = VAR[X].

For events A and B:
Pr[A ∨ B] = Pr[A] + Pr[B] − Pr[A ∧ B]



Pr[A ∧ B] = Pr[A] · Pr[B],
iff A and B are independent.



Pr[A B] = [Pr[][A][ ∧] [B][]]
| Pr[B]




  n
2πn



n! = √



e



�n� - 1 ��
1 + Θ .

n



Ackermann’s function and inverse:



2 [j] i = 1
a(i − 1, 2) j = 1
a(i − 1, a(i, j − 1)) i, j ≥ 2



if X and Y are independent.



Pr[B]
For random variables X and Y :
E[X · Y ] = E[X] · E[Y ],



a(i, j) =











28 268,435,456 107 Binomial distribution:



E[X + Y ] = E[X] + E[Y ],

E[cX] = c E[X].
Bayes’ theorem:



Pr[Ai B] = �nPr[B|Ai] Pr[Ai]
| j=1 [Pr[][A][j][] Pr[][B][|][A][j] []] [.]



29 536,870,912 109
30 1,073,741,824 113


31 2,147,483,648 127
32 4,294,967,296 131


Pascal’s Triangle


1


1 1
1 2 1


1 3 3 1
1 4 6 4 1


1 5 10 10 5 1
1 6 15 20 15 6 1


1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1


1 9 36 84 126 126 84 36 9 1
1 10 45 120 210 252 210 120 45 10 1




    n
Pr[X = k] =
k




p [k] q [n][−][k], q = 1 − p,



Inclusion-exclusion:



�n




p [k] q [n][−][k] = np.



E[X] =



�n 
n
k
k
k=1



�n

Pr[Xi] +
i=1



Poisson distribution:

Pr[X = k] = [e][−][λ][λ][k], E[X] = λ.

k!

Normal (Gaussian) distribution:

1
p(x) = √2πσ [e][−][(][x][−][µ][)][2][/][2][σ][2] [,] E[X] = µ.

The “coupon collector”: We are given a
random coupon each day, and there are n
different types of coupons. The distribution of coupons is uniform. The expected
number of days to pass before we to collect all n types is
nHn.




  - �n
Pr



�n 
Xi =
i=1



E[X] =



�n




 - - �k

Pr
ii<···<ik j=1



�n 
(−1) [k][+1]
k=2 ii<



�k 
Xij .
j=1



Moment inequalities:




  -  Pr X λ E[X]
| | ≥ ≤ λ [1]



λ [,]



��� ��   Pr X E[X] λ σ
   - ≥   - ≤ λ [1][2]



λ [2][ .]



Geometric distribution:
Pr[X = k] = pq [k][−][1], q = 1 − p,



p [.]



�∞



kpq [k][−][1] = [1]

p

k=1


Theoretical Computer Science Cheat Sheet


Trigonometry Matrices More Trig.



�n

ai,kbk,j.

k=1



C











Multiplication:


C = A · B, ci,j =





A





Law of cosines:
c [2] = a [2] +b [2] −2ab cos C.











Determinants: det A ̸= 0 iff A is non-singular.



det A · B = det A · det B,



|Col1|Col2|(0,1)|Col4|
|---|---|---|---|
|c<br>a<br>b<br>C<br>(-1,0)||θ<br>|(1,0<br>(cos|
|c<br>a<br>b<br>C<br>(-1,0)||||
|||||
|||(0,-1)|(0,-1)|


Pythagorean theorem:
C [2] = A [2] + B [2] .



A = 2 [1] [hc,]



Area:






  det A =



�n



π



sign(π)ai,π(i).
i=1



2 [ab][ sin][ C,]



Definitions:
sin a = A/C, cos a = B/C,
csc a = C/A, sec a = C/B,



2 × 2 and 3 × 3 determinant:
a b
���� c d ���� = ad



= [1]



Heron’s formula:


A = s sa sb sc,

[√]     -     -     s = [1] 2 [(][a][ +][ b][ +][ c][)][,]



= [c][2][ sin][ A][ sin][ B]



����



a b
���� + i ����
d e



b c
= g ����
������ e f



a c
���� h ����

 - d f



tan a = [sin][ a]



cot a = [cos][ a]
B [,] sin a




[sin][ a]

cos a [=][ A] B




[cos][ a]

sin a [=][ B] A



A [.]



.
2 sin C



a b
���� c d ���� = ad − bc,

a b c

b c a

d e f = g ���� ���� h ����

������ ������ e f - d



a b c
d e f
g h i



Area, radius of inscribed circle:

1 AB
2 [AB,]
A + B + C [.]


Identities:

1 1
sin x = cos x =
csc x [,] sec x [,]

1
tan x = sin [2] x + cos [2] x = 1,
cot x [,]

1 + tan [2] x = sec [2] x, 1 + cot [2] x = csc [2] x,



aei + bfg + cdh
=

      - ceg − fha − ibd.
Permanents:



sa = s − a,
sb = s − b,

sc = s − c.




  perm A =


π



�n

ai,π(i).
i=1



Hyperbolic Functions



Definitions:




[e][−][x], cosh x = [e][x][ +][ e][−][x]

2 2



sinh x = [e][x][ −] [e][−][x]



,
2



More identities:













1 cos x
 -,

2



1 − cos x



sin [x] 2 [=]



cos [x] 2 [=]




   
π2, sin x = sin(π x),

[−] [x]  


tanh x = [e][x][ −] [e][−][x]



1

[e][x][ −] [e][−][x] csch x =

e [x] + e [−][x][,] sinh x [,]




     sin x = cos π



1 + cos x

,
2



1 + cos x




                    cos x = cos(π x), tan x = cot π2
   -    


1 1
sech x = coth x =
cosh x [,] tanh x [.]



Identities:

cosh [2] x − sinh [2] x = 1, tanh [2] x + sech [2] x = 1,

coth [2] x − csch [2] x = 1, sinh(−x) = − sinh x,

cosh(−x) = cosh x, tanh(−x) = − tanh x,

sinh(x + y) = sinh x cosh y + cosh x sinh y,


cosh(x + y) = cosh x cosh y + sinh x sinh y,


sinh 2x = 2 sinh x cosh x,


cosh 2x = cosh [2] x + sinh [2] x,

cosh x + sinh x = e [x], cosh x − sinh x = e [−][x],

(cosh x + sinh x) [n] = cosh nx + sinh nx, n ∈ Z,



1 − cos x
1 + cos x [,]



tan [x] 2 [=]



cot x = cot(π x), csc x = cot [x] 2
   -    



   
π2,

[−] [x]



2

[−] [cot][ x,]



= [1][ −] [cos][ x],

sin x



sin(x ± y) = sin x cos y ± cos x sin y,

cos(x ± y) = cos x cos y ∓ sin x sin y,



cot [x] 2 [=]



sin x
=
1 + cos x [,]







tan(x y) = [tan][ x][ ±][ tan][ y]
± 1 tan x tan

∓

cot(x y) = [cot][ x][ cot][ y][ ∓] [1]
± cot x cot y



1 + cos x
1 cos x [,]
 


1 tan x tan y [,]
∓



= [1 + cos][ x]



,
sin x



cot x cot y [,]
±



2 tan x
sin 2x = 2 sin x cos x, sin 2x =
1 + tan [2] x [,]

cos 2x = cos [2] x − sin [2] x, cos 2x = 2 cos [2] x − 1,



sin x
=
1 cos x [,]
  


sin x = [e][ix][ −] [e][−][ix]



cos 2x = 1 2 sin [2] x, cos 2x = [1][ −] [tan][2][ x]
     - 1 + tan [2] x


2 tan x
tan 2x = cot 2x = [cot][2][ x][ −] [1]
1 tan [2] x [,] 2 cot x
     


1 + tan [2] x [,]



cos x = [e][ix][ +][ e][−][ix]



,
2i

[ e][−][ix]

,
2



,
2 cot x




[ x] 2 [= cosh][ x][ −] [1][,] 2 cosh [2][ x] 2



2 sinh [2][ x]



2 [= cosh][ x][ + 1][.]



tan x = i [e][ix][ −] [e][−][ix]
    - e [ix] + e [−][ix]



= i [e][2][ix][ −] [1]
 - e [2][ix] + 1



e [ix] + e [−][ix][,]



sin(x + y) sin(x − y) = sin [2] x − sin [2] y,



θ sin θ cos θ tan θ . . . in mathematics

y) cos(x y) = cos [2] x sin [2] y. you don’t under    -     - 0 0 1 0

π 1 √3 √3 stand things, you
6 2 2 3 just get used to

e [ix] = cos x + i sin x, e [iπ] = −1. π4 √22 √22 1 them.

v2.02 c 1994 by Steve Seiden π √3 1  - J. von Neumann
http://www.csc.lsu.edu/~seidensseiden@acm.org⃝ π32 12 02 √∞3



e [2][ix] + 1 [,]



cos(x + y) cos(x − y) = cos [2] x − sin [2] y.



θ sin θ cos θ tan θ



√



sin x = [sinh][ ix],

i



Euler’s equation:
e [ix] = cos x + i sin x, e [iπ] = −1.



0 0 1 0
π 1 √3 √3
6 2 2 3



π 1 3 3
6 2 2 3

π4 √22 √22 1



2
2



3
2



√

2

√



22 1



π
3



√

2

√



3 1
√
2 2



3 2 2 3

π2 1 0
∞



cos x = cosh ix,

tan x = [tanh][ ix] .

i


Theoretical Computer Science Cheat Sheet


Number Theory Graph Theory



The Chinese remainder theorem: There exists a number C such that:


C ≡ r1 mod m1
... ... ...

C ≡ rn mod mn

if mi and mj are relatively prime for i ̸= j.

Euler’s function: φ(x) is the number of
positive integers less than x relatively
prime to x. If [�][n] i=1 [p][e] i [i] is the prime factorization of x then



Notation:
E(G) Edge set
V (G) Vertex set
c(G) Number of components
G[S] Induced subgraph
deg(v) Degree of v
∆(G) Maximum degree
δ(G) Minimum degree
χ(G) Chromatic number
χE(G) Edge chromatic number
G [c] Complement graph
Kn Complete graph
Kn1,n2 Complete bipartite graph
r(k, ℓ) Ramsey number


Geometry


Projective coordinates: triples
(x, y, z), not all x, y and z zero.

(x, y, z) = (cx, cy, cz) ∀c ̸= 0.

Cartesian Projective



Area of circle, volume of sphere:
A = πr [2], V = 3 [4] [πr][3][.]



�n



φ(x) =



pi [e][i][−][1] (pi 1).
i=1 


Euler’s theorem: If a and b are relatively
prime then
1 ≡ a [φ][(][b][)] mod b.

Fermat’s theorem:
1 ≡ a [p][−][1] mod p.

The Euclidean algorithm: if a > b are integers then
gcd(a, b) = gcd(a mod b, b).

If [�][n] i=1 [p] i [e][i] is the prime factorization of x
then



(x1 x0) [2] + (y1 y0) [2],

- - x1 x0 + y1 y0,
|  -  - | [p] |  - | [p][�][1][/p][�]



(x, y) (x, y, 1)
y = mx + b (m, −1, b)
x = c (1, 0, −c)
Distance formula, Lp and L
∞
metric:

 



 S(x) =



�n



d =
d|x



i=1



p [e] i [i][+1] - 1 .
pi 1
  


Perfect Numbers: x is an even perfect number iff x = 2 [n][−][1] (2 [n] −1) and 2 [n] −1 is prime.
Wilson’s theorem: n is a prime iff
(n − 1)! ≡−1 mod n.



Definitions:
Loop An edge connecting a vertex to itself.
Directed Each edge has a direction.
Simple Graph with no loops or
multi-edges.
Walk A sequence v0e1v1 . . . eℓvℓ.
Trail A walk with distinct edges.
Path A trail with distinct
vertices.
Connected A graph where there exists
a path between any two
vertices.
Component A maximal connected
subgraph.
Tree A connected acyclic graph.
Free tree A tree with no root.
DAG Directed acyclic graph.
Eulerian Graph with a trail visiting
each edge exactly once.
Hamiltonian Graph with a cycle visiting
each vertex exactly once.
Cut A set of edges whose removal increases the number of components.
Cut-set A minimal cut.
Cut edge A size 1 cut.
k-Connected A graph connected with
the removal of any k − 1
vertices.
k-Tough ∀S ⊆ V, S ̸= ∅ we have
k · c(G − S) ≤|S|.
k-Regular A graph where all vertices
have degree k.
k-Factor A k-regular spanning
subgraph.
Matching A set of edges, no two of
which are adjacent.
Clique A set of vertices, all of
which are adjacent.
Ind. set A set of vertices, none of
which are adjacent.
Vertex cover A set of vertices which
cover all edges.
Planar graph A graph which can be embeded in the plane.
Plane graph An embedding of a planar
graph.

  



   lim x1 x0 + y1 y0 .
p→∞ | - | [p] | - | [p][�][1][/p]

Area of triangle (x0, y0), (x1, y1)
and (x2, y2):



1 x1 x0 y1 y0
2 [abs] ���� x2 − x0 y2 − y0
    -    


���� .



M¨obius inversion:



1 if i = 1.
0 if i is not square-free.
(−1) [r] if i is the product of
r distinct primes.



Angle formed by three points:





µ(i) =













If G(a) = F (d),

d|a



ℓ1 (x1, y1)



(0, 0)



ℓ1



then F (a) =



d




- 
a
µ(d)G

d

d|a



cos θ = [(][x][1][, y][1][)][ ·][ (][x][2][, y][2][)] .

ℓ1ℓ2




.



= 0.
������



Prime numbers:
pn = n ln n + n ln ln n n + n [ln ln][ n]
           - ln n



Line through two points (x0, y0)
and (x1, y1):

x y 1
x0 y0 1 = 0.

������ ������



x y 1
x0 y0 1
x1 y1 1



ln n




 n
+ O



ln n




,



n n 2!n
π(n) =
ln n [+] (ln n) [2][ +] (ln n) [3]



If G is planar then n − m + f = 2, so
f ≤ 2n − 4, m ≤ 3n − 6.



deg(v) = 2m.
v∈V



Any planar graph has a vertex with degree ≤ 5.




 n
+ O
(ln n) [4]




.



If I have seen farther than others,
it is because I have stood on the
shoulders of giants.

- Issac Newton


Theoretical Computer Science Cheat Sheet


π Calculus



Wallis’ identity:



π = 2 [2][ ·][ 2][ ·][ 4][ ·][ 4][ ·][ 6][ ·][ 6][ · · ·]
      - 1 3 3 5 5 7



Derivatives:




[ +][ v][)]

= [du]
dx dx




[du]

dx [+][ dv] dx




 -  
dudx u dxdv

 



 
dv

dx




[dv]

dx [+][ v du] dx



dx [,]




[du] 2. [d][(][u][ +][ v][)]

dx [,] dx



1 · 3 · 3 · 5 · 5 · 7 · · ·
Brouncker’s continued fraction expansion:



1. [d][(][cu][)]



4. [d][(][u][n][)]




[(][cu][)]

= c [du]
dx dx




[(][u][n][)]

= nu [n][−][1][ du]
dx dx

[(][c][u][)]

= (ln c)c [u][ du]
dx dx



3. [d][(][uv][)]
dx [,] dx




- u dxdv, 6. [d][(][e][cu][)]

v [2] dx




[uv][)]

= u [dv]
dx dx




[e][cu][)]

= ce [cu][ du]
dx dx




[ du]

5. [d][(][u/v][)]
dx [,] dx



dx [,]




     
[u/v][)] = [v] dudx

dx




[ u][)] = [1]

dx u



π 1 [2]
4 [= 1 +]



2 + 3 [2]



2+ 5 [2]




[ du]

8. [d][(ln][ u][)]
dx [,] dx




[1] du

u dx [,]



2+ 2+7 [2] ···



7. [d][(][c][u][)]



Gregrory’s series:
π
4 [= 1][ −] 3 [1]



5 7

[−] [1]




[du] 10. [d][(cos][ u][)]

dx [,] dx




[ u][)]

= sin u [du]
dx - dx



dx [,]



3 [1] [+][ 1] 5



7 [1] [+][ 1] 9



9

[−· · ·]



9. [d][(sin][ u][)]




[ u][)]

= cos u [du]
dx dx



Newton’s series:




[du] 12. [d][(cot][ u][)]

dx [,] dx




[ u][)]

= csc [2] u [du]
dx dx



dx [,]



1 1 · 3
2 [+] 2 3 2 [3][ +] 2 4 5 2 [5][ +][ · · ·]
     -      -      -      -      


11. [d][(tan][ u][)]



13. [d][(sec][ u][)]




[ u][)]

= sec [2] u [du]
dx dx




[ u][)]

= tan u sec u [du]
dx dx



π
6 [= 1]




[du] 14. [d][(csc][ u][)]

dx [,] dx




[ u][)]

= cot u csc u [du]
dx - dx



dx [,]



Sharp’s series:



17. [d][(arctan][ u][)]




[ u][)] 1 du

= 18. [d][(arccot] [u][)]
dx 1 + u [2] dx [,] dx




[u][)] 1

=   dx √1



π 1
6 [=] √3



π 1
6 [=] √




- 1 1 1
1

 - 3 [1] 3 [+] 3 [2] 5 3 [3] 7 [+] [· · ·]

      -       - [−]       


15. [d][(arcsin][ u][)]




[ u][)] 1

dx = √1



−1 du

1 − u [2] dx [,]



1 du

16. [d][(arccos] [u][)]
1 − u [2] dx [,] dx




[u][)] 1 du

=   dx 1 + u [2] dx [,]



Euler’s series:



π [2]



π 1

6 [=] 1 [2][ +][ 1] 2



4 [2][ +][ 1] 5

7 [2][ +][ 1] 9

4 [2][ +][ 1] 5

[1]



5 [2][ +][ · · ·]

9 [2][ +][ · · ·]

5 [2][ −· · ·]




[ u][)]

= cosh u [du]
dx dx



1 du

20. [d][(arccsc][ u][)]
1 − u [2] dx [,] dx




[ u][)] 1

=   dx u√1



π [2]



2 [2][ +][ 1] 3 [2]

3 [2][ +][ 1] 5 [2]

2 [2][ +][ 1] 3 [2]

[1]



π 1

8 [=] 1 [2][ +][ 1] 3

π [2] 1
12 [=] 1 [2][ −] 2 [1]



3 [2][ +][ 1] 4

5 [2][ +][ 1] 7

3 [2][ −] 4 [1]



19. [d][(arcsec][ u][)]




[ u][)] 1

dx = u√1



21. [d][(sinh][ u][)]




[du] 22. [d][(cosh][ u][)]

dx [,] dx




[ u][)]

= sinh u [du]
dx dx



−1 du

1 − u [2] dx [,]



dx [,]



Partial Fractions


Let N (x) and D(x) be polynomial functions of x. We can break down
N (x)/D(x) using partial fraction expansion. First, if the degree of N is greater
than or equal to the degree of D, divide
N by D, obtaining
N (x)
D(x) [=][ Q][(][x][) +][ N] D [ ′] ( [(] x [x] ) [)] [,]

where the degree of N [′] is less than that of
D. Second, factor D(x). Use the following rules: For a non-repeated factor:
N (x) A
(x a)D(x) [=] x a [+][ N] D [ ′] ( [(] x [x] ) [)] [,]
    -    


23. [d][(tanh][ u][)]




[du] 24. [d][(coth][ u][)]

dx [,] dx




[ u][)]

= sech [2] u [du]
dx dx




[ u][)]

= csch [2] u [du]
dx - dx



dx [,]



25. [d][(sech][ u][)]




[du] 26. [d][(csch][ u][)]

dx [,] dx




[ u][)]

= sech u tanh u [du]
dx - dx




[ u][)]

= csch u coth u [du]
dx - dx



dx [,]




[ u][)] 1

dx = √




[u][)] 1

dx = √u [2]



27. [d][(arcsinh][ u][)]



1 du

28. [d][(arccosh] [u][)]
1 + u [2] dx [,] dx



29. [d][(arctanh][ u][)]




[ u][)] 1 du

= 30. [d][(arccoth][ u][)]
dx 1 − u [2] dx [,] dx



1 du

u [2] - 1 dx [,]



1 du

1 + u [2] dx [.]




[u][)] 1

=   dx u√1




[ u][)] 1

=   dx |u|√




[ u][)] 1 du

=
dx u [2] 1 dx [,]

    


31. [d][(arcsech] [u][)]



1 du

- 32. [d][(arccsch][ u][)]

1 − u [2] dx [,] dx



Integrals:




  -  -  -  -  1. cu dx = c u dx, 2. (u + v) dx = u dx + v dx,



where




  N (x)
A =

D(x)




      
[dv] v [du]

dx [dx][ =][ uv][ −] dx





.
x=a




  -  1 1
3. x [n] dx = n = 1, 4.
n + 1 [x][n][+1][,] ̸        - x




        
1

5. e [x] dx = e [x],
x [dx][ = ln][ x,]



dx [dx,]



For a repeated factor:
N (x) m�−1
(x a) [m] D(x) [=]
 - k=0



m�−1



Ak
(x a) [m][−][k][ +] [N] D [ ′] ( [(] x [x] ) [)] [,]
 



  -  dx
6. 7. u [dv]
1 + x [2][ = arctan][ x,] dx




  -  8. sin x dx = − cos x, 9. cos x dx = sin x,

  -   10. tan x dx = − ln | cos x|, 11. cot x dx = ln | cos x|,

  -   12. sec x dx = ln | sec x + tan x|, 13. csc x dx = ln | csc x + cot x|,



k=0



where



Ak = [1]

k!




N (x)

D(x)



��

.
x=a




dk

dx [k]



The reasonable man adapts himself to the
world; the unreasonable persists in trying
to adapt the world to himself. Therefore
all progress depends on the unreasonable.

- George Bernard Shaw




  14. arcsin [x]




 a [+]




[x]

a [dx][ = arcsin][ x] a



a [2] - x [2], a > 0,


Theoretical Computer Science Cheat Sheet




  15. arccos [x]




 
[ x] a

[−]



Calculus Cont.



a 2

[−] [a]




[x]

a [dx][ = arccos][ x] a




                a [2] x [2], a > 0, 16. arctan [x] a

 



[x]

a [dx][ =][ x][ arctan][ x] a




[a] 2 [ln(][a][2][ +][ x][2][)][,] a > 0,




  -   
           -            -            -            17. sin [2] (ax)dx = 21a ax sin(ax) cos(ax), 18. cos [2] (ax)dx = 21a ax + sin(ax) cos(ax),
            
  -   19. sec [2] x dx = tan x, 20. csc [2] x dx = − cot x,




  21. sin [n] x dx =
        - [sin][n][−][1] n [ x][ cos][ x]



n




[ cos][ x]

+ [n][ −] [1]
n n




- sin [n][−][2] x dx, 22. cos [n] x dx = [cos][n][−][1][ x][ sin][ x]




[ sin][ x]

+ [n][ −] [1]
n n




cos [n][−][2] x dx,




  23. tan [n] x dx = [tan][n][−][1][ x]



n




    -     
[n][−][1][ x]

tan [n][−][2] x dx, n = 1, 24. cot [n] x dx =
n 1 - ̸ - [cot] n [n][−][1] 1 [ x]
 - - 



  25. sec [n] x dx = [tan][ x][ sec][n][−][1][ x]




    
[n][−][1][ x]

cot [n][−][2] x dx, n = 1,
n 1 - ̸
 



[ sec][n][−][1]

+ [n][ −] [2]
n − 1 n − 1




sec [n][−][2] x dx, n ̸= 1,




  26. csc [n] x dx =
        - [cot][ x] n [ csc][n] 1 [−][1][ x]



n − 1



n − 1




[ x][ csc][n][−][1]

+ [n][ −] [2]
n − 1 - n − 1




- - csc [n][−][2] x dx, n ̸= 1, 27. sinh x dx = cosh x, 28. cosh x dx = sinh x,



��
2,




  -   -   -   29. tanh x dx = ln cosh x, 30. coth x dx = ln sinh x, 31. sech x dx = arctan sinh x, 32. csch x dx = ln ��tanh x2
| | | |




  33. sinh [2] x dx = [1]




        2 [x,] 34. cosh [2] x dx = 4 [1]

[1]




        2 [x,] 35. sech [2] x dx = tanh x,




                 x [2] + a [2], a > 0, 37. arctanh [x]




[1]

4 [sinh(2][x][) +][ 1] 2



a [+][ a] 2




  36. arcsinh [x]




[1]

4 [sinh(2][x][)][ −] [1] 2




[x]

a [dx][ =][ x][ arcsinh][ x] a




[x]

a [dx][ =][ x][ arctanh][ x] a




[ a] 2 [ln][ |][a][2][ −] [x][2][|][,]




 
a

[−]




 
[x]

a

[−]   
[x]



x [2] + a [2], if arccosh [x] a


x [2] + a [2], if arccosh [x]




  38. arccosh [x] a [dx][ =]











x arccosh [x]

a

x arccosh [x]



a [>][ 0 and][ a >][ 0,]


[x]

a [<][ 0 and][ a >][ 0,]




  dx
39. √a [2]



��

[ x] a [,] a > 0, 41.




     -      
dx

x +
a [2] + x [2][ = ln]




 
[x]

a [+]




   a [2] + x [2], a > 0,




  dx
40.
a [2] + x [2][ =][ 1] a



2 [arcsin][ x] a



a [,] a > 0,



a [2] x [2] + [a] 2 [2]

 


a [arctan][ x] a



a [2] x [2] dx = [x] 2

 



 
[x]

2




  42. (a [2] x [2] ) [3][/][2] dx = [x] 8

   



          dx
a [,] a > 0, 44.
a [2]             - x [2][ = 1] 2



a [2] x [2] + [3][a] 8 [4]

 


a + x
����
2a [ln] a − x




[a]

8 [arcsin][ x] a



a [,] a > 0,




    
dx

���x +
x [2] a [2][ = ln]

 



  dx
43. √a [2]




   
[x]

8 [(5][a][2][ −] [2][x][2][)]




       dx x
����, 45.

  - (a [2]   - x [2] ) [3][/][2][ =] a [2][√] a [2]



a [2] x [2][ = arcsin][ x] a

 



  
[2]

2 [ln] ���x +



��
46.




 
[x]

2



x [2] - a [2] ���, a > 0,



a [2] x [2][,]

 


a [2] x [2] dx = [x] 2
±



a [2] x [2] [a] 2 [2]
± ±




             dx
a [2] ± x [2] ���, 47. √x [2]




                     ����, 49. x√




              
1 x

a + bx [dx,] 51. √a




  dx
48.
ax [2] + bx [= 1] a




     1
a + bx + a x√a



a + bx dx = [2(3][bx][ −] [2][a][)(][a][ +][ bx][)][3][/][2]




  - [√]

50.

  - [√]

52.



+ bx dx = 2√

x

   
x [2]

 - dx =

x



x
����
a [ln] a + bx



,
15b [2]



����, a > 0,



√



a + bx + a

[√]



����
2 [ln]



x



a + bx



√a + bx − [√] a

√a + bx + a

[√]



x 1

a + bx [dx][ =] √



a [2] - x [2]



a [2] - x [2] - a ln

   
[x]

8 [(2][x][2][ −] [a][2][)]



a + √
�����




              
         , 53. x
�����



a [2] x [2] dx = 3

 -  - [1]



a [2] - x [2]




  54. x [2][�]



8 [arcsin][ x] a




[1] 3 [(][a][2][ −] [x][2][)][3][/][2][,]



,
�����




            dx
a [,] a > 0, 55. √a [2]



a [2] x [2] dx = [x] 8

 


a [2] x [2] + [a] 8 [4]

 


a [ln]



a + √
�����



a [2] - x [2]



x



a [2] x [2][ =][ −] a [1]

 



  x dx
56. √a [2]




                    x [2] dx
a [2] - x [2], 57. √a [2]




   
x dx

a [2] x [2][ =][ −]

 



[a]

2 [arcsin][ x] a,



a, a > 0,



a [2] x [2] + [a] 2 [2]

 



[2] a [2] 
 - dx =

x




 
2

[x]




  - [√]

58.




   
+ x [2]

dx =
x


x [2] a [2] dx = 3 [1]
±



a + √
�����



x [2] + a [2][ =][ 1] a



x [2] a [2] a arccos x [a]

 -  - |



a [2] + x [2]



a [2] + x [2] - a ln




        - [√]
, 59.
�����



a [2] x [2][ =][ −] [x] 2

 


x [2] - a [2]



a [2] + x [2]




  
  60. x




                         dx

[1] 61.

3 [(][x][2][ ±][ a][2][)][3][/][2][,] x√x [2]



x



x
a [ln] ���� a + √a



|x| [,] a > 0,



a [2] + x [2]



����,


Theoretical Computer Science Cheat Sheet



,
a [2] x




  dx
62. x√x [2]

  x dx
64. √x [2]




           - [√]
x [2] ± a [2], 65.



Calculus Cont. Finite Calculus



x [2] a [2][ =][ 1] a

 



         dx
|x| [,] a > 0, 63. x [2][√] x [2]



a [arccos][ a] x



√



x [2] ± a [2]



Difference, shift operators:
∆f (x) = f (x + 1) − f (x),

E f (x) = f (x + 1).
Fundamental Theorem:

   f (x) = ∆F (x) ⇔ f (x)δx = F (x) + C.



a [2]
± dx =

x [4] ∓ [(][x][2][ +] 3a [ a][2] x [2][3][)][3][/][2]



x [2] a [2][ =][ ∓]
±




   
x dx

x [2] a [2][ =]
±










1
√b [2]


2
√4ac



,
3a [2] x [3]



x [2] ± a [2]



�b

f (x)δx =

a



2ax + b − √
����� √



if b [2] < 4ac,
4ac b [2][,]
  



  dx
66.
ax [2] + bx + c [=]



ln
b [2] - 4ac



2ax + b − b [2] - 4ac

2ax + b + √b [2] 4ac



b [2] - 4ac



, if b [2]  - 4ac,
�����



�b−1

f (i).

i=a



2 2ax + b

4ac − b [2][ arctan] √4ac −



1
a arcsin √ [−] b [2][2][ax][ −] 4 [b]
√− 



  dx
67. √ax [2] + bx + c [=]












     √1a ln ���2ax + b + 2√a



ax [2] + bx + c���, if a > 0,



��
68.



4a



, if a < 0,
b [2] - 4ac




dx
√ax [2] +



ax [2] + bx + c [,]



ax [2] + bx + c dx = [2][ax][ +][ b]







ax [2] + bx + c + [4][ax][ −] [b][2]



8a



Differences:
∆(cu) = c∆u, ∆(u + v) = ∆u + ∆v,


∆(uv) = u∆v + E v∆u,

∆(x [n] ) = nx [n][−][1],

∆(Hx) = x [−][1], ∆(2 [x] ) = 2 [x],

              -              -              -              ∆(c [x] ) = (c 1)c [x], ∆ mx = mx 1 .
     -     


Sums:

- cu δx = c � u δx,
�(u + v) δx = � u δx + � v δx,

- u∆v δx = uv − E v∆u δx,

- n+1 xn δx = x [,] x−1



ax [2] + bx + c



bx + c

a - 2 [b]




  x dx
69. √ax [2] + bx + c =



√



2a




dx
√ax [2] + bx + c,



x




- n+1 xn δx = xm+1 [,] x−1 δx = Hx,

- cx δx = cc− [x] 1 [,] ��mx - δx = �mx+1�.

Falling Factorial Powers:
x [n] = x(x − 1) · · · (x − n + 1), n > 0,



1 bx + 2c
c arcsin x √b [2] 4ac, if c < 0,
√− | | 


, if c > 0,
�����



2 [√] c√
�����



ax [2] + bx + c + bx + 2c




  dx
70. x√ax [2] + bx + c =










−1
√c ln




  71. x [3][�]



x [2] + a [2] dx = ( [1]



15 [2] [a][2][)(][x][2][ +][ a][2][)][3][/][2][,]




  72. x [n] sin(ax) dx = a
          - [1]




[1]

3 [x][2][ −] 15 [2]



1
x [n] = n < 0,
(x + 1) (x + n ) [,]
                - · · | |

x [n][+][m] = x [m] (x − m) [n] .
Rising Factorial Powers:



a [x][n][ cos(][ax][) +][ n] a

[1]



x [0] = 1,



a




x [n][−][1] cos(ax) dx,




  73. x [n] cos(ax) dx = a [1]

  74. x [n] e [ax] dx = [x][n][e][ax]



a




[1]

a [x][n][ sin(][ax][)][ −] [n] a



a




x [n][−][1] sin(ax) dx,



a - [n] a




x [n][−][1] e [ax] dx,



x [n] = x(x + 1) · · · (x + n − 1), n > 0,

x [0] = 1,



1
x [n] = n < 0,
(x 1) (x n ) [,]
    -    - · · −| |




  -   ln(ax)
75. x [n] ln(ax) dx = x [n][+1]




,

x [n] (ln ax) [m][−][1] dx.




  76. x [n] (ln ax) [m] dx = [x][n][+1]



ln(ax) 1

n + 1 (n + 1) [2]

[−]




[x][n][+1] m

n + 1 [(ln][ ax][)][m][ −] n + 1



x [1] = x [1] = x [1]



x [2] = x [2] + x [1] = x [2] - x [1]



x [n][+][m] = x [m] (x + m) [n] .
Conversion:
x [n] = (−1) [n] (−x) [n] = (x − n + 1) [n]



= 1/(x + 1) [−][n],



x [3] = x [3] + 3x [2] + x [1] = x [3] - 3x [2] + x [1]



x [4] = x [4] + 6x [3] + 7x [2] + x [1] = x [4] - 6x [3] + 7x [2] - x [1]



x [n] = (−1) [n] (−x) [n] = (x + n − 1) [n]



�n



x [5] = x [5] + 15x [4] + 25x [3] + 10x [2] + x [1] = x [5] - 15x [4] + 25x [3] - 10x [2] + x [1]



= 1/(x − 1) [−][n],




x [k] =



�n



k=1

�n


k=1

�n


k=1




x [k] .



x [1] = x [1] x [1] = x [1]




n
k

n
k

n
k



k=1




- n

( 1) [n][−][k] x [k],

k  


x [2] = x [2] + x [1] x [2] = x [2] - x [1]



x [3] = x [3] + 3x [2] + 2x [1] x [3] = x [3] - 3x [2] + 2x [1]




(−1) [n][−][k] x [k],



x [4] = x [4] + 6x [3] + 11x [2] + 6x [1] x [4] = x [4] - 6x [3] + 11x [2] - 6x [1]



x [5] = x [5] + 10x [4] + 35x [3] + 50x [2] + 24x [1] x [5] = x [5] - 10x [4] + 35x [3] - 50x [2] + 24x [1]



x [n] =


x [n] =


x [n] =


Theoretical Computer Science Cheat Sheet


Series



Taylor’s series:

f (x) = f (a) + (x − a)f [′] (a) + [(][x][ −] 2 [a][)][2] f [′′] (a) + · · · =



i=0



�∞



Ordinary power series:



A(x) =



�∞

aix [i] .
i=0



(x a) [i]
 - f [(][i][)] (a).

i!



Expansions:
1
= 1 + x + x [2] + x [3] + x [4] + =
1 x      - · ·
      


�∞



x [i],

i=0



Exponential power series:



A(x) =



i! [.]



�∞



�∞ x [i]

ai

i!

i=0



1
= 1 + cx + c [2] x [2] + c [3] x [3] + =
1 cx - · ·
 
1
= 1 + x [n] + x [2][n] + x [3][n] + =
1 x [n] - · ·
 


�∞



�∞



c [i] x [i],

i=0



Dirichlet power series:



�∞



�∞


i=1


n
k



x [ni],

i=0



A(x) =



ai
i [x][ .]


x [n][−][k] y [k] .



Binomial theorem:



�n


k=0




n
k



= x + 2 [n] x [2] + 3 [n] x [3] + 4 [n] x [4] + =
(1 z) [k][+1] - · ·
 


ix [i],

i=0



i [n] x [i],

i=0



�n


k=0



x
= x + 2x [2] + 3x [3] + 4x [4] + =
(1 x) [2] - · ·

 - −




k!z [k]



(x + y) [n] =



�∞



n�−1

x [n] - y [n] = (x − y) x [n][−][1][−][k] y [k] .

k=0



Difference of like powers:




[1]

2 [x][2][ +][ 1] 6



�∞



e [x] = 1 + x + [1]



6 [x][3][ +][ · · ·] =



x [i]

i! [,]



i [,]



i=0

�∞



�∞

( 1) [i][+1][ x][i]

 i=1



2 [x][2][ +][ 1] 3

[1]



4 [1] [x][4][ −· · ·] =



ln(1 + x) = x 2
            - [1]


1
ln 1 − x = x + 2 [1]



3 [x][3][ −] 4 [1]



For ordinary power series:



�∞

(αai + βbi)x [i],
i=0



ai−kx [i],
i=k



�∞




[1]

2 [x][2][ +][ 1] 3



3 [x][3][ +][ 1] 4



4 [x][4][ +][ · · ·] =



�∞



x [i]

i [,]



(2i + 1)! [,]



αA(x) + βB(x) =


x [k] A(x) =



=
x [k]



3! [x][3][ +][ 1] 5!

[1]



i=1

�∞



�∞ x [2][i][+1]

( 1) [i]

 - (2i
i=0



�∞

( 1) [i][ x][2][i]

 - (2i
i=0



sin x = x 3!
           - [1]



A(x) − [�] i [k] =0 [−][1] [a][i][x][i]



(2i)! [,]



2! [x][2][ +][ 1] 4!

[1]



7! [1] [x][7][ +][ · · ·] =

6! [1] [x][6][ +][ · · ·] =



�∞



cos x = 1 2!
           - [1]




[ 1] 5! [x][5][ −] 7! [1]


4! [x][4][ −] 6! [1]



�∞

ai+kx [i],
i=0



�∞



c [i] aix [i],
i=0



a2i+1x [2][i][+1] .
i=0



tan [−][1] x = x 3
            - [1]



5 [x][5][ −] 7 [1]



3 [x][3][ +][ 1] 5

[1]



7 [1] [x][7][ +][ · · ·] =



�∞



�∞

( 1) [i][ x][2][i][+1]

 - (2i + 1)
i=0



A(cx) =


A [′] (x) =


xA [′] (x) =


  A(x) dx =


A(x) + A( x)

   - =

2


A(x) A( x)
  -   - =

2



�∞

(i + 1)ai+1x [i],
i=0



(2i + 1) [,]




x [i],




x [i],



(1 + x) [n] = 1 + nx + [n][(][n] 2 [−][1)] x [2] + =

                                           - · ·



�∞



i=0

�∞




n
i



�∞

iaix [i],
i=1



(1 1x) [n][+1] = 1 + (n + 1)x + �n+22 �x [2] + · · · =
 



i + n
i



Bix [i]



x
e [x] 1 = 1 − 2 [1]

 


12 [x][2][ −] 7201 [x][4][ +][ · · ·] =



i=0

�∞



i=0

�∞



2 [1] [x][ +][ 1]




x [i],



i! [,]



�∞


i=1



�∞

a2ix [2][i],
i=0



ai−1 x [i],

i



1 √
2x [(1][ −]



1 − 4x) = 1 + x + 2x [2] + 5x [3] + · · · =



i=0

�∞



1
i + 1




x [i],



�∞




2i
i




x [i],




2i
i



�n - = 1 + (2 + n)x + 4+2n x [2] + =
                                  - · ·



i=0

�∞



Summation: If bi = [�][i] j=0 [a][i][ then]



1
B(x) =
1 x [A][(][x][)][.]
    


1
√1 − 4x



1
√�1 − 4x - = 1 + 2x + 6x [2] + 20x [3] + · · · =




1 1 4x
−√  


2x




2i + n
i






 x [i] .



1 1
1 −� x [ln] 1 −�x = x + 2 [3]




[3]

2 [x][2][ +][ 11] 6



6 [x][3][ +][ 25] 12



12 [x][4][ +][ · · ·] =



i=0

�∞



Hix [i],
i=1



Convolution:







�2
= [1]



4 [x][3][ +][ 11] 24



1
2




1
ln
1 − x




[1]

2 [x][2][ +][ 3] 4



24 [x][4][ +][ · · ·] =



�∞



i=2

�∞



�∞


i=0



�i
 ajbi−j

j=0



�i




Hi−1x [i],

i



A(x)B(x) =



x
= x + x [2] + 2x [3] + 3x [4] + =
1 x x [2] - · ·
 - 


�∞



Fix [i],
i=0



Fnx
= Fnx + F2nx [2] + F3nx [3] + =
1 (Fn 1 + Fn+1)x ( 1) [n] x [2] - · ·
 - - - 


Fnix [i] .
i=0



God made the natural numbers;
all the rest is the work of man.

- Leopold Kronecker


Theoretical Computer Science Cheat Sheet


Series Escher’s Knot



Expansions:
1 1
=
(1 − x) [n][+1][ ln] 1 − x

x [n] =




x [i],


n!xi

i! [,]




     
�∞ n + i

(Hn+i Hn)
i=0 - i




- 1
x [i],



�∞


i=0

�∞


i=0

�∞


i=0

�∞


i=1

�∞




i
n

i
n



�∞



�−n
=



x cot x =
i! [,]



x



�∞




x [i], (e [x] - 1) [n] =




n!xi




1
ln
1 − x



�n
=



i=0

�∞



i=0




n
i

i
n



i=0



, ζ(x) =
(2i)!



tan x =


1
=
ζ(x)



�∞



�∞

( 1) [i][−][1][ 2][2][i][(2][2][i][ −] [1)][B][2][i][x][2][i][−][1]

 - (2i)!
i=1



i=1



�∞



µ(i)



=
ζ(x)



i=1



(i) ζ(x − 1)

i [x][,] ζ(x)



( 4) [i] B2ix [2][i]

 -,

(2i)!


1
i [x][,]


φ(i)

i [x][,]




   
1

ζ(x) = Stieltjes Integration

[x][,]



1
1 p [−][x][,]
 


If G is continuous in the interval [a, b] and F is nondecreasing then

           - b

G(x) dF (x)
a



ζ [2] (x) =


ζ(x)ζ(x − 1) =



p

�∞


i=1

�∞


i=1



d(i) where d(n) = [�] d n [1][,]

x [i] |



S(i) where S(n) = [�]

x [i]



d n [d,]
|



b - c

G(x) dF (x) +
a b



exists. If a� ≤c b ≤ c then



c - b

G(x) dF (x) =
a a



G(x) dF (x).
b



ζ(2n) = [2][2][n][−][1][|][B][2][n][|] π [2][n], n N,

(2n)! ∈



b - b

G(x) dF (x) +
a a

b - b

G(x) dF (x) +
a a



H(x) dF (x),
a



If the integrals involved exist

  - b



,
(2i)!



x
=
sin x



�∞




- b



b  -  -  - b

G(x) d F (x) + H(x) =
a a




- - - b
G(x) + H(x) dF (x) =



a




1 −√1 − 4x

2x



�n
=



�∞

( 1) [i][−][1][ (4][i][ −] [2)][B][2][i][x][2][i]

 - (2i)!
i=0



�∞


i=0

�∞


i=1


�∞


i=0

�∞


i=0



n(2i + n 1)!
    - x [i],

i!(n + i)!




 - b



b - b

a c · G(x) dF (x) = a



G(x) dH(x),
a



2 [i/][2] sin [iπ] 4 x [i],

i!



(4i)!
16 [i][√] 2(2i)!(2i + 1)! [x][i][,]




- b



b - - - b

a G(x) d c · F (x) = c a



G(x) dF (x),
a







e [x] sin x =


1 1 x
 - [√] - =

x



If the integrals involved exist, and F possesses a derivative F [′] at every
point in [a, b] then

       - b       - b



b - b

a G(x) dF (x) = G(b)F (b) − G(a)F (a) − a



F (x) dG(x).
a




arcsin x

x



�2
=



4 [i] i! [2]

(i + 1)(2i + 1)! [x][2][i][.]



b - b

G(x) dF (x) =
a a



G(x)F [′] (x) dx.
a



Cramer’s Rule


If we have equations:
a1,1x1 + a1,2x2 + · · · + a1,nxn = b1
a2,1x1 + a2,2x2 + · · · + a2,nxn = b2
... ... ...

an,1x1 + an,2x2 + · · · + an,nxn = bn



Fibonacci Numbers


1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .


Definitions:
Fi = Fi 1+Fi 2, F0 = F1 = 1,

   -   


F i = ( 1) [i][−][1] Fi,

 - −�

[�]




φ [i] φ [i][�],

 - [ˆ]



Let A = (ai,j) and B be the column matrix (bi). Then
there is a unique solution iff det A ̸= 0. Let Ai be A
with column i replaced by B. Then



Cassini’s identity: for i > 0:
Fi+1Fi 1 Fi [2] [= (][−][1)][i][.]

    -    
Additive rule:
Fn+k = FkFn+1 + Fk 1Fn,

        


Fi = √1



5



xi = [det][ A][i]



det A [.]



Improvement makes strait roads, but the crooked
roads without Improvement, are roads of Genius.

- William Blake (The Marriage of Heaven and Hell)



00 47 18 76 29 93 85 34 61 52


86 11 57 28 70 39 94 45 02 63


95 80 22 67 38 71 49 56 13 04


59 96 81 33 07 48 72 60 24 15


73 69 90 82 44 17 58 01 35 26


68 74 09 91 83 55 27 12 46 30


37 08 75 19 92 84 66 23 50 41


14 25 36 40 51 62 03 77 88 99


21 32 43 54 65 06 10 89 97 78


42 53 64 05 16 20 31 98 79 87


The Fibonacci number system:
Every integer n has a unique
representation

n = Fk1 + Fk2 + · · · + Fkm,
where ki ≥ ki+1 + 2 for all i,
1 i < m and km 2.
≤ ≥



Calculation by matrices:

- - Fn−2 Fn−1 = 0
Fn−1 Fn 1



F2n = FnFn+1 + Fn 1Fn.

       



- 0 1
=
1 1



�n
.


