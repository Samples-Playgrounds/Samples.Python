|    | Component     | Description                                                                            |
|---:|:--------------|:---------------------------------------------------------------------------------------|
|  0 | Service       | Used by the service invocation building block to integrate with the hosting            |
|    | discovery     | environment to provide service-to-service discovery.                                   |
|  1 | State         | Provides a uniform interface to interact with a wide variety of state store            |
|    |               | implementations.                                                                       |
|  2 | Pub/sub       | Provides a uniform interface to interact with a wide variety of message bus            |
|    |               | implementations.                                                                       |
|  3 | Bindings      | Provides a uniform interface to trigger application events from external systems and   |
|    |               | invoke external systems with optional data payloads.                                   |
|  4 | Middleware    | Allows custom middleware to plug into the request processing pipeline and invoke       |
|    |               | additional actions on a request or response.                                           |
|  5 | Secret stores | Provides a uniform interface to interact with external secret stores, including cloud, |
|    |               | edge, commercial, open-source services.                                                |