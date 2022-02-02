game_matrix = ([2048,1000000,2],[300,4,5],[6,7,8])

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

print_game_state(game_matrix)
