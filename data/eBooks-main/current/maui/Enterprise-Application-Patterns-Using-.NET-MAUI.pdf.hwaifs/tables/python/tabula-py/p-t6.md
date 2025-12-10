|    | /// <summary>                                                                               |
|---:|:--------------------------------------------------------------------------------------------|
|  0 | /// The <see cref="EventToCommandBehavior"/> is a behavior that allows the user to invoke a |
|  1 | <see cref="ICommand"/> through an event. It is designed to associate Commands to events     |
|  2 | exposed by controls that were not designed to support Commands. It allows you to map any    |
|  3 | arbitrary event on a control to a Command.                                                  |
|  4 | /// </summary>                                                                              |
|  5 | public class EventToCommandBehavior : BaseBehavior<VisualElement>                           |
|  6 | {                                                                                           |
|  7 | // Omitted for brevity...                                                                   |
|  8 |                                                                                             |
|  9 | /// <inheritdoc/>                                                                           |
| 10 | protected override void OnAttachedTo(VisualElement bindable)                                |
| 11 | {                                                                                           |
| 12 | base.OnAttachedTo(bindable);                                                                |
| 13 | RegisterEvent();                                                                            |
| 14 | }                                                                                           |
| 15 |                                                                                             |
| 16 | /// <inheritdoc/>                                                                           |
| 17 | protected override void OnDetachingFrom(VisualElement bindable)                             |
| 18 | {                                                                                           |
| 19 | UnregisterEvent();                                                                          |
| 20 | base.OnDetachingFrom(bindable);                                                             |
| 21 | }                                                                                           |
| 22 |                                                                                             |
| 23 | static void OnEventNamePropertyChanged(BindableObject bindable, object oldValue, object     |
| 24 | newValue)                                                                                   |
| 25 | => ((EventToCommandBehavior)bindable).RegisterEvent();                                      |
| 26 |                                                                                             |
| 27 | void RegisterEvent()                                                                        |
| 28 | {                                                                                           |