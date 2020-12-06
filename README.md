# Football Team Picker
A Tensorflow ML algorithm to optimize the picking of 5 a side football team

The idea is to train a model, based on previous results to pick perfectly balanced teams for a 5-a-side game. The
beauty of the neural network approach used is that it should be able to pick up subtleties from the data, such
as players that play well together, ones that don't and overall team structure (having a balance of hard working
and creative players).

THe model itself predicts who will win between two teams (arbitrarily called the 'black' and 'white' teams).

In order to pick the best players for a close match, I generated all the possible combinations of teams that could be
picked, generated a prediction for each, and chose the one most likely to be a draw (an output of 0.5 from the algo)


