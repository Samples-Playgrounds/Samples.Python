|    | public static class LineColorBehavior                        |
|---:|:-------------------------------------------------------------|
|  0 | {                                                            |
|  1 | ...                                                          |
|  2 | private static void OnApplyLineColorChanged(                 |
|  3 | BindableObject bindable, object oldValue, object newValue)   |
|  4 | {                                                            |
|  5 | var view = bindable as View;                                 |
|  6 | if (view == null)                                            |
|  7 | {                                                            |
|  8 | return;                                                      |
|  9 | }                                                            |
| 10 |                                                              |
| 11 | bool hasLine = (bool)newValue;                               |
| 12 | if (hasLine)                                                 |
| 13 | {                                                            |
| 14 | view.Effects.Add(new EntryLineColorEffect());                |
| 15 | }                                                            |
| 16 | else                                                         |
| 17 | {                                                            |
| 18 | var entryLineColorEffectToRemove =                           |
| 19 | view.Effects.FirstOrDefault(e => e is EntryLineColorEffect); |
| 20 | if (entryLineColorEffectToRemove != null)                    |
| 21 | {                                                            |
| 22 | view.Effects.Remove(entryLineColorEffectToRemove);           |
| 23 | }                                                            |
| 24 | }                                                            |
| 25 | }                                                            |
| 26 | }                                                            |