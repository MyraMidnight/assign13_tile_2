import random

init_seed = int(input("Input seed: "))
random.seed(init_seed)



def checkPos(x, y):
    """Checks for possible directions for output."""
    N = 1
    W = 1
    E = 1
    S = 1

    if x == 2 and y != 3:
        E = 0
    if x == 2 and y == 1:
        W = 0
    if x == 2 and y == 2:
        N = 0
    if x == 2 and y == 3:
        S = 0
    if x == 3 and y != 3:
        W = 0
    if x == 1 and y == 1:
        W,E,S = 0,0,0
    if x == 1:
        W = 0
    if y == 1:
        S = 0
    if y == 3:
        N = 0
    if x == 3:
        E = 0
    return N,W,E,S

def travelNorth(x, y):
    if y == 3:
        invalid_direction()
        return [x,y]
    elif x == 2 and y == 2:
        invalid_direction()
        return [x,y]
    else:
        y += 1
        return [x,y]

def travelEast(x, y):
    if x == 3:
        invalid_direction()
        return [x,y]
    elif x == 2 and y != 3:
        invalid_direction()
        return [x,y]
    elif x == 1 and y == 1:
        invalid_direction()
        return [x,y]
    else:
        x += 1
        return [x,y]

def travelWest(x, y):
    if x == 1:
        invalid_direction()
        return [x,y]
    elif x == 2 and y == 1:
        invalid_direction()
        return [x,y]
    elif x == 3 and y != 3:
        invalid_direction()
        return [x,y]    
    else:
        x -= 1
        return [x,y]

def travelSouth(x, y):
    if y == 1:
        invalid_direction()
        return [x,y]
    elif x == 2 and y == 3:
        invalid_direction()
        return [x,y]    
    else:
        y -= 1
        return [x,y]

def invalid_direction():
    print("Not a valid direction!")
    


def coin_lever(position, coin_count):
  """Check if there is a lever in current location, adds to coin coint if pulled"""
  lever_locations = [[1,2], [2,2], [2,3], [3,2]]
  if position in lever_locations:
    
    pull_lever = random_lever()
    print('Pull a lever (y/n): {}'.format(pull_lever))
    if pull_lever == 'y':   
      coin_count += 1
      print("You received 1 coin, your total is now {}.".format(coin_count))
      return coin_count
  return coin_count


def random_movement():
  directions = ["n", "e", "s", "w"]
  move_choice = random.choice(directions)
  return move_choice

def random_lever():
  choices = ["y", "n"]
  lever_choice = random.choice(choices)
  return lever_choice


def play():
  game_loop = True  
  coin_count = 0
  user_pos = [1,1]
  prev_pos = [0,0]
  victory_pos = [3,1]
  total_move_count = 0


  while game_loop:

    
    if user_pos[0] == 3 and user_pos[1] == 1:
      #quits game if player wins.
      print("Victory! Total coins {}. Moves {}.".format(coin_count,total_move_count))
      game_loop = False
    else:
      #else checks for available directions.
      N,W,E,S = checkPos(user_pos[0], user_pos[1])
      

      if prev_pos != user_pos:
        coin_count = coin_lever(user_pos, coin_count)

      #Prints available directions
      if N == 1 and S == 1 and W == 1:
        print("You can travel: (N)orth or (W)est or (S)outh.")
      elif N == 1 and S == 1 and E == 1:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
      elif S == 1 and W == 1 and E == 1:
        print("You can travel: (E)ast or (W)est or (S)outh.")
      elif N == 1 and S == 1:
        print("You can travel: (N)orth or (S)outh.")
      elif N == 1 and W == 1:
        print("You can travel: (N)orth or (W)est.")
      elif N == 1 and E == 1:
        print("You can travel: (N)orth or (E)ast.")
      elif E == 1 and W == 1:
        print("You can travel: (E)ast or (W)est.")
      elif S == 1 and E == 1:
        print("You can travel: (E)ast or (S)outh.")
      elif S == 1 and W == 1:
        print("You can travel: (S)outh or (W)est.")
      elif N == 1:
        print("You can travel: (N)orth.")

      # Updates postions
      prev_pos[0] = user_pos[0]
      prev_pos[1] = user_pos[1]


      
      direct = random_movement()
      print("Direction: {}".format(direct))
      #call movement functions
      if direct == "n":
        user_pos[0], user_pos[1] = travelNorth(user_pos[0], user_pos[1])

      elif direct == "s":
        user_pos[0], user_pos[1] = travelSouth(user_pos[0], user_pos[1])

      elif direct == "e":
        user_pos[0], user_pos[1] = travelEast(user_pos[0], user_pos[1])

      elif direct == "w":
        user_pos[0], user_pos[1] = travelWest(user_pos[0], user_pos[1])
      
      total_move_count += 1

  play_continue = input("Play again (y/n): ")
  if play_continue == "y":
    play()
    
play()