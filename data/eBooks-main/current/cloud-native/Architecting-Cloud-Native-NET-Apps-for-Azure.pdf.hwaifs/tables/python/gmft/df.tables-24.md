|    | Policy          | Experience                                                                                        |
|---:|:----------------|:--------------------------------------------------------------------------------------------------|
|  0 | Retry           | Configures retry operations on designated operations.                                             |
|  1 | Circuit Breaker | Blocks requested operations for a predefined period when faults exceed a configured threshold     |
|  2 | Timeout         | Places limit on the duration for which a caller can wait for a response.                          |
|  3 | Bulkhead        | Constrains actions to fixed-size resource pool to prevent failing calls from swamping a resource. |
|  4 | Cache           | Stores responses automatically.                                                                   |
|  5 | Fallback        | Defines structured behavior upon a failure.                                                       |