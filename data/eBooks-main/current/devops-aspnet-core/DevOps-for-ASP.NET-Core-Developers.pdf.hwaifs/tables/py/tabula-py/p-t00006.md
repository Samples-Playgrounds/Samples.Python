|    | Feature     | Description           | Unnamed: 0   | GitHub Actions   | Unnamed: 1   | Azure Pipelines   |
|---:|:------------|:----------------------|:-------------|:-----------------|:-------------|:------------------|
|  0 | Environment | A collection of       | Yes          |                  | Yes          |                   |
|  1 | s           | resources to target   |              |                  |              |                   |
|  2 |             | or a logical          |              |                  |              |                   |
|  3 |             | environment           |              |                  |              |                   |
|  4 | Gates/Check | Automatic collection  | Yes          |                  | Yes          |                   |
|  5 | s           | and evaluation of     |              |                  |              |                   |
|  6 |             | signals to control    |              |                  |              |                   |
|  7 |             | continuation          |              |                  |              |                   |
|  8 | Jobs        | Sequence of steps     | Yes          |                  | Yes          |                   |
|  9 |             | that are executed on  |              |                  |              |                   |
| 10 |             | an agent              |              |                  |              |                   |
| 11 | Service     | Manage the lifecycle  | Yes          |                  | Yes          |                   |
| 12 | Containers  | of a containerized    |              |                  |              |                   |
| 13 |             | service instance      |              |                  |              |                   |
| 14 |             | available during a    |              |                  |              |                   |
| 15 |             | job                   |              |                  |              |                   |
| 16 | Service     | Abstract credentials  | No           |                  | Yes          |                   |
| 17 | Connections | to external systems   |              |                  |              |                   |
| 18 | Passwordles | Provide technologies  | Yes          |                  | No           |                   |
| 19 | s           | and support use       |              |                  |              |                   |
| 20 | connections | cases that reduce     |              |                  |              |                   |
| 21 | to cloud    | and potentially       |              |                  |              |                   |
| 22 | providers   | eliminate the use of  |              |                  |              |                   |
| 23 |             | passwords             |              |                  |              |                   |
| 24 | Stages      | Group jobs in a       | No           |                  | Yes          |                   |
| 25 |             | pipeline              |              |                  |              |                   |
| 26 | Templates   | Define reusable,      | Yes          |                  | Yes          |                   |
| 27 |             | parameterized         |              |                  |              |                   |
| 28 |             | building blocks for   |              |                  |              |                   |
| 29 |             | steps, jobs, or       |              |                  |              |                   |
| 30 |             | variables             |              |                  |              |                   |
| 31 | Starter     | Defines a starter     | Yes          |                  | No           |                   |
| 32 | Templates   | workflow based on     |              |                  |              |                   |
| 33 |             | the type of code      |              |                  |              |                   |
| 34 |             | detected in a         |              |                  |              |                   |
| 35 |             | repository            |              |                  |              |                   |
| 36 | Triggers    | Set of events that    | Yes          |                  | Yes          |                   |
| 37 |             | cause the pipeline to |              |                  |              |                   |
| 38 |             | trigger               |              |                  |              |                   |