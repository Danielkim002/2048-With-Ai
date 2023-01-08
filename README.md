# 2048-With-Ai
This project was initially created with the Artificial Intelligence Association club from CSUN
As the club president who reinstated the club and who has no experience with making neural networks I decide to choose a project
that sounded easy. 2048 is a simple 4x4 matrix game where you choose which direction to move the board to combine the numbers on the board.
After the initial start of the club we quickly recreated the game.

Justin created all of the graphics to showcase the game in C#.
Elliot Fayman created the logic that the 2048 game follows in Python.

Due to family circumstances after just reinstating the club and beginning the club's first project I needed to change universities and allocate more time
to focus on familial concerns. Due to a lack of time to establish leadership and any connections within the newly reinstated club the project fell by the 
wayside. After graduating the university I transfered to, I now have more time to pick up and finish this project.

The NN in this project will be trained off of the NEAT protocol using the neat-python extention. 
There will be 16 input neurons(this is the game board)
And there will be 4 output neurons(with all the possible moves we could do up, down, left, right)

Fitness calculation used:

(largest_value*3) + (second_largest_value*2) + (third_largest_value*1)

2048 is a partially luck based game, we cannot feed mathematically perfect moves into our algorithm, and as such NEAT is 
one of the best ways to teach this nearal network

The list below is a list of different attempts and the reasoning behind those attempts.


ATTEMPTS MADE:

---------Initial NN can read the board, and return a 4 list tuple, application then picks the highest value and uses that index as the turn.
If the highest value is a direction that does not change the board, the NN is awarded -3000 fitness score and the game is terminated.
If the game were not terminated then the application would be stuck in an infinite loop of trying to move where it can't.
Initial attempts of this NN strategy resulted in the largest fitness scores of 172, which means that largest value on the board was 32
Thinking the issue was due to number of generations run, i set the NN to run a population of 10,000 genomes for 1,000 generations, this took 13 hours to run.
For the first 500 generations the largest values were once again 172, with wildly varying results each run of the game. after 700 generations there were occasional games of above 300 fitness scores, the final fitness score was in the 400, meaning the final generation had a game where the highest value was 128. This is highly exciting, however this was alot of time for a small improvement, changes must be made to allow for more efficient training.

ATTEMPTS TO BE MADE

----------New NN will function the same as the other NN however it is given "training wheels". Rather that losing the game when the wrong direction is picked, if the NN picks a direction that can't be picked, then the next highest value will be picked for the NN by the application.

----------Recreate the initial NN however this time rather than giving each NN one attempt to play the game, I think the NN should be given 10-100 attempts, and the average fitness of those games should be used as the final fitness(Using the average should hypothetically create an AI that can play consistantly well)(Using a maximum of the games should hypothetically create an AI that can play the game incredibly well when it gets lucky). Allowing the NN to play a multitude of games would allow for the NN to play more games to see how well they play consistantly.

-----------Copy the initial attempt, however this time emphasize the biase to change the weights between generations to allow more diverse NN. The original NN was commonly getting to a size of (5,35), meaning having a higher neuron addition and subtraction bias would not change the performance of the training session.






