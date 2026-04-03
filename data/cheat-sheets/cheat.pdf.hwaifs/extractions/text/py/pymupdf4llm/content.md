|Theoretical Computer Science Cheat Sheet<br>ee|Theoretical Computer Science Cheat Sheet<br>ee|
|---|---|
|Definitions<br>Series<br>f(n) =O(g(n))<br>iff ∃positive c, n0 such that<br>0≤f(n)≤cg(n) ∀n≥n0.<br>n<br>i=1<br>i= n(n+ 1)<br>2<br>,<br>n<br>i=1<br>i2 = n(n+ 1)(2n+ 1)<br>6<br>,<br>n<br>i=1<br>i3 = n2(n+ 1)2<br>4<br>.<br>In general:<br>n<br>i=1<br>im =<br>1<br>m+ 1 (n+ 1)m+1−1−<br>n<br>i=1<br>(i+ 1)m+1 −im+1 −(m+ 1)im<br>n<br>1<br>i=1<br>im =<br>1<br>m+ 1<br>m<br>k=0<br>m+ 1<br>k<br>Bknm+1−k.<br>Geometric series:<br>n<br>i=0<br>ci = cn+1−1<br>c−1<br>,<br>c̸= 1,<br>i=0<br>ci =<br>1<br>1−c,<br>i=1<br>ci =<br>c<br>1−c,<br>|c|<1,<br>n<br>i=0<br>ici = ncn+2−(n+ 1)cn+1+c<br>(c−1)2<br>,<br>c̸= 1,<br>i=0<br>ici =<br>c<br>(1−c)2,<br>|c|<1.<br>Harmonic series:<br>Hn =<br>n<br>i=1<br>1<br>i,<br>n<br>i=1<br>iHi = n(n+ 1)<br>2<br>Hn−n(n−1)<br>4<br>.<br>n<br>i=1<br>Hi = (n+ 1)Hn−n,<br>n<br>i=1<br>i<br>m Hi =<br>n+ 1<br>m+ 1<br>Hn+1−<br>1<br>m+ 1<br>.<br>f(n) = Ω(g(n))<br>iff ∃positive c, n0 such that<br>f(n)≥cg(n)≥0 ∀n≥n0.<br>f(n) = Θ(g(n))<br>iff f(n)<br>=<br>O(g(n)) and<br>f(n) = Ω(g(n)).<br>f(n) =o(g(n))<br>iff limn→∞f(n)/g(n) = 0.<br>lim<br>n→∞an =a<br>iff ∀ǫ > 0, ∃n0 such that<br>|an−a|< ǫ, ∀n≥n0.<br>supS<br>least b ∈R such that b ≥s,<br>∀s∈S.<br>infS<br>greatestb∈R such that b≤<br>s, ∀s∈S.<br>lim inf<br>n→∞an<br>lim<br>n→∞inf{ai |i≥n, i∈N}.<br>lim sup<br>n→∞an<br>lim<br>n→∞sup{ai |i≥n, i∈N}.<br>n<br>k<br>Combinations:<br>Size k sub-<br>sets of a size n set.<br>n<br>k<br>Stirling numbers (1st kind):<br>Arrangements of an n ele-<br>ment set into k cycles.<br>1.<br>n<br>k<br>=<br>n!<br>(n<br>k)!k!,<br>2.<br>n<br>k=0<br>n<br>k<br>= 2n,<br>3.<br>n<br>k<br>=<br>n<br>n−k ,<br>4.<br>n<br>k<br>= n<br>k<br>n−1<br>k<br>1 ,<br>5.<br>n<br>k<br>=<br>n−1<br>k<br>+<br>n−1<br>k−1 ,<br>6.<br>n<br>m<br>m<br>k<br>=<br>n<br>k<br>n−k<br>m−k ,<br>7.<br>n<br>k=0<br>r+k<br>k<br>=<br>r+n+ 1<br>n<br>,<br>8.<br>n<br>k=0<br>k<br>m<br>=<br>n+ 1<br>m+ 1 ,<br>9.<br>n<br>k=0<br>r<br>k<br>s<br>n<br>k<br>=<br>r+s<br>n<br>,<br>10.<br>n<br>k<br>= (−1)k<br>k−n−1<br>k<br>,<br>11.<br>n<br>1<br>=<br>n<br>n<br>= 1,<br>n<br>k<br>Stirling numbers (2nd kind):<br>Partitions of an n element<br>set into k non-empty sets.<br>n<br>k<br>1st order Eulerian numbers:<br>Permutations π1π2. . . πn on<br>{1,2, . . ., n} with k ascents.<br>n<br>k<br>2nd order Eulerian numbers.<br>nD(nr<br>ee<br>ee<br>ee<br>ee<br>Sf<br>|<br>|<br>a<br>a<br>ee<br>a<br>ef<br>—_<br>a<br>;<br>Le<br>Pf<br>a<br>ee<br>() Cu<br>eeee<br>{<br>}<br>7<br>eeeee<br>TT<br>00)<br>ay<br>(‘“)<br>tt tt||
|12.<br>n<br>2<br>= 2n−1 −1,<br>13.<br>n<br>k<br>=k<br>n−1<br>k<br>+<br>n−1<br>k<br>1<br>Cn<br>Catalan Numbers:<br>Binary<br>trees with n+ 1 vertices.<br>14.<br>n<br>1<br>= (n−1)!,<br>15.<br>n<br>2<br>= (n−1)!Hn−1,<br>16.<br>n<br>n<br>= 1,<br>17.<br>n<br>k<br>≥<br>n<br>k<br>,<br>a<br>a<br>|<br>a<br>vt anh|,|
|18.<br>n<br>k<br>= (n−1) n−1<br>k<br>+<br>n−1<br>k−1 ,<br>19.<br>n<br>n<br>1<br>=<br>n<br>n<br>1<br>=<br>n<br>2 ,<br>20.<br>n<br>k=0<br>n<br>k<br>=n!,<br>21. Cn =<br>1<br>n+ 1<br>2n<br>n<br>,<br>22.<br>n<br>0<br>=<br>n<br>n−1<br>= 1,<br>23.<br>n<br>k<br>=<br>n<br>n−1−k<br>,<br>24.<br>n<br>k<br>= (k+ 1)<br>n−1<br>k<br>+ (n−k)<br>n−1<br>k−1<br>,<br>See ee<br>eee<br>a<br>—()<br>)¢)<br>(><br>(<br>(>)<br>)||
|25.<br>0<br>k<br>=<br>1<br>if k = 0,<br>0<br>otherwise<br>26.<br>n<br>1<br>= 2n −n−1,<br>27.<br>n<br>2<br>= 3n −(n+ 1)2n +<br>n+ 1<br>2<br>,<br>()<br>{<br>(<br>()<br>)||
|28. xn =<br>n<br>k=0<br>n<br>k<br>x+k<br>n<br>,<br>29.<br>n<br>m<br>=<br>m<br>k=0<br>n+ 1<br>k<br>(m+ 1−k)n(−1)k,<br>30. m!<br>n<br>m<br>=<br>n<br>k=0<br>n<br>k<br>k<br>n−m ,<br>()<br>(<br>)<br>td<br>(DC)||
|31.<br>n<br>m<br>=<br>n<br>k=0<br>n<br>k<br>n−k<br>m<br>(−1)n−k−mk!,<br>32.<br>n<br>0<br>= 1,<br>33.<br>n<br>n<br>= 0<br>for n̸= 0,<br>(4<br>fC)<br>( )<br>(||
|34.<br>n<br>k<br>= (k+ 1)<br>n−1<br>k<br>+ (2n−1−k)<br>n−1<br>k−1<br>,<br>35.<br>n<br>k=0<br>n<br>k<br>= (2n)n<br>2n<br>,<br>()<br>«<br>)<br>(<br>)<br>()=||
|36.<br>x<br>x−n<br>=<br>n<br>k=0<br>n<br>k<br>x+n−1−k<br>2n<br>,<br>37.<br>n+ 1<br>m+ 1<br>=<br>k<br>n<br>k<br>k<br>m<br>=<br>n<br>k=0<br>k<br>m<br>(m+ 1)n−k,<br>t<br>fF<br>«DM<br>t<br>FLUO<br>Pf||



Theoretical Computer Science Cheat Sheet 

|||Identities Cont.<br>Trees|
|---|---|---|
|38.<br>�n+ 1<br>m+ 1<br>�<br>=<br>�<br>k<br>�n<br>k<br>��k<br>m<br>�<br>=<br>n<br>�<br>k=0<br>�k<br>m<br>�<br>40.<br>�n<br>m<br>�<br>=<br>�<br>k<br>�n<br>k<br>��k+ 1<br>m+ 1<br>�<br>(−1)n−k,<br>42.<br>�m+n+ 1<br>m<br>�<br>=<br>m<br>�<br>k=0<br>k<br>�n+k<br>k<br>�<br>,|nn−k<br>=n!<br>n<br>�<br>k=0<br>1<br>k!<br>�k<br>m<br>�<br>,<br>39.<br>�<br>x<br>x−n<br>�<br>=<br>n<br>�<br>k=0<br>��n<br>k<br>���x+k<br>2n<br>�<br>,<br>41.<br>�n<br>m<br>�<br>=<br>�<br>k<br>�n+ 1<br>k+ 1<br>��k<br>m<br>�<br>(−1)m−k,<br>43.<br>�m+n+ 1<br>m<br>�<br>=<br>m<br>�<br>k=0<br>k(n+k)<br>�n+k<br>k<br>�<br>,<br>Every tree with n<br>vertices has n−1<br>edges.<br>Kraft<br>inequal-<br>ity: If the depths<br>of<br>the<br>leaves of<br>a binary tree are||
|44.<br>�n<br>m<br>�<br>=<br>�<br>k<br>�n+ 1<br>k+ 1<br>��k<br>m<br>�<br>(−1)m−k,<br>46.<br>�<br>n<br>n−m<br>�<br>=<br>�<br>k<br>�m−n<br>m+k<br>��m+n<br>n+k<br>��|45. (n−m)!<br>�n<br>m<br>�<br>=<br>�<br>k<br>�n+ 1<br>k+ 1<br>��k<br>m<br>�<br>(−1)m−k,<br>for n≥m,<br>m+k<br>k<br>�<br>,<br>47.<br>�<br>n<br>n−m<br>�<br>=<br>�<br>k<br>�m−n<br>m+k<br>��m+n<br>n+k<br>��m+k<br>k<br>�<br>,<br>d1, . . . , dn:<br>n<br>�<br>i=1<br>2−di ≤1,<br>and equality holds||
|48.<br>�<br>n<br>ℓ+m<br>��ℓ+m<br>ℓ<br>�<br>=<br>�<br>k<br>�k<br>ℓ<br>��n−k<br>m||��n<br>k<br>�<br>,<br>49.<br>�<br>n<br>ℓ+m<br>��ℓ+m<br>ℓ<br>�<br>=<br>�<br>k<br>�k<br>ℓ<br>��n−k<br>m<br>��n<br>k<br>�<br>.<br>only if every in-<br>ternal node has 2<br>sons.|
|||Recurrences|
|Master method:<br>T(n) =aT(n/b) +f(n),<br>a≥1, b >1||1<br>�<br>T(n)−3T(n/2) =n<br>�<br>Generating functions:<br>1. Multiply both sides of the equa-|
|If ∃ǫ >0 such that f(n) =O(nlogba−ǫ)<br>then<br>T(n) = Θ(nlogba).<br>If f(n) = Θ(nlogba) then<br>T(n) = Θ(nlogba log2n).<br>If∃ǫ >0 such thatf(n) = Ω(nlogba+ǫ),<br>and ∃c < 1 such that af(n/b) ≤cf(n)<br>for large n, then<br>T(n) = Θ(f(n)).||3<br>�<br>T(n/2)−3T(n/4) =n/2<br>�<br>...<br>...<br>...<br>3log2n−1�<br>T(2)−3T(1) = 2<br>�<br>Let m = log2n.<br>Summing the left side<br>we get T(n) −3mT(1) = T(n) −3m =<br>T(n) −nk where k = log23 ≈1.58496.<br>Summing the right side we get<br>m−1<br>�<br>i=0<br>n<br>2i3i =n<br>m−1<br>�<br>i=0<br>�3<br>2<br>�i.<br>tion by xi.<br>2. Sum both sides over all i for<br>which the equation is valid.<br>3. Choose<br>a<br>generating<br>function<br>G(x). UsuallyG(x) = �∞<br>i=0 xigi.<br>3. Rewrite the equation in terms of<br>the generating function G(x).<br>4. Solve for G(x).<br>5. The coefcient ofxi inG(x) isgi.<br>Example:<br>gi+1 = 2gi+ 1,<br>g0 = 0.|
|Substitution (example): Consider the<br>following recurrence<br>Ti+1 = 22i ·T 2<br>i ,<br>T1 = 2.<br>Note that Ti is always a power of two.<br>Let ti = log2Ti. Then we have<br>ti+1 = 2i + 2ti,<br>t1 = 1.<br>Let ui = ti/2i. Dividing both sides of<br>the previous equation by 2i+1 we get||Let c= 3<br>2. Then we have<br>n<br>m−1<br>�<br>i=0<br>ci =n<br>�cm−1<br>c−1<br>�<br>= 2n(clog2n −1)<br>= 2n(c(k−1) logcn −1)<br>= 2nk −2n,<br>Multiply and sum:<br>�<br>i≥0<br>gi+1xi =<br>�<br>i≥0<br>2gixi +<br>�<br>i≥0<br>xi.<br>We chooseG(x) = �<br>i≥0 xigi. Rewrite<br>in terms of G(x):<br>G(x)−g0<br>x<br>= 2G(x) +<br>�<br>i≥0<br>xi.|
|ti+1<br>2i+1 =<br>2i<br>2i+1 + ti<br>2i.<br>Substituting we fnd<br>ui+1 = 1<br>2 +ui,<br>u1 = 1<br>2,<br>which is simply ui = i/2. So we fnd<br>thatTi has the closed formTi = 2i2i−1.<br>Summing factors (example): Consider<br>the following recurrence<br>T(n) = 3T(n/2) +n,<br>T(1) = 1.<br>Rewrite so that all terms involving T<br>are on the left side<br>T(n)−3T(n/2) =n.<br>Now expand the recurrence, and choose||and so T(n) = 3nk −2n. Full history re-<br>currences can often be changed to limited<br>history ones (example): Consider<br>Ti = 1 +<br>i−1<br>�<br>j=0<br>Tj,<br>T0 = 1.<br>Note that<br>Ti+1 = 1 +<br>i<br>�<br>j=0<br>Tj.<br>Subtracting we fnd<br>Ti+1−Ti = 1 +<br>i<br>�<br>j=0<br>Tj −1−<br>i−1<br>�<br>j=0<br>Tj<br>=Ti.<br>Simplify:<br>G(x)<br>x<br>= 2G(x) +<br>1<br>1−x.<br>Solve for G(x):<br>G(x) =<br>x<br>(1−x)(1−2x).<br>Expand this using partial fractions:<br>G(x) =x<br>�<br>2<br>1−2x −<br>1<br>1−x<br>�<br>=x<br><br>2<br>�<br>i≥0<br>2ixi −<br>�<br>i≥0<br>xi<br><br><br>=<br>�<br>i≥0<br>(2i+1 −1)xi+1.|
|a factor which makes the left side “tele-<br>scope”||And so Ti+1 = 2Ti = 2i+1.<br>So gi = 2i −1.|



Theoretical Computer Science Cheat Sheet 

|||π ≈3.14159,|e≈2.71828,<br>γ ≈0.57721,<br>φ= 1+<br>√<br>5<br>2|e≈2.71828,<br>γ ≈0.57721,<br>φ= 1+<br>√<br>5<br>2|≈1.61803,<br>ˆφ= 1−<br>√<br>5<br>2<br>≈−.61803|≈1.61803,<br>ˆφ= 1−<br>√<br>5<br>2<br>≈−.61803||
|---|---|---|---|---|---|---|---|
||i|2i|pi|General||Probability||
||1|2|2|Bernoulli Numbers (Bi = 0, odd i = 1):||Continuous distributions: If||
||2<br>3<br>4<br>5<br>6|4<br>8<br>16<br>32<br>64|3<br>5<br>7<br>11<br>13|B0 = 1, B1 =−1<br>2, B2 = 1<br>6, B4 =−1<br>30,<br>B6 =<br>1<br>42, B8 =−1<br>30, B10 =<br>5<br>66.<br>Change of base, quadratic formula:<br>logbx= logax<br>logab,<br>−b±<br>√<br>b2 −4ac<br>2a<br>.||Pr[a < X < b] =<br>�b<br>a<br>p(x)dx,<br>thenpis the probability density function<br>X. If<br>Pr[X < a] =P(a),<br>then P is the distribution function of X.|of<br> If|
||7|128|17|Euler’s number e:||P and p both exist then||
||8<br>9<br>10<br>11<br>12<br>13<br>14<br>15|256<br>512<br>1,024<br>2,048<br>4,096<br>8,192<br>16,384<br>32,768|19<br>23<br>29<br>31<br>37<br>41<br>43<br>47|e= 1 + 1<br>2 + 1<br>6 + 1<br>24 +<br>1<br>120 +· · ·<br>lim<br>n→∞<br>�<br>1 + x<br>n<br>�n<br>=ex.<br>�<br>1 + 1<br>n<br>�n < e <<br>�<br>1 + 1<br>n<br>�n+1.<br>�<br>1 + 1<br>n<br>�n =e−e<br>2n + 11e<br>24n2 −O<br>�1<br>n3<br>�<br>.<br>Harmonic numbers:<br>1, 3<br>2, 11<br>6 , 25<br>12, 137<br>60 , 49<br>20, 363<br>140, 761<br>280, 7129<br>2520, . . .||P(a) =<br>�a<br>−∞<br>p(x)dx.<br>Expectation: If X is discrete<br>E[g(X)] =<br>�<br>x<br>g(x) Pr[X =x].<br>If X continuous then<br>E[g(X)] =<br>�∞<br>−∞<br>g(x)p(x)dx=<br>�∞<br>−∞<br>g(x)dP(x).<br>Variance, standard deviation:||
||16|65,536|53|lnn < Hn <lnn+ 1,||VAR[X] = E[X2]−E[X]2,||
||17<br>18|131,072<br>262,144|59<br>61|Hn = lnn+γ+O<br>�1<br>n<br>�<br>.||σ =<br>�<br>VAR[X].<br>For events A and B:||
||19|524,288|67|Factorial, Stirling’s approximation:||Pr[A∨B] = Pr[A] + Pr[B]−Pr[A∧B]||
||20|1,048,576|71|1, 2, 6, 24, 120, 720, 5040, 40320, 362880,. . .||Pr[A∧B] = Pr[A]·Pr[B],||
||21<br>22<br>23|2,097,152<br>4,194,304<br>8,388,608|73<br>79<br>83|n! =<br>√<br>2πn<br>�n<br>e<br>�n�<br>1 + Θ<br>�1<br>n<br>��<br>.<br>Ackermann’s function and inverse:||if A and B are independent.<br>Pr[A|B] = Pr[A∧B]<br>Pr[B]||
||24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32|16,777,216<br>33,554,432<br>67,108,864<br>134,217,728<br>268,435,456<br>536,870,912<br>1,073,741,824<br>2,147,483,648<br>4,294,967,296<br>Pascal’s Triangle<br>1<br>1 1|89<br>97<br>101<br>103<br>107<br>109<br>113<br>127<br>131|a(i, j) =<br><br><br><br>2j<br>i= 1<br>a(i−1,2)<br>j = 1<br>a(i−1, a(i, j−1))<br>i, j ≥2<br>α(i) = min{j |a(j, j)≥i}.<br>Binomial distribution:<br>Pr[X =k] =<br>�n<br>k<br>�<br>pkqn−k,<br>q = 1−p,<br>E[X] =<br>n<br>�<br>k=1<br>k<br>�n<br>k<br>�<br>pkqn−k =np.<br>Poisson distribution:<br>Pr[X =k] = e−λλk<br>k!<br>,<br>E[X] =λ.<br>Normal (Gaussian) distribution:||For random variables X and Y:<br>E[X ·Y] = E[X]·E[Y],<br>if X and Y are independent.<br>E[X+Y] = E[X] + E[Y],<br>E[cX] =cE[X].<br>Bayes’ theorem:<br>Pr[Ai|B] =<br>Pr[B|Ai] Pr[Ai]<br>�n<br>j=1 Pr[Aj] Pr[B|Aj].<br>Inclusion-exclusion:<br>Pr<br>�<br>n<br>�<br>i=1<br>Xi<br>�<br>=<br>n<br>�<br>i=1<br>Pr[Xi] +<br>n<br>�<br>(−1)k+1<br>�<br>Pr<br>�<br>k�<br>Xij<br>�<br>.||
|||1 2 1<br>1 3 3 1<br>1 4 6 4 1<br>1 5 10 10 5 1<br>1 6 15 20 15 6 1<br>1 7 21 35 35 21 7 1<br>1 8 28 56 70 56 28 8 1||p(x) =<br>1<br>√<br>2πσe−(x−µ)2/2σ2,<br>E[X] =µ.<br>The “coupon collector”: We are given a<br>random coupon each day, and there are n<br>diferent types of coupons. The distribu-<br>tion of coupons is uniform. The expected<br>number of days to pass before we to col-<br>lect all n types is||k=2<br>ii<···<ik<br>j=1<br>Moment inequalities:<br>Pr<br>�<br>|X| ≥λE[X]<br>�<br>≤1<br>λ,<br>Pr<br>���X −E[X]<br>��≥λ·σ<br>�<br>≤1<br>λ2.<br>Geometric distribution:<br>Pr[X =k] =pqk−1,<br>q = 1−p,||
|1|10|1 9 36 84 126 126 84 36 9 1<br> 45 120 210 252 210 120 45 10 1||nHn.||E[X] =<br>∞<br>�<br>k=1<br>kpqk−1 = 1<br>p.||



**==> picture [577 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
Theoretical Computer Science Cheat Sheet<br>Trigonometry Matrices More Trig.<br>Multiplication: C<br>n<br>(0,1)<br>C = A · B, ci,j = � ai,kbk,j. b a<br>b (cos θ, sin θ) k=1 h<br>C θ<br>A Determinants: det A ̸= 0 iff A is non-singular.<br>(-1,0) (1,0) A c B<br>det A · B = det A · det B, Law of cosines:<br>c a n<br>B (0,-1) det A = � � sign(π)ai,π(i). c [2] = a [2] +b [2] −2ab cos C.<br>Area:<br>Pythagorean theorem: π i=1<br>**----- End of picture text -----**<br>


|c<br>B<br>a<br>(0,-1)<br>Pythagorean theorem:|detA=<br>�<br>π<br>n<br>�<br>i=1<br>sign(π)ai,π(i).<br>|c2 =a2+b2−2abcosC.<br>Area:|
|---|---|---|
|C2 =A2 +B2.<br>Defnitions:<br>sina=A/C,<br>cosa=B/C,<br>csca=C/A,<br>seca=C/B,<br>tana= sina<br>cosa = A<br>B,<br>cota= cosa<br>sina = B<br>A.<br>Area, radius of inscribed circle:<br>1<br>2AB,<br>AB<br>A+B+C.<br>Identities:<br>1<br>1|2×2 and 3×3 determinant:<br>����<br>a<br>b<br>c<br>d<br>����=ad−bc,<br>������<br>a<br>b<br>c<br>d<br>e<br>f<br>g<br>h<br>i<br>������<br>=g<br>����<br>b<br>c<br>e<br>f<br>����−h<br>����<br>a<br>c<br>d<br>f<br>����+i<br>����<br>a<br>b<br>d<br>e<br>����<br>=<br>aei+bfg+cdh<br>−ceg−fha−ibd.<br>Permanents:<br>permA=<br>�<br>π<br>n<br>�<br>i=1<br>ai,π(i).|A= 1<br>2hc,<br>= 1<br>2absinC,<br>= c2sinAsinB<br>2 sinC<br>.<br>Heron’s formula:<br>A= √<br>s·sa·sb·sc,<br>s= 1<br>2(a+b+c),<br>sa =s−a,<br>sb =s−b,|
|sinx=<br>cscx,<br>cosx=<br>secx,|Hyperbolic Functions|sc =s−c.|
|tanx=<br>1<br>cotx,<br>sin2 x+ cos2 x= 1,<br>1 + tan2 x= sec2 x,<br>1 + cot2 x= csc2 x,<br>sinx= cos<br>�π<br>2 −x<br>�<br>,<br>sinx= sin(π−x),<br>cosx=−cos(π−x),<br>tanx= cot<br>�π<br>2 −x<br>�<br>,<br>cotx=−cot(π−x),<br>cscx= cot x<br>2 −cotx,<br>sin(x±y) = sinxcosy±cosxsiny,<br>cos(x±y) = cosxcosy∓sinxsiny,<br>tan(x±y) = tanx±tany<br>1∓tanxtany,<br>cot(x±y) = cotxcoty∓1<br>cotx±coty ,<br>sin 2x= 2 sinxcosx,<br>sin 2x=<br>2 tanx<br>1 + tan2 x,<br>cos 2x= cos2 x−sin2 x,<br>cos 2x= 2 cos2 x−1,<br>cos 2x= 1−2 sin2 x,<br>cos 2x= 1−tan2x<br>1 + tan2 x,<br>tan 2x=<br>2 tanx<br>1−tan2 x,<br>cot 2x= cot2x−1<br>2 cotx<br>,|Defnitions:<br>sinhx = ex−e−x<br>2<br>,<br>coshx= ex+e−x<br>2<br>,<br>tanhx= ex−e−x<br>ex +e−x,<br>cschx =<br>1<br>sinhx,<br>sechx =<br>1<br>coshx,<br>cothx=<br>1<br>tanhx.<br>Identities:<br>cosh2 x−sinh2 x= 1,<br>tanh2 x+ sech2 x= 1,<br>coth2 x−csch2 x= 1,<br>sinh(−x) =−sinhx,<br>cosh(−x) = coshx,<br>tanh(−x) =−tanhx,<br>sinh(x+y) = sinhxcoshy+ coshxsinhy,<br>cosh(x+y) = coshxcoshy+ sinhxsinhy,<br>sinh 2x= 2 sinhxcoshx,<br>cosh 2x= cosh2 x+ sinh2 x,<br>coshx+ sinhx=ex,<br>coshx−sinhx=e−x,<br>(coshx+ sinhx)n = coshnx+ sinhnx,<br>n∈Z,<br>2 sinh2 x<br>2 = coshx−1,<br>2 cosh2 x<br>2 = coshx+ 1.|More identities:<br>sin x<br>2 =<br>�<br>1−cosx<br>2<br>,<br>cos x<br>2 =<br>�<br>1 + cosx<br>2<br>,<br>tan x<br>2 =<br>�<br>1−cosx<br>1 + cosx,<br>= 1−cosx<br>sinx<br>,<br>=<br>sinx<br>1 + cosx,<br>cot x<br>2 =<br>�<br>1 + cosx<br>1−cosx,<br>= 1 + cosx<br>sinx<br>,<br>=<br>sinx<br>1−cosx,<br>sinx= eix−e−ix<br>2i<br>,<br>cosx= eix+e−ix<br>2<br>,<br>tanx=−ieix−e−ix<br>eix +e−ix,|
|sin(x+y) sin(x−y) = sin2 x−sin2 y,<br>cos(x+y) cos(x−y) = cos2 x−sin2 y.<br>Euler’s equation:<br>eix = cosx+isinx,<br>eiπ =−1.<br>v2.02 c⃝1994 by Steve Seiden<br>sseiden@acm.org<br>http://www.csc.lsu.edu/~seiden|θ<br>sinθ<br>cosθ<br>tanθ<br>0<br>0<br>1<br>0<br>π<br>6<br>1<br>2<br>√<br>3<br>2<br>√<br>3<br>3<br>π<br>4<br>√<br>2<br>2<br>√<br>2<br>2<br>1<br>π<br>3<br>√<br>3<br>2<br>1<br>2<br>√<br>3<br>π<br>2<br>1<br>0<br>∞<br>. . .in mathematics<br>you don’t under-<br>stand things, you<br>just get used to<br>them.<br>– J. von Neumann|=−ie2ix−1<br>e2ix + 1,<br>sinx= sinhix<br>i<br>,<br>cosx= coshix,<br>tanx= tanhix<br>i<br>.|



## Theoretical Computer Science Cheat Sheet 

Number Theory 

Graph Theory 

|The Chinese remainder theorem: There ex-|Defnitions:|Notation:|
|---|---|---|
|ists a number C such that:|Loop<br>An edge connecting a ver-|E(G)<br>Edge set|
|C ≡r1 modm1|tex to itself.<br>Directed<br>Each edge has a direction.|V(G)<br>Vertex set<br>c(G)<br>Number of components|
|...<br>...<br>...<br>C ≡rn modmn<br>ifmi andmj are relatively prime fori =j.<br>Euler’s function:<br>φ(x) is the number of<br>positive integers less than x relatively<br>prime to x. If �n<br>i=1 pei<br>i<br>is the prime fac-<br>torization of x then<br>φ(x) =<br>n<br>�<br>pei−1<br>i<br>(pi−1).|Simple<br>Graph with no loops or<br>multi-edges.<br>Walk<br>A sequence v0e1v1. . . eℓvℓ.<br>Trail<br>A walk with distinct edges.<br>Path<br>A<br>trail<br>with<br>distinct<br>vertices.<br>Connected<br>A graph where there exists<br>a path between any two<br>vertices.<br>Component<br>A<br>maximal<br>connected|G[S]<br>Induced subgraph<br>deg(v) Degree of v<br>∆(G)<br>Maximum degree<br>δ(G)<br>Minimum degree<br>χ(G)<br>Chromatic number<br>χE(G) Edge chromatic number<br>Gc<br>Complement graph<br>Kn<br>Complete graph<br>Kn1,n2 Complete bipartite graph<br>r(k, ℓ)<br>Ramsey number|
|i=1<br>Euler’s theorem: If a and b are relatively<br>prime then<br>1≡aφ(b) modb.<br>Fermat’s theorem:<br>1≡ap−1 modp.<br>The Euclidean algorithm: if a > b are in-<br>tegers then<br>gcd(a, b) = gcd(amodb, b).|subgraph.<br>Tree<br>A connected acyclic graph.<br>Free tree<br>A tree with no root.<br>DAG<br>Directed acyclic graph.<br>Eulerian<br>Graph with a trail visiting<br>each edge exactly once.<br>Hamiltonian Graph with a cycle visiting<br>each vertex exactly once.<br>Cut<br>A set of edges whose re-<br>moval increases the num-|Geometry<br>Projective coordinates:<br>triples<br>(x, y, z), not all x, y and z zero.<br>(x, y, z) = (cx, cy, cz)<br>∀c = 0.<br>Cartesian<br>Projective<br>(x, y)<br>(x, y,1)<br>y =mx+b<br>(m,−1, b)<br>x=c<br>(1,0,−c)<br>Distance formula, Lp and L∞|
|If �n<br>i=1 pei<br>i<br>is the prime factorization of x<br>then<br>S(x) =<br>�<br>d|x<br>d=<br>n<br>�<br>i=1<br>pei+1<br>i<br>−1<br>pi−1<br>.<br>Perfect Numbers: xis an even perfect num-<br>ber ifx= 2n−1(2n−1) and 2n−1 is prime.<br>Wilson’s theorem: n is a prime if|ber of components.<br>Cut-set<br>A minimal cut.<br>Cut edge<br>A size 1 cut.<br>k-Connected A graph connected with<br>the removal of any k −1<br>vertices.<br>k-Tough<br>∀S ⊆V, S = ∅we have<br>k·c(G−S)≤|S|.|metric:<br>�<br>(x1−x0)2 + (y1−y0)2,<br>�<br>|x1−x0|p +|y1−y0|p�1/p,<br>lim<br>p→∞<br>�<br>|x1−x0|p +|y1−y0|p�1/p.<br>Area of triangle (x0, y0), (x1, y1)<br>and (x2, y2):|
|(n−1)!≡−1 modn.<br>M¨obius inversion:<br>µ(i) =<br><br><br><br><br><br>1<br>if i= 1.<br>0<br>if i is not square-free.<br>(−1)r<br>if i is the product of<br>r distinct primes.<br>If<br>G(a) =<br>�<br>d|a<br>F(d),<br>then<br>F(a) =<br>�<br>d|a<br>µ(d)G<br>�a<br>d<br>�<br>.|k-Regular<br>A graph where all vertices<br>have degree k.<br>k-Factor<br>A<br>k-regular<br>spanning<br>subgraph.<br>Matching<br>A set of edges, no two of<br>which are adjacent.<br>Clique<br>A set of vertices, all of<br>which are adjacent.<br>Ind. set<br>A set of vertices, none of<br>which are adjacent.<br>Vertex cover A set of vertices which<br>cover all edges.<br>Planar graph A graph which can be em-|1<br>2 abs<br>����<br>x1−x0<br>y1−y0<br>x2−x0<br>y2−y0<br>����.<br>Angle formed by three points:<br>(0,0)<br>θ<br>(x1, y1)<br>(x2, y2)<br>ℓ2<br>ℓ1<br>cosθ = (x1, y1)·(x2, y2)<br>ℓ1ℓ2<br>.<br>Line through two points (x0, y0)<br>and (x1, y1):|
|Prime numbers:<br>pn =nlnn+nln lnn−n+nln lnn<br>lnn|beded in the plane.<br>Plane graph<br>An embedding of a planar<br>graph.|������<br>x<br>y<br>1<br>x0<br>y0<br>1<br>x1<br>y1<br>1<br>������<br>= 0.|
|+O<br>�n<br>lnn<br>�<br>,<br>π(n) =<br>n<br>lnn +<br>n<br>(lnn)2 +<br>2!n<br>(lnn)3<br>+O<br>�<br>n<br>(lnn)4<br>�<br>.|�<br>v∈V<br>deg(v) = 2m.<br>If G is planar then n−m+f = 2, so<br>f ≤2n−4,<br>m≤3n−6.<br>Any planar graph has a vertex with de-<br>gree ≤5.|Area of circle, volume of sphere:<br>A=πr2,<br>V = 4<br>3πr3.<br>If I have seen farther than others,<br>it is because I have stood on the<br>shoulders of giants.<br>– Issac Newton|



Theoretical Computer Science Cheat Sheet 

|π|||Calculus|Calculus|Calculus|Calculus||||
|---|---|---|---|---|---|---|---|---|---|
|Wallis’ identity:|Derivatives:|||||||||
|π = 2· 2·2·4·4·6·6· · ·<br>1·3·3·5·5·7· · ·|1. d(cu)<br>dx<br>=cdu<br>dx,<br>2. d(u+v)<br>dx|||= du<br>dx||+||dv<br>dx,<br>3. d(uv)<br>dx<br>=udv<br>dx +v du<br>dx,||
|Brouncker’s continued fraction expansion:<br>π<br>4 = 1 +<br>12<br>2 +<br>32<br>2+<br>52<br>2+<br>72<br>2+···<br>Gregrory’s series:|4. d(un)<br>dx<br>=nun−1du<br>dx,<br>5. d(u/v)<br>dx<br>7. d(cu)<br>dx<br>= (lnc)cudu<br>dx,|||= v|�|du<br>dx||�|−u<br>�dv<br>dx<br>�<br>v2<br>,<br>6. d(ecu)<br>dx<br>=cecudu<br>dx,<br>8. d(lnu)<br>dx<br>= 1<br>u<br>du<br>dx,|
|π<br>4 = 1−1<br>3 + 1<br>5 −1<br>7 + 1<br>9 −· · ·|9. d(sinu)<br>dx<br>= cosudu<br>dx,||||||||10. d(cosu)<br>dx<br>=−sinudu<br>dx,|
|Newton’s series:||||||||||
|π<br>6 = 1<br>2 +<br>1<br>2·3·23 +<br>1·3<br>2·4·5·25 +· · ·<br>Sharp’s series:|11. <br>13.|d(tanu)<br>dx<br>= sec2 udu<br>dx,<br> d(secu)<br>dx<br>= tanu secudu<br>dx,|||||||12. d(cotu)<br>dx<br>= csc2 udu<br>dx,<br>14. d(cscu)<br>dx<br>=−cotu cscudu<br>dx,|
|π<br>6 =<br>1<br>√<br>3<br>�<br>1−<br>1<br>31 ·3+<br>1<br>32 ·5 −<br>1<br>33 ·7+· · ·<br>�|15.|d(arcsinu)<br>dx<br>=<br>1<br>√<br>1−u2<br>du<br>dx,|||||||16. d(arccosu)<br>dx<br>=<br>−1<br>√<br>1−u2<br>du<br>dx,|
|Euler’s series:|17.|d(arctanu)<br>dx<br>=<br>1<br>1 +u2<br>du<br>dx,|||||||18. d(arccotu)<br>dx<br>=<br>−1<br>1 +u2<br>du<br>dx,|
|π2<br>6 =<br>1<br>12 + 1<br>22 + 1<br>32 + 1<br>42 + 1<br>52 +· · ·<br>π2<br>8 =<br>1<br>12 + 1<br>32 + 1<br>52 + 1<br>72 + 1<br>92 +· · ·|19.|d(arcsecu)<br>dx<br>=<br>1<br>u<br>√<br>1−u2<br>du<br>dx,|||||||20. d(arccscu)<br>dx<br>=<br>−1<br>u<br>√<br>1−u2<br>du<br>dx,|
|π2<br>12 =<br>1<br>12 −1<br>22 + 1<br>32 −1<br>42 + 1<br>52 −· · ·|21.|d(sinhu)<br>dx<br>= coshudu<br>dx,|||||||22. d(coshu)<br>dx<br>= sinhudu<br>dx,|
|Partial Fractions<br>Let N(x) and D(x) be polynomial func-|23.|d(tanhu)<br>dx<br>= sech2 udu<br>dx,|||||||24. d(cothu)<br>dx<br>=−csch2 udu<br>dx,|
|tions<br>of<br>x.<br>We<br>can<br>break<br>down<br>N(x)/D(x) using partial fraction expan-<br>sion. First, if the degree of N is greater<br>than or equal to the degree of D, divide<br>N by D, obtaining|25. <br>27.|d(sechu)<br>dx<br>=−sechu tanhudu<br>dx,<br> d(arcsinhu)<br>dx<br>=<br>1<br>√<br>1 +u2<br>du<br>dx,||||||26. d(cschu)<br>dx<br>=−cschu cothudu<br>dx,<br>28. d(arccoshu)<br>dx<br>=<br>1<br>√<br>u2 −1<br>du<br>dx,||
|N(x)<br>D(x) =Q(x) + N′(x)<br>D(x) ,|29.|d(arctanhu)<br>dx<br>=<br>1<br>1−u2<br>du<br>dx,|||||||30. d(arccothu)<br>dx<br>=<br>1<br>u2 −1<br>du<br>dx,|
|where the degree ofN ′ is less than that of<br>D. Second, factor D(x). Use the follow-<br>ing rules: For a non-repeated factor:<br>N(x)<br>(x−a)D(x) =<br>A<br>x−a + N′(x)<br>D(x) ,<br>where|31. d(arcsechu)<br>dx<br>=<br>−1<br>u<br>√<br>1−u2<br>du<br>dx,<br>Integrals:<br>1.<br>�<br>cu dx=c<br>�<br>u dx,|||||||32. d(arccschu)<br>dx<br>=<br>−1<br>|u|<br>√<br>1 +u2<br>du<br>dx.<br>2.<br>�<br>(u+v)dx=<br>�<br>u dx+<br>�<br>v dx,||
|A=<br>�N(x)<br>D(x)<br>�<br>x=a<br>.|3.<br>�|xn dx=<br>1<br>n+ 1xn+1,<br>n =−1,||4.|||�||1<br>xdx= lnx,<br>5.<br>�<br>ex dx=ex,|
|For a repeated factor:<br>N(x)<br>(x−a)mD(x) =<br>m−1<br>�<br>k=0<br>Ak<br>(x−a)m−k+N′(x)<br>D(x) ,|6.<br>�<br>8.<br>�|dx<br>1 +x2 = arctanx,<br>sinx dx=−cosx,|||||||7.<br>�<br>udv<br>dxdx=uv−<br>�<br>vdu<br>dxdx,<br>9.<br>�<br>cosx dx= sinx,|
|where<br>Ak = 1<br>k!<br>�dk<br>dxk<br>�N(x)<br>D(x)<br>��<br>x=a<br>.|10.|�<br>tanx dx=−ln|cosx|,|||||||11.<br>�<br>cotx dx= ln|cosx|,|
|The reasonable man adapts himself to the|12.|�<br>secx dx= ln|secx+ tanx|,||||||13.<br>�<br>cscx dx= ln|cscx+ cotx|,||
|world; the unreasonable persists in trying<br>to adapt the world to himself. Therefore<br>all progress depends on the unreasonable.|14.|�<br>arcsin x<br>adx= arcsin x<br>a +<br>�<br>a2 −x2,|||||a||>0,|
|– George Bernard Shaw||||||||||



## Theoretical Computer Science Cheat Sheet 

Calculus Cont. 

**==> picture [548 x 678] intentionally omitted <==**

Theoretical Computer Science Cheat Sheet 

|||Calculus Cont.||Finite Calculus|||
|---|---|---|---|---|---|---|
|62.|�|dx<br>x<br>√<br>x2 −a2 = 1<br>a arccos a<br>|x|,<br>a >0,<br>63.<br>�<br>dx<br>x2√<br>x2 ±a2 =∓<br>√<br>x2 ±a2<br>a2x|,|Diference, shift operators:<br>∆f(x) =f(x+ 1)−f(x),|||
|64.|�|x dx<br>√<br>x2 ±a2 =<br>�<br>x2 ±a2,<br>65.<br>�√<br>x2 ±a2<br>x4<br>dx=∓(x2+a2)3/2<br>3a2x3|,|Ef(x) =f(x+ 1).<br>Fundamental Theorem:|||
|66.|�|dx<br>ax2 +bx+c =<br><br><br><br><br><br><br><br><br><br>1<br>√<br>b2 −4ac<br>ln<br>�����<br>2ax+b−<br>√<br>b2 −4ac<br>2ax+b+<br>√<br>b2 −4ac<br>�����,<br>if b2 >4ac,<br>2<br>√<br>4ac−b2 arctan<br>2ax+b<br>√<br>4ac−b2,<br>if b2 <4ac,||f(x) = ∆F(x)⇔<br>�<br>f(x)δx=F(x) +C.<br>b<br>�<br>a<br>f(x)δx=<br>b−1<br>�<br>i=a<br>f(i).<br>Diferences:|||
|67.|�|dx<br>√<br>ax2 +bx+c =<br><br><br><br><br><br><br><br>1<br>√<br>a ln<br>���2ax+b+ 2√<br>a<br>�<br>ax2 +bx+c<br>���,<br>if a >0,<br>1<br>√<br>−a arcsin −2ax−b<br>√<br>b2 −4ac<br>,<br>if a <0,||∆(cu) =c∆u,<br>∆(u+v) = ∆u+ ∆v,<br>∆(uv) =u∆v+ Ev∆u,<br>∆(xn<br>) =nxn<br>−1,|||
|68.|�|�<br>ax2 +bx+c dx= 2ax+b<br>4a<br>�<br>ax2 +bx+c+ 4ax−b2<br>8a<br>�<br>dx<br>√<br>ax2 +bx+c,||∆(Hx) =x−1<br>,<br>∆(2x) = 2x,<br>∆(cx) = (c−1)cx,<br>∆<br>�x<br>m<br>�<br>=<br>�<br>x<br>m−1<br>�<br>.<br>Sums:|||
|69.|�|x dx<br>√<br>ax2 +bx+c<br>=<br>√<br>ax2 +bx+c<br>a<br>−b<br>2a<br>�<br>dx<br>√<br>ax2 +bx+c<br>,||�cu δx=c�u δx,<br>�(u+v)δx=�u δx+�v δx,|||
|70.|�|dx<br>x<br>√<br>ax2 +bx+c<br>=<br><br><br><br><br><br><br><br><br><br>−1<br>√<br>c ln<br>�����<br>2√<br>c<br>√<br>ax2 +bx+c+bx+ 2c<br>x<br>�����,<br>if c >0,<br>1<br>√<br>−c arcsin<br>bx+ 2c<br>|x|<br>√<br>b2 −4ac<br>,<br>if c <0,||�u∆v δx=uv−�<br>Ev∆u δx,<br>�xn<br>δx= xn+1<br>m+1 ,<br>�x−1<br>δx <br>�cxδx=<br>cx<br>c−1,<br>��x<br>m<br>�<br>δx=|=Hx,<br>�<br>x<br>m+1<br>�<br>.||
|71.|�|x3�<br>x2 +a2 dx= ( 1<br>3x2−2<br>15a2)(x2+a2)3/2,||Falling Factorial Powers:<br>xn<br>=x(x−1)· · ·(x−n+ 1),|n >|0,|
|72.<br>73.|�<br>�|xn sin(ax)dx=−1<br>axncos(ax) + n<br>a<br>�<br>xn−1 cos(ax)dx,<br>xn cos(ax)dx= 1<br>axnsin(ax)−n<br>a<br>�<br>xn−1 sin(ax)dx,||x0<br>= 1,<br>xn<br>=<br>1<br>(x+ 1)· · ·(x+|n|),<br>n <0,<br>xn+m<br>=xm<br>(x−m)n<br>.|||
|74.|�|xneax dx= xneax<br>a<br>−n<br>a<br>�<br>xn−1eax dx,||Rising Factorial Powers:<br>x<br>n =x(x+ 1)· · ·(x+n−1),|n >|0,|
|75.<br>76.|�<br>�|xn ln(ax)dx=xn+1<br>�ln(ax)<br>n+ 1 −<br>1<br>(n+ 1)2<br>�<br>,<br>xn(lnax)m dx= xn+1<br>n+ 1(lnax)m−<br>m<br>n+ 1<br>�<br>xn(lnax)m−1 dx.||x<br>0 = 1,<br>x<br>n =<br>1<br>(x−1)· · ·(x−|n|),<br>n <0,<br>x<br>n+m =x<br>m(x+m)<br>n.|||
|||||Conversion:|||
|x1 =||x1<br>=<br>x<br>1||xn<br>= (−1)n(−x)<br>n = (x−n+ 1)<br>n|||
|x2 =||x2<br>+x1<br>=<br>x<br>2−x<br>1||= 1/(x+ 1)<br>−n,|||
|x3 =||x3<br>+ 3x2<br>+x1<br>=<br>x<br>3−3x<br>2+x<br>1||x<br>n = (−1)n(−x)n<br>= (x+n−1)n|||
|x4 =||x4<br>+ 6x3<br>+ 7x2<br>+x1<br>=<br>x<br>4−6x<br>3+ 7x<br>2−x<br>1||= 1/(x−1)−n<br>,|||
|x5 =<br>x<br>1 =||x5<br>+ 15x4<br>+ 25x3<br>+ 10x2<br>+x1<br>=<br>x5<br>−15x<br>4+ 25x<br>3−10x<br>2+x<br>1<br>x1<br>x1<br>=<br>x1||xn =<br>n<br>�<br>k=1<br>�n<br>k<br>�<br>xk<br>=<br>n<br>�<br>k=1<br>�n<br>k<br>�<br>(−1)n−kx<br>k,|||
|x<br>2 =<br>x<br>3 =||x2 +x1<br>x2<br>=<br>x2 −x1<br>x3 + 3x2 + 2x1<br>x3<br>=<br>x3 −3x2 + 2x1||xn<br>=<br>n<br>�<br>k=1<br>�n<br>k<br>�<br>(−1)n−kxk,|||
|x<br>4 =<br>x<br>5 =||x4 + 6x3 + 11x2 + 6x1<br>x4<br>=<br>x4 −6x3 + 11x2 −6x1<br>x5 + 10x4 + 35x3 + 50x2 + 24x1<br>x5<br>=<br>x5 −10x4 + 35x3 −50x2 + 24x1||x<br>n =<br>n<br>�<br>k=1<br>�n<br>k<br>�<br>xk.|||



Theoretical Computer Science Cheat Sheet 

|||Series|Series|||||
|---|---|---|---|---|---|---|---|
|Taylor’s series:|||||||Ordinary power series:|
|f(x) =f(a) + (x−a)f ′(a)<br>Expansions:<br>1<br>1−x<br>1<br>1−cx||+ (x−a)2<br>2<br>f ′′(a) +· · ·=<br>∞<br>�<br>i=0<br>= 1 +x+x2 +x3 +x4 +· · ·<br>= 1 +cx+c2x2 +c3x3 +· · ·|(x−a)i<br>i!<br>f (i)(a).<br>=<br>∞<br>�<br>i=0<br>xi,<br>=<br>∞<br>�<br>cixi,||||A(x) =<br>∞<br>�<br>i=0<br>aixi.<br>Exponential power series:<br>A(x) =<br>∞<br>�<br>i=0<br>ai<br>xi<br>i! .<br>Dirichlet power series:|
||||||i=0||∞|
|1<br>1−xn||= 1 +xn +x2n +x3n +· · ·||=|∞<br>�<br>i=0|xni,|A(x) =<br>�<br>i=1<br>ai<br>ix.|
|x<br>(1−x)2<br>n<br>�<br>k=0<br>�n<br>k<br>�<br>k!zk<br>(1−z)k+1<br>ex||=x+ 2x2 + 3x3 + 4x4 +· · ·<br>=x+ 2nx2 + 3nx3 + 4nx4 + <br>= 1 +x+ 1<br>2x2+ 1<br>6x3+· · ·|· · ·|=<br> =<br>=|∞<br>�<br>i=0<br>∞<br>�<br>i=0<br>∞<br>�<br>i=0|ixi,<br>inxi,<br>xi<br>i! ,|Binomial theorem:<br>(x+y)n =<br>n<br>�<br>k=0<br>�n<br>k<br>�<br>xn−kyk.<br>Diference of like powers:<br>xn −yn = (x−y)<br>n−1<br>�<br>k=0<br>xn−1−kyk.|
|ln(1 +x)<br>ln<br>1<br>1−x<br>sinx<br>cosx<br>tan−1 x||=x−1<br>2x2+ 1<br>3x3−1<br>4x4−· · ·<br>=x+ 1<br>2x2+ 1<br>3x3+ 1<br>4x4+· · ·<br>=x−1<br>3!x3+ 1<br>5!x5−1<br>7!x7+· · ·<br>= 1−1<br>2!x2+ 1<br>4!x4−1<br>6!x6+· · ·<br>=x−1<br>3x3+ 1<br>5x5−1<br>7x7+· · ·||=<br>=<br>=<br>=<br>=|∞<br>�<br>i=1<br>∞<br>�<br>i=1<br>∞<br>�<br>i=0<br>∞<br>�<br>i=0<br>∞<br>�<br>i=0|(−1)i+1xi<br>i ,<br>xi<br>i ,<br>(−1)i<br>x2i+1<br>(2i+ 1)!,<br>(−1)i x2i<br>(2i)!,<br>(−1)i x2i+1<br>(2i+ 1),|For ordinary power series:<br>αA(x) +βB(x) =<br>∞<br>�<br>i=0<br>(αai+βbi)xi,<br>xkA(x) =<br>∞<br>�<br>i=k<br>ai−kxi,<br>A(x)−�k−1<br>i=0 aixi<br>xk<br>=<br>∞<br>�<br>i=0<br>ai+kxi,<br>A(cx) =<br>∞<br>�<br>i=0<br>ciaixi,<br>∞|
|(1 +x)n||= 1 +nx+ n(n−1)<br>2<br>x2 +· · ·||=|∞<br>�<br>i=0|�n<br>i<br>�<br>xi,|A′(x) =<br>�<br>i=0<br>(i+ 1)ai+1xi,<br>∞|
|1<br>(1−x)n+1||= 1 + (n+ 1)x+<br>�n+2<br>2<br>�<br>x2 +·|· ·|=|∞<br>�<br>i=0|�i+n<br>i<br>�<br>xi,|xA′(x) =<br>�<br>i=1<br>iaixi,|
|x<br>ex −1||= 1−1<br>2x+ 1<br>12x2−<br>1<br>720x4+· · ·||=|∞<br>�<br>i=0|Bixi<br>i! ,|�<br>A(x)dx=<br>∞<br>�<br>i=1<br>ai−1<br>i<br>xi,|
|1<br>2x(1−<br>√<br>1−4x)||= 1 +x+ 2x2 + 5x3 +· · ·||=|∞<br>�<br>i=0|1<br>i+ 1<br>�2i<br>i<br>�<br>xi,|A(x) +A(−x)<br>2<br>=<br>∞<br>�<br>i=0<br>a2ix2i,|
|1<br>√<br>1−4x||= 1 + 2x+ 6x2 + 20x3 +· · ·||=|∞<br>�<br>i=0|�2i<br>i<br>�<br>xi,|A(x)−A(−x)<br>2<br>=<br>∞<br>�<br>a2i+1x2i+1.|
|1<br>√<br>1−4x<br>�1−√<br>1−4x<br>2x<br>1<br>1−x ln<br>1<br>1−x|�n|= 1 + (2 +n)x+<br>�4+n<br>2<br>�<br>x2 +·<br>=x+ 3<br>2x2+ 11<br>6 x3+ 25<br>12x4+·|· · <br>· ·|=<br>=|∞<br>�<br>i=0<br>∞<br>�<br>i=1|�2i+n<br>i<br>�<br>xi,<br>Hixi,|i=0<br>Summation: If bi = �i<br>j=0 ai then<br>B(x) =<br>1<br>1−xA(x).<br>Convolution:|
|1<br>2<br>�<br>ln<br>1<br>1−x<br>�2<br>x<br>1−x−x2||= 1<br>2x2+ 3<br>4x3+ 11<br>24x4+· · ·<br>=x+x2 + 2x3 + 3x4 +· · ·||=<br>=|∞<br>�<br>i=2<br>∞<br>�<br>i=0|Hi−1xi<br>i<br>,<br>Fixi,|A(x)B(x) =<br>∞<br>�<br>i=0<br><br><br>i<br>�<br>j=0<br>ajbi−j<br><br>xi.<br>God made the natural numbers;|
|Fnx<br>1−(Fn−1+Fn+1)x−(−1)nx2||=Fnx+F2nx2 +F3nx3 +· · ·||=|∞<br>�<br>i=0|Fnixi.|all the rest is the work of man.<br>– Leopold Kronecker|



Theoretical Computer Science Cheat Sheet 

|||||Series|Series|||Escher’s Knot|
|---|---|---|---|---|---|---|---|---|
|Expansions:|||||||||
|1<br>(1−x)n+1 ln<br>1<br>1−x|||=<br>i=0|(Hn+i−Hn) n+i<br>i||xi,|1<br>x<br>−n<br>=<br>i=0<br>i<br>n<br>xi,||
||x<br>n||=|n<br>i xi,|||(ex −1)n<br>=<br>i<br>n<br>n!xi<br>i! ,||
||||i=0||||i=0||
|ln|1<br>1−x<br>n||=<br>i=0|i<br>n<br>n!xi<br>i! ,|||xcotx<br>=<br>i=0<br>(−4)iB2ix2i<br>(2i)!<br>,||
||tanx||=<br>i=1|(−1)i−122i(22i−1)B2ix2i−1<br>(2i)!<br>,|||ζ(x)<br>=<br>i=1<br>1<br>ix,||
||1||=|µ(i)|||ζ(x−1)<br>=<br>φ(i)||
||ζ(x)||i=1|ix ,|||ζ(x)<br>i=1<br>ix ,||
||ζ(x)<br>ζ2(x)||Stieltjes Integration<br>=<br>p<br>1<br>1−p−x,<br>=<br>i=1<br>d(i)<br>xi<br>where d(n) =<br>d|n 1,<br>If G is continuous in the interval [a, b] and F is nondecreasing then<br>b<br>a<br>G(x)dF(x)<br>—<br>S<br>|||||||
|ζ(x)ζ(x−1)<br>ζ(2n)|||=<br>i=1<br>S(i)<br>xi<br>where S(n) =<br>= 22n−1|B2n|<br>(2n)!<br>π2n,<br>n∈N,|||d|n d,<br>exists. If a≤b≤c then<br>c<br>a<br>G(x)dF(x) =<br>b<br>a<br>G(x)dF(x) +<br>c<br>b<br>G(x)dF(x).<br>If the integrals involved exist<br>b<br>b<br>b<br>.<br>|<br>|<br>||||
||x<br>sinx||=<br>i=0<br>(−1)i−1(4i−2)B2ix2i<br>(2i)!<br>,||||a<br>G(x) +H(x) dF(x) =<br>a<br>b<br>b|G(x)dF(x) +<br>a<br>H(x)dF(x),<br>b|
|1−√<br>1−4x<br>2x||n|=<br>i=0|n(2i+n−1)!<br>i!(n+i)!<br>xi,|||a<br>G(x)d F(x) +H(x) =<br>a<br>b<br>b|G(x)dF(x) +<br>a<br>G(x)dH(x),<br>b|
|ex sinx|||=|2i/2 sin iπ<br>4<br>i!<br>xi,|||a<br>c·G(x)dF(x) =<br>a<br>G(x)d <br>b|c·F(x) =c<br>a<br>G(x)dF(x),<br>b|
||||i=1||||G(x)dF(x) =G(b)F(b)−G(a)F(a)−<br>F(x)dG(x).||
|1−|−√<br>1−x<br>x||=<br>i=0|(4i)!<br>16i√<br>2(2i)!(2i+ 1)!xi,|||a<br>a<br>If the integrals involved exist, andF possesses a derivativeF ′ at every<br>point in [a, b] then||
|arcsinx<br>x<br>2|||=<br>i=0|4ii!2<br>(i+ 1)(2i+ 1)!x2i.|||b<br>a<br>G(x)dF(x) =|b<br>a<br>G(x)F ′(x)dx.|
||||Cramer’s Rule|||||Fibonacci Numbers|
||||||||00 47 18 76 29 93 85 34 61 52||
|If we|have equations:<br>a1,1x1+a1,2x2+· · ·<br>a2,1x1+a2,2x2+· · ·|||· · ·+a1,nxn =b1<br>· · ·+a2,nxn =b2|||86 11 57 28 70 39 94 45 02 63<br>95 80 22 67 38 71 49 56 13 04<br>59 96 81 33 07 48 72 60 24 15|1,1,2,3,5,8,13,21,34,55,89, . . .<br>Definitions:|
||||||||73 69 90 82 44 17 58 01 35 26|Fi =Fi−1+Fi−2,<br>F0 =F1 = 1,|
||...||...|...|||68 74 09 91 83 55 27 12 46 30|F−i = ( 1)i−1Fi,|
|an,1x1+an,2x2+· · ·+an,nxn =bn<br>LetA= (ai,j) andB be the column matrix (bi). <br>there is a unique solution iff detA ̸= 0. Let Ai <br>with column i replaced by B. Then||||||Then<br> be A|37 08 75 19 92 84 66 23 50 41<br>14 25 36 40 51 62 03 77 88 99<br>21 32 43 54 65 06 10 89 97 78<br>42 53 64 05 16 20 31 98 79 87|Fi =<br>1<br>√<br>5<br>φi −ˆφi<br>,<br>Cassini’s identity: for i >0:<br>Fi+1Fi−1−F 2<br>i = (−1)i.|
||||detAi||||The Fibonacci number system:|Additive rule:|



**==> picture [54 x 22] intentionally omitted <==**

The Fibonacci number system: Every integer n has a unique representation 

**==> picture [290 x 66] intentionally omitted <==**

Improvement makes strait roads, but the crooked roads without Improvement, are roads of Genius. – William Blake (The Marriage of Heaven and Hell) 

