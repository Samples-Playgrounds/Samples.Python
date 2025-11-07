|    | public class EventToCommandBehavior : BindableBehavior<View>          |
|---:|:----------------------------------------------------------------------|
|  0 | {                                                                     |
|  1 | ...                                                                   |
|  2 | protected override void OnAttachedTo(View visualElement)              |
|  3 | {                                                                     |
|  4 | base.OnAttachedTo(visualElement);                                     |
|  5 | nan                                                                   |
|  6 | var events = AssociatedObject.GetType().GetRuntimeEvents().ToArray(); |
|  7 | if (events.Any())                                                     |
|  8 | {                                                                     |
|  9 | _eventInfo = events.FirstOrDefault(e => e.Name == EventName);         |
| 10 | if (_eventInfo == null)                                               |
| 11 | throw new ArgumentException(string.Format(                            |
| 12 | "EventToCommand: Can't find any event named '{0}' on attached type",  |
| 13 | EventName));                                                          |
| 14 | nan                                                                   |
| 15 | AddEventHandler(_eventInfo, AssociatedObject, OnFired);               |
| 16 | }                                                                     |
| 17 | }                                                                     |
| 18 | nan                                                                   |
| 19 | protected override void OnDetachingFrom(View view)                    |
| 20 | {                                                                     |
| 21 | if (_handler != null)                                                 |
| 22 | _eventInfo.RemoveEventHandler(AssociatedObject, _handler);            |
| 23 | nan                                                                   |
| 24 | base.OnDetachingFrom(view);                                           |
| 25 | }                                                                     |
| 26 | nan                                                                   |
| 27 | private void AddEventHandler(                                         |
| 28 | EventInfo eventInfo, object item, Action<object, EventArgs> action)   |
| 29 | {                                                                     |
| 30 | ...                                                                   |
| 31 | }                                                                     |
| 32 | nan                                                                   |
| 33 | private void OnFired(object sender, EventArgs eventArgs)              |
| 34 | {                                                                     |
| 35 | ...                                                                   |
| 36 | }                                                                     |
| 37 | }                                                                     |