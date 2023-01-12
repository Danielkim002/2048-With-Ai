# 2048-With-Ai
This project was initially created with the Artificial Intelligence Association club from CSUN.
As the club president who reinstated the club and as someone who has no experience with making neural networks I decide to choose a project
that sounded easy. 2048 is a simple 4x4 matrix game where you choose which direction to move the board to combine the numbers on the board.
After the initial start of the club we quickly recreated the game.

Justin created all of the graphics to showcase the game in C#.

Elliot Fayman created the logic that the 2048 game follows in Python.

Due to family circumstances after just reinstating the club and beginning the club's first project I needed to change universities and allocate more time
to focus on familial concerns. Due to a lack of time to establish leadership and any connections within the newly reinstated club the project and club fell by the 
wayside. After graduating the university I had transfered to, I now have more time to pick up and finish this project.

The NN in this project will be trained off of the NEAT protocol using the neat-python extention. 
There will be 16 input neurons(this is the game board),
and 4 output neurons(these will decide the NN move)

Fitness calculation used:

(largest_value*3) + (second_largest_value*2) + (third_largest_value*1)

2048 is a partially luck based game, we cannot feed mathematically perfect moves into our algorithm, and as such NEAT is 
one of the best ways to teach this neural network.

The list below is a list of different attempts and the reasoning behind those attempts.


#ATTEMPTS MADE

---------Initial NN can read the board, and return a 4 list tuple, application then picks the highest value and uses that index as the turn.
If the highest value is a direction that does not change the board, the NN is awarded -3000 fitness score and the game is terminated.
If the game were not terminated then the application would be stuck in an infinite loop of trying to move where it can't.
Initial attempts of this NN strategy resulted in the largest fitness scores of 172, which means that largest value on the board was 32
Thinking the issue was due to number of generations run, i set the NN to run a population of 10,000 genomes for 1,000 generations, this took 13 hours to run.
For the first 500 generations the largest values were once again 172, with wildly varying results each run of the game. after 700 generations there were occasional games of above 500 fitness scores, the final fitness score was in the 400, meaning the final generation had a game where the highest value was 128. This is highly exciting, however this was alot of time for a small improvement, changes must be made to allow for more efficient training.

----------New NN will functioned the same as the other NN however it is given "training wheels". Rather that losing the game when the wrong direction is picked, if the NN picks a direction that can't be picked, then the next highest value will be picked for the NN by the application. the final saved fitness score was 1124 and the best fitness in the entire run was 1857. This was after a generation of 5,000 genomes and 500 generations(5 hours). This result while wildly higher than the initial attempt is frankly dissapointing, the reason it is dissapointing is that the first 100 generations were already seeing scores of 700, meaning that throughout the learning process the NN did not improve substantially.

-----------train the "training wheels" NN with the fitness being the average of 100 games rather than the fitness being one game. this will hopefully cause the Neat algorithm to pick NN that play more consistantly, and in result this could hopefully cause more steady growth between generations. This attempt failed, I tried to have 500 generations, a population of 2500 and the fitness be an average of 50 games. after 10 hours of calculating each gneration the fitness was on average 200, in the generation was in the 160s. when I went to sleep my computer began to update automatically and the learning process was halted. 

          Lessons Learned:
          -create fail safes such as a save state that saves the most recent generation so in event of failure continuation is an option

#ATTEMPTS TO BE MADE




----------Recreate the initial NN however this time rather than giving each NN one attempt to play the game, I think the NN should be given 10-100 attempts, and the average fitness of those games should be used as the final fitness(Using the average should hypothetically create an AI that can play consistantly well)(Using a maximum of the games should hypothetically create an AI that can play the game incredibly well when it gets lucky). Allowing the NN to play a multitude of games would allow for the NN to play more games to see how well they play consistantly.

-----------Copy the initial attempt, however this time emphasize the biase to change the weights between generations to allow more diverse NN. The original NN was commonly getting to a size of (5,35), meaning having a higher neuron addition and subtraction bias would not change the performance of the training session.






