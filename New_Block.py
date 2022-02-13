#adds new blocks to game
import random
def New_Block(mat):
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
