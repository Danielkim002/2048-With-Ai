import gzip
import os
import random
import time
import numpy as np
from random import randrange
from copy import deepcopy
import json
import neat
import pickle


class Game:
    #game matrix is a touple, game matrix size never changes only values change
    

    
    def __init__(self, matrix = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])):
        self.game_matrix = matrix
        self.game_over = False

    def set_game_matrix(self, game_matrix_inp):
        self.game_matrix = game_matrix_inp

    def find_largest_number(self):
        max = self.game_matrix[0][0]
        for i in self.game_matrix:  # i is array
            for u in i:  # u is number in each array
                if u > max:
                    max = u
        return max

    def print_game_state(self):
        largest_digits = len(str(self.find_largest_number()))
        spaces = 0
        
        row = ""
        for i in self.game_matrix:
            for u in i:
                row += "["
                spaces = largest_digits - len(str(u))
                row += str(u)
                for x in range(0, spaces):
                    row += " "
                row += "] "
            row += "\n"
        print(row)

    def random_starting_board(self):
        self.game_matrix = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
        self.New_Block()
        self.New_Block()

    def New_Block(self):
        mat = self.game_matrix
        emptySpace = len(mat)*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] != 0):
                    emptySpace -=1
        if emptySpace == 0: return mat
        while True:
            valueLoc = random.randint(1, len(mat)*len(mat[0]))
            for x in range(len(mat)):
                for y in range(len(mat[0])):
                    if valueLoc == (x*4)+(y+1) and mat[x][y] != 0:
                        valueLoc+=1
                    elif (valueLoc == (x*4)+(y+1)):
                        mat[x][y] = random.randint(1, 2)*2
                        return mat



    def move_left(self):
        moved_matrix = deepcopy(self.game_matrix)
        # Step 1: Get the value at the left-most position and save its position
        for row in range(4):
            pos = 0
            val_at_pos = moved_matrix[row][pos]
            # Step 2: Iterate from left to right of the row
            for index in range(4):
                # Step 3: Get the value at the current index
                val_at_index = moved_matrix[row][index]
                # Ignore all cases where value at index is 0, and the beginning case
                if index != pos and val_at_index != 0:
                    # Step 5: Check all possible cases:
                    #   If value at position is equal to value at index
                    #   If value at position is equal to 0
                    #   If value at position is not equal to value at index

                    # Case when value at position value is equal to value at index
                    # Multiplies the value at position by two and deletes value at index
                    # Shifts position by one to the right and sets new value at position
                    if val_at_index == val_at_pos:
                        moved_matrix[row][pos] *= 2
                        moved_matrix[row][index] = 0
                        pos += 1
                        val_at_pos = moved_matrix[row][pos]
                    # Case when value at position is equal to 0
                    # Sets value at position to the value at index
                    # Deletes value at index
                    # Shifts position by one the right and sets new value at position
                    elif val_at_pos == 0:
                        moved_matrix[row][pos] = val_at_index
                        moved_matrix[row][index] = 0
                        val_at_pos = moved_matrix[row][pos]
                    # Case when value at position is not equal to value at position
                    # Shifts position by one to the right and sets new value at position
                    # Checks if new value at position is not 0
                    #   If new value position is 0,
                    #       Sets value at new position to the value at index
                    #       Deletes value at index
                    else:
                        pos += 1
                        val_at_pos = moved_matrix[row][pos]
                        if val_at_pos == 0:
                            moved_matrix[row][pos] = val_at_index
                            moved_matrix[row][index] = 0
                            val_at_pos = moved_matrix[row][pos]
        return moved_matrix

    def move_right(self):
        moved_matrix = deepcopy(self.game_matrix)
        for row in range(4):
            pos = 3
            val_at_pos = moved_matrix[row][pos]
            for index in range(4):
                val_at_index = moved_matrix[row][3 - index]
                if (3 - index) != pos and val_at_index != 0:
                    if val_at_index == val_at_pos:
                        moved_matrix[row][pos] *= 2
                        moved_matrix[row][3 - index] = 0
                        pos -= 1
                        val_at_pos = moved_matrix[row][pos]
                    elif val_at_pos == 0:
                        moved_matrix[row][pos] = val_at_index
                        moved_matrix[row][3 - index] = 0
                        val_at_pos = moved_matrix[row][pos]
                    else:
                        pos -= 1
                        val_at_pos = moved_matrix[row][pos]
                        if val_at_pos == 0:
                            moved_matrix[row][pos] = val_at_index
                            moved_matrix[row][3 - index] = 0
                            val_at_pos = moved_matrix[row][pos]
        return moved_matrix

    def move_up(self):
        moved_matrix = deepcopy(self.game_matrix)
        for column in range(4):
            pos = 0
            val_at_pos = moved_matrix[pos][column]
            for index in range(4):
                val_at_index = moved_matrix[index][column]
                if index != pos and val_at_index != 0:
                    if val_at_index == val_at_pos:
                        moved_matrix[pos][column] *= 2
                        moved_matrix[index][column] = 0
                        pos += 1
                        val_at_pos = moved_matrix[pos][column]
                    elif val_at_pos == 0:
                        moved_matrix[pos][column] = val_at_index
                        moved_matrix[index][column] = 0
                        val_at_pos = moved_matrix[pos][column]
                    else:
                        pos += 1
                        val_at_pos = moved_matrix[pos][column]
                        if val_at_pos == 0:
                            moved_matrix[pos][column] = val_at_index
                            moved_matrix[index][column] = 0
                            val_at_pos = moved_matrix[pos][column]
        return moved_matrix

    def move_down(self):
        moved_matrix = deepcopy(self.game_matrix)
        for column in range(4):
            pos = 3
            val_at_pos = moved_matrix[pos][column]
            for index in range(4):
                val_at_index = moved_matrix[3 - index][column]
                if (3 - index) != pos and val_at_index != 0:
                    if val_at_index == val_at_pos:
                        moved_matrix[pos][column] *= 2
                        moved_matrix[3 - index][column] = 0
                        pos -= 1
                        val_at_pos = moved_matrix[pos][column]
                    elif val_at_pos == 0:
                        moved_matrix[pos][column] = val_at_index
                        moved_matrix[3 - index][column] = 0
                        val_at_pos = moved_matrix[pos][column]
                    else:
                        pos -= 1
                        val_at_pos = moved_matrix[pos][column]
                        if val_at_pos == 0:
                            moved_matrix[pos][column] = val_at_index
                            moved_matrix[3 - index][column] = 0
                            val_at_pos = moved_matrix[pos][column]
        return moved_matrix

    def player_turn(self, input):
        # Move values around the board depending on given input
        # Follows the game rules of 2048, will only add numbers if the neighboring value is the same value
        # If value are not the same, stop digit from moving further in that direction
        # Assume that 0 is an empty space and allow free movement on these spots

        # Assume that the board size is always 4x4
        updatedMatrix = deepcopy(self.game_matrix)
        if input == 0:
            updatedMatrix = self.move_left()
            #print("Left")
        elif input == 1:
            updatedMatrix = self.move_right()
            #print("Right")
        if input == 2:
            updatedMatrix = self.move_down()
            #print("Down")
        elif input == 3:
            updatedMatrix = self.move_up()
            #print("Up")
        
        did_move = True
        if updatedMatrix == self.game_matrix:
            did_move = False
        self.game_matrix = updatedMatrix
        updatedMatrix = self.New_Block()
        return did_move

        # implements player move and moves board accordingly

    #returns true if the game is over
    def check_game_state(self, mat):
        if self.move_up() == mat and self.move_down() == mat and self.move_left() == mat and self.move_right() == mat:
            return True
        return False

    def send_game_matrix(self):
        name = []
        ret = np.array((), dtype=float)
        for i in self.game_matrix:
            for u in i:
                name.append(u)
        ret1 = np.array(name)
        ret = ret1.reshape(16, 1)
        return ret
    
    def fitness_func(self):
        one = 0
        two = 0
        three = 0
        for i in self.game_matrix:
            
            for u in i:
                #print("u: ", u ,"\n one = " , one , ":: two = " , two, ":: three = " , three)
                if u>one:
                    three = two
                    two = one
                    one = u
                    continue
                if u>two:
                    three = two
                    two = u
                    continue
                if u>three:
                    three = u
                    continue
        return 3*one + 2*two + 1*three

def playGameUntilEnd(matrix): #This function will play the game until there is a game over
                        #This function will return the final board, as well as the number of turns it took to reach this point.
    game1 = Game()
    
    game1.set_game_matrix(deepcopy(matrix))
    next_turn = controlAlgorithm.nextMove(game1.game_matrix)
    num_turns = 0
    while next_turn != -1:
        game1.player_turn(next_turn)
        num_turns += 1
        #game1.print_game_state()
        
        next_turn = controlAlgorithm.nextMove(game1.game_matrix)
    return game1.game_matrix, num_turns


#This class contains a bair bone algorithm to play the game
#If the board can move down then move down, if it cant do that move left,
#  if if cant do that move right, if it cant do that move up
class controlAlgorithm:
    
    def nextMove(game_matrix):
        game = Game(game_matrix)
        
        if game.move_down() != game_matrix:
            return 2
        elif game.move_left() != game_matrix:
            return 0
        elif game.move_right() != game_matrix:
            return 1
        elif game.move_up() != game_matrix:
            return 3
        else:
            #print("Game over!!")
            return -1
#this function will contain the 2048 "game" that will be run every time for every generation




def main(genomes,config):
    game = Game()
    for genome_id,genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        genome.fitness = 0
        game.random_starting_board()
        
        while not game.check_game_state(game.game_matrix):
            
            output = net.activate(  tuple( x for y in game.game_matrix for x in y )  )
            
            
            if not game.player_turn(output.index(max(output))):
                genome.fitness -= 100
                break

            #print(game.fitness_func())
        genome.fitness += game.fitness_func()
        #print("genome " + genome_id + "finished")
    #print("one generation done?")
            


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet,
    neat.DefaultStagnation,config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,500)
    print('\nBest genome:\n{!s}'.format(winner))


        
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "Neat_config_2048.txt")
    run(config_path)









##Code below is an altered main() function that was a part of a commit that broke the entire program
'''def main(genomes,config):
    game = Game()
    allowed_mistakes = 3
    
    for genome_id,genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        genome.fitness = 0
        game.random_starting_board()
        #mistakes_made = 0
        while not game.check_game_state(game.game_matrix):
            
            output = net.activate(  tuple( x for y in game.game_matrix for x in y )  )

            if not game.player_turn(output.index(max(output))):
                genome.fitness -= 100
                break
            
            output_sorted = sorted(output,reverse = True)
            first_move_bool_value = game.player_turn(output.index(max(output)))
            if not first_move_bool_value and allowed_mistakes <= mistakes_made:
                genome.fitness -= 100
                break
            else:
                for i in output_sorted:
                    if not game.player_turn(output.index(i)):
                        genome.fitness -=10
                        mistakes_made += 1
                    else:
                        break
            

            #print(first_move_bool_value , " + " , mistakes_made)
        genome.fitness += game.fitness_func()
        #print("genome " + genome_id + "finished")
    #print("one generation done?")
            
'''

'''
g1 = Game()
g1.random_starting_board()

all_turns = [None] * 1000

for i in range(1000):
    
    v = playGameUntilEnd(g1.game_matrix)[1]
    #g1.game_matrix
    all_turns[i] = v
    
print(all_turns)
print("average = " ,sum(all_turns)/len(all_turns))
   '''     







"""

scores = []
start = time.time()
for instance in range(1):
    game = Game()
    game.new_block(2)
    game.new_block(2)
    while not game.game_over:
        game.print_game_state(game.game_matrix)
        move = randrange(0, 4)
        if game.player_turn(move):
            game.new_block(2)
        game.game_over = game.check_game_state(game.game_matrix)
        json_format = json.dumps(game.game_matrix)
        print(json_format)
        with open('GamePanel.json', 'w') as f:
            f.write(json_format)
        time.sleep(1)
    scores.append(game.find_largest_number())
"""

"""
stop = time.time()
print(stop - start)
print(scores)
max = 0
average = 0
for index in scores:
    if max < index:
        max = index
    average += index
print(max)
print(average / len(scores))
"""
