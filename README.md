# 2048-With-Ai
This project will have two main steps
Step one will be to re create the game 2048, we do not need to have any fancy visuals
We just need to have a 4x4 matrix which we can feed to the neural network

Next we will need to train a neural network
There will be 16 input neurons(this is the game board)
And there will be 4 output neurons(with all the possible moves we could do up, down, left, right)

Because 2048 is a partially luck based game, we cannot feed mathematically perfect moves into our algorithm
The next best thing is to create a fitness function which will measure how well each ai does

The only way i am aware of how to apply a fitness function is by having a bunch of different ai's run, and after 100-300 or so turns
we keep the ai's with the greater fitness functions and replace the worse ones with ai's that only slightly differ
from the good ones

we can then run these ai's against ourselves and other basic ways to play the game and see if our network runs better
