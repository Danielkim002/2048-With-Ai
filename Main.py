import random
import time
from random import randrange


class Game:
    game_matrix = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    game_over = False

    def find_largest_number(self, matrix):
        max = matrix[0][0]
        for i in matrix:  # i is array
            for u in i:  # u is number in each array
                if u > max:
                    max = u
        return max

    def print_game_state(self, matrix):
        largest_digits = len(str(self.find_largest_number(matrix)))
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

    def new_block(self, mat):
        emptySpace = len(mat) * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (mat[i][j] != 0):
                    emptySpace -= 1
        if emptySpace == 0: return mat
        while True:
            valueLoc = random.randint(1, len(mat) * len(mat[0]))
            for x in range(len(mat)):
                for y in range(len(mat[0])):
                    if valueLoc == (x * 4) + (y + 1) and mat[x][y] != 0:
                        valueLoc += 1
                    elif valueLoc == (x * 4) + (y + 1):
                        # mat[x][y] = random.randint(1, 2) * 2
                        # Commenting it out as 2 for now
                        mat[x][y] = 2
                        return mat

    def moveRowLeft(self, row):
        # Step 1: Get the value at the left-most position and save its position
        pos = 0
        val_at_pos = self.game_matrix[row][pos]
        # Step 2: Iterate from left to right of the row
        for index in range(4):
            # Step 3: Get the value at the current index
            val_at_index = self.game_matrix[row][index]
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
                    self.game_matrix[row][pos] *= 2
                    self.game_matrix[row][index] = 0
                    pos += 1
                    val_at_pos = self.game_matrix[row][pos]
                # Case when value at position is equal to 0
                # Sets value at position to the value at index
                # Deletes value at index
                # Shifts position by one the right and sets new value at position
                elif val_at_pos == 0:
                    self.game_matrix[row][pos] = val_at_index
                    self.game_matrix[row][index] = 0
                    val_at_pos = self.game_matrix[row][pos]
                # Case when value at position is not equal to value at position
                # Shifts position by one to the right and sets new value at position
                # Checks if new value at position is not 0
                #   If new value position is 0,
                #       Sets value at new position to the value at index
                #       Deletes value at index
                else:
                    pos += 1
                    val_at_pos = self.game_matrix[row][pos]
                    if val_at_pos == 0:
                        self.game_matrix[row][pos] = val_at_index
                        self.game_matrix[row][index] = 0
                        val_at_pos = self.game_matrix[row][pos]

    def moveRowRight(self, row):
        pos = 3
        val_at_pos = self.game_matrix[row][pos]
        for index in range(4):
            val_at_index = self.game_matrix[row][3 - index]
            if (3 - index) != pos and val_at_index != 0:
                if val_at_index == val_at_pos:
                    self.game_matrix[row][pos] *= 2
                    self.game_matrix[row][3 - index] = 0
                    pos -= 1
                    val_at_pos = self.game_matrix[row][pos]
                elif val_at_pos == 0:
                    self.game_matrix[row][pos] = val_at_index
                    self.game_matrix[row][3 - index] = 0
                    val_at_pos = self.game_matrix[row][pos]
                else:
                    pos -= 1
                    val_at_pos = self.game_matrix[row][pos]
                    if val_at_pos == 0:
                        self.game_matrix[row][pos] = val_at_index
                        self.game_matrix[row][3 - index] = 0
                        val_at_pos = self.game_matrix[row][pos]

    def moveColumnUp(self, column):
        pos = 0
        val_at_pos = self.game_matrix[pos][column]
        for index in range(4):
            val_at_index = self.game_matrix[index][column]
            if index != pos and val_at_index != 0:
                if val_at_index == val_at_pos:
                    self.game_matrix[pos][column] *= 2
                    self.game_matrix[index][column] = 0
                    pos += 1
                    val_at_pos = self.game_matrix[pos][column]
                elif val_at_pos == 0:
                    self.game_matrix[pos][column] = val_at_index
                    self.game_matrix[index][column] = 0
                    val_at_pos = self.game_matrix[pos][column]
                else:
                    pos += 1
                    val_at_pos = self.game_matrix[pos][column]
                    if val_at_pos == 0:
                        self.game_matrix[pos][column] = val_at_index
                        self.game_matrix[index][column] = 0
                        val_at_pos = self.game_matrix[pos][column]

    def moveColumnDown(self, column):
        pos = 3
        val_at_pos = self.game_matrix[pos][column]
        for index in range(4):
            val_at_index = self.game_matrix[3 - index][column]
            if (3 - index) != pos and val_at_index != 0:
                if val_at_index == val_at_pos:
                    self.game_matrix[pos][column] *= 2
                    self.game_matrix[3 - index][column] = 0
                    pos -= 1
                    val_at_pos = self.game_matrix[pos][column]
                elif val_at_pos == 0:
                    self.game_matrix[pos][column] = val_at_index
                    self.game_matrix[3 - index][column] = 0
                    val_at_pos = self.game_matrix[pos][column]
                else:
                    pos -= 1
                    val_at_pos = self.game_matrix[pos][column]
                    if val_at_pos == 0:
                        self.game_matrix[pos][column] = val_at_index
                        self.game_matrix[3 - index][column] = 0
                        val_at_pos = self.game_matrix[pos][column]

    def player_turn(self, input):
        # Move values around the board depending on given input
        # Follows the game rules of 2048, will only add numbers if the neighboring value is the same value
        # If value are not the same, stop digit from moving further in that direction
        # Assume that 0 is an empty space and allow free movement on these spots

        # Assume that the board size is always 4x4

        if input == 0:
            for row in range(4):
                Game.moveRowLeft(self, row)
            print("Left")
        elif input == 1:
            for row in range(4):
                Game.moveRowRight(self, row)
            print("Right")
        if input == 2:
            for row in range(4):
                Game.moveColumnDown(self, row)
            print("Down")
        elif input == 3:
            for row in range(4):
                Game.moveColumnUp(self, row)
            print("Up")

        # implements player move and moves board accordingly
        None

    def check_game_state(self, mat):
        if self.player_turn("up", mat) == mat and self.player_turn("down", mat) == mat and self.player_turn("left",
                                                                                                            mat) == mat and self.player_turn(
            "right", mat) == mat:
            return False
        return True
        None

    def __init__(self):
        game_matrix = self.new_block(self.game_matrix)
        game_matrix = self.new_block(self.game_matrix)
        while not self.game_over:
            self.print_game_state(self.game_matrix)
            t = randrange(0, 4)
            self.player_turn(t)
            self.new_block(self.game_matrix)
            time.sleep(0.5)
            # game_over = self.check_game_state()

    pass


game = Game()
