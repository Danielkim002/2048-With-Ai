import random
import time
import numpy as np
from random import randrange
from copy import deepcopy
import json


class Neural_network:
    input_layer = np.array(([0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]), dtype=float)
    exit_layer = np.array(([.1236745], [.234157856], [.89], [.2432]), dtype=float)

    def accept_game_matrix(self, input):
        self.input_layer = input

    # finds the largest value in exit layer and sends that node number
    def send_game_move(self):
        ret = 0
        count = 0
        highest = self.exit_layer[0]
        for i in self.exit_layer:
            if i > highest:
                ret = count
                highest = i
            count += 1
        return ret


class Game:
    # game matrix is a touple, game matrix size never changes only values change
    game_matrix = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    game_over = False

    def find_largest_number(self):
        max = self.game_matrix[0][0]
        for i in self.game_matrix:  # i is array
            for u in i:  # u is number in each array
                if u > max:
                    max = u
        return max

    def print_game_state(self, matrix):
        largest_digits = len(str(self.find_largest_number()))
        spaces = 0
        row = ""
        for i in matrix:
            for u in i:
                row += "["
                spaces = largest_digits - len(str(u))
                row += str(u)
                for x in range(0, spaces):
                    row += " "
                row += "] "
            row += "\n"
        print(row)

    def new_block(self, val):
        emptySpace = len(self.game_matrix) * len(self.game_matrix[0])
        for i in range(len(self.game_matrix)):
            for j in range(len(self.game_matrix[0])):
                if self.game_matrix[i][j] != 0:
                    emptySpace -= 1
        if emptySpace == 0:
            return
        while True:
            valueLoc = random.randint(1, len(self.game_matrix) * len(self.game_matrix[0]))
            for x in range(len(self.game_matrix)):
                for y in range(len(self.game_matrix[0])):
                    if valueLoc == (x * 4) + (y + 1) and self.game_matrix[x][y] != 0:
                        valueLoc += 1
                    elif valueLoc == (x * 4) + (y + 1):
                        # mat[x][y] = random.randint(1, 2) * 2
                        # Commenting it out as 2 for now
                        self.game_matrix[x][y] = val
                        return

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
            print("Left")
        elif input == 1:
            updatedMatrix = self.move_right()
            print("Right")
        if input == 2:
            updatedMatrix = self.move_down()
            print("Down")
        elif input == 3:
            updatedMatrix = self.move_up()
            print("Up")

        did_move = True
        if updatedMatrix == self.game_matrix:
            did_move = False
        self.game_matrix = updatedMatrix
        return did_move

        # implements player move and moves board accordingly

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


game = Game()
NN = Neural_network()

"""
print("sending game matrix as numpy array")
print(game.send_game_matrix())
print()
print("current NN input layer")
print(NN.input_layer)
print("recieving and storing game matrix")
NN.accept_game_matrix(game.send_game_matrix())
print("")
print("new NN input layer")
print(NN.input_layer)
print()
print("sending ai move, should be 2")
print(NN.send_game_move())

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
        time.sleep(0.05)
    scores.append(game.find_largest_number())
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
