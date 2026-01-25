|    | 0                                                                   |
|---:|:--------------------------------------------------------------------|
|  0 | using System.Reflection;                                            |
|  1 | using System.Runtime.CompilerServices;                              |
|  2 | using System.Runtime.InteropServices;                               |
|  3 | using System.Runtime.Intrinsics;                                    |
|  4 | using System.Security.Authentication;                               |
|  5 | using System.Security.Cryptography;                                 |
|  6 | using System.Security.Cryptography.X509Certificates;                |
|  7 | using System.Text;                                                  |
|  8 | using System.Text.Json;                                             |
|  9 | using System.Text.RegularExpressions;                               |
| 10 | using System.Threading;                                             |
| 11 | using System.Threading.Tasks;                                       |
| 12 | using System.Xml;                                                   |
| 13 |                                                                     |
| 14 | [MemoryDiagnoser(displayGenColumns: false)]                         |
| 15 | [DisassemblyDiagnoser]                                              |
| 16 | [HideColumns("Error", "StdDev", "Median", "RatioSD")]               |
| 17 | public partial class Program                                        |
| 18 | {                                                                   |
| 19 | static void Main(string[] args) =>                                  |
| 20 | BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args); |
| 21 |                                                                     |
| 22 | // ... copy [Benchmark]s here                                       |
| 23 | }                                                                   |