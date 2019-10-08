user_pos = [1,1]
prev_pos = [0,0]
victory_pos = [3,1]
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
		print("Not a valid direction!")
		return [x,y]
	elif x == 2 and y == 2:
		print("Not a valid direction!")
		return [x,y]
	else:
		y += 1
		return [x,y]

def travelEast(x, y):
	if x == 3:
		print("Not a valid direction!")
		return [x,y]
	elif x == 2 and y != 3:
		print("Not a valid direction!")
		return [x,y]
	else:
		x += 1
		return [x,y]

def travelWest(x, y):
	if x == 1:
		print("Not a valid direction!")
		return [x,y]
	elif x == 2 and y == 1:
		print("Not a valid direction!")
		return [x,y]
	elif x == 3 and y != 3:
		print("Not a valid direction!")
		return [x,y]	
	else:
		x -= 1
		return [x,y]

def travelSouth(x, y):
	if y == 1:
		print("Not a valid direction!")
		return [x,y]
	elif x == 2 and y == 3:
		print("Not a valid direction!")
		return [x,y]	
	else:
		y -= 1
		return [x,y]

def coin_lever(position, coins):
  """Check if there is a lever in current location, adds to coin coint if pulled"""
  lever_locations = [[1,2], [2,2], [2,3], [3,2]]
  if position in lever_locations:
    pull_lever = input('Pull a lever (y/n): ').lower()
    if pull_lever == 'y':
      coins = coins + 1
      print("You received 1 coin, your total is now {}.".format(str(coins)))
      return coins
    else:
      return coins

def main():
  game_loop = True  
  coin_count = 0  
  while game_loop:

    current_coins = coin_lever(user_pos, coin_count)
    coin_count = current_coins
    if user_pos[0] == 3 and user_pos[1] == 1:
      #quits game if player wins.
      print("Victory!")
      game_loop = False
    else:
      #else checks for available directions.
      N,W,E,S = checkPos(user_pos[0], user_pos[1])
      

      if prev_pos[0] == user_pos[0] and prev_pos[1] == user_pos[1]:
        #Doesn't print available directions if move failed
        pass

      else:
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

        # Updates postions, change this
        prev_pos[0] = user_pos[0]
        prev_pos[1] = user_pos[1]


      direct = input("Direction: ").lower()
      

      #call movement functions
      if direct == "n":
        user_pos[0], user_pos[1] = travelNorth(user_pos[0], user_pos[1])

      elif direct == "s":
        user_pos[0], user_pos[1] = travelSouth(user_pos[0], user_pos[1])

      elif direct == "e":
        user_pos[0], user_pos[1] = travelEast(user_pos[0], user_pos[1])

      elif direct == "w":
        user_pos[0], user_pos[1] = travelWest(user_pos[0], user_pos[1])

    
main()