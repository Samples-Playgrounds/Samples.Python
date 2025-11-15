|    | using System.Reflection;                                            |
|---:|:--------------------------------------------------------------------|
|  0 | using System.Runtime.CompilerServices;                              |
|  1 | using System.Runtime.InteropServices;                               |
|  2 | using System.Runtime.Intrinsics;                                    |
|  3 | using System.Security.Authentication;                               |
|  4 | using System.Security.Cryptography;                                 |
|  5 | using System.Security.Cryptography.X509Certificates;                |
|  6 | using System.Text;                                                  |
|  7 | using System.Text.Json;                                             |
|  8 | using System.Text.RegularExpressions;                               |
|  9 | using System.Threading;                                             |
| 10 | using System.Threading.Tasks;                                       |
| 11 | using System.Xml;                                                   |
| 12 |                                                                     |
| 13 | [MemoryDiagnoser(displayGenColumns: false)]                         |
| 14 | [DisassemblyDiagnoser]                                              |
| 15 | [HideColumns("Error", "StdDev", "Median", "RatioSD")]               |
| 16 | public partial class Program                                        |
| 17 | {                                                                   |
| 18 | static void Main(string[] args) =>                                  |
| 19 | BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args); |
| 20 |                                                                     |
| 21 | // ... copy [Benchmark]s here                                       |
| 22 | }                                                                   |