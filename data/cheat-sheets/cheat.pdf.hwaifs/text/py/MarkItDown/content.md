Theoretical Computer Science Cheat Sheet

Deﬁnitions

Series

f (n) = O(g(n))

f (n) = Ω(g(n))

f (n) = Θ(g(n))

f (n) = o(g(n))

an = a

lim
n
→∞

sup S

inf S

an

an

lim inf
n
→∞
lim sup
n

→∞
n
k

(cid:0)
(cid:1)
n
k

(cid:2)

(cid:3)

n
k

(cid:8)

(cid:9)

n
k

(cid:10)

(cid:11)

n
k
Cn
(cid:10)(cid:10)
(cid:11)(cid:11)

14.

18.

22.

25.

(cid:20)

(cid:20)

(cid:21)

n
1
n
k
(cid:21)
n
0
0
k

(cid:28)

(cid:29)

= (n

= (n

=

=

(cid:28)

n

n

(cid:28)
(cid:29)
28. xn =

n
m

(cid:28)

n
k

(cid:28)(cid:28)

(cid:29)

(cid:29)(cid:29)
x

31.

34.

36.

x

(cid:26)

−

n

(cid:27)

iﬀ
0

∃
≤

positive c, n0 such that
f (n)

cg(n)

n0.

n

≤

∀

≥

iﬀ
∃
f (n)

positive c, n0 such that
0

cg(n)

n0.

n

≥

≥
iﬀ f (n) = O(g(n)) and
f (n) = Ω(g(n)).

≥

∀

iﬀ limn

f (n)/g(n) = 0.

→∞
ǫ > 0,
< ǫ,

a

iﬀ
∀
an −
|
least b
S.

|

∈

n0 such that
∃
n0.
n
≥
∀
R such that b

s,

≥

∈

≤

∈
inf

R such that b

s
∀
∈
greatest b
S.
s
s,
∀
ai |
lim
n
→∞
ai |
lim
n
→∞
Combinations: Size k sub-
sets of a size n set.

sup
{

}
N

n, i

n, i

≥

≥

N

∈

∈

{

}

i

i

.

.

Stirling numbers (1st kind):
Arrangements of an n ele-
ment set into k cycles.

Stirling numbers (2nd kind):
Partitions of an n element
set into k non-empty sets.

1st order Eulerian numbers:
Permutations π1π2 . . . πn on
with k ascents.
1, 2, . . . , n

{
2nd order Eulerian numbers.

}

n

i =

n(n + 1)
2

,

i=1
X

In general:

im =

1
m + 1

n

i=1
X
1
n
−

im =

1
m + 1

i=1
X
Geometric series:
1

n

ci =

−
1

cn+1
c

−
ncn+2

i=0
X
n

ici =

i=0
X
Harmonic series:

i2 =

n(n + 1)(2n + 1)
6

,

n

i=1
X

i3 =

n2(n + 1)2
4

.

n

i=1
X

n

(i + 1)m+1

im+1

−

−

(m + 1)im

(cid:21)
(cid:1)

(n + 1)m+1

(cid:20)

m

m + 1
k

(cid:19)

Xk=0 (cid:18)

1

−

−

i=1
X
Bknm+1
−

(cid:0)
k.

,

c

= 1,

∞

ci =

i=0
X
(n + 1)cn+1 + c
(c

1)2

−

−

1

−

1

,

c

,

c

= 1,

∞

ci =

i=1
X
∞

ici =

i=0
X

c

−
c

−

1

(1

,

c

< 1,

c

|

|

c)2 ,

< 1.

c

|

|

Hn =

1
i

,

n

i=1
X

n

i=1
X
n

Hi = (n + 1)Hn −

n,

iHi =

n(n + 1)
2

Hn −

n(n

1)

.

−
4

i
m

Hi =

(cid:19)

n + 1
m + 1

(cid:18)

Hn+1 −

(cid:19) (cid:18)

1
m + 1

.

(cid:19)

n!

(n

k)!k!

,

2.

n
k

= 2n,

i=1 (cid:18)
X
n

Xk=0 (cid:18)

n
k

−
n
k

(cid:18)

−
−

,
(cid:19)

1
1

n
k

(cid:18)
(cid:19)(cid:18)
n + 1
m + 1

k

−

(cid:18)

−

1,

m
k

(cid:19)

(cid:19)(cid:18)
k
m

=

(cid:19)

=

(cid:18)
1)k

= (

−

= 2n

−

1

n
m

,
(cid:19)
n
k

k
k

,
(cid:19)

−
−

−

1

,
(cid:19)

n

i=1
X

(cid:18)

n
k

n
k

(cid:19)

=

=

(cid:18)

(cid:19)
n
m
(cid:18)
n

1.

4.

6.

8.

10.

Xk=0 (cid:18)
n
k

(cid:18)

(cid:19)
n
2

(cid:27)

(cid:26)
1,

−

=

n
1

n

(cid:20)

k

n

−
,
(cid:29)

(cid:19)

5.

7.

9.

n
k
(cid:18)
n

(cid:19)

3.

n

=

(cid:18)
r + k
k

n
k

(cid:19)
1

(cid:18)

−
k

=

+

(cid:18)

n

n
k

(cid:19)

(cid:18)

n

−

−
−

k

,
(cid:19)
1
1

,
(cid:19)

r + n + 1
n

=

(cid:18)

n

Xk=0 (cid:18)
r
k
Xk=0 (cid:18)

n

(cid:19)(cid:18)

r + s
n

(cid:19)
s

−
n
1

=

k

(cid:19)

=

(cid:18)
n
n

,
(cid:19)

,
(cid:19)

= 1,

1
1

,
(cid:27)

11.

13.

n

n
k

(cid:26)

= k

(cid:27)

(cid:26)

(cid:26)

−
k

(cid:27)
1

17.

(cid:20)
21. Cn =

= n!,

(cid:26)

(cid:27)

(cid:27)

(cid:26)

(cid:26)

+

≥

(cid:27)
n
k

n
−
k
−
n
k
(cid:21)
2n
1
n
n + 1
1
n
−
k
1
−
n + 1
2
k

k)

(cid:28)

(cid:18)

(cid:18)

(cid:19)

(cid:29)

(cid:19)

n

(cid:29)(cid:18)

m

(cid:19)

−

,

,

,

,

,

= 0 for n

= 0,

n
k

=

(2n)n
2n ,

(cid:29)(cid:29)
(m + 1)n

k,

−

(cid:27)

1

+ (n

−

(cid:29)
(n + 1)2n +

n

=

n
k

Xk=0 (cid:28)
n
n
(cid:29)(cid:29)
n

n

−
k

(cid:28)
= 3n

−

(cid:27)

n
m

(cid:26)

33.

(cid:28)(cid:28)

35.

Catalan Numbers: Binary
trees with n + 1 vertices.

12.

= (n

1)!Hn

−
n

1

(cid:27)

−

n

(cid:26)
=

n
2

(cid:21)
19.

n
k

(cid:28)

(cid:29)
26.

n

(cid:29)

(cid:28)
n
1
m

(cid:28)

Xk=0 (cid:18)

−
−
= 2n

n + 1
k

16.

=

n
2

(cid:18)

,
(cid:19)

1

(cid:21)

24.

(cid:20)
20.

n
k

(cid:28)

n

−

−

1,

(m + 1

(cid:19)

k)n(

−

−

1)k,

32.

n
0

(cid:28)(cid:28)

(cid:29)(cid:29)

= 1,

= 1,

n
n

(cid:21)
n

n
k

(cid:21)

Xk=0 (cid:20)
= (k + 1)

(cid:29)

27.

n
2

(cid:28)
(cid:29)
30. m!

15.

+

n
k

1
1

−
−

(cid:20)

(cid:20)

,

(cid:21)
23.

1

−
k

(cid:21)
= 1,

−

−

n

n

1)!,

1)

(cid:20)

n

1

−

1
0
n
k

(cid:29)
if k = 0,
otherwise
x + k
n

,
(cid:19)

Xk=0 (cid:28)
=

n

(cid:29)(cid:18)
n
k

Xk=0 (cid:26)
= (k + 1)

(cid:27)(cid:18)
n

29.

=

n
m

(cid:28)
(cid:29)
mk!,

−

n

k

−
m

(
−
(cid:19)

1)n

−

k

1

+ (2n

−
k

1

−

−

k)

(cid:28)(cid:28)

n
k

1
1

,
(cid:29)(cid:29)

−
−

(cid:29)(cid:29)
x + n

n

=

(cid:28)(cid:28)

n
k

Xk=0 (cid:28)(cid:28)

(cid:29)(cid:29)(cid:18)

k

1

−

−
2n

,

(cid:19)

37.

n + 1
m + 1

=

(cid:27)

(cid:26)

n
k

Xk (cid:18)

k
m

(cid:27)

=

(cid:19)(cid:26)

n

Xk=0 (cid:28)(cid:28)
k
m

Xk=0 (cid:26)

6
6
6
Theoretical Computer Science Cheat Sheet

Identities Cont.
n

nn

−

k = n!

Xk=0

1
k!

k
m

(cid:20)

38.

40.

42.

44.

46.

48.

=

(cid:21)

n + 1
m + 1

(cid:20)

(cid:26)

n
m

(cid:27)

=

m + n + 1
m

(cid:26)

(cid:18)

n
m

=

(cid:19)
n

n
k

k
m

n

=

k
m

Xk (cid:20)
n
k

(cid:21)(cid:18)
(cid:19)
k + 1
m + 1

Xk=0 (cid:20)
1)n

(
−

(cid:21)
k,

−

(cid:27)
n + k
k

(
−

(cid:21)

,

(cid:27)
1)m

Xk (cid:18)

(cid:19)(cid:26)
m

=

k

(cid:27)

Xk=0
n + 1
k + 1

(cid:26)
k
m

(cid:27)(cid:20)
m
n
−
m + k

Xk (cid:26)
=

(cid:27)

m

n

−
n
ℓ + m

(cid:26)

(cid:26)

Xk (cid:18)
ℓ + m
ℓ

(cid:19)

=

(cid:27)(cid:18)

k,

−

45. (n

−

m)!

n
m

(cid:18)

(cid:19)

m + n
n + k

n

(cid:27)(cid:26)

(cid:19)(cid:18)
k
ℓ

m + k
k

n
k

(cid:27)(cid:18)

(cid:19)(cid:20)
k

−
m

,

(cid:21)

47.

n

(cid:20)

,
(cid:19)

49.

(cid:20)

Xk (cid:26)

,
(cid:21)

41.

43.

(cid:20)

=

n

=

n + 1
k + 1
m

x

−

x

(cid:20)

n

(cid:21)

=

39.

n
m

(cid:20)
(cid:21)
m + n + 1
m

Xk (cid:20)
=

Xk=0 (cid:28)(cid:28)

(cid:29)(cid:29)(cid:18)

n
k

k
m

x + k
2n

,
(cid:19)
k,

1)m

(
−

−

n + k
k

,

(cid:21)

(cid:20)

(cid:21)(cid:18)

(cid:19)

k(n + k)

n + 1
k + 1

Xk=0
1)m

(cid:21)
k
m

(
−
(cid:21)(cid:26)
(cid:27)
m
n
−
m + k

(cid:19)(cid:18)

=

(cid:19)

Xk (cid:20)

k,

−

for n

m,

≥

m + n
n + k

m + k
k

(cid:19)(cid:26)
n

−
m

k

k
ℓ

(cid:21)(cid:20)

(cid:21)(cid:18)

,
(cid:27)

.
(cid:19)

n
k

Xk (cid:18)
ℓ + m
ℓ

(cid:21)(cid:18)

=

Xk (cid:20)
n

−

m

(cid:21)
n
ℓ + m

Trees

Every tree with n
vertices has n
1
edges.

−

inequal-
Kraft
ity: If the depths
of
the leaves of
a binary tree are
d1, . . . , dn:
n

di

2−

1,

≤

i=1
X

and equality holds
only if every in-
ternal node has 2
sons.

Note that Ti is always a power of two.
Let ti = log2 Ti. Then we have
ti+1 = 2i + 2ti,
t1 = 1.

i=0
X

1)

−

g0

G(x)
x

−

P
= 2G(x) +

Master method:
T (n) = aT (n/b) + f (n),

1, b > 1

a

≥

ǫ > 0 such that f (n) = O(nlogb a
If
∃
then

ǫ)

−

T (n) = Θ(nlogb a).

If f (n) = Θ(nlogb a) then

T (n) = Θ(nlogb a log2 n).

ǫ > 0 such that f (n) = Ω(nlogb a+ǫ),
If
∃
and
cf (n)
for large n, then

c < 1 such that af (n/b)

≤

∃

T (n) = Θ(f (n)).

Substitution (example): Consider the
following recurrence

Ti+1 = 22i

T 2
i ,

·

T1 = 2.

Let ui = ti/2i. Dividing both sides of
the previous equation by 2i+1 we get

ti+1
2i+1 =

2i
2i+1 +

ti
2i .

Substituting we ﬁnd
ui+1 = 1
2 + ui,

u1 = 1
2 ,

which is simply ui = i/2. So we ﬁnd
that Ti has the closed form Ti = 2i2i−1
.
Summing factors (example): Consider
the following recurrence

T (n) = 3T (n/2) + n, T (1) = 1.

Rewrite so that all terms involving T
are on the left side

T (n)

−

3T (n/2) = n.

Now expand the recurrence, and choose
a factor which makes the left side “tele-
scope”

Recurrences

1

T (n)

−
T (n/2)
3
(cid:0)
...
...
(cid:0)
T (2)

1

3T (n/2) = n

(cid:1)

3T (n/4) = n/2
−
...
3T (1) = 2

(cid:1)

−

3log2 n

−

(cid:1)

−

3mT (1) = T (n)

Let m = log2 n. Summing the left side
(cid:0)
3m =
we get T (n)
−
nk where k = log2 3
T (n)
1.58496.
Summing the right side we get
n
2i 3i = n

≈

−

3
2

m

m

−

−

1

1

.

i

i=0
i=0
X
X
Let c = 3
2 . Then we have
m
−

1

n

ci = n

(cid:0)

(cid:1)

cm
c

1
−
1
(cid:18)
−
= 2n(clog2 n
= 2n(c(k
= 2nk

2n,

−

(cid:19)

1)

−
1) logc n

−

and so T (n) = 3nk
2n. Full history re-
−
currences can often be changed to limited
history ones (example): Consider
i
−

1

Ti = 1 +

Tj,

T0 = 1.

Note that

j=0
X

i

Ti+1 = 1 +

Tj.

j=0
X

Subtracting we ﬁnd

Ti+1 −

Ti = 1 +

= Ti.

i

j=0
X

Tj −

1

−

Tj

1

i
−

j=0
X

Generating functions:

1. Multiply both sides of the equa-

tion by xi.

2. Sum both sides over all i for

which the equation is valid.

G(x). Usually G(x) =

3. Choose a generating function
∞i=0 xigi.
3. Rewrite the equation in terms of
the generating function G(x).

P

4. Solve for G(x).
5. The coeﬃcient of xi in G(x) is gi.

Example:

gi+1 = 2gi + 1,

g0 = 0.

Multiply and sum:

gi+1xi =

2gixi +

xi.

0
Xi
≥

0
Xi
≥
We choose G(x) =
in terms of G(x):

0
Xi
≥
0 xigi. Rewrite

i
≥

xi.

0
Xi
≥

1

−

1

.

x

Simplify:

G(x)
x

= 2G(x) +

Solve for G(x):
G(x) =

x
x)(1

(1

.

2x)

−
Expand this using partial fractions:
2

−

1

G(x) = x

1

(cid:18)

−

2x −

1

x

(cid:19)

−

2

2ixi

= x

=





0
Xi
≥
(2i+1

−

0
Xi
≥
1)xi+1.

xi





−

0
Xi
≥
1.

−

And so Ti+1 = 2Ti = 2i+1.

So gi = 2i

3.14159,

π

≈

2i
2
4

8
16

32
64

128
256

512
1,024

2,048
4,096

8,192
16,384

32,768

65,536
131,072

262,144
524,288

1,048,576
2,097,152

4,194,304
8,388,608

16,777,216
33,554,432

67,108,864
134,217,728

268,435,456

536,870,912
1,073,741,824

2,147,483,648
4,294,967,296

i

1
2

3
4

5
6

7
8

9
10

11
12

13
14

15

16
17

18
19

20
21

22
23

24
25

26
27

28

29
30

31
32

e

≈
pi
2
3

5
7

11
13

17
19

23
29

31
37

41
43

47

53
59

61
67

71
73

79
83

89
97

101
103

107

109
113

127
131

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

Theoretical Computer Science Cheat Sheet

2.71828,

0.57721,

γ

≈

General

φ = 1+√5

2 ≈

1.61803,

ˆφ = 1
√5
−
2 ≈ −
Probability

.61803

Bernoulli Numbers (Bi = 0, odd i
6 , B4 =
−
30 , B10 = 5
66 .
Change of base, quadratic formula:

B0 = 1, B1 =
B6 = 1

2 , B2 = 1

42 , B8 =

−

−

1

1

= 1):
1
30 ,

√b2
2a

,

b

±

−

logb x =

loga x
loga b
Euler’s number e:
6 + 1
24 + 1
2 + 1
e = 1 + 1
x
1 +
n
< e <

lim
n
→∞ (cid:16)
n
1 + 1
n

n

120 +

= ex.

4ac

.

−

· · ·

+

n

(cid:1)
= e

(cid:0)
1 + 1
n

e
2n
(cid:0)
(cid:1)
Harmonic numbers:
1, 3
60 , 49
6 , 25
2 , 11

12 , 137

−

n+1

.

(cid:17)
1 + 1
n
11e
(cid:1)
(cid:0)
24n2 −

O

1
n3

.

(cid:19)

(cid:18)

20 , 363

140 , 761

280 , 7129

2520 , . . .

ln n < Hn < ln n + 1,
1
n

Hn = ln n + γ + O

.
(cid:19)

(cid:18)

Factorial, Stirling’s approximation:

1, 2, 6, 24, 120, 720, 5040, 40320, 362880, . . .

n

n! = √2πn

n
e
(cid:18)
Ackermann’s function and inverse:

1 + Θ

1
n

(cid:19)

(cid:18)

(cid:18)

.
(cid:19)(cid:19)

i = 1
j = 1
i, j

≥

2

1))

.

}

q = 1

p,

−

2j
a(i
a(i

−
−
j

a(i, j) =




1, 2)
1, a(i, j

α(i) = min


Binomial distribution:

{

|

a(j, j)

−
i

≥

pkqn

−

k,

n
k
(cid:18)
n

Pr[X = k] =

E[X] =

(cid:19)

k

(cid:18)
Poisson distribution:
e−

Xk=1

Pr[X = k] =

n
k

pkqn

−

k = np.

(cid:19)

Normal (Gaussian) distribution:

p(x) =

1
√2πσ

(x

e−

−

µ)2/2σ2

, E[X] = µ.

The “coupon collector”: We are given a
random coupon each day, and there are n
diﬀerent types of coupons. The distribu-
tion of coupons is uniform. The expected
number of days to pass before we to col-
lect all n types is

nHn.

Continuous distributions: If
b

Pr[a < X < b] =

p(x) dx,

then p is the probability density function of
X. If

a
Z

Pr[X < a] = P (a),
then P is the distribution function of X. If
P and p both exist then

a

P (a) =

p(x) dx.

Expectation: If X is discrete

Z

−∞

E[g(X)] =

g(x) Pr[X = x].

x
X
If X continuous then

E[g(X)] =

∞

g(x)p(x) dx =

∞

g(x) dP (x).

Z
−∞
Variance, standard deviation:

Z

−∞

VAR[X] = E[X 2]
σ =

−
VAR[X].

E[X]2,

For events A and B:

p

Pr[A

Pr[A

∨

∧

B] = Pr[A] + Pr[B]

B] = Pr[A]

Pr[B],

Pr[A

B]

∧

−

iﬀ A and B are independent.

·

·

Pr[A
|

B] =

Pr[A

B]

∧
Pr[B]

For random variables X and Y :
Y ] = E[X]

E[Y ],

E[X

·

if X and Y are independent.

E[X + Y ] = E[X] + E[Y ],
E[cX] = c E[X].

Bayes’ theorem:

Pr[Ai|

B] =

Pr[B
Ai] Pr[Ai]
n
j=1 Pr[Aj] Pr[B

|

.

Aj ]

|

Inclusion-exclusion:
P
n

n

Pr

Xi

=

Pr[Xi] +

k

Pr

Xij

.

h

j=1
^

i

Xk=2
Moment inequalities:

ii<

<ik

X
···

Pr

X

|

| ≥

λ E[X]

1
λ

,

≤

Pr

(cid:2)
X
−

E[X]

≥
h(cid:12)
Geometric distribution:
(cid:12)
1,
Pr[X = k] = pqk

(cid:12)
(cid:12)
−

λ

(cid:3)
σ
·

1
λ2 .

≤

i
q = 1

p,

−

E[X] =

kpqk

1 =

−

1
p

.

∞

Xk=1

λλk
k!

, E[X] = λ.

h

i=1
_

i

n

i=1
X
1)k+1

(
−

6
Theoretical Computer Science Cheat Sheet

Trigonometry

Matrices

b

A

C

(0,1)

θ

(cos θ, sin θ)

(-1,0)

(1,0)

c

a

B

(0,-1)

Multiplication:

C = A

·

n

B,

ci,j =

ai,kbk,j.

Determinants: det A

Xk=1

= 0 iﬀ A is non-singular.

det A

B = det A
n

·

·

det B,

det A =

sign(π)ai,π(i).

Pythagorean theorem:

C2 = A2 + B2.

Deﬁnitions:

sin a = A/C,
csc a = C/A,
A
B

cos a = B/C,
sec a = C/B,
cos a
sin a

,

=

cot a =

tan a =

sin a
cos a
Area, radius of inscribed circle:
AB
1
2 AB,
A + B + C

2 and 3

2

×

×

c
b
a
d
f
e
g h i

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

=

B
A

.

(cid:12)
(cid:12)
(cid:12)
(cid:12)
= g

=

π
X
3 determinant:

i=1
Y

a b
d
c

= ad

bc,

−

(cid:12)
(cid:12)
(cid:12)
c
(cid:12)
f

b
e

(cid:12)
(cid:12)
(cid:12)
(cid:12)

h

−

a
c
d f

(cid:12)
(cid:12)
(cid:12)
aei + bf g + cdh
(cid:12)

(cid:12)
(cid:12)
(cid:12)
(cid:12)
f ha

(cid:12)
(cid:12)
(cid:12)
(cid:12)
ceg

−

−

−

a b
d e

(cid:12)
(cid:12)
(cid:12)
(cid:12)

+ i

(cid:12)
(cid:12)
(cid:12)
(cid:12)

ibd.

.

Permanents:

cot x =

sin(x

cos(x

tan(x

±

±

±

cot(x

±

,

sin x =

Identities:
1
csc x
1
cot x
1 + tan2 x = sec2 x,

tan x =

,

sin x = cos

x

,

π
2 −
(cid:0)
cos(π

(cid:1)
x),

−

cos x =

−

cot(π

x),

−

−
y) = sin x cos y

cos x =

1
sec x
sin2 x + cos2 x = 1,

,

1 + cot2 x = csc2 x,

sin x = sin(π

x),

−

tan x = cot

π
2 −

x

,

(cid:0)
csc x = cot x
2 −

(cid:1)
cot x,

cos x sin y,

±

cos 2x = cos2 x

sin2 x,

cos 2x = 2 cos2 x

y) = cos x cos y

sin x sin y,

±

∓
tan y
tan x tan y
1
∓
cot y

tan x
1
cot x cot y
cot x

∓

,

y) =

y) =

,

sin 2x =

cos 2x =

±
sin 2x = 2 sin x cos x,

−
2 sin2 x,

cos 2x = 1

−

tan 2x =

1

2 tan x

tan2 x

−

sin(x + y) sin(x

y) = sin2 x

sin2 y,

−

−

cos(x + y) cos(x

y) = cos2 x

sin2 y.

−

−

Euler’s equation:

eix = cos x + i sin x,

eiπ =

1.

−
1994 by Steve Seiden

v2.02 c
(cid:13)
sseiden@acm.org
http://www.csc.lsu.edu/~seiden

,

2 tan x
1 + tan2 x
1,
−
tan2 x
1
1 + tan2 x
cot2 x
1

−

,

−
2 cot x

,

n

perm A =

ai,π(i).

π
X
Hyperbolic Functions

i=1
Y

Deﬁnitions:
ex

sinh x =

tanh x =

sech x =

x

e−

,

−
2

x
x ,

ex
e−
−
ex + e−
1
,
cosh x

cosh x =

csch x =

coth x =

ex + e−
2

x

,

,

1
sinh x
1
tanh x

.

Identities:

cosh2 x

−

sinh2 x = 1,

tanh2 x + sech2 x = 1,

coth2 x

csch2 x = 1,

−
x) = cosh x,

cosh(

sinh(

−

x) =

−

sinh x,

tanh(

x) =

tanh x,

−

−
sinh(x + y) = sinh x cosh y + cosh x sinh y,

−

cosh(x + y) = cosh x cosh y + sinh x sinh y,

sinh 2x = 2 sinh x cosh x,

cosh 2x = cosh2 x + sinh2 x,

cosh x + sinh x = ex,

cosh x

−

sinh x = e−

x,

(cosh x + sinh x)n = cosh nx + sinh nx, n

Z,

∈

θ

0
π
6
π
4
π
3
π
2

sin θ

cos θ

tan θ

0
1
2
√2
2
√3
2
1

1
√3
2
√2
2
1
2
0

0
√3
3
1

√3

∞

. . . in mathematics
you don’t under-
stand things, you
just get used to
them.
– J. von Neumann

More Trig.

C

b

h

a

B

A

c

Law of cosines:
c2 = a2+b2
Area:

−

2ab cos C.

A = 1
= 1

=

2 hc,
2 ab sin C,
c2 sin A sin B
2 sin C

.

Heron’s formula:

sa ·
sb ·
2 (a + b + c),

·

sc,

A = √s
s = 1
sa = s
sb = s
sc = s

−
−

a,
b,

c.

−
More identities:

sin x

2 =

cos x

2 =

tan x

2 =

=

=

cot x

2 =

=

=

sin x =

cos x =

=

sin x =

,

,

,

,

1

−

cos x
2
1 + cos x
2
cos x
1
1 + cos x
cos x

−

r

r

r
1

−
sin x
sin x
1 + cos x

,

,

1 + cos x
cos x
1

r
−
1 + cos x
sin x
sin x

,

,

1
−
eix

cos x
ix
e−

,

,

ix

−
2i
eix + e−
2
eix
e−
−
eix + e−
e2ix
1
e2ix + 1

−

i

i

−

−
sinh ix
i

,

,

ix
ix ,

cos x = cosh ix,
tanh ix
i

tan x =

.

,

cot 2x =

2 sinh2 x

2 = cosh x

1,

−

2 cosh2 x

2 = cosh x + 1.

tan x =

6
Number Theory

Graph Theory

Theoretical Computer Science Cheat Sheet

The Chinese remainder theorem: There ex-
ists a number C such that:

Deﬁnitions:
Loop

C

C

≡

...

≡

r1 mod m1
...
rn mod mn

...

= j.

if mi and mj are relatively prime for i
Euler’s function: φ(x) is the number of
positive integers less than x relatively
i=1 pei
is the prime fac-
prime to x.
torization of x then
n
Q

If

n

i

φ(x) =

pei
i

1

−

(pi −

1).

i=1
Y

Euler’s theorem: If a and b are relatively
prime then

aφ(b) mod b.

1

≡

Fermat’s theorem:
ap

1

1 mod p.

−

≡

The Euclidean algorithm: if a > b are in-
tegers then

gcd(a, b) = gcd(a mod b, b).

is the prime factorization of x

n

i=1 pei

i

If
then
Q

S(x) =

d =

x
Xd
|

n

i=1
Y

1

.

pei+1
i
−
1
pi −

Perfect Numbers: x is an even perfect num-
1(2n
ber iﬀ x = 2n
1 is prime.
Wilson’s theorem: n is a prime iﬀ
1)!

1) and 2n

1 mod n.

(n

−

−

−

−

≡ −

M¨obius inversion:

1
0
(
−

1)r

if i = 1.
if i is not square-free.
if i is the product of
r distinct primes.

µ(i) = 


If



then

G(a) =

F (d),

a
Xd
|

F (a) =

µ(d)G

a
Xd
|

(cid:16)

a
d

.

(cid:17)

Prime numbers:

pn = n ln n + n ln ln n

n + n

−

ln ln n
ln n

π(n) =

n
ln n

+

2!n
(ln n)3

+ O

+ O

,

n
ln n
(cid:19)
(cid:18)
n
(ln n)2 +
n
(ln n)4

(cid:18)

.
(cid:19)

Directed
Simple

Walk
Trail
Path

Connected

An edge connecting a ver-
tex to itself.
Each edge has a direction.
Graph with no loops or
multi-edges.
A sequence v0e1v1 . . . eℓvℓ.
A walk with distinct edges.
A trail with
distinct
vertices.
A graph where there exists
a path between any two
vertices.

Component A maximal

connected

Tree
Free tree
DAG
Eulerian

subgraph.
A connected acyclic graph.
A tree with no root.
Directed acyclic graph.
Graph with a trail visiting
each edge exactly once.

Hamiltonian Graph with a cycle visiting

Cut

each vertex exactly once.
A set of edges whose re-
moval increases the num-
ber of components.
Cut-set
A minimal cut.
Cut edge
A size 1 cut.
k-Connected A graph connected with
1

the removal of any k
vertices.

−

k-Tough

k-Regular

k-Factor

Matching

Clique

Ind. set

·

S

=

−

∅
S

⊆
c(G

V, S
S)

we have
.
|

spanning

∀
k
≤ |
A graph where all vertices
have degree k.
A k-regular
subgraph.
A set of edges, no two of
which are adjacent.
A set of vertices, all of
which are adjacent.
A set of vertices, none of
which are adjacent.

Vertex cover A set of vertices which

cover all edges.

Planar graph A graph which can be em-

beded in the plane.

Plane graph An embedding of a planar

graph.

deg(v) = 2m.

V
Xv
∈

If G is planar then n

m + f = 2, so

−
4, m

f

2n

≤

−

3n

6.

−

≤

Any planar graph has a vertex with de-
gree

5.

≤

Number of components
Induced subgraph

Notation:
E(G) Edge set
V (G) Vertex set
c(G)
G[S]
deg(v) Degree of v
∆(G) Maximum degree
δ(G) Minimum degree
χ(G) Chromatic number
χE(G) Edge chromatic number
Gc
Complement graph
Complete graph
Kn
Kn1,n2 Complete bipartite graph
r(k, ℓ) Ramsey number

Geometry

Projective coordinates:
(x, y, z), not all x, y and z zero.

triples

(x, y, z) = (cx, cy, cz)

= 0.

c
∀
Projective

Cartesian

(x, y, 1)
(m,
−
(1, 0,

(x, y)
y = mx + b
x = c
Distance formula, Lp and L
metric:

1, b)
c)

−

∞

y0)2,
1/p
p

x0)2 + (y1 −
p +
y0|
y1 −
|
p +
y1 −

(x1 −
x0|
x1 −
p
|
lim
x1 −
(cid:2)
p
→∞
(cid:2)
Area of triangle (x0, y0), (x1, y1)
and (x2, y2):

x0|

y0|
(cid:3)

1/p

(cid:3)

p

|

|

,

.

x0
x0

1
2 abs

x1 −
x2 −

y0
y0 (cid:12)
(cid:12)
Angle formed by three points:
(cid:12)
(cid:12)

y1 −
y2 −

(cid:12)
(cid:12)
(cid:12)
(cid:12)

.

(x2, y2)

ℓ2

θ
(0, 0)

ℓ1
(x1, y1)

cos θ =

(x1, y1)

(x2, y2)

.

·
ℓ1ℓ2

Line through two points (x0, y0)
and (x1, y1):

x
x0
x1

y
y0
y1

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
A = πr2,

1
1
1

= 0.

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
V = 4

3 πr3.

Area of circle, volume of sphere:

If I have seen farther than others,
it is because I have stood on the
shoulders of giants.
– Issac Newton

6
6
6
Theoretical Computer Science Cheat Sheet

π

Calculus

Derivatives:

Wallis’ identity:
2
1

4
·
3
·
Brouncker’s continued fraction expansion:

· · ·
· · ·

π = 2

4
5

6
5

6
7

2
3

·
·

·
·

·
·

·
·

·

π
4 = 1 +

12

2 +

32
2+ 52
2+ 72

2+···

Gregrory’s series:
1
π
4 = 1

3 + 1

−

1

7 + 1

9 − · · ·

5 −

Newton’s series:

π
6 =

1
2

+

2

·
Sharp’s series:

1
3

·

23 +

2

1
4

·
·

3
5

·

·

25 +

· · ·

π
6 =

1
√3

1

−

1
31

·

+

3

1
32

·

5 −

1
33

·

(cid:16)

Euler’s series:

+

7

· · ·

(cid:17)

12 + 1
12 + 1

π2
6 = 1
π2
8 = 1
π2
12 = 1

32 + 1
52 + 1

22 + 1
32 + 1
22 + 1

1

· · ·

52 +
92 +

42 + 1
72 + 1
42 + 1

1

· · ·
52 − · · ·

12 −

32 −
Partial Fractions

We

Let N (x) and D(x) be polynomial func-
tions of x.
can break down
N (x)/D(x) using partial fraction expan-
sion. First, if the degree of N is greater
than or equal to the degree of D, divide
N by D, obtaining

N (x)
D(x)

= Q(x) +

N ′(x)
D(x)

,

where the degree of N ′ is less than that of
D. Second, factor D(x). Use the follow-
ing rules: For a non-repeated factor:
N ′(x)
D(x)

a)D(x)

N (x)

(x

=

+

A

x

a

,

−

−

where

A =

N (x)
D(x)

(cid:20)

.

(cid:21)x=a

For a repeated factor:
1

m

N (x)
a)mD(x)

=

(x

−
where

−

Xk=0

Ak
a)m

−

(x

N ′(x)
D(x)

,

k +

−

Ak =

dk
dxk

1
k!

(cid:20)

(cid:18)

N (x)
D(x)

.

(cid:19)(cid:21)x=a

The reasonable man adapts himself to the
world; the unreasonable persists in trying
to adapt the world to himself. Therefore
all progress depends on the unreasonable.
– George Bernard Shaw

1.

4.

7.

9.

11.

13.

15.

17.

19.

21.

23.

25.

27.

29.

31.

,

,

,

,

,

,

,

,

,

,

,

,

,

,

.

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

du
dx

d(cu)
dx
d(un)
dx
d(cu)
dx

= c

du
dx

,

,

−

= nun

1 du
dx
= (ln c)cu du
dx

,

2.

d(u + v)
dx

=

5.

d(u/v)
dx

=

d(sin u)
dx

= cos u

du
dx

,

d(tan u)
dx

d(sec u)
dx

= sec2 u

du
dx

,

= tan u sec u

du
dx

,

d(arcsin u)
dx

=

d(arctan u)
dx

=

d(arcsec u)
dx

=

1

u2

√1
−
1
1 + u2

1
u√1

= cosh u

−
du
dx

du
dx

,

du
dx

,

du
dx

,

u2

,

d(sinh u)
dx

d(tanh u)
dx

dv
dx

,

du
dx
v

+

du
dx

(cid:0)

(cid:1)

u

dv
dx

(cid:0)

(cid:1)

−
v2

3.

d(uv)
dx

= u

,

6.

d(ecu)
dx

+ v

dv
du
dx
dx
= cecu du
dx

8.

d(ln u)
dx

=

1
u

du
dx

10.

d(cos u)
dx

sin u

=

−

12.

d(cot u)
dx

= csc2 u

d(csc u)
dx

=

−

cot u csc u

14.

16.

d(arccos u)
dx

18.

d(arccot u)
dx

20.

d(arccsc u)
dx

=

22.

d(cosh u)
dx

1

= −
√1
−
= −

u2
1
1 + u2

1

−
u√1

u2

−
= sinh u

= sech2 u

du
dx

,

24.

d(coth u)
dx

=

−

csch2 u

d(sech u)
dx

=

−

sech u tanh u

du
dx

,

26.

d(csch u)
dx

=

−

csch u coth u

d(arcsinh u)
dx

=

d(arctanh u)
dx

=

d(arcsech u)
dx

=

1
√1 + u2
1

1

−

−
u√1

u2

1

−

du
dx

,

28.

d(arccosh u)
dx

=

1
√u2

du
dx

,

30.

d(arccoth u)
dx

=

u2

1

1

−
1

−

du
dx

,

u2

32.

d(arccsch u)
dx

=

u

|

|

1
√1 + u2

−

Integrals:

1.

3.

6.

8.

Z

Z

Z

Z
10.

12.

14.

Z

Z

Z

cu dx = c

u dx,

2.

(u + v) dx =

u dx +

v dx,

xn dx =

Z
1
n + 1

xn+1, n

=

1,

−

dx
1 + x2 = arctan x,

sin x dx =

cos x,

−

tan x dx =

ln

cos x
|

,

|

−

sec x dx = ln

sec x + tan x
|

,

|

arcsin x

a dx = arcsin x

a +

a2

−

p

4.

Z

Z
1
x

dx = ln x,

u

dv
dx

7.

Z

Z
5.

Z
ex dx = ex,

Z

dx = uv

v

du
dx

dx,

−

Z

9.

cos x dx = sin x,

Z

11.

cot x dx = ln

Z

cos x
|

,

|

13.

csc x dx = ln

Z

x2,

a > 0,

csc x + cot x
|

,

|

6
Theoretical Computer Science Cheat Sheet

Calculus Cont.

15.

17.

19.

21.

23.

25.

26.

29.

33.

36.

38.

39.

40.

42.

43.

46.

48.

50.

52.

54.

56.

58.

60.

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

arccos x

a dx = arccos x

a −

x2,

a > 0,

a2

−

p

16.

Z

sin2(ax)dx = 1
2a

ax

−

(cid:0)
sec2 x dx = tan x,

sin(ax) cos(ax)

,

(cid:1)

arctan x

a dx = x arctan x

a −

a

2 ln(a2 + x2),

a > 0,

18.

cos2(ax)dx = 1
2a

ax + sin(ax) cos(ax)

,

Z

(cid:0)

20.

csc2 x dx =

(cid:1)
cot x,

−

cosn

−

1 x sin x
n
cotn
n

1 x
1 −

−

−

Z

+

n

1

−
n

cotn

−

Z

cosn

−

2 x dx,

Z
2 x dx, n

= 1,

n

+

1

sinn

−

2 x dx,

22.

cosn x dx =

= 1,

24.

Z

Z

cotn x dx =

−

secn

−

2 x dx, n

= 1,

sinn x dx =

tann x dx =

secn x dx =

cscn x dx =

−

sinn

−

−
tann
n

−

1 x cos x
n
1 x
1 −

−
n

Z
2 x dx, n

tann

−

−
tan x secn
−
1
n

Z
1 x

−
cot x cscn
−
1
n

−

+

n
n

1 x

+

−
−
n
n

2
1

−
−

Z
2
1

Z

tanh x dx = ln

cosh x
|

|

, 30.

coth x dx = ln

sinh x
|

|

sinh2 x dx = 1

4 sinh(2x)

Z
1
2 x,

−

Z

cosh2 x dx = 1

4 sinh(2x) + 1

2 x,

34.

Z

a > 0,

arcsinh x

a dx = x arcsinh x

x2 + a2,

p

a −
x
a −
x
+
a

x arccosh

x arccosh

= ln



x +

a2 + x2

arccosh x

a dx =




dx
√a2 + x2
dx
a2 + x2 = 1

x2 + a2,

if arccosh x

a > 0 and a > 0,

if arccosh x

a < 0 and a > 0,

p

x2 + a2,

p
,

a > 0,

cscn

−

2 x dx, n

= 1,

27.

sinh x dx = cosh x,

28.

cosh x dx = sinh x,

Z

Z

, 31.

sech x dx = arctan sinh x, 32.

csch x dx = ln

tanh x
2

,

Z
35.

Z

(cid:12)
(cid:12)
(cid:12)
(cid:12)
sech2 x dx = tanh x,

37.

Z

arctanh x

a dx = x arctanh x

a + a

2 ln

a2

|

x2

,

|

−

(cid:16)
p
a arctan x
a ,

(cid:17)
a > 0,

41.

a2

x2 dx = x
2

−

a2

−

x2 + a2

2 arcsin x
a ,

a > 0,

p

Z p

(a2

−

x2)3/2dx = x

8 (5a2

−

2x2)

a2

−

x2 + 3a4

8 arcsin x
a ,

a > 0,

= arcsin x
a ,

a > 0,

x2

p

44.

dx

√a2

a2

−

±

Z p

dx
ax2 + bx
√a + bx
x
√a2
−
x

x2

x2 dx = x
2

a2

x2

±

±

a2
2 ln

=

1
a

ln

p

x
a + bx

,

(cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:12)
(cid:12)
(cid:12)
(cid:12)

dx = 2√a + bx + a

dx =

a2

x2

−

−

a ln

x2

a2

−

p
x dx

√a2
x2
−
√a2 + x2
x

p
x2 dx = x

8 (2x2

a2)

−

p

=

−

a2

−

x2,

p

dx =

a2 + x2

a ln

−

p
3 (x2
a2 dx = 1

a2)3/2,

±

x

x2

±

p

Z

±

dx

−
,

a2

x2

(cid:12)
(cid:12)
(cid:12)

x2 =

1
2a

ln

a + x
x
a

−

(cid:12)
(cid:12)
(cid:12)
(cid:12)

,

(cid:12)
(cid:12)
(cid:12)
47.
(cid:12)

Z

49.

45.

dx

(a2

Z

= ln

−
x +

√x2

a2

−

(cid:12)
(cid:12)
x√a + bx dx =
(cid:12)

x +

a2

p

(cid:12)
(cid:12)
(cid:12)

Z

dx,

1
x√a + bx
a + √a2
x

(cid:12)
(cid:12)
(cid:12)
(cid:12)
a2
(cid:12)

x2 + a4

−

x2

−

,

(cid:12)
(cid:12)
(cid:12)
(cid:12)
8 arcsin x
a ,
(cid:12)

a > 0,

55.

Z

x
√a + bx

dx =

1
√2

51.

Z

ln

53.

x

a2

Z

p
dx

x2 dx

x2
a2

√a2
−
√x2
−
x

Z

=

√a2

x
2

−

−
a2

−

p

dx =

x2

a2

−

p

dx
x√x2 + a2

61.

Z

a + √a2 + x2
x

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

,

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

57.

59.

Z

Z

dx
x2)3/2 =

x
a2√a2

,

x2

−
a > 0,

x2

a2

,

,

−

p
2(3bx

−
(cid:12)
2a)(a + bx)3/2
(cid:12)
(cid:12)
15b2
√a + bx
√a
√a + bx + √a (cid:12)
(cid:12)
(cid:12)
3 (a2
x2 dx =
(cid:12)

−

1

,

x2)3/2,

a > 0,

−

−

(cid:12)
(cid:12)
(cid:12)
(cid:12)
−

=

1
a ln

−

x2

a + √a2
x

x2 + a2

2 arcsin x

a,

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

x2

−

,

(cid:12)
(cid:12)
(cid:12)
(cid:12)
a > 0,
(cid:12)

a arccos a
x
|

|

,

−

a > 0,

= 1

a ln

(cid:12)
(cid:12)
(cid:12)
(cid:12)

x
a + √a2 + x2

,

(cid:12)
(cid:12)
(cid:12)
(cid:12)

6
6
6
6
62.

64.

66.

67.

68.

69.

70.

71.

72.

73.

74.

75.

76.

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Z

Theoretical Computer Science Cheat Sheet

dx
x√x2
−
x dx

√x2

a2

±

= 1

a arccos a

x

|

a2

=

x2

a2,

±

p

1

dx
ax2 + bx + c

= 



√b2

−
2
√4ac

4ac

b2

−

1
√a
1
√

−

dx
√ax2 + bx + c

= 



ax2 + bx + c dx =

Calculus Cont.

a > 0,

63.

,

|

65.

dx
x2√x2
a2

Z
√x2

a2

±
dx =

√x2

a2

±
a2x

∓
(x2 + a2)3/2
3a2x3

,

,

=

∓

ln

(cid:12)
(cid:12)
(cid:12)
(cid:12)
arctan
(cid:12)

Z
√b2
2ax + b
−
2ax + b + √b2

2ax + b
b2

√4ac

−

,

±
x4
4ac
4ac (cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

−
−

,

if b2 > 4ac,

if b2 < 4ac,

ln

2ax + b + 2√a

ax2 + bx + c

,

if a > 0,

Finite Calculus

Diﬀerence, shift operators:
∆f (x) = f (x + 1)
E f (x) = f (x + 1).

−

f (x),

Fundamental Theorem:
f (x) = ∆F (x)

f (x)δx = F (x) + C.

⇔

b

X

f (x)δx =

f (i).

1

b
−

i=a
X

a
X
Diﬀerences:
∆(cu) = c∆u,

∆(u + v) = ∆u + ∆v,

(cid:12)
(cid:12)
arcsin −
(cid:12)

2ax

√b2

−

p
b
,
−
4ac

a

2ax + b
4a

ax2 + bx + c +

b2

4ax

−
8a

p

(cid:12)
(cid:12)
(cid:12)

Z

if a < 0,

dx
√ax2 + bx + c

,

1,

∆(uv) = u∆v + E v∆u,
∆(xn) = nxn
−
1,
1)cx,

∆(Hx) = x−
∆(cx) = (c
Sums:

−

∆(2x) = 2x,
x
m

=

m

x

1

.

−

∆

(cid:0)

(cid:1)

(cid:0)

(cid:1)

x dx
√ax2 + bx + c

=

√ax2 + bx + c
a

b
2a

−

dx
√ax2 + bx + c

,

Z

cu δx = c

u δx,

P

P
(u + v) δx =

u δx +

v δx,

Z p

ln

2√c√ax2 + bx + c + bx + 2c
x

dx
x√ax2 + bx + c

= 


3 x2
x2 + a2 dx = ( 1

x3

(cid:12)
(cid:12)
(cid:12)
(cid:12)
arcsin
(cid:12)

bx + 2c
√b2

4ac

,

−

c

x
−
|
|
15 a2)(x2 + a2)3/2,

2

1
−
√c

1
√

−

,

if c > 0,

if c < 0,

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

p

xn sin(ax) dx =

−

1

a xn cos(ax) + n

a

xn

−

1 cos(ax) dx,

Z
xn

−

n
a

1 sin(ax) dx,

xn cos(ax) dx = 1

a xn sin(ax)

xneax dx =

xneax

a −

xn ln(ax) dx = xn+1

n
a

xn

−

Z
ln(ax)
n + 1 −

−

Z
1eax dx,

xn(ln ax)m dx =

(ln ax)m

(cid:18)
xn+1
n + 1

1
(n + 1)2

m
n + 1

−

,

(cid:19)

xn(ln ax)m

1 dx.

−

Z

x1 =
x2 =
x3 =
x4 =
x5 =

x1
x2 + x1
x3 + 3x2 + x1
x4 + 6x3 + 7x2 + x1
x5 + 15x4 + 25x3 + 10x2 + x1

=
=

=
=

=

x5

−

x1 =
x2 =
x3 =
x4 =
x5 = x5 + 10x4 + 35x3 + 50x2 + 24x1

x1
x2 + x1
x3 + 3x2 + 2x1
x4 + 6x3 + 11x2 + 6x1

x1 =
x2 =
x3 =
x4 =
x5 = x5

−

x1

x2

x1
−
3x2 + x1

x3

−

x1

−
6x3 + 7x2

x4
15x4 + 25x3

−

x1
−
10x2 + x1

−
= 1/(x
n

x2

x1
3x2 + 2x1

−

x3

−

6x3 + 11x2

x4
10x4 + 35x3

6x1
50x2 + 24x1

−

−

−

P

P

P
u∆v δx = uv
−
xn δx = xn+1
m+1 ,
cx δx = cx
c
−
Falling Factorial Powers:
P

P

P

1 ,

xn = x(x
x0 = 1,

1)

−

xn =

(x + 1)

(x +

· · ·
m)n.

xn+m = xm(x
Rising Factorial Powers:

−

P
E v∆u δx,

x−

1 δx = Hx,

x
P
m

δx =

x
m+1

.

P (cid:0)

(cid:1)

(cid:1)
n + 1), n > 0,

(cid:0)

(x

−

, n < 0,

n

)

|

|

xn = x(x + 1)

x0 = 1,

(x + n

−

1), n > 0,

· · ·

1

· · ·

1

xn =

−

1)

· · ·

(x
(x
xn+m = xm(x + m)n.
Conversion:
xn = (
1)n(

x)n = (x

−

−

= 1/(x + 1)−
1)n(

xn = (

n,

, n < 0,

n

)

|

− |

n + 1)n

−

x)n = (x + n
−
1)−

n,

1)n

−

n
k

(
−

(cid:27)

1)n

−

kxk,

xn =

xn =

xn =

−
n
k

n

xk =

(cid:27)

1)n

−

(
−

Xk=1 (cid:26)
kxk,

n

Xk=1 (cid:26)
n
k

Xk=1 (cid:20)

n

Xk=1 (cid:20)

(cid:21)

(cid:21)

n
k

xk.

Taylor’s series:

f (x) = f (a) + (x

a)f ′(a) +

−

a)2

(x

−
2

f ′′(a) +

=

· · ·

Theoretical Computer Science Cheat Sheet

Series

a)i

−
i!

f (i)(a).

∞

(x

i=0
X

∞

xi,

= 1 + x + x2 + x3 + x4 +

= 1 + cx + c2x2 + c3x3 +

· · ·

· · ·

= 1 + xn + x2n + x3n +

· · ·

= x + 2x2 + 3x3 + 4x4 +

· · ·

= x + 2nx2 + 3nx3 + 4nx4 +

· · ·

= 1 + x + 1

2 x2 + 1

6 x3 +

· · ·

= x

−

1

2 x2 + 1

3 x3

1
4 x4

−

− · · ·

= x + 1

2 x2 + 1

3 x3 + 1

4 x4 +

· · ·

= x

= 1

= x

−

−

−

1

3! x3 + 1

5! x5

1

2! x2 + 1

4! x4

1

7! x7 +

· · ·

1

6! x6 +

· · ·

−

−

1

3 x3 + 1

5 x5

1

7 x7 +

−

· · ·

= 1 + nx + n(n
−
2

1)

x2 +

· · ·

= 1 + (n + 1)x +

= 1

−

1

2 x + 1

12 x2

n+2
2

x2 +

· · ·

(cid:1)
720 x4 +

1

(cid:0)

−

· · ·

= 1 + 2x + 6x2 + 20x3 +

· · ·

= 1 + (2 + n)x +

4+n
2

x2 +

= x + 3

2 x2 + 11

(cid:0)
(cid:1)
6 x3 + 25
12 x4 +

· · ·

· · ·

= 1

2 x2 + 3

4 x3 + 11

24 x4 +

· · ·

= x + x2 + 2x3 + 3x4 +

· · ·

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

=

=

=

=

=

=

=

=

=

i=0
X
∞

i=0
X
∞

i=0
X
∞

i=0
X
∞

i=0
X
∞

i=0
X
∞

i=1
X
∞

i=1
X
∞

i=0
X
∞

i=0
X
∞

i=0
X
∞

cixi,

xni,

ixi,

inxi,

xi
i!

,

1)i+1 xi
i

,

(
−

xi
i

,

1)i x2i+1
(2i + 1)!

,

(
−

,

1)i x2i
(2i)!
1)i x2i+1
(2i + 1)

(
−

(
−

,

n
i

xi,

i=0 (cid:18)
X
∞

i=0 (cid:18)
X
∞

(cid:19)
i + n
i
Bixi
i!

,

xi,

(cid:19)

i=0
X
∞

i=0
X
∞

i=0 (cid:18)
X
∞

i=0 (cid:18)
X
∞

1
i + 1

xi,

2i
i

(cid:19)

(cid:18)
xi,

2i
i

(cid:19)
2i + n
i

xi,

(cid:19)

Hixi,

1xi

,

Hi

−
i

Fixi,

Fnixi.

i=1
X
∞

i=2
X
∞

i=0
X
∞

i=0
X

Ordinary power series:

A(x) =

∞

aixi.

i=0
X

i=0
X

Exponential power series:
xi
i!

A(x) =

ai

∞

.

Dirichlet power series:

∞

A(x) =

Binomial theorem:

i=1
X

ai
ix .

n

(x + y)n =

n
k

xn

−

kyk.

(cid:19)

Xk=0 (cid:18)

Diﬀerence of like powers:

xn

−

yn = (x

y)

−

For ordinary power series:

1

n

−

xn

−

1

−

kyk.

Xk=0

αA(x) + βB(x) =

xkA(x) =

∞

i=0
X
∞

(αai + βbi)xi,

kxi,

ai

−

Xi=k

1
k
i=0 aixi
−

A(x)

−

xk
P

A(cx) =

A′(x) =

xA′(x) =

A(x) dx =

Z
A(x) + A(

x)

−

2

A(x)

x)

A(
−
2

−

=

=

∞

=

ai+kxi,

∞

i=0
X
∞

i=0
X
∞

i=1
X
∞

i=1
X
∞

i=0
X
∞

i=0
X

i=0
X
ciaixi,

(i + 1)ai+1xi,

iaixi,

ai
−
i

1

xi,

a2ix2i,

a2i+1x2i+1.

i
j=0 ai then

Summation: If bi =
1

B(x) =

Convolution:

A(x)B(x) =

1

−

A(x).

P
x

i

∞

i=0
X

ajbi

−

j

xi.







j=0
X

God made the natural numbers;
all the rest is the work of man.
– Leopold Kronecker

Expansions:

1

1

−
1

x

1

1

(1

−
1

−
x

−

cx

xn

x)2

k!zk

n

Xk=0 (cid:26)

n
k

(1

(cid:27)

−

z)k+1

ex

ln(1 + x)

ln

1

1

−

x

sin x

cos x

tan−

1 x

(1 + x)n

1
x)n+1

x

1

−
√1

1

−

−

4x
√1
2x

4x

−

n

(cid:19)

1

−

x
2

ln

1

1

(1

−

ex

1
2x

(1

−

1

−

√1

√1

1

4x

(cid:18)
1

1

1
2

x

−

ln

(cid:18)

1

x

(cid:19)

−

x
x

x2

1

−

−
Fnx
1 + Fn+1)x

1

(Fn

−

−

1)nx2 = Fnx + F2nx2 + F3nx3 +

· · ·

(
−

−

4x)

−

= 1 + x + 2x2 + 5x3 +

· · ·

Expansions:
1
x)n+1 ln

(1

−

1

−

1

x

n

ln

(cid:18)

xn

1

1

x

(cid:19)

−

tan x

1
ζ(x)

ζ(x)

ζ2(x)

ζ(x)ζ(x

1)

−

ζ(2n)

x
sin x

1

−

√1
2x

−

(cid:18)

n

4x

(cid:19)

ex sin x

1

−

√1
x

x

−

s

arcsin x
x

2

(cid:19)

(cid:18)

Hn)

n + i
i

xi,

(cid:19)

(cid:18)

∞

i=0
X
∞

(Hn+i −
n
i

xi,

(cid:21)

=

=

=

=

=

i=0 (cid:20)
X
∞

i=0 (cid:20)
X
∞

(
−

i=1
X
∞

i=1
X

i
n

,

n!xi
i!
1 22i(22i

(cid:21)
1)i

−

µ(i)
ix ,
1
p−

1

−
d(i)
xi

S(i)
xi
B2n|

−
|
(2n)!

1

x ,

where d(n) =

where S(n) =

π2n, n

N,

∈
2)B2ix2i
(2i)!

1 (4i

1)i

−

(
−

−

n(2i + n

1)!

−
i!(n + i)!

xi,

2i/2 sin iπ
4
i!

xi,

(4i)!
16i√2(2i)!(2i + 1)!

xi,

4ii!2
(i + 1)(2i + 1)!

x2i.

=

=

=

=

=

=

=

=

=

p
Y
∞

i=1
X
∞

i=1
X
22n

∞

i=0
X
∞

i=0
X
∞

i=1
X
∞

i=0
X
∞

i=0
X

Cramer’s Rule

If we have equations:

a1,1x1 + a1,2x2 +
a2,1x1 + a2,2x2 +

...

...

an,1x1 + an,2x2 +

+ a1,nxn = b1
+ a2,nxn = b2
...
+ an,nxn = bn

· · ·
· · ·

· · ·

Let A = (ai,j) and B be the column matrix (bi). Then
there is a unique solution iﬀ det A
= 0. Let Ai be A
with column i replaced by B. Then

xi =

det Ai
det A

.

Improvement makes strait roads, but the crooked
roads without Improvement, are roads of Genius.
– William Blake (The Marriage of Heaven and Hell)

Theoretical Computer Science Cheat Sheet

Series

Escher’s Knot

1
x

n

−

(cid:19)

(cid:18)
(ex

1)n =

−

∞

=

xi,

i
n

(cid:27)

i=0 (cid:26)
X
∞

i=0 (cid:26)
X
(
∞
−

,

n!xi
i
i!
n
(cid:27)
4)iB2ix2i
(2i)!

,

x cot x

1

,

ζ(x)

1)B2ix2i

−

−
(2i)!

ζ(x

1)

−
ζ(x)

=

=

=

i=0
X
∞

i=1
X
∞

i=1
X

1
ix ,
φ(i)
ix ,

If G is continuous in the interval [a, b] and F is nondecreasing then

Stieltjes Integration

n 1,

d

|

P

n d,

d

|

P

b

a
Z

b

exists. If a

b

c then

≤

≤
c
G(x) dF (x) =

a
Z
If the integrals involved exist

Z

a

G(x) dF (x)

G(x) dF (x) +

G(x) dF (x).

c

b
Z

b

b

,

b

a
Z

b

G(x) + H(x)

dF (x) =

G(x) dF (x) +

H(x) dF (x),

(cid:0)
G(x) d

(cid:1)
F (x) + H(x)

a
Z

b

a
Z

b

=

G(x) dF (x) +

G(x) dH(x),

a
Z

b

a

Z

·

c

b

(cid:0)

G(x) dF (x) =

a
Z

a
Z

(cid:1)
b
G(x) d

c

·

G(x) dF (x) = G(b)F (b)

(cid:0)
(cid:1)
G(a)F (a)

a
Z
b

F (x)

= c

G(x) dF (x),

a
Z
b

F (x) dG(x).

a
Z

−
If the integrals involved exist, and F possesses a derivative F ′ at every
point in [a, b] then

a
Z

−

b

a
Z

G(x) dF (x) =

G(x)F ′(x) dx.

b

a
Z

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

+ Fkm ,

n = Fk1 + Fk2 +
where ki ≥
1
≤

i < m and km ≥

· · ·

ki+1 + 2 for all i,
2.

Fibonacci Numbers

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .

Deﬁnitions:
Fi = Fi
−
F

1+Fi
−
i = (
−
Fi = 1
√5

−

2, F0 = F1 = 1,
1)i

−

1Fi,
ˆφi

,

φi

−

(cid:17)
(cid:16)
Cassini’s identity: for i > 0:
F 2
1)i.

i = (

Fi+1Fi
1 −
Additive rule:

−

−

Fn+k = FkFn+1 + Fk
F2n = FnFn+1 + Fn
−
Calculation by matrices:

1Fn,
−
1Fn.

Fn
Fn

−

−

(cid:18)

2 Fn
1

1

−

Fn (cid:19)

0
1

1
1

n

.

(cid:19)

=

(cid:18)

6
