|    | <Grid Grid.Column="1" HorizontalOptions="Center">                                  |
|---:|:-----------------------------------------------------------------------------------|
|  0 | <Label Text="REGISTER" TextColor="Gray"/>                                          |
|  1 | <Grid.GestureRecognizers>                                                          |
|  2 | <TapGestureRecognizer Command="{Binding RegisterCommand}" NumberOfTapsRequired="1" |
|  3 | />                                                                                 |
|  4 | </Grid.GestureRecognizers>                                                         |
|  5 | </Grid>                                                                            |