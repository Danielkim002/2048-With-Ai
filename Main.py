class Game:
    game_matrix = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
    game_over = False

    def find_largest_number(matrix):
        max = matrix[0][0]
        for i in matrix: #i is array
            for u in i:#u is number in each array
                if u > max:
                    max = u
        return max

    def print_game_state(matrix):
        largest_digits = len(str(find_largest_number(matrix)))
        spaces = 0
        row = ""
        for i in matrix:

            for u in i:
                row +="["
                spaces = largest_digits-len(str(u))
                row += str(u)
                for x in range(0,spaces):
                    row += " "
                row += "] "
            row +="\n"
        print(row)

    def new_block():
        #finds which blocks are empty and randomly selects one to fill with either a 2 or a 4
        #if cant add a block, keep game matrix the same
        None

    def player_turn():
        #implements player move and moves board accordingly
        None

    def check_game_state():
        #checks if the game is over, if it isnt over, return False
        None

    game_matrix = new_block(game_matrix)
    while not game_over:
        
        print_game_state()
        player_turn()
        new_block()
        game_over = check_game_state()
