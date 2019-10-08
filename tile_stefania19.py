#start by putting the player in tile 1,1

grid_rows = 3
grid_col = 3
#[1 rows x , 1 columns y]
user_pos = [1,1]
victory_pos = [3,1]

def player_location(row, col) :
    """Finds out if user is within the grid, player_location(position) and feed it a [1,1] position."""
    if 0 < row < 4 and 0 < col < 4 :
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

#print available directions
def available_directions(current_pos):
    """Takes current position ([x,y]) and prints out available directions for the player"""
    print("You can travel:", end=" ")
    #north +
    if player_location(current_pos[0], current_pos[1]+ 1) == True:
        print('(N)orth', end=" ")
    #south -
    if player_location(current_pos[0], current_pos[1]-1) == True:
        print('(S)outh', end=" ")
    #east +
    if player_location(current_pos[0]+ 1, current_pos[1]) == True:
        print('(E)ast', end=" ")
    #west -
    if player_location(current_pos[0]- 1, current_pos[1]) == True:
        print('(W)est', end=" ")

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
            #as long as the move is not false/invalid, move the player and ask again
            player_direction(move_player(user_pos, direction))
        else: 
            #asks user again for a direction, staying in same position
            print('Not a valid direction!')
            move_player(position, input("Direction: ").lower())
    else: 
        print("Not a valid direction!")
        player_direction(position)

def possible_move(user_pos): 
    """function is given user_pos and indicates which direction player can move"""

#direction = input("Direction: ")

player_direction(user_pos)


