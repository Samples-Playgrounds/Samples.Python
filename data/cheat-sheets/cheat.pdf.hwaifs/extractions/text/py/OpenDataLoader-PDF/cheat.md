![image 1](cheat_images/imageFile1.png)

![image 2](cheat_images/imageFile2.png)

![image 3](cheat_images/imageFile3.png)

Theoretical Computer Science Cheat Sheet

![image 4](cheat_images/imageFile4.png)

![image 5](cheat_images/imageFile5.png)

![image 6](cheat_images/imageFile6.png)

![image 7](cheat_images/imageFile7.png)

Deﬁnitions Series f(n) = O(g(n)) iﬀ ∃ positive c,n0 such that

![image 8](cheat_images/imageFile8.png)

![image 9](cheat_images/imageFile9.png)

![image 10](cheat_images/imageFile10.png)

![image 11](cheat_images/imageFile11.png)

![image 12](cheat_images/imageFile12.png)

n

n

n

n2(n + 1)2 4

n(n + 1) 2

n(n + 1)(2n + 1) 6

i2 =

i3 =

0 ≤ f(n) ≤ cg(n) ∀n ≥ n0.

i =

. In general:

,

,

![image 13](cheat_images/imageFile13.png)

![image 14](cheat_images/imageFile14.png)

![image 15](cheat_images/imageFile15.png)

i=1

i=1

i=1

![image 16](cheat_images/imageFile16.png)

![image 17](cheat_images/imageFile17.png)

![image 18](cheat_images/imageFile18.png)

![image 19](cheat_images/imageFile19.png)

![image 20](cheat_images/imageFile20.png)

![image 21](cheat_images/imageFile21.png)

![image 22](cheat_images/imageFile22.png)

![image 23](cheat_images/imageFile23.png)

![image 24](cheat_images/imageFile24.png)

![image 25](cheat_images/imageFile25.png)

f(n) = Ω(g(n)) iﬀ ∃ positive c,n0 such that f(n) ≥ cg(n) ≥ 0 ∀n ≥ n0.

n

n

1 m + 1

(i + 1)m+1 − im+1 − (m + 1)im

(n + 1)m+1 − 1 −

im =

![image 26](cheat_images/imageFile26.png)

![image 27](cheat_images/imageFile27.png)

![image 28](cheat_images/imageFile28.png)

![image 29](cheat_images/imageFile29.png)

![image 30](cheat_images/imageFile30.png)

![image 31](cheat_images/imageFile31.png)

![image 32](cheat_images/imageFile32.png)

![image 33](cheat_images/imageFile33.png)

![image 34](cheat_images/imageFile34.png)

![image 35](cheat_images/imageFile35.png)

f(n) = Θ(g(n)) iﬀ f(n) = O(g(n)) and f(n) = Ω(g(n)).

![image 36](cheat_images/imageFile36.png)

i=1

i=1

n−1

m

1 m + 1

m + 1 k

![image 37](cheat_images/imageFile37.png)

![image 38](cheat_images/imageFile38.png)

![image 39](cheat_images/imageFile39.png)

![image 40](cheat_images/imageFile40.png)

![image 41](cheat_images/imageFile41.png)

![image 42](cheat_images/imageFile42.png)

![image 43](cheat_images/imageFile43.png)

![image 44](cheat_images/imageFile44.png)

![image 45](cheat_images/imageFile45.png)

![image 46](cheat_images/imageFile46.png)

im =

Bknm+1 k. Geometric series:

f(n) = o(g(n)) iﬀ limn→∞ f(n)/g(n) = 0.

![image 47](cheat_images/imageFile47.png)

i=1

![image 48](cheat_images/imageFile48.png)

![image 49](cheat_images/imageFile49.png)

![image 50](cheat_images/imageFile50.png)

![image 51](cheat_images/imageFile51.png)

![image 52](cheat_images/imageFile52.png)

![image 53](cheat_images/imageFile53.png)

k=0

![image 54](cheat_images/imageFile54.png)

![image 55](cheat_images/imageFile55.png)

![image 56](cheat_images/imageFile56.png)

![image 57](cheat_images/imageFile57.png)

an = a iﬀ ∀ǫ > 0, ∃n0 such that |an − a| < ǫ, ∀n ≥ n0.

lim n→∞

n

∞

∞

cn+1 − 1 c − 1

1 1 − c

c 1 − c

ci

ci

ci

, |c| < 1,

, c = 1,

,

![image 58](cheat_images/imageFile58.png)

![image 59](cheat_images/imageFile59.png)

![image 60](cheat_images/imageFile60.png)

![image 61](cheat_images/imageFile61.png)

![image 62](cheat_images/imageFile62.png)

![image 63](cheat_images/imageFile63.png)

![image 64](cheat_images/imageFile64.png)

![image 65](cheat_images/imageFile65.png)

![image 66](cheat_images/imageFile66.png)

![image 67](cheat_images/imageFile67.png)

supS least b ∈ R such that b ≥ s, ∀s ∈ S.

![image 68](cheat_images/imageFile68.png)

![image 69](cheat_images/imageFile69.png)

![image 70](cheat_images/imageFile70.png)

i=0

i=0

i=1

∞

n

ncn+2 − (n + 1)cn+1 + c (c − 1)2

c (1 − c)2

![image 71](cheat_images/imageFile71.png)

![image 72](cheat_images/imageFile72.png)

![image 73](cheat_images/imageFile73.png)

![image 74](cheat_images/imageFile74.png)

![image 75](cheat_images/imageFile75.png)

![image 76](cheat_images/imageFile76.png)

![image 77](cheat_images/imageFile77.png)

![image 78](cheat_images/imageFile78.png)

![image 79](cheat_images/imageFile79.png)

![image 80](cheat_images/imageFile80.png)

ici =

ici =

inf S greatest b ∈ R such that b ≤

, |c < 1. Harmonic series:

, c = 1,

![image 81](cheat_images/imageFile81.png)

![image 82](cheat_images/imageFile82.png)

s, ∀s ∈ S. liminf n→∞

i=0

i=0

![image 83](cheat_images/imageFile83.png)

![image 84](cheat_images/imageFile84.png)

![image 85](cheat_images/imageFile85.png)

![image 86](cheat_images/imageFile86.png)

![image 87](cheat_images/imageFile87.png)

![image 88](cheat_images/imageFile88.png)

![image 89](cheat_images/imageFile89.png)

![image 90](cheat_images/imageFile90.png)

![image 91](cheat_images/imageFile91.png)

![image 92](cheat_images/imageFile92.png)

inf{ai | i ≥ n,i ∈ N}. limsup n→∞

an lim

n

n

n(n − 1) 4

1 i

n(n + 1) 2

n→∞

Hn −

Hn =

iHi =

,

.

![image 93](cheat_images/imageFile93.png)

![image 94](cheat_images/imageFile94.png)

![image 95](cheat_images/imageFile95.png)

![image 96](cheat_images/imageFile96.png)

![image 97](cheat_images/imageFile97.png)

![image 98](cheat_images/imageFile98.png)

![image 99](cheat_images/imageFile99.png)

![image 100](cheat_images/imageFile100.png)

![image 101](cheat_images/imageFile101.png)

![image 102](cheat_images/imageFile102.png)

![image 103](cheat_images/imageFile103.png)

![image 104](cheat_images/imageFile104.png)

![image 105](cheat_images/imageFile105.png)

sup{ai i ≥ n,i ∈ N}.

an lim

i=1

i=1

n→∞

n

n

1 m + 1

i m

n + 1 m + 1

![image 106](cheat_images/imageFile106.png)

![image 107](cheat_images/imageFile107.png)

![image 108](cheat_images/imageFile108.png)

![image 109](cheat_images/imageFile109.png)

![image 110](cheat_images/imageFile110.png)

![image 111](cheat_images/imageFile111.png)

![image 112](cheat_images/imageFile112.png)

![image 113](cheat_images/imageFile113.png)

![image 114](cheat_images/imageFile114.png)

![image 115](cheat_images/imageFile115.png)

n k Combinations: Size k sub-

Hn+1 −

Hi = (n + 1)Hn − n,

Hi =

.

![image 116](cheat_images/imageFile116.png)

sets of a size n set.

i=1

i=1

![image 117](cheat_images/imageFile117.png)

![image 118](cheat_images/imageFile118.png)

![image 119](cheat_images/imageFile119.png)

![image 120](cheat_images/imageFile120.png)

![image 121](cheat_images/imageFile121.png)

![image 122](cheat_images/imageFile122.png)

![image 123](cheat_images/imageFile123.png)

![image 124](cheat_images/imageFile124.png)

![image 125](cheat_images/imageFile125.png)

![image 126](cheat_images/imageFile126.png)

![image 127](cheat_images/imageFile127.png)

n

n k Stirling numbers (1st kind):

n k

n k

n n − k

n! (n − k)!k!

n k

= 2n, 3.

, 2.

=

,

=

1.

Arrangements of an n element set into k cycles.

![image 128](cheat_images/imageFile128.png)

k=0

n − 1 k − 1

n − 1 k

n − 1 k − 1

n k

n k

n k

, 5.

=

=

+

,

4.

![image 129](cheat_images/imageFile129.png)

![image 130](cheat_images/imageFile130.png)

![image 131](cheat_images/imageFile131.png)

![image 132](cheat_images/imageFile132.png)

![image 133](cheat_images/imageFile133.png)

![image 134](cheat_images/imageFile134.png)

![image 135](cheat_images/imageFile135.png)

![image 136](cheat_images/imageFile136.png)

![image 137](cheat_images/imageFile137.png)

![image 138](cheat_images/imageFile138.png)

n k Stirling numbers (2nd kind):

![image 139](cheat_images/imageFile139.png)

Partitions of an n element set into k non-empty sets.

n

n m

m k

n k

n k m − k

r k k

r + n + 1 n

=

, 7.

=

,

6.

k=0

![image 140](cheat_images/imageFile140.png)

![image 141](cheat_images/imageFile141.png)

![image 142](cheat_images/imageFile142.png)

![image 143](cheat_images/imageFile143.png)

![image 144](cheat_images/imageFile144.png)

![image 145](cheat_images/imageFile145.png)

![image 146](cheat_images/imageFile146.png)

![image 147](cheat_images/imageFile147.png)

![image 148](cheat_images/imageFile148.png)

![image 149](cheat_images/imageFile149.png)

n k 1st order Eulerian numbers: Permutations π1π2 ...πn on {1,2,...,n} with k ascents.

n

n

k m

n + 1 m + 1

r k

s n − k

r + s n

=

, 9.

=

,

8.

k=0

k=0

k − n − 1 k

n 1

n n

n k

= (−1)k

![image 150](cheat_images/imageFile150.png)

![image 151](cheat_images/imageFile151.png)

![image 152](cheat_images/imageFile152.png)

![image 153](cheat_images/imageFile153.png)

![image 154](cheat_images/imageFile154.png)

![image 155](cheat_images/imageFile155.png)

![image 156](cheat_images/imageFile156.png)

![image 157](cheat_images/imageFile157.png)

![image 158](cheat_images/imageFile158.png)

![image 159](cheat_images/imageFile159.png)

n k 2nd order Eulerian numbers.

, 11.

=

= 1,

10.

![image 160](cheat_images/imageFile160.png)

![image 161](cheat_images/imageFile161.png)

![image 162](cheat_images/imageFile162.png)

![image 163](cheat_images/imageFile163.png)

![image 164](cheat_images/imageFile164.png)

![image 165](cheat_images/imageFile165.png)

![image 166](cheat_images/imageFile166.png)

![image 167](cheat_images/imageFile167.png)

![image 168](cheat_images/imageFile168.png)

![image 169](cheat_images/imageFile169.png)

Cn Catalan Numbers: Binary trees with n + 1 vertices.

n − 1 k

n − 1 k − 1

n 2

n k

= 2n−1 − 1, 13.

= k

+

,

12.

![image 170](cheat_images/imageFile170.png)

![image 171](cheat_images/imageFile171.png)

![image 172](cheat_images/imageFile172.png)

![image 173](cheat_images/imageFile173.png)

![image 174](cheat_images/imageFile174.png)

![image 175](cheat_images/imageFile175.png)

![image 176](cheat_images/imageFile176.png)

![image 177](cheat_images/imageFile177.png)

n 1

n 2

n n

n k ≥

n k

= (n − 1)!, 15.

= (n − 1)!Hn−1, 16.

= 1, 17.

,

14.

n

n − 1 k

n − 1 k − 1

2n n

1 n + 1

n k

n n − 1

n n − 1

n 2

n k

= (n − 1)

,

+

, 19.

=

=

, 20.

= n!, 21. Cn =

18.

![image 178](cheat_images/imageFile178.png)

k=0

n − 1 k

n − 1 k − 1

n 0

n n − 1

n k

n n − 1 − k

n k

+ (n − k)

=

= 1, 23.

=

, 24.

= (k + 1)

,

22.

n 1

n 2

n + 1 2

0 k

1 if k = 0, 0 otherwise

= 2n − n − 1, 27.

= 3n − (n + 1)2n +

,

=

26.

25.

n

m

n

n k

x k n

n m

n + 1 k

n m

n k

k n − m

28. xn =

(m + 1 − k)n(−1)k, 30. m!

, 29.

=

=

,

k=0

k=0

k=0

n

n − k m

n m

n k

n 0

n n

(−1)n−k−mk!, 32.

=

= 1, 33.

= 0 for n = 0,

31.

k=0

n

(2n)n 2n

n − 1 k

n − 1 k − 1

n k

n k

![image 179](cheat_images/imageFile179.png)

+ (2n − 1 − k)

,

= (k + 1)

, 35.

=

34.

![image 180](cheat_images/imageFile180.png)

k=0

n

n

x + n − 1 − k 2n

x x − n

n k

n + 1 m + 1

n k

k m

k m

(m + 1)n−k,

=

, 37.

=

=

36.

k=0

k

k=0

![image 181](cheat_images/imageFile181.png)

![image 182](cheat_images/imageFile182.png)

![image 183](cheat_images/imageFile183.png)

![image 184](cheat_images/imageFile184.png)

Theoretical Computer Science Cheat Sheet

![image 185](cheat_images/imageFile185.png)

![image 186](cheat_images/imageFile186.png)

![image 187](cheat_images/imageFile187.png)

![image 188](cheat_images/imageFile188.png)

Identities Cont. Trees 38.

n

n

n

![image 189](cheat_images/imageFile189.png)

![image 190](cheat_images/imageFile190.png)

![image 191](cheat_images/imageFile191.png)

![image 192](cheat_images/imageFile192.png)

Every tree with n vertices has n − 1 edges.

k m

x x − n

n k

x + k 2n

1 k!

n + 1 m + 1

n k

k m

k m

nn−k = n!

, 39.

=

,

=

=

![image 193](cheat_images/imageFile193.png)

![image 194](cheat_images/imageFile194.png)

k=0

k=0

k

k=0

n m

n k

k + 1 m + 1

n m

n + 1 k + 1

k m

(−1)n−k, 41.

(−1)m−k,

=

=

40.

Kraft inequality: If the depths of the leaves of a binary tree are d1,...,dn:

k

k

m

m

n + k k

n + k k

m + n + 1 m

m + n + 1 m

k(n + k)

,

k

, 43.

=

=

42.

k=0

k=0

n m

n + 1 k + 1

k m

n m

n + 1 k + 1

k m

( 1)m−k, 45. (n m)!

( 1)m−k, for n ≥ m,

=

=

n

44.

2−d

≤ 1,

i

k

k

m − n m + k

m − n m + k

n n − m

- m + n
- n + k


m + k k

n n − m

- m + n
- n + k


m + k k

i=1

=

, 47.

=

,

46.

and equality holds only if every internal node has 2 sons.

k

k

n − k m

n − k m

n ℓ + m

ℓ + m ℓ

k ℓ

n k

n ℓ + m

ℓ + m ℓ

k ℓ

n k

=

, 49.

=

.

48.

k

k

![image 195](cheat_images/imageFile195.png)

![image 196](cheat_images/imageFile196.png)

![image 197](cheat_images/imageFile197.png)

Recurrences Master method:

![image 198](cheat_images/imageFile198.png)

![image 199](cheat_images/imageFile199.png)

![image 200](cheat_images/imageFile200.png)

![image 201](cheat_images/imageFile201.png)

![image 202](cheat_images/imageFile202.png)

Generating functions:

1 T(n) − 3T(n/2) = n 3 T(n/2) 3T(n/4) = n/2

T(n) = aT(n/b) + f(n), a ≥ 1,b > 1 If ∃ǫ > 0 such that f(n) = O(nlogb a ǫ) then

- 1. Multiply both sides of the equation by xi.
- 2. Sum both sides over all i for which the equation is valid.
- 3. Choose a generating function G(x). Usually G(x) = ∞i=0 xigi.


. . . 3log2 n 1 T(2) − 3T(1) = 2

T(n) = Θ(nlogb a). If f(n) = Θ(nlogb a) then

Let m = log2 n. Summing the left side we get T(n) − 3mT(1) = T(n) − 3m =

T(n) = Θ(nlogb a log2 n).

- 3. Rewrite the equation in terms of the generating function G(x).
- 4. Solve for G(x).
- 5. The coeﬃcient of xi in G(x) is gi.


If ∃ǫ > 0 such that f(n) = Ω(nlogb a+ǫ), and ∃c < 1 such that af(n/b) ≤ cf(n) for large n, then

T(n) − nk where k = log2 3 ≈ 1.58496. Summing the right side we get

m−1

m−1

n

Example:

i .

- 2i
- 3i n


3 2

T(n) = Θ(f(n)).

![image 203](cheat_images/imageFile203.png)

![image 204](cheat_images/imageFile204.png)

gi+1 = 2gi + 1, g0 = 0. Multiply and sum:

i=0

i=0

Substitution (example): Consider the following recurrence

Let c = 32. Then we have n

![image 205](cheat_images/imageFile205.png)

gi+1xi =

2gixi +

xi.

m−1

i

Ti+1 = 22

· T2i, T1 = 2.

cm − 1 c − 1

ci n

i≥0

i≥0

i≥0

![image 206](cheat_images/imageFile206.png)

Note that Ti is always a power of two. Let ti = log2 Ti. Then we have

i=0

We choose G(x) = i≥0 xigi. Rewrite in terms of G(x):

= 2n(clog2 n − 1)

ti+1 = 2i + 2ti, t1 = 1.

= 2n(c(k−1) logc n 1)

G(x) − g0 x

xi.

= 2G(x) +

![image 207](cheat_images/imageFile207.png)

Let ui = ti/2i. Dividing both sides of the previous equation by 2i+1 we get

= 2nk − 2n,

i≥0

2i 2i+1

and so T(n) = 3nk − 2n. Full history recurrences can often be changed to limited history ones (example): Consider

Simplify:

ti+1 2i+1

ti 2i

. Substituting we ﬁnd

=

+

G(x) x

1 1 x

![image 208](cheat_images/imageFile208.png)

![image 209](cheat_images/imageFile209.png)

![image 210](cheat_images/imageFile210.png)

. Solve for G(x):

= 2G(x) +

![image 211](cheat_images/imageFile211.png)

![image 212](cheat_images/imageFile212.png)

- i−1
- j=0


ui+1 = 12 + ui, u1 = 12, which is simply ui i/2. So we ﬁnd that Ti has the closed form Ti = 2i2

![image 213](cheat_images/imageFile213.png)

![image 214](cheat_images/imageFile214.png)

Tj, T0 = 1.

Ti = 1 +

x (1 x)(1 2x)

G(x) =

. Expand this using partial fractions: G(x) = x

![image 215](cheat_images/imageFile215.png)

i 1

.

Note that

- i
- j=0


Summing factors (example): Consider the following recurrence

1 1 − x

2 1 − 2x −

Tj.

Ti+1 = 1 +

![image 216](cheat_images/imageFile216.png)

![image 217](cheat_images/imageFile217.png)

T(n) = 3T(n/2) + n, T(1) = 1.

xi

= x

Subtracting we ﬁnd Ti+1 − Ti = 1 +

Rewrite so that all terms involving T are on the left side

2ixi −

2

- i−1
- j=0


- i
- j=0




Tj − 1 −

Tj

i≥0

i≥0

T(n) − 3T(n/2) = n.

(2i+1 − 1)xi+1.

=

= Ti. And so Ti+1 = 2Ti = 2i+1.

Now expand the recurrence, and choose a factor which makes the left side “telescope”

i≥0

So gi = 2i 1.

![image 218](cheat_images/imageFile218.png)

![image 223](cheat_images/imageFile223.png)

![image 224](cheat_images/imageFile224.png)

√5 2 ≈ −.61803

√5 2 ≈ 1.61803, ˆφ = 1−

![image 225](cheat_images/imageFile225.png)

![image 226](cheat_images/imageFile226.png)

π ≈ 3.14159, e ≈ 2.71828, γ ≈ 0.57721, φ = 1+

![image 227](cheat_images/imageFile227.png)

![image 228](cheat_images/imageFile228.png)

![image 229](cheat_images/imageFile229.png)

![image 230](cheat_images/imageFile230.png)

![image 231](cheat_images/imageFile231.png)

![image 232](cheat_images/imageFile232.png)

![image 233](cheat_images/imageFile233.png)

![image 234](cheat_images/imageFile234.png)

![image 235](cheat_images/imageFile235.png)

i 2i pi General Probability

![image 236](cheat_images/imageFile236.png)

![image 237](cheat_images/imageFile237.png)

- 1 2 2 Bernoulli Numbers (Bi = 0, odd i = 1): B0 = 1, B1 −12, B2 16, B4 130,

![image 238](cheat_images/imageFile238.png)

![image 239](cheat_images/imageFile239.png)

![image 240](cheat_images/imageFile240.png)

![image 241](cheat_images/imageFile241.png)

![image 242](cheat_images/imageFile242.png)

![image 243](cheat_images/imageFile243.png)

B6 = 142, B8 = − 130, B10 = 566. Change of base, quadratic formula:

![image 244](cheat_images/imageFile244.png)

![image 245](cheat_images/imageFile245.png)

![image 246](cheat_images/imageFile246.png)

logb x =

loga x loga b

![image 247](cheat_images/imageFile247.png)

, −b ±

√b2 − 4ac 2a

![image 248](cheat_images/imageFile248.png)

![image 249](cheat_images/imageFile249.png)

. Euler’s number e:

e = 1 + 12 + 16 + 124 + 1120 + ···

![image 250](cheat_images/imageFile250.png)

![image 251](cheat_images/imageFile251.png)

![image 252](cheat_images/imageFile252.png)

![image 253](cheat_images/imageFile253.png)

lim n→∞

1 +

x n

![image 254](cheat_images/imageFile254.png)

n

= ex.

1 + 1n n < e < 1 + 1n

![image 255](cheat_images/imageFile255.png)

![image 256](cheat_images/imageFile256.png)

n+1 .

1 + 1n n = e −

![image 257](cheat_images/imageFile257.png)

e 2n

![image 258](cheat_images/imageFile258.png)

+

11e 24n2 − O

![image 259](cheat_images/imageFile259.png)

1 n3

![image 260](cheat_images/imageFile260.png)

. Harmonic numbers:

1, 32, 116, 2512, 13760, 4920, 363140, 761280, 71292520,... lnn < Hn < lnn + 1, Hn = lnn + γ + O

![image 261](cheat_images/imageFile261.png)

![image 262](cheat_images/imageFile262.png)

![image 263](cheat_images/imageFile263.png)

![image 264](cheat_images/imageFile264.png)

![image 265](cheat_images/imageFile265.png)

![image 266](cheat_images/imageFile266.png)

![image 267](cheat_images/imageFile267.png)

![image 268](cheat_images/imageFile268.png)

1 n

![image 269](cheat_images/imageFile269.png)

. Factorial, Stirling’s approximation: 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, ...

n! =

√

![image 270](cheat_images/imageFile270.png)

2πn

n e

![image 271](cheat_images/imageFile271.png)

n

1 + Θ

1 n

![image 272](cheat_images/imageFile272.png)

. Ackermann’s function and inverse:

a(i,j) =   

2j i = 1 a(i − 1,2) j = 1 a(i − 1,a(i,j − 1)) i,j ≥ 2

α(i) = min{j | a(j,j) ≥ i}.

![image 273](cheat_images/imageFile273.png)

Continuous distributions: If Pr[a < X < b] =

b

a

p(x)dx,

then p is the probability density function of X. If

Pr[X < a] = P(a), then P is the distribution function of X. If P and p both exist then

P(a) =

a

−∞

p(x)dx. Expectation: If X is discrete

E[g(X)] =

x

g(x)Pr[X x].

If X continuous then E[g(X)] =

∞

−∞

g(x)p(x)dx =

∞

−∞

g(x)dP(x). Variance, standard deviation:

VAR[X] = E[X2] − E[X]2, σ = VAR[X].

![image 274](cheat_images/imageFile274.png)

For events A and B: Pr[A ∨ B] = Pr[A] + Pr[B] − Pr[A ∧ B] Pr[A ∧ B] = Pr[A] · Pr[B],

iﬀ A and B are independent. Pr[A|B] =

- Pr[A ∧ B]

![image 275](cheat_images/imageFile275.png)

- Pr[B


For random variables X and Y : E[X · Y ] = E[X] · E[Y ],

if X and Y are independent. E[X + Y ] = E[X] + E[Y ],

E[cX] = c E[X]. Bayes’ theorem:

Pr[Ai|B] =

Pr[B|Ai]Pr[Ai]

![image 276](cheat_images/imageFile276.png)

n j=1 Pr[Aj]Pr[B|Aj]

. Inclusion-exclusion:

Pr

n

i=1

Xi =

n

i=1

Pr[Xi] +

n

k=2

(−1)k+1

ii<···<ik

Pr

k

j=1

Xi

j

.

Moment inequalities: Pr |X| ≥ λE[X] ≤

1 λ

![image 277](cheat_images/imageFile277.png)

,

Pr X − E X] ≥ λ · σ ≤

1 λ2

![image 278](cheat_images/imageFile278.png)

. Geometric distribution:

Pr[X = k] = pqk 1, q = 1 − p,

E[X] =

∞

k=1

kpqk 1 =

1 p

![image 279](cheat_images/imageFile279.png)

.

![image 280](cheat_images/imageFile280.png)

![image 281](cheat_images/imageFile281.png)

- 2 4 3

![image 282](cheat_images/imageFile282.png)

![image 283](cheat_images/imageFile283.png)

![image 284](cheat_images/imageFile284.png)

![image 285](cheat_images/imageFile285.png)

![image 286](cheat_images/imageFile286.png)

![image 287](cheat_images/imageFile287.png)

- 3 8 5

![image 288](cheat_images/imageFile288.png)

![image 289](cheat_images/imageFile289.png)

![image 290](cheat_images/imageFile290.png)

![image 291](cheat_images/imageFile291.png)

![image 292](cheat_images/imageFile292.png)

![image 293](cheat_images/imageFile293.png)

- 4 16 7

![image 294](cheat_images/imageFile294.png)

![image 295](cheat_images/imageFile295.png)

![image 296](cheat_images/imageFile296.png)

![image 297](cheat_images/imageFile297.png)

![image 298](cheat_images/imageFile298.png)

![image 299](cheat_images/imageFile299.png)

- 5 32 11

![image 300](cheat_images/imageFile300.png)

![image 301](cheat_images/imageFile301.png)

![image 302](cheat_images/imageFile302.png)

![image 303](cheat_images/imageFile303.png)

![image 304](cheat_images/imageFile304.png)

![image 305](cheat_images/imageFile305.png)

- 6 64 13

![image 306](cheat_images/imageFile306.png)

![image 307](cheat_images/imageFile307.png)

![image 308](cheat_images/imageFile308.png)

![image 309](cheat_images/imageFile309.png)

![image 310](cheat_images/imageFile310.png)

![image 311](cheat_images/imageFile311.png)

- 7 128 17

![image 312](cheat_images/imageFile312.png)

![image 313](cheat_images/imageFile313.png)

![image 314](cheat_images/imageFile314.png)

![image 315](cheat_images/imageFile315.png)

![image 316](cheat_images/imageFile316.png)

![image 317](cheat_images/imageFile317.png)

- 8 256 19

![image 318](cheat_images/imageFile318.png)

![image 319](cheat_images/imageFile319.png)

![image 320](cheat_images/imageFile320.png)

![image 321](cheat_images/imageFile321.png)

![image 322](cheat_images/imageFile322.png)

![image 323](cheat_images/imageFile323.png)

- 9 512 23

![image 324](cheat_images/imageFile324.png)

![image 325](cheat_images/imageFile325.png)

![image 326](cheat_images/imageFile326.png)

![image 327](cheat_images/imageFile327.png)

![image 328](cheat_images/imageFile328.png)

![image 329](cheat_images/imageFile329.png)

- 10 1,024 29

![image 330](cheat_images/imageFile330.png)

![image 331](cheat_images/imageFile331.png)

![image 332](cheat_images/imageFile332.png)

![image 333](cheat_images/imageFile333.png)

![image 334](cheat_images/imageFile334.png)

![image 335](cheat_images/imageFile335.png)

- 11 2,048 31

![image 336](cheat_images/imageFile336.png)

![image 337](cheat_images/imageFile337.png)

![image 338](cheat_images/imageFile338.png)

![image 339](cheat_images/imageFile339.png)

![image 340](cheat_images/imageFile340.png)

![image 341](cheat_images/imageFile341.png)

- 12 4,096 37

![image 342](cheat_images/imageFile342.png)

![image 343](cheat_images/imageFile343.png)

![image 344](cheat_images/imageFile344.png)

![image 345](cheat_images/imageFile345.png)

![image 346](cheat_images/imageFile346.png)

![image 347](cheat_images/imageFile347.png)

- 13 8,192 41

![image 348](cheat_images/imageFile348.png)

![image 349](cheat_images/imageFile349.png)

![image 350](cheat_images/imageFile350.png)

![image 351](cheat_images/imageFile351.png)

![image 352](cheat_images/imageFile352.png)

![image 353](cheat_images/imageFile353.png)

- 14 16,384 43

![image 354](cheat_images/imageFile354.png)

![image 355](cheat_images/imageFile355.png)

![image 356](cheat_images/imageFile356.png)

![image 357](cheat_images/imageFile357.png)

![image 358](cheat_images/imageFile358.png)

![image 359](cheat_images/imageFile359.png)

- 15 32,768 47

![image 360](cheat_images/imageFile360.png)

![image 361](cheat_images/imageFile361.png)

![image 362](cheat_images/imageFile362.png)

![image 363](cheat_images/imageFile363.png)

![image 364](cheat_images/imageFile364.png)

![image 365](cheat_images/imageFile365.png)

- 16 65,536 53

![image 366](cheat_images/imageFile366.png)

![image 367](cheat_images/imageFile367.png)

![image 368](cheat_images/imageFile368.png)

![image 369](cheat_images/imageFile369.png)

![image 370](cheat_images/imageFile370.png)

![image 371](cheat_images/imageFile371.png)

- 17 131,072 59

![image 372](cheat_images/imageFile372.png)

![image 373](cheat_images/imageFile373.png)

![image 374](cheat_images/imageFile374.png)

![image 375](cheat_images/imageFile375.png)

![image 376](cheat_images/imageFile376.png)

![image 377](cheat_images/imageFile377.png)

- 18 262,144 61

![image 378](cheat_images/imageFile378.png)

![image 379](cheat_images/imageFile379.png)

![image 380](cheat_images/imageFile380.png)

![image 381](cheat_images/imageFile381.png)

![image 382](cheat_images/imageFile382.png)

![image 383](cheat_images/imageFile383.png)

- 19 524,288 67

![image 384](cheat_images/imageFile384.png)

![image 385](cheat_images/imageFile385.png)

![image 386](cheat_images/imageFile386.png)

![image 387](cheat_images/imageFile387.png)

![image 388](cheat_images/imageFile388.png)

![image 389](cheat_images/imageFile389.png)

- 20 1,048,576 71

![image 390](cheat_images/imageFile390.png)

![image 391](cheat_images/imageFile391.png)

![image 392](cheat_images/imageFile392.png)

![image 393](cheat_images/imageFile393.png)

![image 394](cheat_images/imageFile394.png)

![image 395](cheat_images/imageFile395.png)

- 21 2,097,152 73

![image 396](cheat_images/imageFile396.png)

![image 397](cheat_images/imageFile397.png)

![image 398](cheat_images/imageFile398.png)

![image 399](cheat_images/imageFile399.png)

![image 400](cheat_images/imageFile400.png)

![image 401](cheat_images/imageFile401.png)

- 22 4,194,304 79

![image 402](cheat_images/imageFile402.png)

![image 403](cheat_images/imageFile403.png)

![image 404](cheat_images/imageFile404.png)

![image 405](cheat_images/imageFile405.png)

![image 406](cheat_images/imageFile406.png)

![image 407](cheat_images/imageFile407.png)

- 23 8,388,608 83

![image 408](cheat_images/imageFile408.png)

![image 409](cheat_images/imageFile409.png)

![image 410](cheat_images/imageFile410.png)

![image 411](cheat_images/imageFile411.png)

![image 412](cheat_images/imageFile412.png)

![image 413](cheat_images/imageFile413.png)

- 24 16,777,216 89

![image 414](cheat_images/imageFile414.png)

![image 415](cheat_images/imageFile415.png)

![image 416](cheat_images/imageFile416.png)

![image 417](cheat_images/imageFile417.png)

![image 418](cheat_images/imageFile418.png)

![image 419](cheat_images/imageFile419.png)

- 25 33,554,432 97

![image 420](cheat_images/imageFile420.png)

![image 421](cheat_images/imageFile421.png)

![image 422](cheat_images/imageFile422.png)

![image 423](cheat_images/imageFile423.png)

![image 424](cheat_images/imageFile424.png)

![image 425](cheat_images/imageFile425.png)

- 26 67,108,864 101

![image 426](cheat_images/imageFile426.png)

![image 427](cheat_images/imageFile427.png)

![image 428](cheat_images/imageFile428.png)

![image 429](cheat_images/imageFile429.png)

![image 430](cheat_images/imageFile430.png)

![image 431](cheat_images/imageFile431.png)

- 27 134,217,728 103

![image 432](cheat_images/imageFile432.png)

![image 433](cheat_images/imageFile433.png)

![image 434](cheat_images/imageFile434.png)

![image 435](cheat_images/imageFile435.png)

![image 436](cheat_images/imageFile436.png)

![image 437](cheat_images/imageFile437.png)

![image 438](cheat_images/imageFile438.png)

![image 439](cheat_images/imageFile439.png)

![image 440](cheat_images/imageFile440.png)

![image 441](cheat_images/imageFile441.png)

![image 442](cheat_images/imageFile442.png)

![image 443](cheat_images/imageFile443.png)

![image 444](cheat_images/imageFile444.png)

- 28 268,435,456 107 Binomial distribution:

![image 445](cheat_images/imageFile445.png)

![image 446](cheat_images/imageFile446.png)

![image 447](cheat_images/imageFile447.png)

Pr[X = k] =

n k

pkqn k, q = 1 − p,

E[X] =

n

k=1

k

n k

pkqn k = np. Poisson distribution: Pr[X = k] =

e−λλk k!

![image 448](cheat_images/imageFile448.png)

, E[X] = λ. Normal (Gaussian) distribution:

p(x) =

1 √2πσ

![image 449](cheat_images/imageFile449.png)

![image 450](cheat_images/imageFile450.png)

e (x µ)

2/2σ2, E[X] = µ.

The “coupon collector”: We are given a random coupon each day, and there are n diﬀerent types of coupons. The distribution of coupons is uniform. The expected number of days to pass before we to collect all n types is

nHn.

![image 451](cheat_images/imageFile451.png)

![image 452](cheat_images/imageFile452.png)

![image 453](cheat_images/imageFile453.png)

- 29 536,870,912 109

![image 454](cheat_images/imageFile454.png)

![image 455](cheat_images/imageFile455.png)

![image 456](cheat_images/imageFile456.png)

![image 457](cheat_images/imageFile457.png)

![image 458](cheat_images/imageFile458.png)

![image 459](cheat_images/imageFile459.png)

- 30 1,073,741,824 113

![image 460](cheat_images/imageFile460.png)

![image 461](cheat_images/imageFile461.png)

![image 462](cheat_images/imageFile462.png)

![image 463](cheat_images/imageFile463.png)

![image 464](cheat_images/imageFile464.png)

![image 465](cheat_images/imageFile465.png)

- 31 2,147,483,648 127

![image 466](cheat_images/imageFile466.png)

![image 467](cheat_images/imageFile467.png)

![image 468](cheat_images/imageFile468.png)

![image 469](cheat_images/imageFile469.png)

![image 470](cheat_images/imageFile470.png)

![image 471](cheat_images/imageFile471.png)

- 32 4,294,967,296 131 Pascal’s Triangle


![image 472](cheat_images/imageFile472.png)

![image 473](cheat_images/imageFile473.png)

![image 474](cheat_images/imageFile474.png)

![image 475](cheat_images/imageFile475.png)

![image 476](cheat_images/imageFile476.png)

![image 477](cheat_images/imageFile477.png)

![image 478](cheat_images/imageFile478.png)

![image 479](cheat_images/imageFile479.png)

![image 480](cheat_images/imageFile480.png)

![image 481](cheat_images/imageFile481.png)

![image 482](cheat_images/imageFile482.png)

![image 483](cheat_images/imageFile483.png)

![image 484](cheat_images/imageFile484.png)

![image 485](cheat_images/imageFile485.png)

![image 486](cheat_images/imageFile486.png)

![image 487](cheat_images/imageFile487.png)

![image 488](cheat_images/imageFile488.png)

![image 489](cheat_images/imageFile489.png)

![image 490](cheat_images/imageFile490.png)

![image 491](cheat_images/imageFile491.png)

![image 492](cheat_images/imageFile492.png)

![image 493](cheat_images/imageFile493.png)

![image 494](cheat_images/imageFile494.png)

![image 495](cheat_images/imageFile495.png)

![image 496](cheat_images/imageFile496.png)

![image 497](cheat_images/imageFile497.png)

![image 498](cheat_images/imageFile498.png)

![image 499](cheat_images/imageFile499.png)

![image 500](cheat_images/imageFile500.png)

![image 501](cheat_images/imageFile501.png)

![image 502](cheat_images/imageFile502.png)

1

![image 503](cheat_images/imageFile503.png)

- 1 1

![image 504](cheat_images/imageFile504.png)

![image 505](cheat_images/imageFile505.png)

![image 506](cheat_images/imageFile506.png)

![image 507](cheat_images/imageFile507.png)

- 1 2 1

![image 508](cheat_images/imageFile508.png)

![image 509](cheat_images/imageFile509.png)

![image 510](cheat_images/imageFile510.png)

![image 511](cheat_images/imageFile511.png)

- 1 3 3 1

![image 512](cheat_images/imageFile512.png)

![image 513](cheat_images/imageFile513.png)

![image 514](cheat_images/imageFile514.png)

![image 515](cheat_images/imageFile515.png)

- 1 4 6 4 1

![image 516](cheat_images/imageFile516.png)

![image 517](cheat_images/imageFile517.png)

![image 518](cheat_images/imageFile518.png)

![image 519](cheat_images/imageFile519.png)

- 1 5 10 10 5 1

![image 520](cheat_images/imageFile520.png)

![image 521](cheat_images/imageFile521.png)

![image 522](cheat_images/imageFile522.png)

![image 523](cheat_images/imageFile523.png)

- 1 6 15 20 15 6 1

![image 524](cheat_images/imageFile524.png)

![image 525](cheat_images/imageFile525.png)

![image 526](cheat_images/imageFile526.png)

![image 527](cheat_images/imageFile527.png)

- 1 7 21 35 35 21 7 1

![image 528](cheat_images/imageFile528.png)

![image 529](cheat_images/imageFile529.png)

![image 530](cheat_images/imageFile530.png)

![image 531](cheat_images/imageFile531.png)

- 1 8 28 56 70 56 28 8 1

![image 532](cheat_images/imageFile532.png)

![image 533](cheat_images/imageFile533.png)

![image 534](cheat_images/imageFile534.png)

![image 535](cheat_images/imageFile535.png)

- 1 9 36 84 126 126 84 36 9 1


![image 536](cheat_images/imageFile536.png)

![image 537](cheat_images/imageFile537.png)

![image 538](cheat_images/imageFile538.png)

![image 539](cheat_images/imageFile539.png)

![image 540](cheat_images/imageFile540.png)

![image 541](cheat_images/imageFile541.png)

![image 542](cheat_images/imageFile542.png)

1 10 45 120 210 252 210 120 45 10 1

![image 543](cheat_images/imageFile543.png)

![image 548](cheat_images/imageFile548.png)

![image 549](cheat_images/imageFile549.png)

![image 550](cheat_images/imageFile550.png)

![image 551](cheat_images/imageFile551.png)

Trigonometry Matrices More Trig.

![image 552](cheat_images/imageFile552.png)

![image 553](cheat_images/imageFile553.png)

![image 554](cheat_images/imageFile554.png)

![image 555](cheat_images/imageFile555.png)

![image 556](cheat_images/imageFile556.png)

C

Multiplication: C = A · B, ci,j =

n

<table>
  <tr>
    <th> </th>
    <th>θ<br><br>(0,1)<br><br>(cos</th>
  </tr>
  <tr>
    <td>,0)</td>
    <td>(0,-1)<br><br>(</td>
  </tr>
</table>


ai,kbk,j. Determinants: det A = 0 iﬀ A is non-singular.

a

b

h A

b

θ,sinθ)

k=1

C

A

c

B

detA · B = detA · detB, detA =

Law of cosines: c2 = a2+b2−2ab cosC. Area:

c

a

n

sign(π)ai,π(i). 2 × 2 and 3 × 3 determinant:

B

π

i=1

Pythagorean theorem:

C2 = A2 + B2. Deﬁnitions:

A = 12hc,

a b c d

![image 557](cheat_images/imageFile557.png)

= ad bc,

= 12ab sinC,

![image 558](cheat_images/imageFile558.png)

sina = A/C, cosa = B/C, csca = C/A, seca = C/B,

c2 sinAsinB 2 sinC

a b c d e f g h i

=

. Heron’s formula:

b c e f − h

a c d f

a b d e

![image 559](cheat_images/imageFile559.png)

= g

+ i

sina cosa

- A

![image 560](cheat_images/imageFile560.png)

- B


cosa sina

B A

tana =

. Area, radius of inscribed circle:

=

, cota =

=

![image 561](cheat_images/imageFile561.png)

![image 562](cheat_images/imageFile562.png)

![image 563](cheat_images/imageFile563.png)

aei + bfg + cdh

A = √s · sa · sb · sc, s = 12(a + b + c),

=

![image 564](cheat_images/imageFile564.png)

− ceg − fha − ibd. Permanents:

AB A + B + C

- 1

![image 565](cheat_images/imageFile565.png)

- 2 AB,


.

![image 566](cheat_images/imageFile566.png)

![image 567](cheat_images/imageFile567.png)

n

- sa = s − a,
- sb = s − b,
- sc = s − c. More identities:


ai,π(i).

permA =

Identities: sinx =

π

i=1

1 sec x

1 csc x

![image 568](cheat_images/imageFile568.png)

![image 569](cheat_images/imageFile569.png)

![image 570](cheat_images/imageFile570.png)

![image 571](cheat_images/imageFile571.png)

![image 572](cheat_images/imageFile572.png)

![image 573](cheat_images/imageFile573.png)

![image 574](cheat_images/imageFile574.png)

![image 575](cheat_images/imageFile575.png)

![image 576](cheat_images/imageFile576.png)

![image 577](cheat_images/imageFile577.png)

![image 578](cheat_images/imageFile578.png)

, tanx =

, cosx =

Hyperbolic Functions

![image 579](cheat_images/imageFile579.png)

![image 580](cheat_images/imageFile580.png)

![image 581](cheat_images/imageFile581.png)

![image 582](cheat_images/imageFile582.png)

![image 583](cheat_images/imageFile583.png)

![image 584](cheat_images/imageFile584.png)

![image 585](cheat_images/imageFile585.png)

![image 586](cheat_images/imageFile586.png)

![image 587](cheat_images/imageFile587.png)

![image 588](cheat_images/imageFile588.png)

![image 589](cheat_images/imageFile589.png)

1 cotx

Deﬁnitions: sinhx =

, sin2 x + cos2 x = 1, 1 + tan2 x = sec2 x, 1 + cot2 x = csc2 x,

![image 590](cheat_images/imageFile590.png)

ex − e−x 2

ex + e−x 2

![image 591](cheat_images/imageFile591.png)

1 − cosx 2

sin x2 =

, tanhx =

, coshx =

,

![image 592](cheat_images/imageFile592.png)

![image 593](cheat_images/imageFile593.png)

![image 594](cheat_images/imageFile594.png)

![image 595](cheat_images/imageFile595.png)

ex − e−x ex + e x

1 sinhx

, cschx =

, sechx =

![image 596](cheat_images/imageFile596.png)

![image 597](cheat_images/imageFile597.png)

sinx = cos π2 − x , sinx = sin(π − x), cosx = − cos(π − x), tanx = cot π2 − x , cotx = cot(π x), csc x = cot x2 cotx, sin(x ± y) = sinxcosy ± cosxsiny,

- cos x2 =

![image 598](cheat_images/imageFile598.png)

![image 599](cheat_images/imageFile599.png)

1 + cosx 2

![image 600](cheat_images/imageFile600.png)

,

tan x2 =

![image 601](cheat_images/imageFile601.png)

![image 602](cheat_images/imageFile602.png)

1 − cosx 1 + cosx

![image 603](cheat_images/imageFile603.png)

,

=

1 − cosx sinx

![image 604](cheat_images/imageFile604.png)

,

=

sinx 1 + cosx

![image 605](cheat_images/imageFile605.png)

,

- cot x2 =


![image 606](cheat_images/imageFile606.png)

1 coshx

1 tanhx

, cothx =

.

![image 607](cheat_images/imageFile607.png)

![image 608](cheat_images/imageFile608.png)

![image 609](cheat_images/imageFile609.png)

Identities: cosh2 x − sinh2 x = 1, tanh2 x + sech2 x = 1, coth2 x − csch2 x = 1, sinh(−x) = − sinhx, cosh(−x) = coshx, tanh(−x) = − tanhx, sinh(x + y) = sinhxcoshy + coshxsinhy, cosh(x + y) = coshxcoshy + sinhxsinhy, sinh2x = 2 sinhxcoshx, cosh2x = cosh2 x + sinh2 x, coshx + sinhx = ex, coshx − sinhx = e−x, (coshx + sinhx)n = coshnx + sinhnx, n ∈ Z,

![image 610](cheat_images/imageFile610.png)

- cos(x ± y) = cosxcos y ∓ sinxsiny,

tan(x ± y) =

tanx ± tany 1 ∓ tanxtany

![image 611](cheat_images/imageFile611.png)

,

- cot(x ± y) =


![image 612](cheat_images/imageFile612.png)

1 + cosx 1 − cosx

,

![image 613](cheat_images/imageFile613.png)

![image 614](cheat_images/imageFile614.png)

1 + cosx sinx

cotxcoty ∓ 1 cotx ± coty

=

,

![image 615](cheat_images/imageFile615.png)

, sin2x = 2 sinxcosx, sin2x =

![image 616](cheat_images/imageFile616.png)

sinx 1 − cosx

2 tanx 1 + tan2 x

,

=

,

![image 617](cheat_images/imageFile617.png)

![image 618](cheat_images/imageFile618.png)

eix − e−ix 2i

cos2x = cos2 x sin2 x, cos2x = 2 cos2 x − 1, cos2x = 1 − 2 sin2 x, cos2x =

sinx =

,

![image 619](cheat_images/imageFile619.png)

1 − tan2 x 1 + tan2 x

eix + e ix 2

,

,

cosx =

![image 620](cheat_images/imageFile620.png)

![image 621](cheat_images/imageFile621.png)

cot2 x − 1 2 cotx

eix − e−ix eix + e ix

2 tanx 1 − tan2 x

,

tan2x =

, cot2x =

tanx = −i

,

- 2 sinh2 x2 = coshx − 1, 2 cosh2 x2 = coshx + 1. θ sinθ cosθ tanθ

![image 622](cheat_images/imageFile622.png)

![image 623](cheat_images/imageFile623.png)

![image 624](cheat_images/imageFile624.png)

![image 625](cheat_images/imageFile625.png)

![image 626](cheat_images/imageFile626.png)

![image 627](cheat_images/imageFile627.png)

![image 628](cheat_images/imageFile628.png)

![image 629](cheat_images/imageFile629.png)

![image 630](cheat_images/imageFile630.png)

![image 631](cheat_images/imageFile631.png)

![image 632](cheat_images/imageFile632.png)

![image 633](cheat_images/imageFile633.png)

![image 634](cheat_images/imageFile634.png)

0 0 1 0

π 6

![image 635](cheat_images/imageFile635.png)

- 1

![image 636](cheat_images/imageFile636.png)

- 2


√3 2

![image 637](cheat_images/imageFile637.png)

![image 638](cheat_images/imageFile638.png)

√3 3

![image 639](cheat_images/imageFile639.png)

![image 640](cheat_images/imageFile640.png)

π 4

![image 641](cheat_images/imageFile641.png)

√2 2

![image 642](cheat_images/imageFile642.png)

![image 643](cheat_images/imageFile643.png)

√2

![image 644](cheat_images/imageFile644.png)

![image 645](cheat_images/imageFile645.png)

2 1 π

![image 646](cheat_images/imageFile646.png)

- 3


![image 647](cheat_images/imageFile647.png)

![image 648](cheat_images/imageFile648.png)

![image 649](cheat_images/imageFile649.png)

e2ix − 1 e2ix + 1

sin(x + y)sin(x − y) = sin2 x − sin2 y, cos(x + y)cos(x y) = cos2 x sin2 y. Euler’s equation:

= i

,

![image 650](cheat_images/imageFile650.png)

![image 651](cheat_images/imageFile651.png)

![image 652](cheat_images/imageFile652.png)

... in mathematics you don’t understand things, you just get used to them.

![image 653](cheat_images/imageFile653.png)

sinhix i

,

sinx =

![image 654](cheat_images/imageFile654.png)

cosx = coshix, tanx =

eix = cosx + i sinx, eiπ = −1.

tanhix i

√3

![image 655](cheat_images/imageFile655.png)

![image 656](cheat_images/imageFile656.png)

![image 657](cheat_images/imageFile657.png)

![image 658](cheat_images/imageFile658.png)

![image 659](cheat_images/imageFile659.png)

√3 2

![image 660](cheat_images/imageFile660.png)

![image 661](cheat_images/imageFile661.png)

![image 662](cheat_images/imageFile662.png)

![image 663](cheat_images/imageFile663.png)

![image 664](cheat_images/imageFile664.png)

– J. von Neumannv2.02c1994 by Steve Seiden

.

![image 665](cheat_images/imageFile665.png)

- 1

![image 666](cheat_images/imageFile666.png)

- 2


![image 667](cheat_images/imageFile667.png)

![image 668](cheat_images/imageFile668.png)

![image 669](cheat_images/imageFile669.png)

sseiden@acm.org http://www.csc.lsu.edu/~seiden

π 2 1 0 ∞

![image 670](cheat_images/imageFile670.png)

![image 671](cheat_images/imageFile671.png)

![image 672](cheat_images/imageFile672.png)

![image 673](cheat_images/imageFile673.png)

![image 674](cheat_images/imageFile674.png)

Theoretical Computer Science Cheat Sheet

![image 675](cheat_images/imageFile675.png)

![image 676](cheat_images/imageFile676.png)

![image 677](cheat_images/imageFile677.png)

![image 678](cheat_images/imageFile678.png)

Number Theory Graph Theory The Chinese remainder theorem: There exists a number C such that:

![image 679](cheat_images/imageFile679.png)

![image 680](cheat_images/imageFile680.png)

![image 681](cheat_images/imageFile681.png)

![image 682](cheat_images/imageFile682.png)

![image 683](cheat_images/imageFile683.png)

Notation: E(G) Edge set V (G) Vertex set c(G) Number of components G[S] Induced subgraph deg(v) Degree of v ∆(G) Maximum degree δ(G) Minimum degree χ(G) Chromatic number χE(G) Edge chromatic number Gc Complement graph Kn Complete graph Kn

Deﬁnitions: Loop An edge connecting a vertex to itself.

![image 684](cheat_images/imageFile684.png)

![image 685](cheat_images/imageFile685.png)

C ≡ r1 mod m1

Directed Each edge has a direction. Simple Graph with no loops or multi-edges.

. . .

C ≡ rn mod mn if mi and mj are relatively prime for i = j. Euler’s function: φ(x) is the number of positive integers less than x relatively prime to x. If ni=1 pe

Walk A sequence v0e1v1 ...eℓvℓ. Trail A walk with distinct edges. Path A trail with distinct

vertices.

Connected A graph where there exists a path between any two vertices.

i is the prime factorization of x then

i

1,n2 Complete bipartite graph r(k,ℓ) Ramsey number

n

pe

i−1

i (pi − 1).

φ(x) =

Component A maximal connected

i=1

![image 686](cheat_images/imageFile686.png)

![image 687](cheat_images/imageFile687.png)

![image 688](cheat_images/imageFile688.png)

![image 689](cheat_images/imageFile689.png)

![image 690](cheat_images/imageFile690.png)

subgraph. Tree A connected acyclic graph. Free tree A tree with no root. DAG Directed acyclic graph. Eulerian Graph with a trail visiting

![image 691](cheat_images/imageFile691.png)

![image 692](cheat_images/imageFile692.png)

![image 693](cheat_images/imageFile693.png)

![image 694](cheat_images/imageFile694.png)

Geometry Projective coordinates: triples (x,y,z), not all x, y and z zero.

Euler’s theorem: If a and b are relatively prime then

![image 695](cheat_images/imageFile695.png)

![image 696](cheat_images/imageFile696.png)

![image 697](cheat_images/imageFile697.png)

![image 698](cheat_images/imageFile698.png)

![image 699](cheat_images/imageFile699.png)

![image 700](cheat_images/imageFile700.png)

![image 701](cheat_images/imageFile701.png)

![image 702](cheat_images/imageFile702.png)

![image 703](cheat_images/imageFile703.png)

1 ≡ aφ(b) mod b. Fermat’s theorem:

(x,y,z) = (cx,cy,cz) ∀c = 0. Cartesian Projective (x,y) (x,y,1) y = mx + b (m,−1,b) x = c (1,0,−c)

each edge exactly once. Hamiltonian Graph with a cycle visiting each vertex exactly once.

1 ≡ ap−1 mod p.

![image 704](cheat_images/imageFile704.png)

The Euclidean algorithm: if a > b are integers then

Cut A set of edges whose removal increases the number of components.

gcd(a,b) = gcd(a mod b,b). If ni=1 pe

Distance formula, Lp and L∞ metric:

i is the prime factorization of x then

i

Cut-set A minimal cut. Cut edge A size 1 cut. k-Connected A graph connected with

![image 705](cheat_images/imageFile705.png)

(x1 − x0)2 + (y1 − y0)2,

n

pe

i+1

i − 1 pi 1

|x1 − x0 p + |y1 − y0|p 1/p, lim p→∞

.

d =

S(x) =

![image 706](cheat_images/imageFile706.png)

i=1

the removal of any k − 1 vertices.

x1 − x0|p + |y1 − y0 p 1/p.

d|x

Perfect Numbers: x is an even perfect number iﬀ x = 2n−1(2n−1) and 2n−1 is prime. Wilson’s theorem: n is a prime iﬀ

Area of triangle (x0,y0), (x1,y1) and (x2,y2):

k-Tough ∀S ⊆ V,S = ∅ we have k · c(G − S) ≤ |S|. k-Regular A graph where all vertices have degree k. k-Factor A k-regular spanning subgraph. Matching A set of edges, no two of which are adjacent. Clique A set of vertices, all of which are adjacent. Ind. set A set of vertices, none of which are adjacent. Vertex cover A set of vertices which cover all edges. Planar graph A graph which can be embeded in the plane. Plane graph An embedding of a planar graph.

x1 − x0 y1 − y0 x2 − x0 y2 − y0

(n 1)! ≡ −1 mod n. Mo¨bius inversion:

- 1

![image 707](cheat_images/imageFile707.png)

- 2 abs


. Angle formed by three points:

1 if i = 1. 0 if i is not square-free. (−1)r if i is the product of

 

µ(i) =

(x2,y2) ℓ2



r distinct primes. If

θ

F(d),

G(a) =

(x1,y1)

ℓ1 cosθ =

(0,0)

d a

(x1,y1) · (x2,y2) ℓ1ℓ2

.

![image 708](cheat_images/imageFile708.png)

then

a d

µ(d)G

F(a) =

.

Line through two points (x0,y0) and (x1,y1):

![image 709](cheat_images/imageFile709.png)

d|a

x y 1 x0 y0 1 x1 y1 1

Prime numbers: pn = n lnn + n lnlnn − n + n

lnlnn lnn

= 0.

![image 710](cheat_images/imageFile710.png)

n lnn

![image 711](cheat_images/imageFile711.png)

Area of circle, volume of sphere: A = πr2, V = 43πr3.

,

+ O

deg(v) = 2m. If G is planar then n m + f = 2, so

![image 712](cheat_images/imageFile712.png)

![image 713](cheat_images/imageFile713.png)

v∈V

n lnn

2!n (ln n)3

n (ln n)2

π(n) =

+

![image 714](cheat_images/imageFile714.png)

![image 715](cheat_images/imageFile715.png)

![image 716](cheat_images/imageFile716.png)

![image 717](cheat_images/imageFile717.png)

![image 718](cheat_images/imageFile718.png)

![image 719](cheat_images/imageFile719.png)

![image 720](cheat_images/imageFile720.png)

![image 721](cheat_images/imageFile721.png)

![image 722](cheat_images/imageFile722.png)

![image 723](cheat_images/imageFile723.png)

![image 724](cheat_images/imageFile724.png)

![image 725](cheat_images/imageFile725.png)

If I have seen farther than others, it is because I have stood on the shoulders of giants.

f ≤ 2n − 4, m ≤ 3n − 6. Any planar graph has a vertex with degree ≤ 5.

n (lnn)4

.

+ O

![image 726](cheat_images/imageFile726.png)

– Issac Newton

![image 727](cheat_images/imageFile727.png)

![image 728](cheat_images/imageFile728.png)

![image 729](cheat_images/imageFile729.png)

![image 730](cheat_images/imageFile730.png)

Theoretical Computer Science Cheat Sheet

![image 731](cheat_images/imageFile731.png)

![image 732](cheat_images/imageFile732.png)

![image 733](cheat_images/imageFile733.png)

![image 734](cheat_images/imageFile734.png)

π Calculus Wallis’ identity:

![image 735](cheat_images/imageFile735.png)

![image 736](cheat_images/imageFile736.png)

![image 737](cheat_images/imageFile737.png)

![image 738](cheat_images/imageFile738.png)

Derivatives: 1.

2 · 2 · 4 · 4 · 6 · 6 ··· 1 · 3 · 3 · 5 · 5 · 7 ···

π = 2 ·

du dx

d(u + v) dx

du dx

dv dx

d(uv) dx

dv dx

du dx

d(cu) dx

![image 739](cheat_images/imageFile739.png)

= c

, 2.

=

+

, 3.

= u

+ v

,

![image 740](cheat_images/imageFile740.png)

![image 741](cheat_images/imageFile741.png)

![image 742](cheat_images/imageFile742.png)

![image 743](cheat_images/imageFile743.png)

![image 744](cheat_images/imageFile744.png)

![image 745](cheat_images/imageFile745.png)

![image 746](cheat_images/imageFile746.png)

![image 747](cheat_images/imageFile747.png)

Brouncker’s continued fraction expansion:

v dudx − u dvdx v2

d(ecu) dx

d(un) dx

du dx

d(u/v) dx

du dx

12 2 + 32

![image 748](cheat_images/imageFile748.png)

![image 749](cheat_images/imageFile749.png)

= nun−1

= cecu

, 6.

, 5.

=

,

4.

π 4 = 1 +

![image 750](cheat_images/imageFile750.png)

![image 751](cheat_images/imageFile751.png)

![image 752](cheat_images/imageFile752.png)

![image 753](cheat_images/imageFile753.png)

![image 754](cheat_images/imageFile754.png)

![image 755](cheat_images/imageFile755.png)

![image 756](cheat_images/imageFile756.png)

![image 757](cheat_images/imageFile757.png)

![image 758](cheat_images/imageFile758.png)

2+ 52

![image 759](cheat_images/imageFile759.png)

2+ 72 2+···

![image 760](cheat_images/imageFile760.png)

- 7.

d(cu) dx

![image 761](cheat_images/imageFile761.png)

= (lnc)cu

du dx

![image 762](cheat_images/imageFile762.png)

, 8.

d(ln u) dx

![image 763](cheat_images/imageFile763.png)

=

1 u

![image 764](cheat_images/imageFile764.png)

du dx

![image 765](cheat_images/imageFile765.png)

,

- 9.

d(sinu) dx

![image 766](cheat_images/imageFile766.png)

= cosu

du dx

![image 767](cheat_images/imageFile767.png)

, 10.

d(cosu) dx

![image 768](cheat_images/imageFile768.png)

= − sinu

du dx

![image 769](cheat_images/imageFile769.png)

,

- 11.

d(tanu) dx

![image 770](cheat_images/imageFile770.png)

= sec2 u

du dx

![image 771](cheat_images/imageFile771.png)

, 12.

d(cotu) dx

![image 772](cheat_images/imageFile772.png)

= csc2 u

du dx

![image 773](cheat_images/imageFile773.png)

,

- 13.

d(sec u) dx

![image 774](cheat_images/imageFile774.png)

= tanu secu

du dx

![image 775](cheat_images/imageFile775.png)

, 14.

d(csc u) dx

![image 776](cheat_images/imageFile776.png)

= − cotu cscu

du dx

![image 777](cheat_images/imageFile777.png)

,

15.

d(arcsinu) dx

![image 778](cheat_images/imageFile778.png)

=

1 √1 − u2

![image 779](cheat_images/imageFile779.png)

![image 780](cheat_images/imageFile780.png)

du dx

![image 781](cheat_images/imageFile781.png)

, 16.

d(arccosu) dx

![image 782](cheat_images/imageFile782.png)

= −1 √1 − u2

![image 783](cheat_images/imageFile783.png)

![image 784](cheat_images/imageFile784.png)

du dx

![image 785](cheat_images/imageFile785.png)

,

17.

d(arctanu) dx

![image 786](cheat_images/imageFile786.png)

=

1 1 + u2

![image 787](cheat_images/imageFile787.png)

du dx

![image 788](cheat_images/imageFile788.png)

, 18.

d(arccotu) dx

![image 789](cheat_images/imageFile789.png)

= −1 1 + u2

![image 790](cheat_images/imageFile790.png)

du dx

![image 791](cheat_images/imageFile791.png)

,

19.

d(arcsecu) dx

![image 792](cheat_images/imageFile792.png)

=

1 u√1 − u2

![image 793](cheat_images/imageFile793.png)

![image 794](cheat_images/imageFile794.png)

du dx

![image 795](cheat_images/imageFile795.png)

, 20.

d(arccscu) dx

![image 796](cheat_images/imageFile796.png)

= −1 u√1 u2

![image 797](cheat_images/imageFile797.png)

![image 798](cheat_images/imageFile798.png)

du dx

![image 799](cheat_images/imageFile799.png)

,

21.

d(sinhu) dx

![image 800](cheat_images/imageFile800.png)

= coshu

du dx

![image 801](cheat_images/imageFile801.png)

, 22.

d(coshu) dx

![image 802](cheat_images/imageFile802.png)

= sinhu

du dx

![image 803](cheat_images/imageFile803.png)

,

23.

d(tanhu) dx

![image 804](cheat_images/imageFile804.png)

= sech2 u

du dx

![image 805](cheat_images/imageFile805.png)

, 24.

d(cothu) dx

![image 806](cheat_images/imageFile806.png)

= − csch2 u

du dx

![image 807](cheat_images/imageFile807.png)

,

25.

d(sechu) dx

![image 808](cheat_images/imageFile808.png)

= − sechu tanhu

du dx

![image 809](cheat_images/imageFile809.png)

, 26.

d(cschu) dx

![image 810](cheat_images/imageFile810.png)

= − cschu cothu

du dx

![image 811](cheat_images/imageFile811.png)

,

27.

d(arcsinhu) dx

![image 812](cheat_images/imageFile812.png)

=

1 √1 + u2

![image 813](cheat_images/imageFile813.png)

![image 814](cheat_images/imageFile814.png)

du dx

![image 815](cheat_images/imageFile815.png)

, 28.

d(arccoshu) dx

![image 816](cheat_images/imageFile816.png)

=

1 √u2 − 1

![image 817](cheat_images/imageFile817.png)

![image 818](cheat_images/imageFile818.png)

du dx

![image 819](cheat_images/imageFile819.png)

,

29.

d(arctanhu) dx

![image 820](cheat_images/imageFile820.png)

=

1 1 − u2

![image 821](cheat_images/imageFile821.png)

du dx

![image 822](cheat_images/imageFile822.png)

, 30.

d(arccothu) dx

![image 823](cheat_images/imageFile823.png)

=

1 u2 − 1

![image 824](cheat_images/imageFile824.png)

du dx

![image 825](cheat_images/imageFile825.png)

,

31.

d(arcsechu) dx

![image 826](cheat_images/imageFile826.png)

= −1 u√1 − u2

![image 827](cheat_images/imageFile827.png)

![image 828](cheat_images/imageFile828.png)

du dx

![image 829](cheat_images/imageFile829.png)

, 32.

d(arccschu) dx

![image 830](cheat_images/imageFile830.png)

= −1 u|

![image 831](cheat_images/imageFile831.png)

√1 + u2

![image 832](cheat_images/imageFile832.png)

du dx

![image 833](cheat_images/imageFile833.png)

. Integrals:

1. cu dx = c u dx, 2. (u + v)dx = u dx + v dx,

3. xn dx =

1 n + 1

![image 834](cheat_images/imageFile834.png)

xn+1, n = 1, 4.

1 x

![image 835](cheat_images/imageFile835.png)

dx = lnx, 5. ex dx = ex,

6.

dx 1 + x2

![image 836](cheat_images/imageFile836.png)

= arctanx, 7. u

dv dx

![image 837](cheat_images/imageFile837.png)

dx = uv − v

du dx

![image 838](cheat_images/imageFile838.png)

dx,

8. sinxdx = − cosx, 9. cosxdx = sinx,

10. tanxdx = − ln|cosx|, 11. cotxdx = ln cosx|,

12. secxdx = ln|secx + tanx|, 13. cscxdx = ln|cscx + cotx|,

- 14. arcsin xadx = arcsin xa + a2 x2, a > 0,








Gregrory’s series: π 4 = 1 13 + 15

1 7 + 19 − ···

![image 839](cheat_images/imageFile839.png)

![image 840](cheat_images/imageFile840.png)

![image 841](cheat_images/imageFile841.png)

![image 842](cheat_images/imageFile842.png)

![image 843](cheat_images/imageFile843.png)

Newton’s series:

1 · 3 2 · 4 · 5 · 25

- 1

![image 844](cheat_images/imageFile844.png)

- 2


1 2 · 3 · 23

π 6 =

+ ··· Sharp’s series:

+

+

![image 845](cheat_images/imageFile845.png)

![image 846](cheat_images/imageFile846.png)

![image 847](cheat_images/imageFile847.png)

1 √3

1 31 · 3

1 32 · 5 −

1 33 · 7

π 6 =

1−

+··· Euler’s series:

+

![image 848](cheat_images/imageFile848.png)

![image 849](cheat_images/imageFile849.png)

![image 850](cheat_images/imageFile850.png)

![image 851](cheat_images/imageFile851.png)

![image 852](cheat_images/imageFile852.png)

![image 853](cheat_images/imageFile853.png)

π2

6 = 112 + 122 + 132 + 142 + 152 + ··· π2

![image 854](cheat_images/imageFile854.png)

![image 855](cheat_images/imageFile855.png)

![image 856](cheat_images/imageFile856.png)

![image 857](cheat_images/imageFile857.png)

![image 858](cheat_images/imageFile858.png)

![image 859](cheat_images/imageFile859.png)

8 = 112 + 132 + 152 + 172 + 192 + ···

![image 860](cheat_images/imageFile860.png)

![image 861](cheat_images/imageFile861.png)

![image 862](cheat_images/imageFile862.png)

![image 863](cheat_images/imageFile863.png)

![image 864](cheat_images/imageFile864.png)

![image 865](cheat_images/imageFile865.png)

π2 12 = 112 − 122 + 132 − 142 + 152 − ···

![image 866](cheat_images/imageFile866.png)

![image 867](cheat_images/imageFile867.png)

![image 868](cheat_images/imageFile868.png)

![image 869](cheat_images/imageFile869.png)

![image 870](cheat_images/imageFile870.png)

![image 871](cheat_images/imageFile871.png)

![image 872](cheat_images/imageFile872.png)

![image 873](cheat_images/imageFile873.png)

![image 874](cheat_images/imageFile874.png)

![image 875](cheat_images/imageFile875.png)

![image 876](cheat_images/imageFile876.png)

![image 877](cheat_images/imageFile877.png)

![image 878](cheat_images/imageFile878.png)

Partial Fractions Let N(x) and D(x) be polynomial functions of x. We can break down N(x)/D(x) using partial fraction expansion. First, if the degree of N is greater than or equal to the degree of D, divide N by D, obtaining

![image 879](cheat_images/imageFile879.png)

![image 880](cheat_images/imageFile880.png)

![image 881](cheat_images/imageFile881.png)

![image 882](cheat_images/imageFile882.png)

![image 883](cheat_images/imageFile883.png)

![image 884](cheat_images/imageFile884.png)

![image 885](cheat_images/imageFile885.png)

N′(x) D(x)

N(x) D(x)

= Q(x) +

,

![image 886](cheat_images/imageFile886.png)

![image 887](cheat_images/imageFile887.png)

where the degree of N′ is less than that of D. Second, factor D(x). Use the following rules: For a non-repeated factor:

N′(x) D(x)

A x − a

N(x) (x − a)D(x)

, where

=

+

![image 888](cheat_images/imageFile888.png)

![image 889](cheat_images/imageFile889.png)

![image 890](cheat_images/imageFile890.png)

N(x) D(x) x=a

A =

.

![image 891](cheat_images/imageFile891.png)

For a repeated factor:

m−1

N′(x) D(x)

N(x) (x − a)mD(x)

Ak (x − a)m−k +

=

,

![image 892](cheat_images/imageFile892.png)

![image 893](cheat_images/imageFile893.png)

![image 894](cheat_images/imageFile894.png)

k=0

where

dk dxk

N(x) D(x) x a

1 k!

.

Ak

![image 895](cheat_images/imageFile895.png)

![image 896](cheat_images/imageFile896.png)

![image 897](cheat_images/imageFile897.png)

![image 898](cheat_images/imageFile898.png)

![image 899](cheat_images/imageFile899.png)

![image 900](cheat_images/imageFile900.png)

![image 901](cheat_images/imageFile901.png)

![image 902](cheat_images/imageFile902.png)

![image 903](cheat_images/imageFile903.png)

![image 904](cheat_images/imageFile904.png)

The reasonable man adapts himself to the world; the unreasonable persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable. – George Bernard Shaw

![image 905](cheat_images/imageFile905.png)

![image 906](cheat_images/imageFile906.png)

![image 907](cheat_images/imageFile907.png)

![image 908](cheat_images/imageFile908.png)

![image 909](cheat_images/imageFile909.png)

![image 910](cheat_images/imageFile910.png)

![image 911](cheat_images/imageFile911.png)

Theoretical Computer Science Cheat Sheet

![image 912](cheat_images/imageFile912.png)

![image 913](cheat_images/imageFile913.png)

![image 914](cheat_images/imageFile914.png)

Calculus Cont. 15. arccos xadx = arccos xa − a2 − x2, a > 0, 16. arctan xadx = xarctan xa − a2 ln(a2 + x2), a > 0,

![image 915](cheat_images/imageFile915.png)

![image 916](cheat_images/imageFile916.png)

![image 917](cheat_images/imageFile917.png)

![image 918](cheat_images/imageFile918.png)

![image 919](cheat_images/imageFile919.png)

![image 920](cheat_images/imageFile920.png)

![image 921](cheat_images/imageFile921.png)

![image 922](cheat_images/imageFile922.png)

![image 923](cheat_images/imageFile923.png)

17. sin2(ax)dx = 12a ax sin(ax)cos(ax) , 18. cos2(ax)dx = 12a ax + sin(ax)cos(ax) ,

![image 924](cheat_images/imageFile924.png)

![image 925](cheat_images/imageFile925.png)

19. sec2 xdx = tanx, 20. csc2 xdx = − cotx,

sinn−1 xcosx n

cosn−1 xsinx n

n − 1 n

n − 1 n

21. sinn xdx = −

sinn−2 xdx, 22. cosn xdx =

cosn 2 xdx,

+

+

![image 926](cheat_images/imageFile926.png)

![image 927](cheat_images/imageFile927.png)

![image 928](cheat_images/imageFile928.png)

![image 929](cheat_images/imageFile929.png)

tann 1 x n − 1 − tann−2 xdx, n = 1, 24. cotn xdx = −

cotn 1 x n − 1 − cotn−2 xdx, n = 1,

23. tann xdx =

![image 930](cheat_images/imageFile930.png)

![image 931](cheat_images/imageFile931.png)

- 25. secn xdx =

tanxsecn 1 x n − 1

![image 932](cheat_images/imageFile932.png)

+

n − 2 n − 1

![image 933](cheat_images/imageFile933.png)

secn−2 xdx, n = 1,

- 26. cscn xdx = −


cotxcscn−1 x n − 1

n − 2 n − 1

cscn−2 xdx, n = 1, 27. sinhxdx = coshx, 28. coshxdx = sinhx,

+

![image 934](cheat_images/imageFile934.png)

![image 935](cheat_images/imageFile935.png)

29. tanhxdx = ln|coshx|, 30. cothxdx = ln|sinhx|, 31. sechxdx = arctansinhx, 32. cschxdx = ln tanh x2 ,

![image 936](cheat_images/imageFile936.png)

33. sinh2 xdx = 14 sinh(2x) − 12x, 34. cosh2 xdx = 14 sinh(2x) + 12x, 35. sech2 xdx = tanhx,

![image 937](cheat_images/imageFile937.png)

![image 938](cheat_images/imageFile938.png)

![image 939](cheat_images/imageFile939.png)

![image 940](cheat_images/imageFile940.png)

![image 941](cheat_images/imageFile941.png)

36. arcsinh xadx = xarcsinh xa − x2 + a2, a > 0, 37. arctanh xadx = xarctanh xa + a2 ln|a2 − x2|,

![image 942](cheat_images/imageFile942.png)

![image 943](cheat_images/imageFile943.png)

![image 944](cheat_images/imageFile944.png)

![image 945](cheat_images/imageFile945.png)

![image 946](cheat_images/imageFile946.png)

- 38. arccosh xadx = 

![image 947](cheat_images/imageFile947.png)

 

xarccosh

x a − x2 + a2, if arccosh xa > 0 and a > 0,

![image 948](cheat_images/imageFile948.png)

![image 949](cheat_images/imageFile949.png)

![image 950](cheat_images/imageFile950.png)

xarccosh

x a

![image 951](cheat_images/imageFile951.png)

+ x2 + a2, if arccosh xa < 0 and a > 0,

![image 952](cheat_images/imageFile952.png)

![image 953](cheat_images/imageFile953.png)

- 39.

dx √a2 x2

![image 954](cheat_images/imageFile954.png)

![image 955](cheat_images/imageFile955.png)

= ln x + a2 + x2 , a > 0,

![image 956](cheat_images/imageFile956.png)

- 40.


dx a2 + x2

2

![image 957](cheat_images/imageFile957.png)

![image 958](cheat_images/imageFile958.png)

= 1a arctan xa, a > 0, 41. a2 − x2 dx = x2 a2 − x2 + a

2 arcsin xa, a > 0,

![image 959](cheat_images/imageFile959.png)

![image 960](cheat_images/imageFile960.png)

![image 961](cheat_images/imageFile961.png)

![image 962](cheat_images/imageFile962.png)

![image 963](cheat_images/imageFile963.png)

![image 964](cheat_images/imageFile964.png)

- 42. (a2 − x2)3/2dx = x8(5a2 − 2x2) a2 − x2 + 3a

![image 965](cheat_images/imageFile965.png)

![image 966](cheat_images/imageFile966.png)

4

![image 967](cheat_images/imageFile967.png)

8 arcsin xa, a > 0,

![image 968](cheat_images/imageFile968.png)

- 43.


dx (a2 − x2)3/2

dx √a2 − x2

- 1

![image 969](cheat_images/imageFile969.png)

- 2a


dx a2 − x2

a + x a − x

x a2√a2 − x2

= arcsin xa, a > 0, 44.

,

, 45.

=

ln

=

![image 970](cheat_images/imageFile970.png)

![image 971](cheat_images/imageFile971.png)

![image 972](cheat_images/imageFile972.png)

![image 973](cheat_images/imageFile973.png)

![image 974](cheat_images/imageFile974.png)

![image 975](cheat_images/imageFile975.png)

![image 976](cheat_images/imageFile976.png)

![image 977](cheat_images/imageFile977.png)

dx √x2 − a2

2

![image 978](cheat_images/imageFile978.png)

![image 979](cheat_images/imageFile979.png)

![image 980](cheat_images/imageFile980.png)

![image 981](cheat_images/imageFile981.png)

46. a2 ± x2 dx = x2 a2 ± x2 ± a

2 ln x + a2 ± x2 , 47.

= ln x + x2 − a2 , a > 0,

![image 982](cheat_images/imageFile982.png)

![image 983](cheat_images/imageFile983.png)

![image 984](cheat_images/imageFile984.png)

![image 985](cheat_images/imageFile985.png)

√

2(3bx − 2a)(a + bx)3/2 15b2

1 a

x a + bx

dx ax2 + bx

![image 986](cheat_images/imageFile986.png)

a bxdx

,

ln

, 49. x

48.

![image 987](cheat_images/imageFile987.png)

![image 988](cheat_images/imageFile988.png)

![image 989](cheat_images/imageFile989.png)

![image 990](cheat_images/imageFile990.png)

√a + bx x

√a + bx −

√a √a + bx + √a

√

![image 991](cheat_images/imageFile991.png)

![image 992](cheat_images/imageFile992.png)

![image 993](cheat_images/imageFile993.png)

x √a + bx

1 x√a + bx

1 √2

![image 994](cheat_images/imageFile994.png)

dx, 51.

dx =

a + bx + a

, a > 0,

ln

dx = 2

50.

![image 995](cheat_images/imageFile995.png)

![image 996](cheat_images/imageFile996.png)

![image 997](cheat_images/imageFile997.png)

![image 998](cheat_images/imageFile998.png)

![image 999](cheat_images/imageFile999.png)

![image 1000](cheat_images/imageFile1000.png)

![image 1001](cheat_images/imageFile1001.png)

![image 1002](cheat_images/imageFile1002.png)

![image 1003](cheat_images/imageFile1003.png)

![image 1004](cheat_images/imageFile1004.png)

√a2 − x2 x

a + √a2 − x2 x

![image 1005](cheat_images/imageFile1005.png)

![image 1006](cheat_images/imageFile1006.png)

![image 1007](cheat_images/imageFile1007.png)

![image 1008](cheat_images/imageFile1008.png)

, 53. x a2 − x2 dx = −13(a2 − x2)3/2,

dx = a2 − x2 − a ln

52.

![image 1009](cheat_images/imageFile1009.png)

![image 1010](cheat_images/imageFile1010.png)

![image 1011](cheat_images/imageFile1011.png)

a + √a2 − x2 x

![image 1012](cheat_images/imageFile1012.png)

dx √a2 − x2

4

![image 1013](cheat_images/imageFile1013.png)

![image 1014](cheat_images/imageFile1014.png)

54. x2 a2 − x2 dx = x8(2x2 − a2) a2 − x2 + a

= −1a ln

8 arcsin xa, a > 0, 55.

,

![image 1015](cheat_images/imageFile1015.png)

![image 1016](cheat_images/imageFile1016.png)

![image 1017](cheat_images/imageFile1017.png)

![image 1018](cheat_images/imageFile1018.png)

![image 1019](cheat_images/imageFile1019.png)

![image 1020](cheat_images/imageFile1020.png)

![image 1021](cheat_images/imageFile1021.png)

x2 dx √a2 − x2

xdx √a2 − x2

2

![image 1022](cheat_images/imageFile1022.png)

![image 1023](cheat_images/imageFile1023.png)

= −x2 a2 − x2 + a

2 arcsin xa, a > 0,

= − a2 − x2, 57.

56.

![image 1024](cheat_images/imageFile1024.png)

![image 1025](cheat_images/imageFile1025.png)

![image 1026](cheat_images/imageFile1026.png)

![image 1027](cheat_images/imageFile1027.png)

![image 1028](cheat_images/imageFile1028.png)

![image 1029](cheat_images/imageFile1029.png)

![image 1030](cheat_images/imageFile1030.png)

√x2 − a2 x

√a2 + x2 x

a + √a2 + x2 x

![image 1031](cheat_images/imageFile1031.png)

![image 1032](cheat_images/imageFile1032.png)

![image 1033](cheat_images/imageFile1033.png)

![image 1034](cheat_images/imageFile1034.png)

![image 1035](cheat_images/imageFile1035.png)

dx x2 a2 a arccos a|x|, a > 0,

dx a2 + x2 a ln

, 59.

58.

![image 1036](cheat_images/imageFile1036.png)

![image 1037](cheat_images/imageFile1037.png)

![image 1038](cheat_images/imageFile1038.png)

![image 1039](cheat_images/imageFile1039.png)

dx x√x2 + a2

x a + √a2 + x2

![image 1040](cheat_images/imageFile1040.png)

60. x x2 ± a2 dx = 13(x2 ± a2)3/2, 61.

= 1a ln

,

![image 1041](cheat_images/imageFile1041.png)

![image 1042](cheat_images/imageFile1042.png)

![image 1043](cheat_images/imageFile1043.png)

![image 1044](cheat_images/imageFile1044.png)

![image 1045](cheat_images/imageFile1045.png)

![image 1046](cheat_images/imageFile1046.png)

![image 1047](cheat_images/imageFile1047.png)

![image 1053](cheat_images/imageFile1053.png)

![image 1054](cheat_images/imageFile1054.png)

Calculus Cont. Finite Calculus 62.

√x2 ± a2 a2x

![image 1055](cheat_images/imageFile1055.png)

![image 1056](cheat_images/imageFile1056.png)

![image 1057](cheat_images/imageFile1057.png)

![image 1058](cheat_images/imageFile1058.png)

![image 1059](cheat_images/imageFile1059.png)

Diﬀerence, shift operators: ∆f(x) = f(x + 1) − f(x), Ef(x) = f(x + 1).

dx x√x2 − a2

dx x2√x2 ± a2

= 1a arccos ax , a > 0, 63.

= ∓

,

![image 1060](cheat_images/imageFile1060.png)

![image 1061](cheat_images/imageFile1061.png)

![image 1062](cheat_images/imageFile1062.png)

![image 1063](cheat_images/imageFile1063.png)

![image 1064](cheat_images/imageFile1064.png)

![image 1065](cheat_images/imageFile1065.png)

![image 1066](cheat_images/imageFile1066.png)

√x2 ± a2 x4

(x2 + a2)3/2 3a2x3

![image 1067](cheat_images/imageFile1067.png)

xdx √x2 ± a2

![image 1068](cheat_images/imageFile1068.png)

= x2 ± a2, 65.

dx = ∓

,

64.

![image 1069](cheat_images/imageFile1069.png)

![image 1070](cheat_images/imageFile1070.png)

![image 1071](cheat_images/imageFile1071.png)

![image 1072](cheat_images/imageFile1072.png)

Fundamental Theorem: f(x) = ∆F(x) ⇔ f(x)δx = F(x) + C.

b

b−1

- 66.

dx ax2 bx + c

![image 1073](cheat_images/imageFile1073.png)

=

 



- 1

![image 1074](cheat_images/imageFile1074.png)

√b2 − 4ac

![image 1075](cheat_images/imageFile1075.png)

ln

2ax + b −

√b2 − 4ac 2ax + b + √b2 − 4ac

![image 1076](cheat_images/imageFile1076.png)

![image 1077](cheat_images/imageFile1077.png)

![image 1078](cheat_images/imageFile1078.png)

, if b2 > 4ac,

- 2


![image 1079](cheat_images/imageFile1079.png)

√4ac − b2

![image 1080](cheat_images/imageFile1080.png)

arctan

2ax + b √4ac − b2

![image 1081](cheat_images/imageFile1081.png)

![image 1082](cheat_images/imageFile1082.png)

, if b2 < 4ac,

- 67.

dx √ax2 + bx + c

![image 1083](cheat_images/imageFile1083.png)

![image 1084](cheat_images/imageFile1084.png)

=

 



1 √a

![image 1085](cheat_images/imageFile1085.png)

![image 1086](cheat_images/imageFile1086.png)

ln 2ax + b + 2√a ax2 + bx + c , if a > 0, 1

![image 1087](cheat_images/imageFile1087.png)

![image 1088](cheat_images/imageFile1088.png)

![image 1089](cheat_images/imageFile1089.png)

√

![image 1090](cheat_images/imageFile1090.png)

−a

arcsin −2ax − b √b2 − 4ac

![image 1091](cheat_images/imageFile1091.png)

![image 1092](cheat_images/imageFile1092.png)

, if a < 0,

- 68. ax2 + bx + c dx =

![image 1093](cheat_images/imageFile1093.png)

2ax + b 4a

![image 1094](cheat_images/imageFile1094.png)

![image 1095](cheat_images/imageFile1095.png)

ax2 + bx + c +

4ax − b2 8a

![image 1096](cheat_images/imageFile1096.png)

dx √ax2 + bx + c

![image 1097](cheat_images/imageFile1097.png)

![image 1098](cheat_images/imageFile1098.png)

,

- 69.

xdx √ax2 + bx c

![image 1099](cheat_images/imageFile1099.png)

![image 1100](cheat_images/imageFile1100.png)

=

√ax2 + bx + c a

![image 1101](cheat_images/imageFile1101.png)

![image 1102](cheat_images/imageFile1102.png)

b 2a

![image 1103](cheat_images/imageFile1103.png)

dx √ax2 + bx + c

![image 1104](cheat_images/imageFile1104.png)

![image 1105](cheat_images/imageFile1105.png)

,

- 70.

dx x√ax2 + bx + c

![image 1106](cheat_images/imageFile1106.png)

![image 1107](cheat_images/imageFile1107.png)

=

 



−1 √c

![image 1108](cheat_images/imageFile1108.png)

![image 1109](cheat_images/imageFile1109.png)

ln

2√c√ax2 + bx + c + bx + 2c x

![image 1110](cheat_images/imageFile1110.png)

![image 1111](cheat_images/imageFile1111.png)

![image 1112](cheat_images/imageFile1112.png)

, if c > 0, 1 √ c

![image 1113](cheat_images/imageFile1113.png)

![image 1114](cheat_images/imageFile1114.png)

arcsin

bx + 2c |x|

![image 1115](cheat_images/imageFile1115.png)

√b2 − 4ac

![image 1116](cheat_images/imageFile1116.png)

, if c < 0,

- 71. x3 x2 + a2 dx = (13x2 − 215a2)(x2 + a2)3/2,

![image 1117](cheat_images/imageFile1117.png)

![image 1118](cheat_images/imageFile1118.png)

![image 1119](cheat_images/imageFile1119.png)

- 72. xn sin(ax)dx = −1axn cos(ax) + na xn−1 cos(ax)dx,

![image 1120](cheat_images/imageFile1120.png)

![image 1121](cheat_images/imageFile1121.png)

- 73. xn cos(ax)dx = 1axn sin(ax) − na xn−1 sin(ax)dx,

![image 1122](cheat_images/imageFile1122.png)

![image 1123](cheat_images/imageFile1123.png)

- 74. xneax dx =

xneax a − na xn 1eax dx,

![image 1124](cheat_images/imageFile1124.png)

![image 1125](cheat_images/imageFile1125.png)

- 75. xn ln(ax)dx = xn+1

ln(ax) n + 1 −

![image 1126](cheat_images/imageFile1126.png)

1 (n + 1)2

![image 1127](cheat_images/imageFile1127.png)

,

- 76. xn(lnax)m dx =


f(i).

f(x)δx =

a

i=a

Diﬀerences: ∆(cu) = c∆u, ∆(u + v) = ∆u + ∆v,

∆(uv) = u∆v + E v∆u, ∆(xn) = nxn−1,

![image 1128](cheat_images/imageFile1128.png)

![image 1129](cheat_images/imageFile1129.png)

∆(Hx) = x−1, ∆(2x) = 2x, ∆(cx) = (c − 1)cx, ∆ xm = xm 1 . Sums:

![image 1130](cheat_images/imageFile1130.png)

cu δx = c u δx, (u + v)δx = u δx + v δx,

u∆v δx = uv − Ev∆u δx, xn δx x

n+1

m+1 , x−1 δx Hx, cx δx = c

![image 1131](cheat_images/imageFile1131.png)

![image 1132](cheat_images/imageFile1132.png)

![image 1133](cheat_images/imageFile1133.png)

![image 1134](cheat_images/imageFile1134.png)

x

c−1 , xm δx = xm+1 .

![image 1135](cheat_images/imageFile1135.png)

Falling Factorial Powers: xn = x(x − 1)···(x − n + 1), n > 0, x0 = 1, xn =

![image 1136](cheat_images/imageFile1136.png)

![image 1137](cheat_images/imageFile1137.png)

1 (x + 1)···(x + n|)

, n < 0,

![image 1138](cheat_images/imageFile1138.png)

![image 1139](cheat_images/imageFile1139.png)

xn+m = xm(x − m)n. Rising Factorial Powers:

![image 1140](cheat_images/imageFile1140.png)

![image 1141](cheat_images/imageFile1141.png)

![image 1142](cheat_images/imageFile1142.png)

xn = x(x + 1)···(x + n − 1), n > 0, x0 = 1, xn =

![image 1143](cheat_images/imageFile1143.png)

![image 1144](cheat_images/imageFile1144.png)

1 (x − 1)···(x − |n|)

![image 1145](cheat_images/imageFile1145.png)

, n < 0,

![image 1146](cheat_images/imageFile1146.png)

xn+1 n + 1

- m

![image 1147](cheat_images/imageFile1147.png)

- n + 1


(lnax)m −

xn(ln ax)m−1 dx.

![image 1148](cheat_images/imageFile1148.png)

![image 1149](cheat_images/imageFile1149.png)

xn+m = xm(x + m)n. Conversion: xn = ( 1)n( x)n = (x n + 1)n

![image 1150](cheat_images/imageFile1150.png)

![image 1151](cheat_images/imageFile1151.png)

![image 1152](cheat_images/imageFile1152.png)

![image 1153](cheat_images/imageFile1153.png)

![image 1154](cheat_images/imageFile1154.png)

![image 1155](cheat_images/imageFile1155.png)

![image 1156](cheat_images/imageFile1156.png)

![image 1157](cheat_images/imageFile1157.png)

![image 1158](cheat_images/imageFile1158.png)

![image 1159](cheat_images/imageFile1159.png)

![image 1160](cheat_images/imageFile1160.png)

![image 1161](cheat_images/imageFile1161.png)

x1 = x1 = x1 x2 = x2 + x1 = x2 − x1 x3 = x3 + 3x2 + x1 = x3 − 3x2 + x1 x4 x4 + 6x3 + 7x2 x1 x4 − 6x3 + 7x2 − x1 x5 x5 + 15x4 + 25x3 + 10x2 + x1 x5 15x4 + 25x3 10x2 + x1

![image 1162](cheat_images/imageFile1162.png)

![image 1163](cheat_images/imageFile1163.png)

![image 1164](cheat_images/imageFile1164.png)

= 1/(x + 1) n, xn = (−1)n(−x)n = (x + n 1)n

![image 1165](cheat_images/imageFile1165.png)

![image 1166](cheat_images/imageFile1166.png)

![image 1167](cheat_images/imageFile1167.png)

![image 1168](cheat_images/imageFile1168.png)

![image 1169](cheat_images/imageFile1169.png)

![image 1170](cheat_images/imageFile1170.png)

![image 1171](cheat_images/imageFile1171.png)

![image 1172](cheat_images/imageFile1172.png)

![image 1173](cheat_images/imageFile1173.png)

![image 1174](cheat_images/imageFile1174.png)

![image 1175](cheat_images/imageFile1175.png)

![image 1176](cheat_images/imageFile1176.png)

![image 1177](cheat_images/imageFile1177.png)

![image 1178](cheat_images/imageFile1178.png)

![image 1179](cheat_images/imageFile1179.png)

![image 1180](cheat_images/imageFile1180.png)

![image 1181](cheat_images/imageFile1181.png)

= 1/(x − 1)−n, xn =

![image 1182](cheat_images/imageFile1182.png)

![image 1183](cheat_images/imageFile1183.png)

![image 1184](cheat_images/imageFile1184.png)

![image 1185](cheat_images/imageFile1185.png)

![image 1186](cheat_images/imageFile1186.png)

![image 1187](cheat_images/imageFile1187.png)

![image 1188](cheat_images/imageFile1188.png)

![image 1189](cheat_images/imageFile1189.png)

![image 1190](cheat_images/imageFile1190.png)

n

n

n k

n k

![image 1191](cheat_images/imageFile1191.png)

![image 1192](cheat_images/imageFile1192.png)

![image 1193](cheat_images/imageFile1193.png)

![image 1194](cheat_images/imageFile1194.png)

![image 1195](cheat_images/imageFile1195.png)

![image 1196](cheat_images/imageFile1196.png)

![image 1197](cheat_images/imageFile1197.png)

(−1)n kxk,

xk =

![image 1198](cheat_images/imageFile1198.png)

![image 1199](cheat_images/imageFile1199.png)

x1 = x1 x1 = x1 x2 = x2 + x1 x2 = x2 − x1 x3 = x3 + 3x2 + 2x1 x3 = x3 − 3x2 + 2x1 x4 = x4 + 6x3 + 11x2 + 6x1 x4 = x4 − 6x3 + 11x2 − 6x1 x5 = x5 + 10x4 + 35x3 + 50x2 + 24x1 x5 = x5 − 10x4 + 35x3 − 50x2 + 24x1

k=1

k=1

![image 1200](cheat_images/imageFile1200.png)

n

![image 1201](cheat_images/imageFile1201.png)

n k

(−1)n−kxk,

xn =

![image 1202](cheat_images/imageFile1202.png)

![image 1203](cheat_images/imageFile1203.png)

![image 1204](cheat_images/imageFile1204.png)

k=1

![image 1205](cheat_images/imageFile1205.png)

![image 1206](cheat_images/imageFile1206.png)

n

n k

![image 1207](cheat_images/imageFile1207.png)

xn =

xk.

![image 1208](cheat_images/imageFile1208.png)

![image 1209](cheat_images/imageFile1209.png)

![image 1210](cheat_images/imageFile1210.png)

k=1

![image 1211](cheat_images/imageFile1211.png)

![image 1212](cheat_images/imageFile1212.png)

![image 1213](cheat_images/imageFile1213.png)

![image 1214](cheat_images/imageFile1214.png)

Theoretical Computer Science Cheat Sheet Series Taylor’s series:

![image 1215](cheat_images/imageFile1215.png)

![image 1216](cheat_images/imageFile1216.png)

![image 1217](cheat_images/imageFile1217.png)

![image 1218](cheat_images/imageFile1218.png)

![image 1219](cheat_images/imageFile1219.png)

![image 1220](cheat_images/imageFile1220.png)

![image 1221](cheat_images/imageFile1221.png)

Ordinary power series: A(x) =

∞

(x − a)i i!

(x − a)2 2

∞

f(i)(a). Expansions:

f′′(a) + ··· =

f(x) = f(a) + (x − a)f′(a) +

aixi.

![image 1222](cheat_images/imageFile1222.png)

![image 1223](cheat_images/imageFile1223.png)

i=0

i=0

Exponential power series: A(x) =

∞

1 1 − x

xi, 1 1 − cx

= 1 + x + x2 + x3 + x4 + ···

∞

xi i!

![image 1224](cheat_images/imageFile1224.png)

ai

. Dirichlet power series:

i=0

![image 1225](cheat_images/imageFile1225.png)

∞

i=0

cixi, 1 1 − xn

= 1 + cx + c2x2 + c3x3 + ··· =

![image 1226](cheat_images/imageFile1226.png)

i=0

∞

∞

ai ix

A(x) =

. Binomial theorem:

xni, x (1 − x)2

= 1 + xn + x2n + x3n + ··· =

![image 1227](cheat_images/imageFile1227.png)

![image 1228](cheat_images/imageFile1228.png)

i=1

i=0

∞

ixi,

= x + 2x2 + 3x3 + 4x4 + ··· =

n

n k

![image 1229](cheat_images/imageFile1229.png)

(x + y)n =

xn−kyk. Diﬀerence of like powers:

i=0

n

∞

k!zk (1 z)k+1

n k

k=0

inxi,

= x + 2nx2 + 3nx3 + 4nx4 + ··· =

![image 1230](cheat_images/imageFile1230.png)

i=0

k=0

n−1

∞

xi i!

xn 1 kyk. For ordinary power series: αA(x) + βB(x) =

xn − yn = (x − y)

ex = 1 + x + 12x2 + 16x3 + ··· =

,

![image 1231](cheat_images/imageFile1231.png)

![image 1232](cheat_images/imageFile1232.png)

![image 1233](cheat_images/imageFile1233.png)

k=0

i=0

∞

xi i

(−1)i+1

ln(1 + x) = x − 12x2 + 13x3 − 14x4 − ··· =

,

∞

![image 1234](cheat_images/imageFile1234.png)

![image 1235](cheat_images/imageFile1235.png)

![image 1236](cheat_images/imageFile1236.png)

![image 1237](cheat_images/imageFile1237.png)

(αai + βbi)xi,

i=1

∞

xi i

1 1 x

i=0

= x + 12x2 + 13x3 + 14x4 + ··· =

ln

,

![image 1238](cheat_images/imageFile1238.png)

![image 1239](cheat_images/imageFile1239.png)

![image 1240](cheat_images/imageFile1240.png)

![image 1241](cheat_images/imageFile1241.png)

![image 1242](cheat_images/imageFile1242.png)

∞

xkA(x) =

ai kxi,

i=1

∞

x2i+1 (2i + 1)!

(−1)i

sinx = x − 13!x3 + 15!x5 − 17!x7 + ··· =

i=k

,

![image 1243](cheat_images/imageFile1243.png)

![image 1244](cheat_images/imageFile1244.png)

![image 1245](cheat_images/imageFile1245.png)

![image 1246](cheat_images/imageFile1246.png)

∞

A(x) − k−1i=0 aixi xk

i=0

ai+kxi,

∞

=

x2i (2i)!

![image 1247](cheat_images/imageFile1247.png)

( 1)i

cosx = 1 12!x2 + 14!x4 16!x6 + ···

,

i=0

![image 1248](cheat_images/imageFile1248.png)

![image 1249](cheat_images/imageFile1249.png)

![image 1250](cheat_images/imageFile1250.png)

![image 1251](cheat_images/imageFile1251.png)

∞

i=0

ciaixi,

∞

A(cx) =

x2i+1 (2i + 1)

(−1)i

tan−1 x = x − 13x3 + 15x5 − 17x7 + ··· =

,

i=0

![image 1252](cheat_images/imageFile1252.png)

![image 1253](cheat_images/imageFile1253.png)

![image 1254](cheat_images/imageFile1254.png)

![image 1255](cheat_images/imageFile1255.png)

∞

i=0

∞

(i + 1)ai+1xi,

A′(x) =

n i

(1 + x)n = 1 + nx + n(n−1)2x2 + ··· =

xi, 1 (1 − x)n+1

![image 1256](cheat_images/imageFile1256.png)

i=0

i=0

∞

∞

i + n i

iaixi,

xA′(x) =

= 1 + (n + 1)x + n+22 x2 + ··· =

xi, x ex − 1

![image 1257](cheat_images/imageFile1257.png)

i=1

i=0

∞

∞

Bixi i!

ai−1 i

xi,

= 1 − 12x + 112x2 − 1720x4 + ··· =

A(x)dx =

,

![image 1258](cheat_images/imageFile1258.png)

![image 1259](cheat_images/imageFile1259.png)

![image 1260](cheat_images/imageFile1260.png)

![image 1261](cheat_images/imageFile1261.png)

![image 1262](cheat_images/imageFile1262.png)

![image 1263](cheat_images/imageFile1263.png)

i=1

i=0

∞

√1 − 4x) = 1 + x + 2x2 + 5x3 + ··· =

∞

1 i + 1

- 1

![image 1264](cheat_images/imageFile1264.png)

- 2x


2i i

A(x) + A(−x) 2

xi, 1 √1 − 4x

![image 1265](cheat_images/imageFile1265.png)

(1 −

a2ix2i,

![image 1266](cheat_images/imageFile1266.png)

![image 1267](cheat_images/imageFile1267.png)

i=0

i=0

∞

2i i

∞

A(x) − A(−x) 2

xi, 1 √1 − 4x

= 1 + 2x + 6x2 + 20x3 + ··· =

a2i+1x2i+1.

![image 1268](cheat_images/imageFile1268.png)

=

![image 1269](cheat_images/imageFile1269.png)

![image 1270](cheat_images/imageFile1270.png)

i=0

√1 − 4x 2x

i=0

n

∞

![image 1271](cheat_images/imageFile1271.png)

1 −

2i + n i

= 1 + (2 + n)x + 4+n2 x2 + ··· =

xi, 1 1 − x

Summation: If bi ij=0 ai then B(x) =

![image 1272](cheat_images/imageFile1272.png)

![image 1273](cheat_images/imageFile1273.png)

![image 1274](cheat_images/imageFile1274.png)

i=0

1 1 − x

∞

A(x). Convolution:

1 1 − x

![image 1275](cheat_images/imageFile1275.png)

Hixi,

= x + 32x2 + 116x3 + 2512x4 ··· =

ln

![image 1276](cheat_images/imageFile1276.png)

![image 1277](cheat_images/imageFile1277.png)

![image 1278](cheat_images/imageFile1278.png)

![image 1279](cheat_images/imageFile1279.png)

![image 1280](cheat_images/imageFile1280.png)

i=1

∞

2

Hi−1xi i

ajbi−j

 

1 1 − x

- 1

![image 1281](cheat_images/imageFile1281.png)

- 2


∞

- i
- j=0


= 12x2 + 34x3 + 1124x4 + ··· =

ln

, x 1 − x − x2

xi.

![image 1282](cheat_images/imageFile1282.png)

![image 1283](cheat_images/imageFile1283.png)

![image 1284](cheat_images/imageFile1284.png)

![image 1285](cheat_images/imageFile1285.png)

![image 1286](cheat_images/imageFile1286.png)

A(x)B(x) =

i=2

i=0

∞

Fixi, Fnx 1 − (Fn−1 + Fn+1)x − (−1)nx2

= x + x2 + 2x3 + 3x4 ··· =

![image 1287](cheat_images/imageFile1287.png)

![image 1288](cheat_images/imageFile1288.png)

![image 1289](cheat_images/imageFile1289.png)

![image 1290](cheat_images/imageFile1290.png)

![image 1291](cheat_images/imageFile1291.png)

![image 1292](cheat_images/imageFile1292.png)

![image 1293](cheat_images/imageFile1293.png)

![image 1294](cheat_images/imageFile1294.png)

God made the natural numbers; all the rest is the work of man.

i=0

∞

Fnixi.

= Fnx + F2nx2 + F3nx3 + ··· =

![image 1295](cheat_images/imageFile1295.png)

– Leopold Kronecker

i=0

![image 1296](cheat_images/imageFile1296.png)

![image 1302](cheat_images/imageFile1302.png)

![image 1303](cheat_images/imageFile1303.png)

Series Escher’s Knot Expansions: 1 (1 − x)n+1

![image 1304](cheat_images/imageFile1304.png)

![image 1305](cheat_images/imageFile1305.png)

![image 1306](cheat_images/imageFile1306.png)

![image 1307](cheat_images/imageFile1307.png)

![image 1308](cheat_images/imageFile1308.png)

![image 1309](cheat_images/imageFile1309.png)

∞

∞

−n

i n

n + i i

1 x

1 1 − x

xi,

xi,

(Hn+i − Hn)

=

ln

=

![image 1310](cheat_images/imageFile1310.png)

![image 1311](cheat_images/imageFile1311.png)

![image 1312](cheat_images/imageFile1312.png)

i=0

i=0

∞

∞

n!xi i!

n i

i n

xn =

xi, (ex − 1)n =

![image 1313](cheat_images/imageFile1313.png)

,

![image 1314](cheat_images/imageFile1314.png)

i=0

i=0

∞

∞

n

(−4)iB2ix2i (2i)!

n!xi i!

1 1 − x

i n

ln

=

, xcotx =

,

![image 1315](cheat_images/imageFile1315.png)

![image 1316](cheat_images/imageFile1316.png)

![image 1317](cheat_images/imageFile1317.png)

i=0

i=0

∞

∞

22i(22i − 1)B2ix2i−1 (2i)!

1 ix

( 1)i−1

tanx =

, 1 ζ(x)

, ζ(x) =

![image 1318](cheat_images/imageFile1318.png)

![image 1319](cheat_images/imageFile1319.png)

i=1

i=1

∞

∞

ζ(x − 1) ζ(x)

µ(i) ix

φ(i) ix

,

,

=

=

![image 1320](cheat_images/imageFile1320.png)

![image 1321](cheat_images/imageFile1321.png)

![image 1322](cheat_images/imageFile1322.png)

![image 1323](cheat_images/imageFile1323.png)

i=1

i=1

1 1 − p x

![image 1324](cheat_images/imageFile1324.png)

![image 1325](cheat_images/imageFile1325.png)

![image 1326](cheat_images/imageFile1326.png)

![image 1327](cheat_images/imageFile1327.png)

![image 1328](cheat_images/imageFile1328.png)

![image 1329](cheat_images/imageFile1329.png)

![image 1330](cheat_images/imageFile1330.png)

![image 1331](cheat_images/imageFile1331.png)

![image 1332](cheat_images/imageFile1332.png)

Stieltjes Integrationζ(x) =

,

![image 1333](cheat_images/imageFile1333.png)

p

![image 1334](cheat_images/imageFile1334.png)

![image 1335](cheat_images/imageFile1335.png)

![image 1336](cheat_images/imageFile1336.png)

![image 1337](cheat_images/imageFile1337.png)

![image 1338](cheat_images/imageFile1338.png)

![image 1339](cheat_images/imageFile1339.png)

![image 1340](cheat_images/imageFile1340.png)

![image 1341](cheat_images/imageFile1341.png)

![image 1342](cheat_images/imageFile1342.png)

If G is continuous in the interval [a,b] and F is nondecreasing then

∞

d(i) xi

b

ζ2(x) =

where d(n) = d|n 1,

![image 1343](cheat_images/imageFile1343.png)

G(x)dF(x) exists. If a ≤ b ≤ c then

i=1

a

∞

S(i) xi

ζ(x)ζ(x − 1) =

where S(n) = d|n d,

![image 1344](cheat_images/imageFile1344.png)

c

b

c

i=1

G(x)dF(x). If the integrals involved exist

G(x)dF(x) +

G(x)dF(x) =

22n−1|B2n| (2n)!

b

a

a

π2n, n ∈ N, x sinx

ζ(2n) =

![image 1345](cheat_images/imageFile1345.png)

b

∞

(4i − 2)B2ix2i (2i)!

(−1)i−1

=

,

![image 1346](cheat_images/imageFile1346.png)

![image 1347](cheat_images/imageFile1347.png)

- a

G(x) + H(x) dF(x) =

b

a

G(x)dF(x) +

b

a

H(x)dF(x),

- b


i=0

√1 − 4x 2x

n

∞

![image 1348](cheat_images/imageFile1348.png)

n(2i + n − 1)! i!(n + i)!

1 −

xi,

=

- a

G(x)d F(x) + H(x) =

b

a

G(x)dF(x) +

b

a

G(x)dH(x),

- b

a

- c · G(x)dF(x) =


![image 1349](cheat_images/imageFile1349.png)

![image 1350](cheat_images/imageFile1350.png)

b

b

i=0

G(x)d c · F(x) = c

G(x)dF(x),

∞

2i/2 sin iπ4 i!

![image 1351](cheat_images/imageFile1351.png)

a

a

xi,

ex sinx =

![image 1352](cheat_images/imageFile1352.png)

b

b

i=1

G(x)dF(x) = G(b)F(b) − G(a)F(a) −

F(x)dG(x).

√1 − x x

![image 1353](cheat_images/imageFile1353.png)

a

a

∞

![image 1354](cheat_images/imageFile1354.png)

1 −

(4i)! 16i√2(2i)!(2i + 1)!

If the integrals involved exist, and F possesses a derivative F′ at every point in [a,b] then

xi,

=

![image 1355](cheat_images/imageFile1355.png)

![image 1356](cheat_images/imageFile1356.png)

![image 1357](cheat_images/imageFile1357.png)

i=0

∞

2

b

b

4ii!2 (i + 1)(2i + 1)!

arcsinx x

G(x)F′(x)dx.

x2i.

G(x)dF(x) =

=

![image 1358](cheat_images/imageFile1358.png)

![image 1359](cheat_images/imageFile1359.png)

a

a

i=0

![image 1360](cheat_images/imageFile1360.png)

![image 1361](cheat_images/imageFile1361.png)

![image 1362](cheat_images/imageFile1362.png)

![image 1363](cheat_images/imageFile1363.png)

![image 1364](cheat_images/imageFile1364.png)

Fibonacci Numbers If we have equations:

Cramer’s Rule

![image 1365](cheat_images/imageFile1365.png)

![image 1366](cheat_images/imageFile1366.png)

![image 1367](cheat_images/imageFile1367.png)

00 47 18 76 29 93 85 34 61 52 86 11 57 28 70 39 94 45 02 63 95 80 22 67 38 71 49 56 13 04 59 96 81 33 07 48 72 60 24 15 73 69 90 82 44 17 58 01 35 26 68 74 09 91 83 55 27 12 46 30 37 08 75 19 92 84 66 23 50 41 14 25 36 40 51 62 03 77 88 99 21 32 43 54 65 06 10 89 97 78 42 53 64 05 16 20 31 98 79 87

![image 1368](cheat_images/imageFile1368.png)

![image 1369](cheat_images/imageFile1369.png)

![image 1370](cheat_images/imageFile1370.png)

![image 1371](cheat_images/imageFile1371.png)

![image 1372](cheat_images/imageFile1372.png)

![image 1373](cheat_images/imageFile1373.png)

![image 1374](cheat_images/imageFile1374.png)

![image 1375](cheat_images/imageFile1375.png)

![image 1376](cheat_images/imageFile1376.png)

![image 1377](cheat_images/imageFile1377.png)

1,1,2,3,5,8,13,21,34,55,89,... Deﬁnitions: Fi = Fi−1+Fi−2, F0 = F1 = 1,

- a1,1x1 + a1,2x2 + ··· + a1,nxn = b1
- a2,1x1 + a2,2x2 + ··· + a2,nxn = b2


. . . an,1x1 an,2x2 + ··· + an,nxn bn

F−i = (−1)i−1Fi, Fi = 1√5 φi ˆφi ,

![image 1378](cheat_images/imageFile1378.png)

![image 1379](cheat_images/imageFile1379.png)

Let A = (ai,j) and B be the column matrix (bi). Then there is a unique solution iﬀ detA = 0. Let Ai be A with column i replaced by B. Then

Cassini’s identity: for i > 0:

Fi+1Fi 1 − F2i = (−1)i. Additive rule:

![image 1380](cheat_images/imageFile1380.png)

detAi detA

![image 1381](cheat_images/imageFile1381.png)

![image 1382](cheat_images/imageFile1382.png)

![image 1383](cheat_images/imageFile1383.png)

![image 1384](cheat_images/imageFile1384.png)

![image 1385](cheat_images/imageFile1385.png)

![image 1386](cheat_images/imageFile1386.png)

![image 1387](cheat_images/imageFile1387.png)

![image 1388](cheat_images/imageFile1388.png)

The Fibonacci number system: Every integer n has a unique representation

xi =

.

![image 1389](cheat_images/imageFile1389.png)

Fn+k = FkFn+1 + Fk−1Fn, F2n = FnFn+1 + Fn−1Fn. Calculation by matrices:

![image 1390](cheat_images/imageFile1390.png)

![image 1391](cheat_images/imageFile1391.png)

![image 1392](cheat_images/imageFile1392.png)

![image 1393](cheat_images/imageFile1393.png)

![image 1394](cheat_images/imageFile1394.png)

![image 1395](cheat_images/imageFile1395.png)

![image 1396](cheat_images/imageFile1396.png)

![image 1397](cheat_images/imageFile1397.png)

Improvement makes strait roads, but the crooked roads without Improvement, are roads of Genius.

+ ··· + Fk

,

+ Fk

n = Fk

m

2

1

n

where ki ≥ ki+1 + 2 for all i, 1 ≤ i < m and km ≥ 2.

Fn−2 Fn−1 Fn−1 Fn

- 0 1
- 1 1


.

– William Blake (The Marriage of Heaven and Hell)

![image 1398](cheat_images/imageFile1398.png)

