game_matrix = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
game_over = False
def find_largest_number(matrix):
    max = matrix[0][0]
    for i in matrix:#i is array
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

def new_block(matrix):
    None
def player_turn(string,matrix):
    None
def player_move():
    #returns player move as a string making sure it is valid
    None
def check_game_state(matrix):
    #checks if the game is over, if it isnt over, return False
    None
    
while not game_over:
    game_matrix = new_block(game_matrix)
    print_game_state(game_matrix)
    player_turn(player_move(),game_matrix)
    game_over = check_game_state(game_matrix)
