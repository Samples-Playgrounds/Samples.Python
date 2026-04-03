|                                                                                                               | Theoretical                                                                                                                                          | Computer Science Cheat Sheet                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                               | Definitions                                                                                                                                          | Series                                                                                                                                                                                                                                                        |
| f(n) = O(g(n))                                                                                                | iff $\exists$ positive $c, n_0$ such that $0 \le f(n) \le cg(n) \ \forall n \ge n_0$ .                                                               | $\sum_{i=1}^{n} i = \frac{n(n+1)}{2},  \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6},  \sum_{i=1}^{n} i^3 = \frac{n^2(n+1)^2}{4}.$                                                                                                                              |
| $f(n) = \Omega(g(n))$                                                                                         | iff $\exists$ positive $c, n_0$ such that $f(n) \ge cg(n) \ge 0 \ \forall n \ge n_0$ .                                                               | i=1 $i=1$ $i=1$ In general:                                                                                                                                                                                                                                   |
| $f(n) = \Theta(g(n))$                                                                                         | iff $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$ .                                                                                                     | $\sum_{i=1}^{n} i^{m} = \frac{1}{m+1} \left[ (n+1)^{m+1} - 1 - \sum_{i=1}^{n} \left( (i+1)^{m+1} - i^{m+1} - (m+1)i^{m} \right) \right]$                                                                                                                      |
| f(n) = o(g(n))                                                                                                | iff $\lim_{n\to\infty} f(n)/g(n) = 0$ .                                                                                                              | $\sum_{k=1}^{m} i^m = \frac{1}{m+1} \sum_{k=1}^{m} {m+1 \choose k} B_k n^{m+1-k}.$                                                                                                                                                                            |
| $\lim_{n \to \infty} a_n = a$                                                                                 | iff $\forall \epsilon > 0$ , $\exists n_0$ such that $ a_n - a  < \epsilon$ , $\forall n \ge n_0$ .                                                  | k=0 Geometric series:                                                                                                                                                                                                                                         |
| $\sup S$                                                                                                      | least $b \in \mathbb{R}$ such that $b \ge s$ , $\forall s \in S$ .                                                                                   | $\sum_{i=0}^{n} c^{i} = \frac{c^{n+1} - 1}{c - 1},  c \neq 1,  \sum_{i=0}^{\infty} c^{i} = \frac{1}{1 - c},  \sum_{i=1}^{\infty} c^{i} = \frac{c}{1 - c},   c  < 1,$                                                                                          |
| $\inf S$                                                                                                      | greatest $b \in \mathbb{R}$ such that $b \le s$ , $\forall s \in S$ .                                                                                | $\sum_{i=0}^{n} ic^{i} = \frac{nc^{n+2} - (n+1)c^{n+1} + c}{(c-1)^{2}},  c \neq 1,  \sum_{i=0}^{\infty} ic^{i} = \frac{c}{(1-c)^{2}},   c  < 1$                                                                                                               |
| $ \liminf_{n \to \infty} a_n $                                                                                | $\lim_{n\to\infty}\inf\{a_i\mid i\geq n, i\in\mathbb{N}\}.$                                                                                          | Harmonic series: $n = \sum_{i=1}^{n} 1$ $n(n+1)$ $n(n-1)$                                                                                                                                                                                                     |
| $\limsup_{n \to \infty} a_n$                                                                                  | $\lim_{n \to \infty} \sup \{ a_i \mid i \ge n, i \in \mathbb{N} \}.$                                                                                 | $H_n = \sum_{i=1}^n \frac{1}{i}, \qquad \sum_{i=1}^n iH_i = \frac{n(n+1)}{2}H_n - \frac{n(n-1)}{4}.$                                                                                                                                                          |
| $\binom{n}{k}$                                                                                                | Combinations: Size $k$ subsets of a size $n$ set.                                                                                                    | $\sum_{i=1}^{n} H_i = (n+1)H_n - n,  \sum_{i=1}^{n} {i \choose m} H_i = {n+1 \choose m+1} \left( H_{n+1} - \frac{1}{m+1} \right).$                                                                                                                            |
| $\begin{bmatrix} n \\ k \end{bmatrix}$                                                                        | Stirling numbers (1st kind):<br>Arrangements of an $n$ element set into $k$ cycles.                                                                  | $1. \ \binom{n}{k} = \frac{n!}{(n-k)!k!}, \qquad 2. \ \sum_{k=0}^{n} \binom{n}{k} = 2^{n}, \qquad 3. \ \binom{n}{k} = \binom{n}{n-k},$                                                                                                                        |
| $\binom{n}{k}$                                                                                                | Stirling numbers (2nd kind):<br>Partitions of an $n$ element<br>set into $k$ non-empty sets.                                                         | $4.  \binom{n}{k} = \frac{n}{k} \binom{n-1}{k-1}, \qquad \qquad 5.  \binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1}, \\ 6.  \binom{n}{m} \binom{m}{k} = \binom{n}{k} \binom{n-k}{m-k}, \qquad \qquad 7.  \sum_{k=0}^{n} \binom{r+k}{k} = \binom{r+n+1}{n}, $ |
| $\left\langle {n\atop k}\right\rangle$                                                                        | 1st order Eulerian numbers:<br>Permutations $\pi_1\pi_2\pi_n$ on $\{1,2,,n\}$ with $k$ ascents.                                                      | $8. \ \sum_{k=0}^{n} \binom{k}{m} = \binom{n+1}{m+1}, \qquad \qquad 9. \ \sum_{k=0}^{n-1} \binom{r}{k} \binom{s}{n-k} = \binom{r+s}{n},$                                                                                                                      |
| $\left\langle\!\!\left\langle {n\atop k}\right\rangle\!\!\right\rangle$                                       | 2nd order Eulerian numbers.                                                                                                                          | <b>10.</b> $\binom{n}{k} = (-1)^k \binom{k-n-1}{k}$ , <b>11.</b> $\binom{n}{1} = \binom{n}{n} = 1$ ,                                                                                                                                                          |
| $C_n$                                                                                                         | Catalan Numbers: Binary trees with $n+1$ vertices.                                                                                                   | <b>10.</b> $\binom{n}{k} = (-1)^k \binom{k-n-1}{k}$ , <b>11.</b> $\binom{n}{1} = \binom{n}{n} = 1$ , <b>12.</b> $\binom{n}{2} = 2^{n-1} - 1$ , <b>13.</b> $\binom{n}{k} = k \binom{n-1}{k} + \binom{n-1}{k-1}$ ,                                              |
|                                                                                                               | 1)!, <b>15.</b> $\begin{bmatrix} n \\ 2 \end{bmatrix} = (n - 1)^n$                                                                                   | $-1)!H_{n-1},$ <b>16.</b> $\begin{bmatrix} n \\ n \end{bmatrix} = 1,$ <b>17.</b> $\begin{bmatrix} n \\ k \end{bmatrix} \ge \begin{Bmatrix} n \\ k \end{Bmatrix},$                                                                                             |
|                                                                                                               |                                                                                                                                                      | ${n \choose n-1} = {n \choose n-1} = {n \choose 2},  \textbf{20.} \ \sum_{k=0}^n {n \choose k} = n!,  \textbf{21.} \ C_n = \frac{1}{n+1} {2n \choose n},$                                                                                                     |
|                                                                                                               |                                                                                                                                                      | $\binom{n}{n-1-k}$ , $24. \binom{n}{k} = (k+1)\binom{n-1}{k} + (n-k)\binom{n-1}{k-1}$ ,                                                                                                                                                                       |
| ` '                                                                                                           | •                                                                                                                                                    | $\binom{n}{1} = 2^n - n - 1,$ <b>27.</b> $\binom{n}{2} = 3^n - (n+1)2^n + \binom{n+1}{2},$                                                                                                                                                                    |
| 20                                                                                                            |                                                                                                                                                      | $\sum_{k=0}^{n} \binom{n+1}{k} (m+1-k)^n (-1)^k, \qquad 30. \ m! \begin{Bmatrix} n \\ m \end{Bmatrix} = \sum_{k=0}^{n} \binom{n}{k} \binom{k}{n-m},$                                                                                                          |
| $31.  \left\langle {n \atop m} \right\rangle = \sum_{k=0}^{n}$                                                | ${n \brace k} {n-k \brack m} (-1)^{n-k-m} k!,$                                                                                                       | <b>32.</b> $\left\langle \left\langle n \atop 0 \right\rangle \right\rangle = 1,$ <b>33.</b> $\left\langle \left\langle n \atop n \right\rangle \right\rangle = 0$ for $n \neq 0,$                                                                            |
| $34.  \left\langle \!\! \left\langle \!\! \begin{array}{c} n \\ k \end{array} \!\! \right\rangle = (k + 1)^n$ | $+1$ ) $\left\langle \left\langle {n-1\atop k}\right\rangle \right\rangle + (2n-1-k)\left\langle \left\langle {n\atop k}\right\rangle \right\rangle$ |                                                                                                                                                                                                                                                               |
| $36. \left\{ \begin{array}{c} x \\ x-n \end{array} \right\} = \frac{1}{k}$                                    | $\sum_{k=0}^{n} \left\langle \!\! \left\langle n \right\rangle \!\! \right\rangle \left( x + n - 1 - k \right), $ $2n$                               | <b>37.</b> $\binom{n+1}{m+1} = \sum_{k} \binom{n}{k} \binom{k}{m} = \sum_{k=0}^{n} \binom{k}{m} (m+1)^{n-k},$                                                                                                                                                 |

Identities Cont.

$$38. \begin{bmatrix} n+1 \\ m+1 \end{bmatrix} = \sum_{k} \begin{bmatrix} n \\ k \end{bmatrix} \binom{k}{m} = \sum_{k=0}^{n} \begin{bmatrix} k \\ m \end{bmatrix} n^{\frac{n-k}{2}} = n! \sum_{k=0}^{n} \frac{1}{k!} \begin{bmatrix} k \\ m \end{bmatrix}, \qquad 39. \begin{bmatrix} x \\ x-n \end{bmatrix} = \sum_{k=0}^{n} \left\langle \binom{n}{k} \right\rangle \binom{x+k}{2n},$$

$$40. \begin{Bmatrix} n \\ m \end{Bmatrix} = \sum_{k=0}^{n} \binom{n}{k} \binom{k+1}{m+1} (-1)^{n-k}, \qquad 41. \begin{bmatrix} n \\ m \end{bmatrix} = \sum_{k=0}^{n} \binom{n+1}{k+1} \binom{k}{m} (-1)^{m-k},$$

**42.** 
$${m+n+1 \choose m} = \sum_{k=0}^{m} k {n+k \choose k},$$
 **43.**  ${m+n+1 \choose m} = \sum_{k=0}^{m} k(n+k) {n+k \choose k},$ 

**44.** 
$$\binom{n}{m} = \sum_{k} {n+1 \brace k+1} {k \brack m} (-1)^{m-k}, \quad \textbf{45.} \quad (n-m)! \binom{n}{m} = \sum_{k} {n+1 \brack k+1} {k \brack m} (-1)^{m-k}, \quad \text{for } n \ge m,$$

$$46. \begin{cases} n \\ n-m \end{cases} = \sum_{k} \binom{m-n}{m+k} \binom{m+n}{n+k} \binom{m+k}{k}, \qquad 47. \begin{bmatrix} n \\ n-m \end{bmatrix} = \sum_{k} \binom{m-n}{m+k} \binom{m+n}{n+k} \binom{m+k}{k},$$

**48.** 
$${n \choose \ell+m} {\ell+m \choose \ell} = \sum_{k} {k \choose \ell} {n-k \choose m} {n \choose k},$$

$$49. \begin{bmatrix} n-m \end{bmatrix} \xrightarrow{\sum_{k}} (m+k)(n+k)(k)$$

$$\ell = \sum_{k} \begin{bmatrix} k \\ \ell \end{bmatrix} \begin{bmatrix} n-k \\ m \end{bmatrix} \binom{n}{k}$$

Trees

Every tree with nvertices has n-1edges.

Kraft inequality: If the depths of the leaves of a binary tree are

$$d_1, \dots, d_n$$
:  

$$\sum_{i=1}^{n} 2^{-d_i} \le 1,$$

and equality holds only if every internal node has 2 sons

#### Recurrences

Master method:

$$T(n) = aT(n/b) + f(n), \quad a \ge 1, b > 1$$

If  $\exists \epsilon > 0$  such that  $f(n) = O(n^{\log_b a - \epsilon})$ then

$$T(n) = \Theta(n^{\log_b a}).$$

If 
$$f(n) = \Theta(n^{\log_b a})$$
 then 
$$T(n) = \Theta(n^{\log_b a} \log_2 n).$$

If  $\exists \epsilon > 0$  such that  $f(n) = \Omega(n^{\log_b a + \epsilon})$ , and  $\exists c < 1$  such that  $af(n/b) \leq cf(n)$ for large n, then

$$T(n) = \Theta(f(n)).$$

Substitution (example): Consider the following recurrence

$$T_{i+1} = 2^{2^i} \cdot T_i^2, \quad T_1 = 2.$$

Note that  $T_i$  is always a power of two. Let  $t_i = \log_2 T_i$ . Then we have

$$t_{i+1} = 2^i + 2t_i, \quad t_1 = 1.$$

Let  $u_i = t_i/2^i$ . Dividing both sides of the previous equation by  $2^{i+1}$  we get

$$\frac{t_{i+1}}{2^{i+1}} = \frac{2^i}{2^{i+1}} + \frac{t_i}{2^i}.$$

Substituting we find

$$u_{i+1} = \frac{1}{2} + u_i, \qquad u_1 = \frac{1}{2},$$

which is simply  $u_i = i/2$ . So we find that  $T_i$  has the closed form  $T_i = 2^{i2^{i-1}}$ . Summing factors (example): Consider the following recurrence

$$T(n) = 3T(n/2) + n, T(1) = 1.$$

Rewrite so that all terms involving Tare on the left side

$$T(n) - 3T(n/2) = n.$$

Now expand the recurrence, and choose a factor which makes the left side "telescope"

$$1(T(n) - 3T(n/2) = n)$$
$$3(T(n/2) - 3T(n/4) = n/2)$$
$$\vdots \qquad \vdots$$

Let  $m = \log_2 n$ . Summing the left side we get  $T(n) - 3^m T(1) = T(n) - 3^m =$  $T(n) - n^k$  where  $k = \log_2 3 \approx 1.58496$ . Summing the right side we get

 $3^{\log_2 n - 1} (T(2) - 3T(1) = 2)$ 

$$\sum_{i=0}^{m-1} \frac{n}{2^i} 3^i = n \sum_{i=0}^{m-1} \left(\frac{3}{2}\right)^i.$$

Let  $c = \frac{3}{2}$ . Then we have

$$n \sum_{i=0}^{m-1} c^{i} = n \left( \frac{c^{m} - 1}{c - 1} \right)$$

$$= 2n(c^{\log_{2} n} - 1)$$

$$= 2n(c^{(k-1)\log_{c} n} - 1)$$

$$= 2n^{k} - 2n$$

and so  $T(n) = 3n^k - 2n$ . Full history recurrences can often be changed to limited history ones (example): Consider

$$T_i = 1 + \sum_{j=0}^{i-1} T_j, \quad T_0 = 1.$$

Note that

$$T_{i+1} = 1 + \sum_{j=0}^{i} T_j.$$

Subtracting we find

$$T_{i+1} - T_i = 1 + \sum_{j=0}^{i} T_j - 1 - \sum_{j=0}^{i-1} T_j$$
  
=  $T_i$ .

And so 
$$T_{i+1} = 2T_i = 2^{i+1}$$
.

Generating functions:

- 1. Multiply both sides of the equation by  $x^i$ .
- 2. Sum both sides over all i for which the equation is valid.
- 3. Choose a generating function G(x). Usually  $G(x) = \sum_{i=0}^{\infty} x^i g_i$ .
- 3. Rewrite the equation in terms of the generating function G(x).
- 4. Solve for G(x).
- 5. The coefficient of  $x^i$  in G(x) is  $g_i$ . Example:

$$q_{i+1} = 2q_i + 1, \quad q_0 = 0.$$

$$\sum_{i\geq 0}^{\infty} g_{i+1}x^i = \sum_{i\geq 0}^{\infty} 2g_ix^i + \sum_{i\geq 0}^{\infty} x^i.$$

We choose  $G(x) = \sum_{i \geq 0} x^i g_i$ . Rewrite

$$\frac{G(x) - g_0}{x} = 2G(x) + \sum_{i>0} x^i.$$

Simplify

$$\frac{G(x)}{x} = 2G(x) + \frac{1}{1-x}.$$

Solve for 
$$G(x)$$
:
$$G(x) = \frac{x}{(1-x)(1-2x)}.$$

Expand this using partial fractions:

$$G(x) = x \left( \frac{2}{1 - 2x} - \frac{1}{1 - x} \right)$$

$$= x \left( 2 \sum_{i \ge 0} 2^i x^i - \sum_{i \ge 0} x^i \right)$$

$$= \sum_{i \ge 0} (2^{i+1} - 1) x^{i+1}.$$

So 
$$g_i = 2^i - 1$$
.

| Theoretical Computer Science Cheat Sheet              |                        |                  |                                                                                                                                          |                                                                                                    |
|-------------------------------------------------------|------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
|                                                       | $\pi \approx 3.14159,$ | $e \approx 2.71$ | 1828, $\gamma \approx 0.57721$ , $\phi = \frac{1+\sqrt{5}}{2} \approx$                                                                   | 1.61803, $\hat{\phi} = \frac{1-\sqrt{5}}{2} \approx61803$                                          |
| i                                                     | $2^i$                  | $p_i$            | General                                                                                                                                  | Probability                                                                                        |
| 1                                                     | 2                      | 2                | Bernoulli Numbers ( $B_i = 0$ , odd $i \neq 1$ ):                                                                                        | Continuous distributions: If                                                                       |
| 2                                                     | 4                      | 3                | $B_0 = 1, B_1 = -\frac{1}{2}, B_2 = \frac{1}{6}, B_4 = -\frac{1}{30},$                                                                   | $\Pr[a < X < b] = \int_{-\infty}^{\infty} p(x)  dx,$                                               |
| 3                                                     | 8                      | 5                | $B_6 = \frac{1}{42}, B_8 = -\frac{1}{30}, B_{10} = \frac{5}{66}.$                                                                        | $J_a$ then $p$ is the probability density function of                                              |
| 4                                                     | 16                     | 7                | Change of base, quadratic formula:                                                                                                       | X. If                                                                                              |
| 5                                                     | 32                     | 11               | $\log_b x = \frac{\log_a x}{\log_a b}, \qquad \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$                                                       | $\Pr[X < a] = P(a),$                                                                               |
| 6                                                     | 64                     | 13               | $\log_a b$ 2a Euler's number $e$ :                                                                                                       | then $P$ is the distribution function of $X$ . If                                                  |
| 7                                                     | 128                    | 17               | Euler's number $e$ : $e = 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \cdots$                                         | P and $p$ both exist then                                                                          |
| 8                                                     | 256                    | 19               | 2 0 24 120                                                                                                                               | $P(a) = \int_{-a}^{a} p(x)  dx.$                                                                   |
| 9                                                     | 512                    | 23               | $\lim_{n \to \infty} \left( 1 + \frac{x}{n} \right)^n = e^x.$                                                                            | $J_{-\infty}$ Expectation: If X is discrete                                                        |
| 10                                                    | 1,024                  | 29               | $\left(1 + \frac{1}{n}\right)^n < e < \left(1 + \frac{1}{n}\right)^{n+1}$ .                                                              | _                                                                                                  |
| 11                                                    | 2,048                  | 31               |                                                                                                                                          | $E[g(X)] = \sum_{x} g(x) \Pr[X = x].$                                                              |
| 12                                                    | 4,096                  | 37               | $\left(1 + \frac{1}{n}\right)^n = e - \frac{e}{2n} + \frac{11e}{24n^2} - O\left(\frac{1}{n^3}\right).$                                   | If X continuous then                                                                               |
| 13                                                    | 8,192                  | 41               | Harmonic numbers:                                                                                                                        | $\mathbb{E}[g(X)] = \int_{-\infty}^{\infty} g(x)p(x)  dx = \int_{-\infty}^{\infty} g(x)  dP(x).$   |
| 14                                                    | 16,384                 | 43               | $1, \frac{3}{2}, \frac{11}{6}, \frac{25}{12}, \frac{137}{60}, \frac{49}{20}, \frac{363}{140}, \frac{761}{280}, \frac{7129}{2520}, \dots$ | $J = \infty$ $J = \infty$                                                                          |
| 15                                                    | 32,768                 | 47<br>52         |                                                                                                                                          | Variance, standard deviation: $VAR[Y] = F[Y^2] = F[Y]^2$                                           |
| 16                                                    | 65,536                 | 53<br>50         | $ \ln n < H_n < \ln n + 1, $                                                                                                             | $VAR[X] = E[X^2] - E[X]^2,$                                                                        |
| $\begin{array}{ c c } \hline 17 \\ 18 \\ \end{array}$ | 131,072                | 59<br>61         | $H_n = \ln n + \gamma + O\left(\frac{1}{n}\right).$                                                                                      | $\sigma = \sqrt{\text{VAR}[X]}.$                                                                   |
| $\frac{18}{19}$                                       | 262,144<br>524,288     | 61<br>67         | Factorial, Stirling's approximation:                                                                                                     | For events A and B:<br>$Pr[A \lor B] = Pr[A] + Pr[B] - Pr[A \land B]$                              |
| $\frac{19}{20}$                                       | 1,048,576              | 71               | 1, 2, 6, 24, 120, 720, 5040, 40320, 362880,                                                                                              | $Pr[A \lor B] = Pr[A] + Pr[B] - Pr[A \land B]$ $Pr[A \land B] = Pr[A] \cdot Pr[B],$                |
| $\frac{20}{21}$                                       | 2,097,152              | 73               | _, _, 0, _1, 1_0, .20, 0010, 10020, 002000,                                                                                              | $\text{FI}[A \land B] = \text{FI}[A] \cdot \text{FI}[B],$ iff A and B are independent.             |
| $\frac{21}{22}$                                       | 4,194,304              | 79               | $n! = \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \left(1 + \Theta\left(\frac{1}{n}\right)\right).$                                         | _                                                                                                  |
| 23                                                    | 8,388,608              | 83               |                                                                                                                                          | $\Pr[A B] = \frac{\Pr[A \land B]}{\Pr[B]}$                                                         |
| 24                                                    | 16,777,216             | 89               | Ackermann's function and inverse: $(2i) \qquad i=1$                                                                                      | For random variables $X$ and $Y$ :                                                                 |
| 25                                                    | 33,554,432             | 97               | $a(i,j) = \begin{cases} 2^j & i = 1\\ a(i-1,2) & j = 1\\ a(i-1,a(i,j-1)) & i,j \ge 2 \end{cases}$                                        | $\mathbf{E}[X \cdot Y] = \mathbf{E}[X] \cdot \mathbf{E}[Y],$                                       |
| 26                                                    | 67,108,864             | 101              | $\left(\begin{array}{cc} a(i-1,a(i,j-1)) & i,j \geq 2 \end{array}\right)$                                                                | if $X$ and $Y$ are independent.                                                                    |
| 27                                                    | 134,217,728            | 103              | $\alpha(i) = \min\{j \mid a(j,j) \ge i\}.$                                                                                               | E[X+Y] = E[X] + E[Y],                                                                              |
| 28                                                    | 268,435,456            | 107              | Binomial distribution:                                                                                                                   | $\mathbf{E}[cX] = c  \mathbf{E}[X].$                                                               |
| 29                                                    | 536,870,912            | 109              | $\Pr[X=k] = \binom{n}{k} p^k q^{n-k}, \qquad q = 1 - p,$                                                                                 | Bayes' theorem:                                                                                    |
| 30                                                    | 1,073,741,824          | 113              | $\prod_{i \in A} = \kappa_i = \binom{k}{p} q \qquad , \qquad q = 1 - p,$                                                                 | $\Pr[A_i B] = \frac{\Pr[B A_i]\Pr[A_i]}{\sum_{i=1}^n \Pr[A_j]\Pr[B A_j]}.$                         |
| 31                                                    | 2,147,483,648          | 127              | $E[X] = \sum_{k=1}^{n} k \binom{n}{k} p^k q^{n-k} = np.$                                                                                 | 3                                                                                                  |
| 32                                                    | 4,294,967,296          | 131              | $E[N] = \sum_{k=1}^{n} {\binom{k}{p}}^{q} \qquad = np.$                                                                                  | Inclusion-exclusion:                                                                               |
|                                                       | Pascal's Triangl       | e                | Poisson distribution:                                                                                                                    | $\Pr\left[\bigvee_{i=1} X_i\right] = \sum_{i=1} \Pr[X_i] +$                                        |
|                                                       | 1                      |                  | $\Pr[X = k] = \frac{e^{-\lambda} \lambda^k}{k!},  \operatorname{E}[X] = \lambda.$                                                        | t=1 $t=1$                                                                                          |
| 1 1                                                   |                        |                  | k! Normal (Gaussian) distribution:                                                                                                       | $\sum_{k=2}^{n} (-1)^{k+1} \sum_{i_i < \dots < i_k} \Pr\left[\bigwedge_{j=1}^k X_{i_j}\right].$    |
| 1 2 1                                                 |                        |                  | 1                                                                                                                                        |                                                                                                    |
| 1 3 3 1                                               |                        |                  | $p(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/2\sigma^2},  E[X] = \mu.$                                                              | Moment inequalities:                                                                               |
| 1 4 6 4 1                                             |                        |                  | The "coupon collector": We are given a                                                                                                   | $\Pr\left[ X  \ge \lambda \operatorname{E}[X]\right] \le \frac{1}{\lambda},$                       |
| 1 5 10 10 5 1                                         |                        |                  | random coupon each day, and there are $n$ different types of coupons. The distribu-                                                      | $\Pr\left[\left X - \mathrm{E}[X]\right  \ge \lambda \cdot \sigma\right] \le \frac{1}{\lambda^2}.$ |
| 1 6 15 20 15 6 1                                      |                        |                  | tion of coupons is uniform. The expected                                                                                                 |                                                                                                    |
|                                                       |                        | 1                | number of days to pass before we to col-                                                                                                 | Geometric distribution: $Pr[Y = k] = ma^{k-1} \qquad a = 1  m$                                     |
|                                                       |                        | 8 1              | lect all $n$ types is                                                                                                                    | $\Pr[X = k] = pq^{k-1}, \qquad q = 1 - p,$                                                         |
| 1 9 36 84 126 126 84 36 9 1                           |                        |                  | $nH_n$ .                                                                                                                                 | $E[X] = \sum_{k=1}^{\infty} kpq^{k-1} = \frac{1}{p}.$                                              |
| 1 10 45 120 210 252 210 120 45 10 1                   |                        |                  |                                                                                                                                          | $\overline{k=1}$ $p$                                                                               |

#### Trigonometry

![](_page_3_Picture_2.jpeg)

Pythagorean theorem:  $C^2 = A^2 + B^2$ .

$$C^2 = A^2 + B^2$$

Definitions:

$$\sin a = A/C, \quad \cos a = B/C,$$

$$\csc a = C/A, \quad \sec a = C/B,$$

$$\tan a = \frac{\sin a}{\cos a} = \frac{A}{B}, \quad \cot a = \frac{\cos a}{\sin a} = \frac{B}{A}.$$

Area, radius of inscribed circle:

$$\frac{1}{2}AB$$
,  $\frac{AB}{A+B+C}$ 

Identities:  

$$\sin x = \frac{1}{\csc x}, \qquad \cos x = \frac{1}{\sec x},$$

$$\tan x = \frac{1}{\cot x}, \qquad \sin^2 x + \cos^2 x = 1,$$

$$1 + \tan^2 x = \sec^2 x, \qquad 1 + \cot^2 x = \csc^2 x,$$

$$\sin x = \cos\left(\frac{\pi}{2} - x\right), \qquad \sin x = \sin(\pi - x),$$

$$\cos x = -\cos(\pi - x), \qquad \tan x = \cot\left(\frac{\pi}{2} - x\right),$$

$$\cot x = -\cot(\pi - x), \qquad \csc x = \cot\frac{x}{2} - \cot x,$$

$$\sin(x \pm y) = \sin x \cos y \pm \cos x \sin y,$$

$$\cos(x \pm y) = \cos x \cos y \mp \sin x \sin y,$$

$$\tan(x \pm y) = \frac{\tan x \pm \tan y}{1 \mp \tan x \tan y},$$

$$\cot(x \pm y) = \frac{\cot x \cot y \mp 1}{\cot x \pm \cot y},$$

$$\sin 2x = 2\sin x \cos x, \qquad \sin 2x = \frac{2\tan x}{1 + \tan^2 x},$$

$$\cos^2 x = \cos^2 x - \sin^2 x = \cos^2 x - 2\cos^2 x - 1$$

$$\cos 2x = \cos^2 x - \sin^2 x$$
,  $\cos 2x = 2\cos^2 x - 1$ ,

$$\cos 2x = 1 - 2\sin^2 x,$$
  $\cos 2x = \frac{1 - \tan^2 x}{1 + \tan^2 x},$ 

$$\tan 2x = \frac{2\tan x}{1 - \tan^2 x},$$
  $\cot 2x = \frac{\cot^2 x - 1}{2\cot x}$ 

$$\sin(x+y)\sin(x-y) = \sin^2 x - \sin^2 y$$

$$\cos(x+y)\cos(x-y) = \cos^2 x - \sin^2 y.$$

Euler's equation:

$$e^{ix} = \cos x + i\sin x, \qquad e^{i\pi} = -1.$$

v2.02 ©1994 by Steve Seiden sseiden@acm.org http://www.csc.lsu.edu/~seiden

## Matrices

Multiplication:

$$C = A \cdot B, \quad c_{i,j} = \sum_{k=1}^{n} a_{i,k} b_{k,j}.$$

Determinants: det  $A \neq 0$  iff A is non-singular.

$$\det A \cdot B = \det A \cdot \det B,$$

$$\det A = \sum_{\pi} \prod_{i=1}^{n} \operatorname{sign}(\pi) a_{i,\pi(i)}.$$

 $2\times 2$  and  $3\times 3$  determinant:

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc,$$

$$\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = g \begin{vmatrix} b & c \\ e & f \end{vmatrix} - h \begin{vmatrix} a & c \\ d & f \end{vmatrix} + i \begin{vmatrix} a & b \\ d & e \end{vmatrix}$$
$$aei + bfg + cdh$$

Permanents:

$$\operatorname{perm} A = \sum_{\pi} \prod_{i=1}^{n} a_{i,\pi(i)}.$$

# Hyperbolic Functions

## Definitions:

$$\sinh x = \frac{e^x - e^{-x}}{2}, \qquad \cosh x = \frac{e^x + e^{-x}}{2},$$

$$\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}}, \qquad \operatorname{csch} x = \frac{1}{\sinh x},$$

$$\operatorname{sech} x = \frac{1}{\cosh x}, \qquad \coth x = \frac{1}{\tanh x}.$$

## Identities:

 $\cosh^2 x - \sinh^2 x = 1, \qquad \tanh^2 x + \operatorname{sech}^2 x = 1,$  $\coth^2 x - \operatorname{csch}^2 x = 1,$  $\sinh(-x) = -\sinh x,$  $\cosh(-x) = \cosh x$  $\tanh(-x) = -\tanh x,$  $\sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y,$  $\cosh(x+y) = \cosh x \cosh y + \sinh x \sinh y,$  $\sinh 2x = 2 \sinh x \cosh x$ ,  $\cosh 2x = \cosh^2 x + \sinh^2 x,$ 

| $\cos x + \sin x = e^{-x},$          | $\cos n x - \sin n$                       | $x = e^{-x}$         |
|--------------------------------------|-------------------------------------------|----------------------|
| $(\cosh x + \sinh x)^n = \cosh$      | $nx + \sinh nx$                           | $n \in \mathbb{Z}$ , |
| $2\sinh^2\frac{x}{2} = \cosh x - 1,$ | $2\cosh^2\frac{x}{2} = \cos^2\frac{x}{2}$ | $\cosh x + 1.$       |

| $\theta$                        | $\sin \theta$        | $\cos \theta$        | $\tan \theta$        |
|---------------------------------|----------------------|----------------------|----------------------|
| 0                               | 0                    | 1                    | 0                    |
| $\frac{\pi}{6}$                 | $\frac{1}{2}$        | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $\frac{\pi}{4}$                 | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | 1                    |
| $\frac{\pi}{3}$ $\frac{\pi}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$        | $\sqrt{3}$           |
| $\frac{\pi}{2}$                 | 1                    | 0                    | $\infty$             |

... in mathematics you don't understand things, you just get used to them. – J. von Neumann

## More Trig.

![](_page_3_Picture_38.jpeg)

Law of cosines:

$$c^2 = a^2 + b^2 - 2ab\cos C$$

$$A = \frac{1}{2}hc,$$

$$= \frac{1}{2}ab\sin C,$$

$$= \frac{c^2\sin A\sin B}{2\sin C}.$$

$$A = \sqrt{s \cdot s_a \cdot s_b \cdot s_c},$$

$$s = \frac{1}{2}(a+b+c),$$

$$s_a = s-a,$$

$$s_b = s-b,$$

$$s_c = s-c.$$

More identities

whose identities:  

$$\sin \frac{x}{2} = \sqrt{\frac{1 - \cos x}{2}},$$

$$\cos \frac{x}{2} = \sqrt{\frac{1 + \cos x}{2}},$$

$$\tan \frac{x}{2} = \sqrt{\frac{1 - \cos x}{1 + \cos x}},$$

$$= \frac{1 - \cos x}{\sin x},$$

$$= \frac{1 + \cos x}{1 + \cos x},$$

$$\cot \frac{x}{2} = \sqrt{\frac{1 + \cos x}{1 - \cos x}}$$

$$= \frac{1 + \cos x}{\sin x},$$
$$= \frac{\sin x}{1 - \cos x},$$

$$\sin x = \frac{e^{ix} - e^{-ix}}{2i},$$

$$\cos x = \frac{e^{ix} + e^{-ix}}{2},$$

$$\tan x = -i\frac{e^{ix} - e^{-ix}}{e^{ix} + e^{-ix}}$$

$$=-i\frac{e^{2ix}-1}{e^{2ix}+1},$$

$$\sin x = \frac{\sinh ix}{i},$$

$$\cos x = \cosh ix$$

$$\tan x = \frac{\tanh ix}{i}.$$

#### Theoretical Computer Science Cheat Sheet Graph Theory Number Theory The Chinese remainder theorem: There ex-Definitions: ists a number C such that: LoopAn edge connecting a vertex to itself. $C \equiv r_1 \mod m_1$ DirectedEach edge has a direction. SimpleGraph with no loops or : : : multi-edges. $C \equiv r_n \bmod m_n$ WalkA sequence $v_0e_1v_1\ldots e_\ell v_\ell$ . TrailA walk with distinct edges. if $m_i$ and $m_j$ are relatively prime for $i \neq j$ . Path $\operatorname{trail}$ with distinct Euler's function: $\phi(x)$ is the number of vertices. positive integers less than x relatively Connectedprime to x. If $\prod_{i=1}^{n} p_i^{e_i}$ is the prime fac-A graph where there exists a path between any two torization of x then vertices. $\phi(x) = \prod_{i=1} p_i^{e_i - 1} (p_i - 1).$ Componentmaximal connected subgraph. Euler's theorem: If a and b are relatively TreeA connected acyclic graph. prime then Free tree A tree with no root. $1 \equiv a^{\phi(b)} \bmod b$ . DAGDirected acyclic graph. EulerianGraph with a trail visiting Fermat's theorem: each edge exactly once. $1 \equiv a^{p-1} \bmod p$ . Hamiltonian Graph with a cycle visiting The Euclidean algorithm: if a > b are ineach vertex exactly once. tegers then CutA set of edges whose re $gcd(a, b) = gcd(a \mod b, b).$ moval increases the number of components. If $\prod_{i=1}^{n} p_i^{e_i}$ is the prime factorization of xCut-setA minimal cut. Cut edge A size 1 cut. $S(x) = \sum_{i=1}^{n} d = \prod_{i=1}^{n} \frac{p_i^{e_i+1} - 1}{p_i - 1}.$ k-Connected A graph connected with the removal of any k-1vertices. Perfect Numbers: x is an even perfect num- $\forall S \subseteq V, S \neq \emptyset$ we have *k-Tough* ber iff $x = 2^{n-1}(2^n-1)$ and $2^n-1$ is prime. $k \cdot c(G - S) < |S|$ . Wilson's theorem: n is a prime iff k-Regular A graph where all vertices $(n-1)! \equiv -1 \mod n$ . have degree k. Möbius inversion: k-Factor Α k-regular spanning $\mu(i) = \begin{cases} 1 & \text{if } i = 1. \\ 0 & \text{if } i \text{ is not square-free.} \\ (-1)^r & \text{if } i \text{ is the product of} \\ r & \text{distinct primes.} \end{cases}$ subgraph. A set of edges, no two of Matching which are adjacent. CliqueA set of vertices, all of which are adjacent. $G(a) = \sum_{d \mid a} F(d),$ Ind. set A set of vertices, none of which are adjacent. then Vertex cover A set of vertices which $F(a) = \sum_{d} \mu(d) G\left(\frac{a}{d}\right).$ cover all edges. Planar graph A graph which can be embeded in the plane. Prime numbers: $p_n = n \ln n + n \ln \ln n - n + n \frac{\ln \ln n}{\ln n}$ Plane graph An embedding of a planar graph.

 $+O\left(\frac{n}{\ln n}\right)$ 

 $\pi(n) = \frac{n}{\ln n} + \frac{n}{(\ln n)^2} + \frac{2!n}{(\ln n)^3}$ 

 $+O\left(\frac{n}{(\ln n)^4}\right).$ 

| $\sum de$ | g(v) | = | 2m. |
|-----------|------|---|-----|
| $v \in V$ |      |   |     |

If G is planar then n-m+f=2, so

$$f \le 2n - 4, \quad m \le 3n - 6.$$

Any planar graph has a vertex with degree < 5.

| Notation:      |                          |  |
|----------------|--------------------------|--|
| E(G)           | Edge set                 |  |
| V(G)           | Vertex set               |  |
| c(G)           | Number of components     |  |
| G[S]           | Induced subgraph         |  |
| deg(v)         | Degree of $v$            |  |
| $\Delta(G)$    | Maximum degree           |  |
| $\delta(G)$    | Minimum degree           |  |
| $\chi(G)$      | Chromatic number         |  |
| $\chi_E(G)$    | Edge chromatic number    |  |
| $G^c$          | Complement graph         |  |
| $K_n$          | Complete graph           |  |
| $K_{n_1, n_2}$ | Complete bipartite graph |  |
| $r(k,\ell)$    | Ramsey number            |  |

#### Geometry

Projective coordinates: triples (x, y, z), not all x, y and z zero.

$$(x,y,z) = (cx,cy,cz) \quad \forall c \neq 0.$$

Cartesian

Distance formula,  $L_p$  and  $L_{\infty}$ 

$$\sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2},$$

$$\left[ |x_1 - x_0|^p + |y_1 - y_0|^p \right]^{1/p},$$

$$\lim_{n \to \infty} \left[ |x_1 - x_0|^p + |y_1 - y_0|^p \right]^{1/p}.$$

Area of triangle  $(x_0, y_0), (x_1, y_1)$ 

$$\frac{1}{2} \operatorname{abs} \begin{vmatrix} x_1 - x_0 & y_1 - y_0 \\ x_2 - x_0 & y_2 - y_0 \end{vmatrix}.$$

Angle formed by three points:

![](_page_4_Figure_15.jpeg)

Line through two points  $(x_0, y_0)$ and  $(x_1, y_1)$ :

$$\begin{vmatrix} x & y & 1 \\ x_0 & y_0 & 1 \\ x_1 & y_1 & 1 \end{vmatrix} = 0.$$

Area of circle, volume of sphere:

$$A = \pi r^2, \qquad V = \frac{4}{3}\pi r^3.$$

If I have seen farther than others, it is because I have stood on the shoulders of giants.

- Issac Newton

Wallis' identity:

$$\pi = 2 \cdot \frac{2 \cdot 2 \cdot 4 \cdot 4 \cdot 6 \cdot 6 \cdots}{1 \cdot 3 \cdot 3 \cdot 5 \cdot 5 \cdot 7 \cdots}$$

Brouncker's continued fraction expansion:

$$\frac{\pi}{4} = 1 + \frac{1^2}{2 + \frac{3^2}{2 + \frac{5^2}{2 + \frac{7^2}{2}}}}$$

Gregory's series: 
$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots$$

Newton's series:

$$\frac{\pi}{6} = \frac{1}{2} + \frac{1}{2 \cdot 3 \cdot 2^3} + \frac{1 \cdot 3}{2 \cdot 4 \cdot 5 \cdot 2^5} + \cdots$$

$$\frac{\pi}{6} = \frac{1}{\sqrt{3}} \left( 1 - \frac{1}{3^1 \cdot 3} + \frac{1}{3^2 \cdot 5} - \frac{1}{3^3 \cdot 7} + \cdots \right)$$

Euler's series:

$$\frac{\pi^2}{6} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \frac{1}{5^2} + \cdots$$

$$\frac{\pi^2}{8} = \frac{1}{1^2} + \frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} + \frac{1}{9^2} + \cdots$$

$$\frac{\pi^2}{12} = \frac{1}{1^2} - \frac{1}{2^2} + \frac{1}{3^2} - \frac{1}{4^2} + \frac{1}{5^2} - \cdots$$

#### Partial Fractions

Let N(x) and D(x) be polynomial functions of x. We can break down N(x)/D(x) using partial fraction expansion. First, if the degree of N is greater than or equal to the degree of D, divide N by D, obtaining

$$\frac{N(x)}{D(x)} = Q(x) + \frac{N'(x)}{D(x)},$$

where the degree of N' is less than that of D. Second, factor D(x). Use the following rules: For a non-repeated factor:

$$\frac{N(x)}{(x-a)D(x)} = \frac{A}{x-a} + \frac{N'(x)}{D(x)},$$

where

$$A = \left[\frac{N(x)}{D(x)}\right]_{x=a}.$$

For a repeated factor:

$$\frac{N(x)}{(x-a)^m D(x)} = \sum_{k=0}^{m-1} \frac{A_k}{(x-a)^{m-k}} + \frac{N'(x)}{D(x)},$$

$$A_k = \frac{1}{k!} \left[ \frac{d^k}{dx^k} \left( \frac{N(x)}{D(x)} \right) \right]_{x=a}.$$

The reasonable man adapts himself to the world: the unreasonable persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable. - George Bernard Shaw

Derivatives:

1. 
$$\frac{d(cu)}{dx} = c\frac{du}{dx}$$
,

$$2. \ \frac{d(u+v)}{dx} = \frac{du}{dx} + \frac{dv}{dx}$$

1. 
$$\frac{d(cu)}{dx} = c\frac{du}{dx}$$
, 2.  $\frac{d(u+v)}{dx} = \frac{du}{dx} + \frac{dv}{dx}$ , 3.  $\frac{d(uv)}{dx} = u\frac{dv}{dx} + v\frac{du}{dx}$ 

$$\mathbf{4.} \ \frac{d(u^n)}{dx} = nu^{n-1}\frac{du}{dx},$$

**4.** 
$$\frac{d(u^n)}{dx} = nu^{n-1}\frac{du}{dx}, \quad \textbf{5.} \quad \frac{d(u/v)}{dx} = \frac{v\left(\frac{du}{dx}\right) - u\left(\frac{dv}{dx}\right)}{v^2}, \quad \textbf{6.} \quad \frac{d(e^{cu})}{dx} = ce^{cu}\frac{du}{dx}$$

Calculus

$$6. \ \frac{d(e^{cu})}{dx} = ce^{cu}\frac{du}{dx}$$

7. 
$$\frac{d(c^u)}{dx} = (\ln c)c^u \frac{du}{dx},$$

$$8. \ \frac{d(\ln u)}{dx} = \frac{1}{u} \frac{du}{dx},$$

9. 
$$\frac{d(\sin u)}{dx} = \cos u \frac{du}{dx},$$

$$\mathbf{10.} \ \frac{d(\cos u)}{dx} = -\sin u \frac{du}{dx},$$

11. 
$$\frac{d(\tan u)}{dx} = \sec^2 u \frac{du}{dx}$$

$$12. \ \frac{d(\cot u)}{dx} = \csc^2 u \frac{du}{dx},$$

13. 
$$\frac{d(\sec u)}{dx} = \tan u \sec u \frac{du}{dx}$$
,

14. 
$$\frac{d(\csc u)}{dx} = -\cot u \csc u \frac{du}{dx}$$

15. 
$$\frac{d(\arcsin u)}{dx} = \frac{1}{\sqrt{1-u^2}} \frac{du}{dx}$$

**16.** 
$$\frac{d(\arccos u)}{dx} = \frac{-1}{\sqrt{1-u^2}} \frac{du}{dx}$$

17. 
$$\frac{d(\arctan u)}{dx} = \frac{1}{1+u^2} \frac{du}{dx}$$

18. 
$$\frac{d(\operatorname{arccot} u)}{dx} = \frac{-1}{1 + u^2} \frac{du}{dx},$$

19. 
$$\frac{d(\operatorname{arcsec} u)}{dx} = \frac{1}{u\sqrt{1-u^2}} \frac{du}{dx}$$

**20.** 
$$\frac{d(\arccos u)}{dx} = \frac{-1}{u\sqrt{1-u^2}} \frac{du}{dx}$$

$$21. \ \frac{d(\sinh u)}{dx} = \cosh u \frac{du}{dx},$$

22. 
$$\frac{d(\cosh u)}{dx} = \sinh u \frac{du}{dx}$$

23. 
$$\frac{d(\tanh u)}{dx} = \operatorname{sech}^2 u \frac{du}{dx}$$

$$24. \frac{d(\coth u)}{dx} = -\operatorname{csch}^2 u \frac{du}{dx},$$

**25.** 
$$\frac{d(\operatorname{sech} u)}{dx} = -\operatorname{sech} u \tanh u \frac{du}{dx},$$

**26.** 
$$\frac{d(\operatorname{csch} u)}{dx} = -\operatorname{csch} u \operatorname{coth} u \frac{du}{dx}$$

27. 
$$\frac{d(\operatorname{arcsinh} u)}{dx} = \frac{1}{\sqrt{1+u^2}} \frac{du}{dx},$$

28. 
$$\frac{d(\operatorname{arccosh} u)}{dx} = \frac{1}{\sqrt{u^2 - 1}} \frac{du}{dx}$$

29. 
$$\frac{d(\operatorname{arctanh} u)}{dx} = \frac{1}{1 - u^2} \frac{du}{dx}$$

30. 
$$\frac{d(\operatorname{arccoth} u)}{dx} = \frac{1}{u^2 - 1} \frac{du}{dx}$$

31. 
$$\frac{d(\operatorname{arcsech} u)}{dx} = \frac{-1}{u\sqrt{1-u^2}}\frac{du}{dx}$$

32. 
$$\frac{d(\operatorname{arccsch} u)}{dx} = \frac{-1}{|u|\sqrt{1+u^2}} \frac{du}{dx}.$$

Integrals:

1. 
$$\int cu \, dx = c \int u \, dx,$$

$$\int 1 dx dx = 5$$

$$2. \int (u+v) dx = \int u dx + \int v dx,$$

$$3. \int x^n \, dx = \frac{1}{n+1} x^{n-1}$$

**3.** 
$$\int x^n dx = \frac{1}{n+1} x^{n+1}, \quad n \neq -1, \qquad$$
**4.**  $\int \frac{1}{x} dx = \ln x, \qquad$ **5.**  $\int e^x dx = e^x,$ 

$$\mathbf{5.} \int e^x \, dx = e^x,$$

$$\mathbf{6.} \int \frac{dx}{1+x^2} = \arctan x,$$

7. 
$$\int u \frac{dv}{dx} dx = uv - \int v \frac{du}{dx} dx,$$

$$8. \int \sin x \, dx = -\cos x,$$

$$9. \int \cos x \, dx = \sin x,$$

$$\mathbf{10.} \int \tan x \, dx = -\ln|\cos x|,$$

$$\mathbf{11.} \int \cot x \, dx = \ln|\cos x|,$$

12. 
$$\int \sec x \, dx = \ln|\sec x + \tan x|,$$

13. 
$$\int \csc x \, dx = \ln|\csc x + \cot x|,$$

14. 
$$\int \arcsin \frac{x}{a} dx = \arcsin \frac{x}{a} + \sqrt{a^2 - x^2}, \quad a > 0,$$

Calculus Cont.

15. 
$$\int \arccos \frac{x}{a} dx = \arccos \frac{x}{a} - \sqrt{a^2 - x^2}, \quad a > 0,$$

**16.** 
$$\int \arctan \frac{x}{a} dx = x \arctan \frac{x}{a} - \frac{a}{2} \ln(a^2 + x^2), \quad a > 0,$$

17. 
$$\int \sin^2(ax) dx = \frac{1}{2a} (ax - \sin(ax)\cos(ax)),$$

**18.** 
$$\int \cos^2(ax)dx = \frac{1}{2a} (ax + \sin(ax)\cos(ax)),$$

$$19. \int \sec^2 x \, dx = \tan x,$$

$$20. \int \csc^2 x \, dx = -\cot x,$$

**21.** 
$$\int \sin^n x \, dx = -\frac{\sin^{n-1} x \cos x}{n} + \frac{n-1}{n} \int \sin^{n-2} x \, dx,$$

**22.** 
$$\int \cos^n x \, dx = \frac{\cos^{n-1} x \sin x}{n} + \frac{n-1}{n} \int \cos^{n-2} x \, dx,$$

**23.** 
$$\int \tan^n x \, dx = \frac{\tan^{n-1} x}{n-1} - \int \tan^{n-2} x \, dx, \quad n \neq 1,$$

**24.** 
$$\int \cot^n x \, dx = -\frac{\cot^{n-1} x}{n-1} - \int \cot^{n-2} x \, dx, \quad n \neq 1,$$

**25.** 
$$\int \sec^n x \, dx = \frac{\tan x \sec^{n-1} x}{n-1} + \frac{n-2}{n-1} \int \sec^{n-2} x \, dx, \quad n \neq 1,$$

**26.** 
$$\int \csc^n x \, dx = -\frac{\cot x \csc^{n-1} x}{n-1} + \frac{n-2}{n-1} \int \csc^{n-2} x \, dx, \quad n \neq 1, \quad$$
**27.**  $\int \sinh x \, dx = \cosh x, \quad$ **28.**  $\int \cosh x \, dx = \sinh x,$ 

**29.** 
$$\int \tanh x \, dx = \ln|\cosh x|, \ \mathbf{30.} \ \int \coth x \, dx = \ln|\sinh x|, \ \mathbf{31.} \ \int \operatorname{sech} x \, dx = \arctan \sinh x, \ \mathbf{32.} \ \int \operatorname{csch} x \, dx = \ln\left|\tanh \frac{x}{2}\right|,$$

**33.** 
$$\int \sinh^2 x \, dx = \frac{1}{4} \sinh(2x) - \frac{1}{2}x,$$
 **34.**  $\int \cosh^2 x \, dx = \frac{1}{4} \sinh(2x) + \frac{1}{2}x,$ 

**34.** 
$$\int \cosh^2 x \, dx = \frac{1}{4} \sinh(2x) + \frac{1}{2}x,$$

**35.** 
$$\int \operatorname{sech}^2 x \, dx = \tanh x,$$

**36.** 
$$\int \operatorname{arcsinh} \frac{x}{a} dx = x \operatorname{arcsinh} \frac{x}{a} - \sqrt{x^2 + a^2}, \quad a > 0,$$

37. 
$$\int \operatorname{arctanh} \frac{x}{a} dx = x \operatorname{arctanh} \frac{x}{a} + \frac{a}{2} \ln |a^2 - x^2|,$$

**38.** 
$$\int \operatorname{arccosh} \frac{x}{a} dx = \begin{cases} x \operatorname{arccosh} \frac{x}{a} - \sqrt{x^2 + a^2}, & \text{if } \operatorname{arccosh} \frac{x}{a} > 0 \text{ and } a > 0, \\ x \operatorname{arccosh} \frac{x}{a} + \sqrt{x^2 + a^2}, & \text{if } \operatorname{arccosh} \frac{x}{a} < 0 \text{ and } a > 0, \end{cases}$$

**39.** 
$$\int \frac{dx}{\sqrt{a^2 + x^2}} = \ln\left(x + \sqrt{a^2 + x^2}\right), \quad a > 0,$$

**40.** 
$$\int \frac{dx}{a^2 + x^2} = \frac{1}{a} \arctan \frac{x}{a}, \quad a > 0,$$

**41.** 
$$\int \sqrt{a^2 - x^2} \, dx = \frac{x}{2} \sqrt{a^2 - x^2} + \frac{a^2}{2} \arcsin \frac{x}{a}, \quad a > 0,$$

**42.** 
$$\int (a^2 - x^2)^{3/2} dx = \frac{x}{8} (5a^2 - 2x^2) \sqrt{a^2 - x^2} + \frac{3a^4}{8} \arcsin \frac{x}{a}, \quad a > 0,$$

**43.** 
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin \frac{x}{a}, \quad a > 0,$$
 **44.** 
$$\int \frac{dx}{a^2 - x^2} = \frac{1}{2a} \ln \left| \frac{a + x}{a - x} \right|,$$
 **45.** 
$$\int \frac{dx}{(a^2 - x^2)^{3/2}} = \frac{x}{a^2 \sqrt{a^2 - x^2}},$$

44. 
$$\int \frac{dx}{a^2 - x^2} = \frac{1}{2a} \ln \left| \frac{a+x}{a-x} \right|,$$

**45.** 
$$\int \frac{ax}{(a^2 - x^2)^{3/2}} = \frac{x}{a^2 \sqrt{a^2 - x^2}},$$

**46.** 
$$\int \sqrt{a^2 \pm x^2} \, dx = \frac{x}{2} \sqrt{a^2 \pm x^2} \pm \frac{a^2}{2} \ln \left| x + \sqrt{a^2 \pm x^2} \right|,$$

**47.** 
$$\int \frac{dx}{\sqrt{x^2 - a^2}} = \ln \left| x + \sqrt{x^2 - a^2} \right|, \quad a > 0,$$

48. 
$$\int \frac{dx}{ax^2 + bx} = \frac{1}{a} \ln \left| \frac{x}{a + bx} \right|,$$

**49.** 
$$\int x\sqrt{a+bx} \, dx = \frac{2(3bx-2a)(a+bx)^{3/2}}{15b^2},$$

**50.** 
$$\int \frac{\sqrt{a+bx}}{x} dx = 2\sqrt{a+bx} + a \int \frac{1}{x\sqrt{a+bx}} dx,$$

51. 
$$\int \frac{x}{\sqrt{a+bx}} dx = \frac{1}{\sqrt{2}} \ln \left| \frac{\sqrt{a+bx} - \sqrt{a}}{\sqrt{a+bx} + \sqrt{a}} \right|, \quad a > 0,$$

**52.** 
$$\int \frac{\sqrt{a^2 - x^2}}{x} dx = \sqrt{a^2 - x^2} - a \ln \left| \frac{a + \sqrt{a^2 - x^2}}{x} \right|,$$

**53.** 
$$\int x\sqrt{a^2 - x^2} \, dx = -\frac{1}{3}(a^2 - x^2)^{3/2},$$

**54.** 
$$\int x^2 \sqrt{a^2 - x^2} \, dx = \frac{x}{8} (2x^2 - a^2) \sqrt{a^2 - x^2} + \frac{a^4}{8} \arcsin \frac{x}{a}, \quad a > 0,$$

**55.** 
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = -\frac{1}{a} \ln \left| \frac{a + \sqrt{a^2 - x^2}}{x} \right|,$$

**56.** 
$$\int \frac{x \, dx}{\sqrt{a^2 - x^2}} = -\sqrt{a^2 - x^2},$$

57. 
$$\int \frac{x^2 dx}{\sqrt{a^2 - x^2}} = -\frac{x}{2} \sqrt{a^2 - x^2} + \frac{a^2}{2} \arcsin \frac{x}{a}, \quad a > 0,$$

**58.** 
$$\int \frac{\sqrt{a^2 + x^2}}{x} dx = \sqrt{a^2 + x^2} - a \ln \left| \frac{a + \sqrt{a^2 + x^2}}{x} \right|,$$

**59.** 
$$\int \frac{\sqrt{x^2 - a^2}}{x} dx = \sqrt{x^2 - a^2} - a \arccos \frac{a}{|x|}, \quad a > 0,$$

**60.** 
$$\int x\sqrt{x^2 \pm a^2} \, dx = \frac{1}{3}(x^2 \pm a^2)^{3/2},$$

**61.** 
$$\int \frac{dx}{x\sqrt{x^2 + a^2}} = \frac{1}{a} \ln \left| \frac{x}{a + \sqrt{a^2 + x^2}} \right|,$$

Calculus Cont.

**62.** 
$$\int \frac{dx}{x\sqrt{x^2 - a^2}} = \frac{1}{a} \arccos \frac{a}{|x|}, \quad a > 0, \qquad 63. \int \frac{dx}{x^2\sqrt{x^2 \pm a^2}} = \mp \frac{\sqrt{x^2 \pm a^2}}{a^2 x},$$

**63.** 
$$\int \frac{dx}{x^2 \sqrt{x^2 \pm a^2}} = \mp \frac{\sqrt{x^2 \pm a^2}}{a^2 x},$$

**64.** 
$$\int \frac{x \, dx}{\sqrt{x^2 \pm a^2}} = \sqrt{x^2 \pm a^2},$$

**65.** 
$$\int \frac{\sqrt{x^2 \pm a^2}}{x^4} dx = \mp \frac{(x^2 + a^2)^{3/2}}{3a^2 x^3},$$

**66.** 
$$\int \frac{dx}{ax^2 + bx + c} = \begin{cases} \frac{1}{\sqrt{b^2 - 4ac}} \ln \left| \frac{2ax + b - \sqrt{b^2 - 4ac}}{2ax + b + \sqrt{b^2 - 4ac}} \right|, & \text{if } b^2 > 4ac, \\ \frac{2}{\sqrt{4ac - b^2}} \arctan \frac{2ax + b}{\sqrt{4ac - b^2}}, & \text{if } b^2 < 4ac, \end{cases}$$

**67.** 
$$\int \frac{dx}{\sqrt{ax^2 + bx + c}} = \begin{cases} \frac{1}{\sqrt{a}} \ln \left| 2ax + b + 2\sqrt{a}\sqrt{ax^2 + bx + c} \right|, & \text{if } a > 0, \\ \frac{1}{\sqrt{-a}} \arcsin \frac{-2ax - b}{\sqrt{b^2 - 4ac}}, & \text{if } a < 0, \end{cases}$$

**68.** 
$$\int \sqrt{ax^2 + bx + c} \, dx = \frac{2ax + b}{4a} \sqrt{ax^2 + bx + c} + \frac{4ax - b^2}{8a} \int \frac{dx}{\sqrt{ax^2 + bx + c}},$$

70. 
$$\int \frac{dx}{x\sqrt{ax^2 + bx + c}} = \begin{cases} \frac{-1}{\sqrt{c}} \ln \left| \frac{2\sqrt{c}\sqrt{ax^2 + bx + c} + bx + 2c}{x} \right|, & \text{if } c > 0, \\ \frac{1}{\sqrt{-c}} \arcsin \frac{bx + 2c}{|x|\sqrt{b^2 - 4ac}}, & \text{if } c < 0, \end{cases}$$

71. 
$$\int x^3 \sqrt{x^2 + a^2} \, dx = (\frac{1}{3}x^2 - \frac{2}{15}a^2)(x^2 + a^2)^{3/2},$$

**72.** 
$$\int x^n \sin(ax) \, dx = -\frac{1}{a} x^n \cos(ax) + \frac{n}{a} \int x^{n-1} \cos(ax) \, dx,$$

73. 
$$\int x^n \cos(ax) dx = \frac{1}{a} x^n \sin(ax) - \frac{n}{a} \int x^{n-1} \sin(ax) dx$$

**74.** 
$$\int x^n e^{ax} dx = \frac{x^n e^{ax}}{a} - \frac{n}{a} \int x^{n-1} e^{ax} dx,$$

**75.** 
$$\int x^n \ln(ax) \, dx = x^{n+1} \left( \frac{\ln(ax)}{n+1} - \frac{1}{(n+1)^2} \right),$$

**76.** 
$$\int x^n (\ln ax)^m \, dx = \frac{x^{n+1}}{n+1} (\ln ax)^m - \frac{m}{n+1} \int x^n (\ln ax)^{m-1} \, dx.$$

$$\begin{array}{cccccccccccccccccccccccccccccccccccc$$

Finite Calculus

Difference, shift operators:

$$\Delta f(x) = f(x+1) - f(x),$$
  
 
$$E f(x) = f(x+1).$$

Fundamental Theorem:

$$f(x) = \Delta F(x) \Leftrightarrow \sum f(x)\delta x = F(x) + C.$$
  
$$\sum_{i=0}^{b} f(x)\delta x = \sum_{i=0}^{b-1} f(i).$$

Differences:

$$\Delta(cu) = c\Delta u, \qquad \Delta(u+v) = \Delta u + \Delta v,$$

$$\Delta(uv) = u\Delta v + \mathbf{E}\,v\Delta u,$$

$$\Delta(x^{\underline{n}}) = nx^{\underline{n}-1},$$

$$\Delta(H_x) = x^{-1}, \qquad \qquad \Delta(2^x) = 2^x,$$

$$\Delta(c^x) = (c-1)c^x, \qquad \Delta\binom{x}{m} = \binom{x}{m-1}.$$

$$\sum cu\,\delta x = c\sum u\,\delta x,$$

$$\sum (u+v)\,\delta x = \sum u\,\delta x + \sum v\,\delta x,$$

$$\sum u \Delta v \, \delta x = uv - \sum E \, v \Delta u \, \delta x,$$

$$\sum x^{\underline{n}} \delta x = \frac{x^{\underline{n+1}}}{\underline{m+1}}, \qquad \sum x^{\underline{-1}} \delta x = H_x,$$

$$\sum c^x \, \delta x = \frac{c^x}{c-1}, \qquad \sum {x \choose m} \, \delta x = {x \choose m+1}.$$

Falling Factorial Powers:

$$x^{\underline{n}} = x(x-1)\cdots(x-n+1), \quad n > 0,$$

$$x^{0} = 1$$
.

$$x^{\underline{n}} = \frac{1}{(x+1)\cdots(x+|n|)}, \quad n < 0,$$

$$x^{\underline{n+m}} = x^{\underline{m}}(x-m)^{\underline{n}}.$$

Rising Factorial Powers:

$$x^{\overline{n}} = x(x+1)\cdots(x+n-1), \quad n > 0,$$

$$x^0 = 1,$$

$$x^{\overline{n}} = \frac{1}{(x-1)\cdots(x-|n|)}, \quad n < 0,$$

$$x^{\overline{n+m}} = x^{\overline{m}}(x+m)^{\overline{n}}.$$

Conversion:

$$x^{\underline{n}} = (-1)^n (-x)^{\overline{n}} = (x - n + 1)^{\overline{n}}$$

$$=1/(x+1)^{-n},$$

$$x^{\overline{n}} = (-1)^n (-x)^{\underline{n}} = (x+n-1)^{\underline{n}}$$

$$=1/(x-1)\frac{-n}{x}$$

$$x^{n} = \sum_{k=1}^{n} \begin{Bmatrix} n \\ k \end{Bmatrix} x^{\underline{k}} = \sum_{k=1}^{n} \begin{Bmatrix} n \\ k \end{Bmatrix} (-1)^{n-k} x^{\overline{k}},$$

$$x^{\underline{n}} = \sum_{k=1}^{n} \begin{bmatrix} n \\ k \end{bmatrix} (-1)^{n-k} x^k,$$

$$x^{\overline{n}} = \sum_{k=1}^{n} \begin{bmatrix} n \\ k \end{bmatrix} x^k.$$

Series

Taylor's series:

$$f(x) = f(a) + (x - a)f'(a) + \frac{(x - a)^2}{2}f''(a) + \dots = \sum_{i=0}^{\infty} \frac{(x - a)^i}{i!}f^{(i)}(a).$$

Expansions:

$$\begin{array}{cccccccccccccccccccccccccccccccccccc$$

Ordinary power series:

$$A(x) = \sum_{i=0}^{\infty} a_i x^i.$$

Exponential power series:

$$A(x) = \sum_{i=0}^{\infty} a_i \frac{x^i}{i!}.$$

Dirichlet power series:

$$A(x) = \sum_{i=1}^{\infty} \frac{a_i}{i^x}.$$

Binomial theorem

$$(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k.$$

Difference of like powers:

$$x^{n} - y^{n} = (x - y) \sum_{k=0}^{n-1} x^{n-1-k} y^{k}.$$

For ordinary power series:

$$\alpha A(x) + \beta B(x) = \sum_{i=0}^{\infty} (\alpha a_i + \beta b_i) x^i$$

$$x^k A(x) = \sum_{i=k}^{\infty} a_{i-k} x^i,$$

$$\frac{A(x) - \sum_{i=0}^{k-1} a_i x^i}{x^k} = \sum_{i=0}^{\infty} a_{i+k} x^i,$$

$$A(cx) = \sum_{i=0}^{\infty} c^i a_i x^i,$$
$$A'(x) = \sum_{i=0}^{\infty} (i+1)a_{i+1} x^i,$$

$$xA'(x) = \sum_{i=0}^{\infty} ia_i x^i,$$

$$\int A(x) \, dx = \sum_{i=1}^{\infty} \frac{a_{i-1}}{i} x^i,$$

$$\frac{A(x) + A(-x)}{2} = \sum_{i=0}^{\infty} a_{2i} x^{2i},$$

$$\frac{A(x) - A(-x)}{2} = \sum_{i=0}^{\infty} a_{2i+1} x^{2i+1}.$$

Summation: If  $b_i = \sum_{j=0}^i a_i$  then

$$B(x) = \frac{1}{1-x}A(x).$$

Convolution:

$$A(x)B(x) = \sum_{i=0}^{\infty} \left( \sum_{j=0}^{i} a_j b_{i-j} \right) x^i.$$

God made the natural numbers; all the rest is the work of man.

- Leopold Kronecker

Series Escher's Knot

Expansions:

$$\frac{1}{(1-x)^{n+1}} \ln \frac{1}{1-x} = \sum_{i=0}^{\infty} (H_{n+i} - H_n) \binom{n+i}{i} x^i,$$

$$x^{\overline{n}} = \sum_{i=0}^{\infty} \binom{n}{i} x^i,$$

$$\left(\ln \frac{1}{1-x}\right)^n = \sum_{i=0}^{\infty} \left[\frac{i}{n}\right] \frac{n! x^i}{i!},$$

$$\tan x = \sum_{i=1}^{\infty} (-1)^{i-1} \frac{2^{2i} (2^{2i} - 1) B_{2i} x^{2i-1}}{(2i)!},$$

$$\frac{1}{\zeta(x)} = \sum_{i=1}^{\infty} \frac{\mu(i)}{i^x},$$

$$\zeta(x) = \prod_{p} \frac{1}{1-p^{-x}},$$

$$\zeta^2(x) = \sum_{i=1}^{\infty} \frac{d(i)}{x^i} \text{ where } d(n) = \sum_{d|n} 1,$$

$$\zeta(x)\zeta(x-1) = \sum_{i=1}^{\infty} \frac{S(i)}{x^i} \text{ where } S(n) = \sum_{d|n} d,$$

$$\zeta(2n) = \frac{2^{2n-1} |B_{2n}|}{(2n)!} \pi^{2n}, \quad n \in \mathbb{N},$$

$$\frac{x}{\sin x} = \sum_{i=0}^{\infty} (-1)^{i-1} \frac{(4^i - 2) B_{2i} x^{2i}}{(2i)!},$$

$$\left(\frac{1-\sqrt{1-4x}}{2x}\right)^n = \sum_{i=0}^{\infty} \frac{n(2i+n-1)!}{i!(n+i)!} x^i,$$

$$e^x \sin x = \sum_{i=0}^{\infty} \frac{2^{i/2} \sin \frac{i\pi}{4}}{i!} x^i,$$

$$\sqrt{\frac{1-\sqrt{1-x}}{x}} = \sum_{i=0}^{\infty} \frac{(4i)!}{16^i \sqrt{2}(2i)!(2i+1)!} x^i,$$

$$\left(\frac{\arcsin x}{x}\right)^2 = \sum_{i=0}^{\infty} \frac{4^{i}i!^2}{(i+1)(2i+1)!} x^{2i}.$$

$$\left(\frac{1}{x}\right)^{-n} = \sum_{i=0}^{\infty} \begin{Bmatrix} i \\ n \end{Bmatrix} x^{i},$$

$$(e^{x} - 1)^{n} = \sum_{i=0}^{\infty} \begin{Bmatrix} i \\ n \end{Bmatrix} \frac{n! x^{i}}{i!},$$

$$x \cot x = \sum_{i=0}^{\infty} \frac{(-4)^{i} B_{2i} x^{2i}}{(2i)!},$$

$$\frac{i^{i-1}}{j}, \qquad \zeta(x) = \sum_{i=1}^{\infty} \frac{1}{i^{x}},$$

$$\frac{\zeta(x-1)}{\zeta(x)} = \sum_{i=0}^{\infty} \frac{\phi(i)}{i^{x}},$$

![](_page_9_Picture_5.jpeg)

## Stieltjes Integration

If G is continuous in the interval [a, b] and F is nondecreasing then

$$\int_{a}^{b} G(x) \, dF(x)$$

exists. If  $a \leq b \leq c$  then

$$\int_{a}^{c} G(x) \, dF(x) = \int_{a}^{b} G(x) \, dF(x) + \int_{b}^{c} G(x) \, dF(x).$$

If the integrals involved exist

$$\int_{a}^{b} (G(x) + H(x)) dF(x) = \int_{a}^{b} G(x) dF(x) + \int_{a}^{b} H(x) dF(x),$$

$$\int_{a}^{b} G(x) d(F(x) + H(x)) = \int_{a}^{b} G(x) dF(x) + \int_{a}^{b} G(x) dH(x),$$

$$\int_{a}^{b} c \cdot G(x) dF(x) = \int_{a}^{b} G(x) d(c \cdot F(x)) = c \int_{a}^{b} G(x) dF(x),$$

$$\int_{a}^{b} G(x) dF(x) = G(b)F(b) - G(a)F(a) - \int_{a}^{b} F(x) dG(x).$$

If the integrals involved exist, and F possesses a derivative F' at every point in [a,b] then

$$\int_a^b G(x) dF(x) = \int_a^b G(x)F'(x) dx.$$

#### Cramer's Rule

If we have equations:

$$a_{1,1}x_1 + a_{1,2}x_2 + \dots + a_{1,n}x_n = b_1$$

$$a_{2,1}x_1 + a_{2,2}x_2 + \dots + a_{2,n}x_n = b_2$$

$$\vdots \qquad \vdots \qquad \vdots$$

$$a_{n,1}x_1 + a_{n,2}x_2 + \dots + a_{n,n}x_n = b_n$$

Let  $A = (a_{i,j})$  and B be the column matrix  $(b_i)$ . Then there is a unique solution iff det  $A \neq 0$ . Let  $A_i$  be A with column i replaced by B. Then

$$x_i = \frac{\det A_i}{\det A}.$$

Improvement makes strait roads, but the crooked roads without Improvement, are roads of Genius.

- William Blake (The Marriage of Heaven and Hell)

 00
 47
 18
 76
 29
 93
 85
 34
 61
 52

 86
 11
 57
 28
 70
 39
 94
 45
 02
 63

 95
 80
 22
 67
 38
 71
 49
 56
 13
 04

 59
 96
 81
 33
 07
 48
 72
 60
 24
 15

 73
 69
 90
 82
 44
 17
 58
 01
 35
 26

 68
 74
 09
 91
 83
 55
 27
 12
 46
 30

 37
 08
 75
 19
 92
 84
 66
 23
 50
 41

 14
 25
 36
 40
 51
 62
 03
 77
 88
 99

 21
 32
 43
 54
 65
 06
 10
 89
 97
 78

 42
 53
 64

The Fibonacci number system: Every integer n has a unique representation

$$n = F_{k_1} + F_{k_2} + \dots + F_{k_m},$$
  
where  $k_i \ge k_{i+1} + 2$  for all  $i$ ,  $1 \le i < m$  and  $k_m \ge 2$ .

#### Fibonacci Numbers

 $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$ Definitions:

$$F_{i} = F_{i-1} + F_{i-2}, \quad F_{0} = F_{1} = 1,$$

$$F_{-i} = (-1)^{i-1} F_{i},$$

$$F_{i} = \frac{1}{\sqrt{5}} \left( \phi^{i} - \hat{\phi}^{i} \right),$$

Cassini's identity: for i > 0:

$$F_{i+1}F_{i-1} - F_i^2 = (-1)^i.$$

Additive rule:

$$F_{n+k} = F_k F_{n+1} + F_{k-1} F_n,$$
  

$$F_{2n} = F_n F_{n+1} + F_{n-1} F_n.$$

Calculation by matrices:

$$\begin{pmatrix} F_{n-2} & F_{n-1} \\ F_{n-1} & F_n \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}^n.$$