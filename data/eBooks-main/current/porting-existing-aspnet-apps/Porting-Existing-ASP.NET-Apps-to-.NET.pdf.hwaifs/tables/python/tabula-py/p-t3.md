|    | using Microsoft.Extensions.Configuration;       |
|---:|:------------------------------------------------|
|  0 |                                                 |
|  1 | public class TestModel : PageModel              |
|  2 | {                                               |
|  3 | private readonly IConfiguration _configuration; |
|  4 |                                                 |
|  5 | public TestModel(IConfiguration configuration)  |
|  6 | {                                               |
|  7 | _configuration= configuration;                  |
|  8 | }                                               |
|  9 |                                                 |
| 10 | public ContentResult OnGet()                    |
| 11 | {                                               |