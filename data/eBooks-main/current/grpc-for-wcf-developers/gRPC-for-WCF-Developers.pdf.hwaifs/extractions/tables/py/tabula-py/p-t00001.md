|    | Unnamed: 0                                  | Features   | WCF               | gRPC                      |
|---:|:--------------------------------------------|:-----------|:------------------|:--------------------------|
|  0 | Objective                                   |            | Separate business | Separate business code    |
|  1 |                                             |            | code from         | from interface definition |
|  2 |                                             |            | networking        | and networking            |
|  3 |                                             |            | implementation.   | implementation.           |
|  4 | Define services and messages (chapters 3-4) |            | Service Contract, | Uses proto file to        |
|  5 |                                             |            | Operation         | declare services and      |
|  6 |                                             |            | Contract, and     | messages.                 |
|  7 |                                             |            | Data Contract.    |                           |
|  8 | Language (chapters 3-5)                     |            | Contracts written | Protocol Buffer           |
|  9 |                                             |            | in C# or Visual   | language.                 |
| 10 |                                             |            | Basic.            |                           |
| 11 | Wire format (chapter 3)                     |            | Configurable,     | Protocol Buffer binary    |
| 12 |                                             |            | including         | format (although it’s     |
| 13 |                                             |            | SOAP/XML, Plain   | possible to use other     |
| 14 |                                             |            | XML, JSON, and    | formats).                 |
| 15 |                                             |            | .NET Binary.      |                           |
| 16 | Interoperability (chapter 4)                |            | When using        | Official support: .NET,   |
| 17 |                                             |            | SOAP over HTTP.   | Java, Python, JavaScript, |
| 18 |                                             |            |                   | C/C++, Go, Rust, Ruby,    |
| 19 |                                             |            |                   | Swift, Dart, PHP.         |
| 20 |                                             |            |                   | Unofficial support for    |
| 21 |                                             |            |                   | other languages from      |
| 22 |                                             |            |                   | the community.            |
| 23 | Networking (chapter 4)                      |            | Configured at run | HTTP/2, currently over    |
| 24 |                                             |            | time. Switch      | TCP only with ASP.NET     |
| 25 |                                             |            | between NetTCP,   | Core gRPC.                |
| 26 |                                             |            | HTTP, and         |                           |
| 27 |                                             |            | MSMQ.             |                           |