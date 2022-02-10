def check_game_state(mat):
  if player_turn("up", mat) == mat and player_turn("down", mat) == mat and player_turn("left", mat) == mat and player_turn("right", mat) == mat: 
    return False
  return True