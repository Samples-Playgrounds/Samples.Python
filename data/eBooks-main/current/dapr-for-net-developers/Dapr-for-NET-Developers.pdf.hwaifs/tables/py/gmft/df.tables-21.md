|    |       |                                                                                                                                                 |
|---:|:------|:------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | 1.    | An exiting vehicle triggers the MQTT input binding that sends a message containing the vehicle license number, lane, and timestamp.             |
|  1 | 2.    | The MQTT input binding invokes the TrafficControl service with the message.                                                                     |
|  2 | 3.    | The TrafficControl service retrieves the state for the vehicle, appends the entry, and saves the updated vehicle state back to the state store. |
|  3 | 4.    | The TrafficControl service publishes the speeding violation using pub/sub to the speedingviolations topic.                                      |
|  4 | 5.    | The FineCollection service receives the speeding violation using a pub/sub subscription on the speedingviolations topic.                        |
|  5 | 6.    | The FineCollection service invokes the vehicleinfo endpoint of the VehicleRegistration service using service invocation.                        |
|  6 | 7.    | The FineCollection service invokes an output binding for sending the email.                                                                     |
|  7 | Click | any trace line (span) to see more details. If you click on the last line, you’ll see the sendmail                                               |