import random
init_seed = int(input("Input seed: "))
random.seed(init_seed)



def checkPos(position):
  """Checks user current position and tells them available directions"""
  # positions are: [Col, Row], user starts in bottom left corner.
  # the directions are [N,W,E,S]
  available_dir = []
  if position == [1,1]:
    available_dir = [True, False, False, False]
  elif position == [1,2]:
    available_dir = [True, True, False, True]
  elif position == [1,3]:
    available_dir = [False, True, False, True]
  elif position == [2,1]:
    available_dir = [True, False, False, False]
  elif position == [2,2]:
    available_dir = [False, False, True, True]
  elif position == [2,3]:
    available_dir = [False, True, True, False]
  elif position == [3,1]:
    available_dir = [True, False, False, False]
  elif position == [3,2]:
    available_dir = [True, False, False, True]
  elif position == [3,3]:
    available_dir = [False, False, True, True]

  #create a list of directions for print
  directions = ['(N)orth', '(W)est', '(E)ast','(S)outh']
  string_directions = []
  for i in range(4):
    if available_dir[i] == True:
      string_directions.append(directions[i])

  #return the directions
  return [available_dir, string_directions]
     
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
      directions = ['(N)orth', '(W)est', '(E)ast','(S)outh']
      available_directions = checkPos(user_pos)
      #check if
      for i in range(4):
        if available_directions[i] == True:
          directions_string += 

      if prev_pos != user_pos:
        coin_count = coin_lever(user_pos, coin_count)
      
      #Prints available directions
      print(' or '.join(available_directions[1]))

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