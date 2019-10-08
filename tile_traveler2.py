user_pos = [1,1]
prev_pos = [0,0]
victory_pos = [3,1]

def checkPos(position):
  """Checks user current position and tells them available directions"""
  # positions are: [Col, Row], user starts in bottom left corner.
  # hardcoded room directions, the directions are [N,W,E,S]
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
    
def coin_lever(position, coin_count):
  """Check if there is a lever in current location, adds to coin coint if pulled"""
  lever_locations = [[1,2], [2,2], [2,3], [3,2]]
  if position in lever_locations:
    pull_lever = input('Pull a lever (y/n): ').lower()
    if pull_lever == 'y':   
      coin_count += 1
      print("You received 1 coin, your total is now {}.".format(coin_count))
      return coin_count
  return coin_count

def check_move(current_pos, available_directions, direction):
  """Checks if user can move into desired direction"""
  dir_strings = ['n','w','e', 's']
  #converts the available_directions to match the input to be compared
  for i in range(4):
    if available_directions[i] == True:
      available_directions[i] = dir_strings[i]
  #if direction was available, then it should be found
  if direction in available_directions:
    #update the position
    #north +
    if direction == "n":
        current_pos[1] += 1
    #south -
    elif direction == "s":
        current_pos[1] -= 1
    #east +
    elif direction == "e":
        current_pos[0] += 1
    #west -
    elif direction == "w":
        current_pos[0] -= 1
    return current_pos
  else: 
    print("Not a valid direction!")
    return False

def move_player(current_pos, avalable_directions):
  """Handles player movement"""

def ask_direction(current_pos, current_directions):
  invalid_direction = True
  list_directions = current_directions[0]
  available_directions = current_directions[1]
  while invalid_direction:
    print(' or '.join(available_directions))
    direction = input("Direction: ").lower()
    check = check_move(current_pos, list_directions, direction)
    if check != False:
      invalid_direction = False
      return direction

def play():
  game_loop = True  
  coin_count = 0
  while game_loop:

    if user_pos[0] == 3 and user_pos[1] == 1:
      #quits game if player wins.
      print("Victory! Total coins {}.".format(coin_count))

      game_loop = False
    else:
      coin_count = coin_lever(user_pos, coin_count)
      #else checks for available directions.
      current_directions = checkPos(user_pos)

      #Asks the player for input directions, loops if invalid
      move_player = ask_direction(user_pos,current_directions)

      # Updates postions, change this
      prev_pos = move_player
      

    
play()