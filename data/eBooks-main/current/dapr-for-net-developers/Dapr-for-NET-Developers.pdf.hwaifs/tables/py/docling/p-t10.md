|    | Status           | Action                                                           |
|---:|:-----------------|:-----------------------------------------------------------------|
|  0 | SUCCESS          | The message is considered as processed successfully and dropped. |
|  1 | RETRY            | The message is retried.                                          |
|  2 | DROP             | A warning is logged and the message is dropped.                  |
|  3 | Any other status | The message is retried.                                          |