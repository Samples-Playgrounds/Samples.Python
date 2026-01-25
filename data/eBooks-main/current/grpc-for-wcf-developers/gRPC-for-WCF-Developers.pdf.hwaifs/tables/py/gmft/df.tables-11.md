|    | WCF                                                           |                  | gRPC      |
|---:|:--------------------------------------------------------------|:-----------------|:----------|
|  0 | Regular request/reply                                         | Unary            | nan       |
|  1 | Duplex service with session using a client callback interface | Server streaming | nan       |
|  2 | Full duplex service with session                              | Bidirectional    | streaming |
|  3 | One-way operations                                            | Client streaming | nan       |