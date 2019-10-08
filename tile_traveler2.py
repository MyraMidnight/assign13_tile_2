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
		return x,y
	elif x == 2 and y == 2:
		print("Not a valid direction!")
		return x,y
	else:
		y += 1
		return x,y

def travelEast(x, y):
	if x == 3:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y != 3:
		print("Not a valid direction!")
		return x,y
	else:
		x += 1
		return x,y

def travelWest(x, y):
	if x == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 3 and y != 3:
		print("Not a valid direction!")
		return x,y	
	else:
		x -= 1
		return x,y

def travelSouth(x, y):
	if y == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y == 3:
		print("Not a valid direction!")
		return x,y	
	else:
		y -= 1
		return x,y

N = 0
S = 0
W = 0
E = 0


# Position of player, change into list [x,y]
current_y_pos = 1
current_x_pos = 1
last_x_pos = 0
last_y_pos = 0

game_loop = True
while game_loop:

	if current_x_pos == 3 and current_y_pos == 1:
		#quits game if player wins.
		print("Victory!")
		game_loop = False
	else:
		#else checks for available directions.
		N,W,E,S = checkPos(current_x_pos, current_y_pos)
		

		if last_x_pos == current_x_pos and last_y_pos == current_y_pos:
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
			last_x_pos = current_x_pos
			last_y_pos = current_y_pos


		direct = input("Direction: ")
		

		#call movement functions
		if direct.lower() == "n":
			current_x_pos, current_y_pos = travelNorth(current_x_pos, current_y_pos)

		elif direct.lower() == "s":
			current_x_pos, current_y_pos = travelSouth(current_x_pos, current_y_pos)

		elif direct.lower() == "e":
			current_x_pos, current_y_pos = travelEast(current_x_pos, current_y_pos)

		elif direct.lower() == "w":
			current_x_pos, current_y_pos = travelWest(current_x_pos, current_y_pos)

	
		

































































'''
#start by putting the player in tile 1,1

grid_rows = 3
grid_col = 3
#[1 rows x , 1 columns y]
user_pos = [1,1]
victory_pos = [3,1]
#coins = 0
directions = ["(N)orth", "(W)est", "(E)ast","(S)outh"]

def player_location(row, col) :
    """Finds out if user is within the grid, player_location(position) and feed it a [1,1] position."""
    if 0 < row < 4 and 0 < col < 4:
        #user is within the grid
        return True
    else:
        #print('Outside of grid')
        return False

def move_player(current_pos, direction):
    """Moves the player in specified direction, move_player(current_pos, direction) \n current_pos = [x,y]"""
    new_pos = current_pos
    #north +
    if direction == "n":
        new_pos[1] += 1
    #south -
    elif direction == "s":
        new_pos[1] -= 1
    #east +
    elif direction == "e":
        new_pos[0] += 1
    #west -
    elif direction == "w":
        new_pos[0] -= 1
    #check if new location is within grid
    if player_location(new_pos[0], new_pos[1]) == True:
        return new_pos
    else:   
        return False

#player has to be able to input travel direction
def player_direction(position): 
    """User gives directional input, n/N, e/E, s/S, w/W"""
    #print out available directions
    available_directions(position)
    print()
    #ask user for a direction
    direction = input("Direction: ").lower()
    if direction in ["s", "n", "e", "w"]:

        if move_player(position, direction) != False:



    else: 
        print("Not a valid direction!")
        player_direction(position)

def walls(current_pos, new_pos):
	"""Implements check for walls. """
	walls = [ 
		[[1,1],[2,1]] , 
		[[2,3],[2,2]] , 
		[[2,2],[3,2]] , 
		[[2,1],[3,1]] ]



game_loop = True
while game_loop:
	player_direction(user_pos)

	move_player(direction)





'''