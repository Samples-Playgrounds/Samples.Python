|    | Field    | Description                                      | Example                           |
|---:|:---------|:-------------------------------------------------|:----------------------------------|
|  0 | time     | ISO8601 formatted timestamp                      | 2021-01-10T14:19:31.000Z          |
|  1 | level    | Level of the entry (debug, info, warn, or error) | info                              |
|  2 | type     | Log Type                                         | log                               |
|  3 | msg      | Log Message                                      | metrics server started on :62408/ |
|  4 | scope    | Logging Scope                                    | dapr.runtime                      |
|  5 | instance | Hostname where Dapr runs                         | TSTSRV01                          |