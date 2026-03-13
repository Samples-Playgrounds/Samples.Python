|    | {                                   |
|---:|:------------------------------------|
|  0 | "bindings": [                       |
|  1 | {                                   |
|  2 | "name": "myBlob",                   |
|  3 | "type": "blobTrigger",              |
|  4 | "direction": "in",                  |
|  5 | "path": "images/{name}",            |
|  6 | "connection": "AzureWebJobsStorage" |
|  7 | },                                  |
|  8 | {                                   |
|  9 | "name": "$return",                  |
| 10 | "type": "queue",                    |
| 11 | "direction": "out",                 |
| 12 | "queueName": "images",              |
| 13 | "connection": "AzureWebJobsStorage" |
| 14 | }                                   |
| 15 | ],                                  |
| 16 | "disabled": false                   |
| 17 | }                                   |