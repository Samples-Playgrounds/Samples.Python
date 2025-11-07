|    | UnregisterEvent();                                                                 |
|---:|:-----------------------------------------------------------------------------------|
|  0 | nan                                                                                |
|  1 | var eventName = EventName;                                                         |
|  2 | if (View is null || string.IsNullOrWhiteSpace(eventName))                          |
|  3 | {                                                                                  |
|  4 | return;                                                                            |
|  5 | }                                                                                  |
|  6 | nan                                                                                |
|  7 | eventInfo = View.GetType()?.GetRuntimeEvent(eventName) ??                          |
|  8 | throw new ArgumentException($"{nameof(EventToCommandBehavior)}: Couldn't           |
|  9 | resolve the event.", nameof(EventName));                                           |
| 10 | nan                                                                                |
| 11 | ArgumentNullException.ThrowIfNull(eventInfo.EventHandlerType);                     |
| 12 | ArgumentNullException.ThrowIfNull(eventHandlerMethodInfo);                         |
| 13 | nan                                                                                |
| 14 | eventHandler = eventHandlerMethodInfo.CreateDelegate(eventInfo.EventHandlerType,   |
| 15 | this) ??                                                                           |
| 16 | throw new ArgumentException($"{nameof(EventToCommandBehavior)}: Couldn't create    |
| 17 | event handler.", nameof(EventName));                                               |
| 18 | nan                                                                                |
| 19 | eventInfo.AddEventHandler(View, eventHandler);                                     |
| 20 | }                                                                                  |
| 21 | nan                                                                                |
| 22 | void UnregisterEvent()                                                             |
| 23 | {                                                                                  |
| 24 | if (eventInfo is not null && eventHandler is not null)                             |
| 25 | {                                                                                  |
| 26 | eventInfo.RemoveEventHandler(View, eventHandler);                                  |
| 27 | }                                                                                  |
| 28 | nan                                                                                |
| 29 | eventInfo = null;                                                                  |
| 30 | eventHandler = null;                                                               |
| 31 | }                                                                                  |
| 32 | nan                                                                                |
| 33 | /// <summary>                                                                      |
| 34 | /// Virtual method that executes when a Command is invoked                         |
| 35 | /// </summary>                                                                     |
| 36 | /// <param name="sender"></param>                                                  |
| 37 | /// <param name="eventArgs"></param>                                               |
| 38 | [Microsoft.Maui.Controls.Internals.Preserve(Conditional = true)]                   |
| 39 | protected virtual void OnTriggerHandled(object? sender = null, object? eventArgs = |
| 40 | null)                                                                              |
| 41 | {                                                                                  |
| 42 | var parameter = CommandParameter                                                   |
| 43 | ?? EventArgsConverter?.Convert(eventArgs, typeof(object), null, null);             |
| 44 | nan                                                                                |
| 45 | var command = Command;                                                             |
| 46 | if (command?.CanExecute(parameter) ?? false)                                       |
| 47 | {                                                                                  |
| 48 | command.Execute(parameter);                                                        |
| 49 | }                                                                                  |
| 50 | }                                                                                  |
| 51 | }                                                                                  |