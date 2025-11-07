|    |       |                                                                                                                                                                 |
|---:|:------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 |       | http://localhost:<dapr-port>/v1.0/state/<store-name>/                                                                                                           |
|  1 | •     | <dapr-port>: the HTTP port that Dapr listens on.                                                                                                                |
|  2 | •     | <store-name>: the name of the state store component to use.                                                                                                     |
|  3 | state | Figure 5-1 shows how a Dapr-enabled shopping basket service stores a key/value pair using the Dapr store component named statestore.                            |
|  4 |       | :::image type=“content” source=“./media/state-management/state-management-flow.png” alt￾text=“Diagram of storing a key/value pair in a Dapr state store.”:::    |
|  5 |       | Figure 5-1. Storing a key/value pair in a Dapr state store.                                                                                                     |
|  6 |       | Note the steps in the previous figure:                                                                                                                          |
|  7 | 1.    | The basket service calls the state management API on the Dapr sidecar. The body of the request encloses a JSON array that can contain multiple key/value pairs. |
|  8 | 2.    | The Dapr sidecar determines the state store based on the component configuration file. In this case, it’s a Redis cache state store.                            |
|  9 | 3.    | The sidecar persists the data to the Redis cache.                                                                                                               |
| 10 | data  | Retrieving the stored data is a similar API call. In the example below, a curl command retrieves the by calling the Dapr sidecar API:                           |