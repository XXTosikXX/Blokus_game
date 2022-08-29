from tkinter import *
import tkinter.font as font
from tkinter import ttk
import random

moves = []
game_state = "Options"
field_size = 14
scale = 1.0
canvasX = 400
canvasY = 320
startX = 400 - 4
startY = 320 - 4
players = ["Player 1", "Player 2"]
player_types = ["Player", "Player"]
player_id = 0
colors = ["#6666ff", "#ffff66", "#ff6666", "#66ff66"]
active_tile = "None"
move_count = 0
rotation = 0
field_rotation = 0
mirror = 0
log = []
team_mode = False
options_field_size = ""
field_values = ['10x10 (very small)', '12x12 (small)', '14x14 (standard)', '16x16 (big)',
'18x18 (large)', '20x20 (extra large)']
player_values = ['Player', 'AI level 1', 'AI level 2', 'AI level 3']
tiles_list = ["I5", "I4", "I3", "I2", "I1", "U5", "O4", "X5", "P5", "W5",
"T5", "T4", "V5", "V3", "Z5", "Z4", "F5", "L5", "L4", "N5", "Y5"]
sidepanel_id = 0
I5 = [2, 7, 12, 17, 22]
I4 = [7, 12, 17, 22]
I3 = [7, 12, 17]
I2 = [12, 17]
I1 = [12]
U5 = [6, 11, 12, 13, 8]
O4 = [12, 17, 13, 18]
X5 = [11, 7, 12, 17, 13]
P5 = [7, 12, 17, 8, 13]
W5 = [6, 11, 12, 17, 18]
T5 = [11, 12, 13, 17, 22]
T4 = [11, 12, 13, 17]
V5 = [2, 7, 12, 13, 14]
V3 = [7, 12, 13]
Z5 = [6, 7, 12, 17, 18]
Z4 = [11, 12, 17, 18]
F5 = [11, 12, 7, 2, 8]
L5 = [2, 7, 12, 17, 18]
L4 = [2, 7, 12, 13]
N5 = [16, 17, 12, 13, 14]
Y5 = [11, 12, 7, 13, 14]
P = [1, 2, 3, 6, 8, 11, 12, 13, 16, 21]
L = [1, 6, 11, 16, 21, 22, 23]
A = [1, 2, 3, 6, 8, 11, 12, 13, 16, 18, 21, 23]
Y = [1, 3, 5, 8, 11, 12, 13, 17, 22]
E = [1, 2, 3, 6, 11, 12, 13, 17, 21, 22, 23]
R = [1, 2, 3, 6, 8, 11, 12, 13, 16, 18, 21, 24]

player0_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

player1_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

player2_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

player3_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

def turn_field(event = None, rotate_to = None):
    global field
    global field_rotation
    fun_field = field[::1]
    if rotate_to != None:
        if rotate_to == 0:
            return fun_field
        elif rotate_to == 1:
            rotated_field = list(zip(*fun_field[::-1]))
        elif rotate_to == 2:
            rotated_field = []
            for line in fun_field[::-1]:
                rotated_field.append(reversed(line))
        elif rotate_to == 3:
            rotated_field = list(zip(*fun_field))[::-1]
        return rotated_field
    else:
        if event.char == "c":
            field_rotation += 1
            field_rotation = field_rotation % 4
        else:
            field_rotation -= 1
            field_rotation = field_rotation % 4
    update()

def rezoom(event = None):
    global scale
    global canvasX
    global canvasY
    x = win.winfo_width()
    y = win.winfo_height()
    """print(f\"""#############################################\n
    Stats rescaling:\n
    X-Factor: {x/canvasX}\n
    Y-Factor: {y/canvasY}\n
    CanvasX: {canvasX}\n
    CanvasY: {canvasY}\n
    x: {x}\n
    y: {y}\n
    scale: {scale}\""")"""
    if (x/canvasX < y/canvasY):
        #canvas.scale("all", 2, 2, x/canvasX, x/canvasX)
        canvasY = canvasY*x/canvasX
        canvasX = canvasX*x/canvasX
    elif (x/canvasX > y/canvasY):
        #canvas.scale("all", 2, 2, y/canvasY, y/canvasY)
        canvasX = canvasX*y/canvasY
        canvasY = canvasY*y/canvasY
    if (game_state == "Game"):
        canvas.config(width = canvasX-4, height = canvasY-4)
    scale = canvasX/startX
    update()

def generate_field(x, y):
    field = []
    for i in range(y):
        field.append(["#",]*x)
    return field

def draw_field(field, canvas):
    rotated_field = turn_field(rotate_to=field_rotation)
    for row, y in enumerate(rotated_field):
        for column, x in enumerate(y):
            if (x == "#"):
                if ((column + row) % 2 == 0):
                    color = "#fafafa"
                else:
                    color = "#eeeeee"
            else:
                color = colors[x]
            draw_square(column, row, color, canvas)

def draw_square(x, y, color, canvas):
    a = 260/field_size * scale
    coords = 2+x*a, 2+y*a, 2+(x+1)*a, 2+(y+1)*a
    canvas.create_rectangle(coords, fill = color)

def click_event(event):
    if (game_state == "Options"):
        return
    global player_id
    global sidepanel_id
    global active_tile
    x = event.x
    y = event.y
    a = 260/field_size * scale
    SqX = int((x-1)//a)
    SqY = int((y-1)//a)
    if field_rotation == 2:
        SqX = field_size-1 - SqX
        SqY = field_size-1 - SqY
    elif field_rotation == 1:
        SqX, SqY = SqY, field_size-1-SqX
    elif field_rotation == 3:
        SqX, SqY = field_size-1-SqY, SqX
    #print(f"Coords: {SqX}, {SqY}")
    if (SqX >= field_size or SqY >= field_size or SqX < 0 or SqY < 0):
        if (x >= 268*scale and x <= 388*scale and y >= 40*scale and y <= (40+38*7)*scale and sidepanel_id == player_id):  #sidepanel gets clicked
            vx = int((x/scale - 260 - 8) / 40)
            vy = int((y/scale - 40) / 38)
            id = player_id
            tile_list = list(globals()[f'player{id}_tiles'].items())
            tile_name = tile_list[vy*3+vx][0]
            if (active_tile != tile_name):
                active_tile = tile_name
            else:
                active_tile = "None"
        elif (x >= 0 and x <= 260*scale and y >= 250*scale and y <= 315.5*scale):
            active_tile = None
            if len(players) < 4:
                id = int(x//(270*scale/len(players)))
            elif not team_mode:
                id = int(2*((y-260*scale)//(27.75*scale))+(x//(130*scale+2)))
            else:
                id = int(2*((y-260*scale)//(19*scale))+(x//(130*scale+2)))
            if id >= 4 or id < 0:
                return
            sidepanel_id = id
            if player_id != sidepanel_id:
                active_tile = "None"
    else: #field gets clicked
        if (active_tile != "None" and sidepanel_id == player_id):
            if (place_tile(field, active_tile, SqX, SqY, rotation, mirror)):
                find_and_select_next_player()
        else:
            print("Select the tile first")
    update()

def find_and_select_next_player():
    global sidepanel_id
    id = player_id+1
    for vid in range(len(players)):
        next_id = (id+vid) % len(players)
        count_corners(field)
        #print(f"Checking moves for {next_id}")
        moves = check_for_moves(next_id, field)
        if (moves):
            change_player(next_id)
            sidepanel_id = player_id
            if (player_types[next_id] != "Player"):
                update()
                win.after(100, AI_move)
                break
            break
        else:
            print(f"{players[next_id]} has no more moves!")
    else:
        game_over()

def AI_move():
    global move_count
    global moves
    if (player_types[player_id][0:2] != "AI"):
        return
    if (player_types[player_id][-1] == "1"):
        count_corners(field)
        moves = check_for_moves(player_id, field)
        if (moves):
            move = random.choice(moves)
            name, x, y, rotation, mirror = move.split("_")
            place_tile(field, name, int(x), int(y), int(rotation), int(mirror), AI = True)
            """print(f\"""##############
                    name:       {name}
                    x:          {x}
                    y:          {y}
                    rotation:   {rotation}
                    mirror:     {mirror}
                    player_id:  {player_id}
                    move_count: {move_count}
            \""")"""
            find_and_select_next_player()
            update()
    elif (player_types[player_id][-1] == "2"):
        count_corners(field)
        moves = check_for_moves(player_id, field)
        if (moves):
            move_scores = []
            for move in moves:
                AI_field = copy_field(field)
                name, x, y, rotation, mirror = move.split("_")
                AI_field = AI_place_tile(AI_field, name, int(x), int(y), int(rotation), int(mirror))
                count_corners(AI_field)
                score = len(globals()[f'Player{player_id}_corners'])
                for id in range(len(players)):
                    if id != player_id:
                        score -= len(globals()[f'Player{id}_corners'])
                score += 2*int(name[-1])
                move_scores.append(score)
            best_move = max(move_scores)
            deleted = 0
            for index, move in enumerate(move_scores.copy()):
                #print(f"move : {move}, score: {best_move}")
                if move != best_move:
                    move_scores.remove(move)
                    moves.pop(index-deleted)
                    deleted += 1
            if len(move_scores) > 1:
                selected_move = random.choice(moves)
            else:
                selected_move = moves[0]
            name, x, y, rotation, mirror = selected_move.split("_")
            place_tile(field, name, int(x), int(y), int(rotation), int(mirror), AI = True)
            #print(f"Best selected move is: {selected_move} with score: {best_move}")
            #print(f"All best moves: {move_scores}")
            find_and_select_next_player()
            update()

def copy_field(field):
    new_field = []
    for row, y in enumerate(field):
        new_field.append([])
        for column, x in enumerate(y):
            new_field[row].append(x)
    return new_field

def AI_place_tile(AI_field, name, x, y, rotation, mirror):
    tiles = globals()[f'{name}']
    tiles = apply_rotation(tiles, rotation)
    tiles = apply_mirror(tiles, mirror)
    AI_field = draw_tile(player_id, AI_field, tiles, x, y, return_field = True)
    return AI_field

def place_tile(local_field, name, x, y, rotation, mirror, AI = False):
    global log
    global move_count
    global active_tile
    if(check_piece(name, player_id)):
        tiles = globals()[f'{name}']
        tiles = apply_rotation(tiles, rotation)
        tiles = apply_mirror(tiles, mirror)
        if field_rotation and not AI:
            tiles = apply_rotation(tiles, (4-int(field_rotation))%4)
        if (check_move(player_id, local_field, tiles, x, y, True)):
            draw_tile(player_id, local_field, tiles, x, y)
            globals()[f'player{player_id}_tiles'][f'{name}'] = 0
            move_count += 1
            log.append(f"{player_id}_{name}_{x}_{y}_{rotation}_{mirror}_{field_rotation}")
            active_tile = "None"
            return True
    else:
        print(f"{players[player_id]} has no more pieces of that kind!")
        return False

def check_tile(player_id, field, tiles, name, x, y):
    if (check_piece(name, player_id)):
        if check_move(player_id, field, tiles, x, y, False):
            return True
    return False

def change_player(id = None):
    global player_id
    if (id == None):
        player_id += 1
        player_id = player_id % len(players)
    else:
        player_id = id

def check_piece(name, id):
    if globals()[f"player{id}_tiles"][f"{name}"] == 1:
        return True
    return False

def check_move(player_id, local_field, tiles, x, y, msg):
    if (move_count // len(players) == 0):
        valid_first_move = check_first_move(local_field, tiles, x, y)
        if (valid_first_move == False):
            if (msg):
                print("First tile should occupy square in a corner!")
            return False
    valid_boundaries = check_boundaries(tiles, x, y, msg)
    if (valid_boundaries):
        valid_CAE = check_CAE(player_id, local_field, tiles, x, y, msg) #CAE = Corners And Edges
        if (valid_CAE):
            return True
    return False

def check_first_move(field, tiles, x, y):
    skip = False
    true_counter = 0
    bottom_left = bottom_right = top_left = top_right = False
    if (field[0][field_size-1] != "#"):               # top_right
        bottom_left = True
        true_counter += 1
    if (field[0][0] != "#"):                        # top_left
        bottom_right = True
        true_counter += 1
    if (field[field_size-1][0] != "#"):             # bottom_left
        top_right = True
        true_counter += 1
    if (field[field_size-1][field_size-1] != "#"):  # bottom_right
        top_left = True
        true_counter += 1

    if (true_counter == 0):
        bottom_left = bottom_right = top_left = top_right = True
    elif (true_counter == 2):
        if (top_left and bottom_right):
            top_left, bottom_right = False, False
            bottom_left, top_right = True, True
            skip = True
        if (bottom_left and top_right and not skip):
            bottom_left = top_right = False
            top_left = bottom_right = True
    elif (true_counter == 3):
        if (not top_right):
            top_right = top_left = bottom_right = False
            bottom_left = True
        elif (not top_left):
            top_right = top_left = bottom_left = False
            bottom_right = True
        elif (not bottom_right):
            top_right = bottom_right = bottom_left = False
            top_left = True
        elif (not bottom_left):
            bottom_right = top_left = bottom_left = False
            top_right = True
    for tile in tiles:
        vx = (tile % 5) - 2
        vy = (tile // 5) - 2
        if (bottom_left and x+vx == 0 and y+vy == field_size-1):
            return True
        if (bottom_right and x+vx == field_size-1 and y+vy == field_size-1):
            return True
        if (top_right and x+vx == field_size-1 and y+vy == 0):
            return True
        if (top_left and x+vx == 0 and y+vy == 0):
            return True
    return False

def apply_rotation(tiles, rotation):
    if (rotation == 0):
        return tiles
    rotated_tiles = []
    for tile in tiles:
        vx = (tile % 5) - 2
        vy = (tile // 5) - 2
        if (rotation == 1):
            vx, vy = -vy, vx
        elif (rotation == 2):
            vx, vy = -vx, -vy
        elif (rotation == 3):
            vx, vy = vy, -vx
        else:
            print(f"Invalid rotation: {rotation}")
            break
        new_tile = (2+vy)*5 + (vx+2)
        rotated_tiles.append(new_tile)
    return rotated_tiles

def check_CAE(id, field, tiles, x, y, msg):
    edge_flag = True
    corner_flag = False
    for tile in tiles:
        vx = (tile % 5) - 2
        vy = (tile // 5) - 2
        if (field[y+vy][x+vx] == "#"):
            if (y+vy != 0):
                if (field[y+vy-1][x+vx] == id):
                    edge_flag = False
                    break
            if (y+vy != field_size-1):
                if (field[y+vy+1][x+vx] == id):
                    edge_flag = False
                    break
            if (x+vx != 0):
                if (field[y+vy][x+vx-1] == id):
                    edge_flag = False
                    break
            if (x+vx != field_size-1):
                if (field[y+vy][x+vx+1] == id):
                    edge_flag = False
                    break
            if (y+vy != 0 and x+vx != 0):
                if (field[y+vy-1][x+vx-1] == id):
                    corner_flag = True
            if (y+vy != 0 and x+vx != field_size-1):
                if (field[y+vy-1][x+vx+1] == id):
                    corner_flag = True
            if (y+vy != field_size-1 and x+vx != 0):
                if (field[y+vy+1][x+vx-1] == id):
                    corner_flag = True
            if (y+vy != field_size-1 and x+vx != field_size-1):
                if (field[y+vy+1][x+vx+1] == id):
                    corner_flag = True
        else:
            if (msg):
                print("Cannot place over other tiles!")
            return False
    if (edge_flag):
        if (corner_flag):
            return True
        elif (move_count // len(players) == 0):
            return True
        else:
            if (msg):
                print("Tiles have to touch each other with at least 1 corner!")
            return False
    else:
        if (msg):
            print("Edges of your tiles should not touch each other!")
        return False

def check_boundaries(tiles, x, y, msg):
    valid = True
    for tile in tiles:
        if (x < 0 or x >= field_size or y < 0 or y >= field_size):
            valid = False
        v = 0
        h = 0
        v = (tile // 5) - 2
        h = (tile % 5) - 2
        if ((v == -2 and y <= 1) or (v == -1 and y == 0) or (v == 2 and y >= field_size - 2) or (v == 1 and y == field_size - 1)):
            valid = False
            break
        if ((h == -2 and x <= 1) or (h == -1 and x == 0) or (h == 2 and x >= field_size - 2) or (h == 1 and x == field_size - 1)):
            valid = False
            break

    if (valid):
        return True
    else:
        if (msg):
            print("Invalid location, out of map")
        return False

def draw_tile(player_id, field, tiles, x, y, return_field = False):
    for tile in tiles:
        vx = (tile % 5)-2
        vy = (tile // 5)-2
        field[y+vy][x+vx] = player_id
    if return_field:
        return field

def draw_sidepanel():
    coords = 260*scale+2, 2, 394.5*scale, 315.5*scale
    canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
    coords = (8+260)*scale, 2.5*scale, (8+260+120)*scale, (2.5+36)*scale
    canvas.create_rectangle(coords, fill = "#eeeeee")
    tile_list = list(globals()[f'player{sidepanel_id}_tiles'].items())
    for ny in range(7):
        for nx in range(3):
            coords = (260+nx*40+8)*scale, (40+ny*38)*scale, (260+(nx+1)*40+8)*scale, (40+(ny+1)*38)*scale
            tile_name = tile_list[ny*3+nx][0]
            tile = globals()[f'{tile_name}']
            tile = apply_rotation(tile, rotation)
            tile = apply_mirror(tile, mirror)
            if (active_tile == tile_name):
                outline_color = '#999999'
                border = 2*scale
                coords = (260+nx*40+8+1)*scale+1, (40+ny*38+1)*scale+1, (260+(nx+1)*40+8-1)*scale, (40+(ny+1)*38-1)*scale
            else:
                border = 1
                outline_color = '#000000'
            canvas.create_rectangle(coords, fill = "#ffffff", outline = outline_color, width = border)
            if (globals()[f"player{sidepanel_id}_tiles"][f'{tile_name}'] == 0):
                color = "#aaaaaa"
            else:
                color = colors[sidepanel_id]
            for square in tile:
                vx = (square % 5)
                vy = (square // 5)
                coords = (260+nx*40+8+vx*8)*scale, (40+ny*38+vy*38/5)*scale, (260+nx*40+8+(vx+1)*8)*scale, (40+ny*38+(vy+1)*38/5)*scale
                canvas.create_rectangle(coords, fill = color, outline = "#000000")
            coords = (260+nx*40+8+18.5)*scale, (40+ny*38+(18.5/40*38))*scale, (260+nx*40+8+21.5)*scale, (40+ny*38+(21.5/40*38))*scale
            canvas.create_oval(coords, fill = "#000000")

def draw_scoreboard():
    text_font = font.Font(size=int(8*scale))
    score_list = count_score()
    coords = 2, (260)*scale+2, (260)*scale+2, (315.5)*scale
    canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
    if len(players) < 4:
        for id in range(len(players)):
            coords = 260/len(players)*id*scale+2, (260)*scale, 260/len(players)*(id+1)*scale+2, (315.5)*scale
            if player_id == id:
                canvas.create_rectangle(coords, fill = "white", outline = f"black", width=1)
            else:
                canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
            coords = (260/len(players))*(id+0.5)*scale+2, (260+10)*scale
            globals()[f"name_{id}"] = canvas.create_text(coords, text=f"{players[id]}", fill="black", font=text_font)
            coords = (260/len(players)*id+5)*scale+2, (315.5-5)*scale+2, (260/len(players)*id+15)*scale+2, (315.5-15)*scale
            canvas.create_rectangle(coords, fill = colors[id], outline = "#888888", width=1)
            coords = (260/len(players))*(id+1-0.04)*scale+2, (315.5-10)*scale
            globals()[f"score_{id}"] = canvas.create_text(coords, text=f"Score: {score_list[id]}", fill="black", font=text_font, anchor="e")
            size = canvas.bbox(globals()[f"name_{id}"])
            if (size[2]-size[0])/scale >= 260/len(players):
                print(f"Name for {players[id]} doesnt fit!")
                players[id] = players[id][0:-1]
                draw_scoreboard()
    elif not team_mode:
        for id in range(len(players)):
            coords = (130*(id%2))*scale+2, (260+27.75*(id//2))*scale, (130*(id%2+1))*scale+2, (260+27.75*(id//2+1))*scale
            if player_id == id:
                canvas.create_rectangle(coords, fill = "white", outline = "black", width=1)
            else:
                canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
            coords = (65+130*(id%2))*scale+2, (260+8+27.75*(id//2))*scale
            globals()[f"name_{id}"] = canvas.create_text(coords, text=f"{players[id]}", fill="black", font=text_font)
            coords = (5+130*(id%2))*scale+2, (315.5-5-27.75*(1-(id//2)))*scale, (15+130*(id%2))*scale+2, (315.5-15-27.75*(1-(id//2)))*scale
            canvas.create_rectangle(coords, fill = colors[id], outline = "#888888", width=1)
            coords = (100+130*(id%2))*scale+2, (260+20+27.75*(id//2))*scale
            globals()[f"score_{id}"] = canvas.create_text(coords, text=f"Score: {score_list[id]}", fill="black", font=text_font)
            size = canvas.bbox(globals()[f"name_{id}"])
            if (size[2]-size[0])/scale >= 260/len(players):
                print(f"Name for {players[id]} doesnt fit!")
                players[id] = players[id][0:-1]
                draw_scoreboard()
    else:
        coords = 2, (260)*scale, 130*scale+2, (315.5)*scale
        canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
        coords = 130*scale+2, (260)*scale, 260*scale+2, (315.5)*scale
        canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
        for id in range(len(players)):
            coords = ((130)*(id%2))*scale+2, (260+19*(id//2))*scale, ((130)*(id%2+1))*scale+2, (260+20+19*(id//2))*scale
            count_corners(field)
            if player_id == id:
                canvas.create_rectangle(coords, fill = "white", outline = "black", width=1)
            else:
                canvas.create_rectangle(coords, fill = "#cccccc", outline = "black", width=1)
            coords = ((130)*(id%2)+5)*scale+2, (260+19*(id//2)+5)*scale+1, ((130)*(id%2)+15)*scale+2, (260+19*(id//2)+15)*scale+1
            canvas.create_rectangle(coords, fill = colors[id], outline = "#888888", width=1)
            coords = ((130)*(id%2)+24)*scale+2, (260+19*(id//2)+5)*scale
            globals()[f"name_{id}"] = canvas.create_text(coords, text=f"{players[id]}", fill="black", font=text_font, anchor="nw")
            size = canvas.bbox(globals()[f"name_{id}"])
            if (size[2]-size[0])/scale >= 105:
                print(f"Name for {players[id]} doesnt fit!")
                players[id] = players[id][0:-1]
                draw_scoreboard()
            if id // 2 == 1:
                coords = (130)*(id%2+0.75)*scale+2, (315.5-8)*scale
                globals()[f"score_{id}"] = canvas.create_text(coords, text=f"Score: {score_list[id]+score_list[id-2]}", fill="black", font=text_font)

def update():
    #print("updating")
    if (game_state == "Game"):
        canvas.delete('all')
        draw_field(field, canvas)
        draw_sidepanel()
        draw_scoreboard()
        update_canvas_font()
    elif (game_state == "Options"):
        update_options_font()
        frame.config(width=startX*scale, height=startY*scale)
        check_team_mode()

def update_canvas_font():
    text_font = font.Font(size=int(8*scale))
    for id in range(len(players)):
        canvas.itemconfig(globals()[f"name_{id}"], font=text_font)
        if not team_mode:
            canvas.itemconfig(globals()[f"score_{id}"], font=text_font)
        else:
            if id//2 == 1:
                canvas.itemconfig(globals()[f"score_{id}"], font=text_font)

def update_options_font():
    text_font = font.Font(size=int(9*scale))
    restart_font = font.Font(size=int(6*scale))
    combobox_font = font.Font(size=int(9*scale))
    cancel['font'] = text_font
    apply['font'] = text_font
    apply_and_restart['font'] = restart_font
    label_amount['font'] = text_font
    radio_2['font'] = text_font
    radio_3['font'] = text_font
    radio_4['font'] = text_font
    label_field['font'] = text_font
    combobox_field['font'] = text_font
    checkbox_team_mode['font'] = text_font
    label_player_names['font'] = text_font
    entry_player_0['font'] = text_font
    entry_player_1['font'] = text_font
    entry_player_2['font'] = text_font
    entry_player_3['font'] = text_font
    label_team_1['font'] = text_font
    label_team_2['font'] = text_font
    label_field.config(padx=5*scale, pady=5*scale)
    label_amount.config(padx=5*scale, pady=5*scale)
    combobox_player_type_0['font'] = text_font
    combobox_player_type_1['font'] = text_font
    combobox_player_type_2['font'] = text_font
    combobox_player_type_3['font'] = text_font

def draw_options():
    frame.pack(anchor="nw")
    cancel.place(anchor = "nw", relx=0.1, rely=13/16, relwidth=0.2, relheight=1/8)
    apply.place(anchor = "nw", relx=0.4, rely=13/16, relwidth=0.2, relheight=1/8)
    apply_and_restart.place(anchor = "nw", relx=0.7, rely=13/16, relwidth=0.2, relheight=1/8)
    label_amount.place(anchor = "nw", relx=0.05, rely=0.05, relwidth=0.35, relheight=0.06)
    radio_2.place(anchor = "nw", relx=0.05, rely=0.11, relwidth=0.16, relheight=0.06)
    radio_3.place(anchor = "nw", relx=0.05, rely=0.17, relwidth=0.16, relheight=0.06)
    radio_4.place(anchor = "nw", relx=0.05, rely=0.23, relwidth=0.16, relheight=0.06)
    label_field.place(anchor = "nw",  relx=0.55, rely=0.05, relheight=0.06)
    combobox_field.place(anchor = "nw", relx=0.55, rely=0.11, relwidth=0.4, relheight=0.08)
    label_player_names.place(anchor = "nw", relx=0.05, rely=0.35, relwidth=0.8, relheight=0.08)
    draw_entries(rewrite=True)
    for id in range(len(player_types)):
        index = player_values.index(player_types[id])
        globals()[f'combobox_player_type_{id}'].current(index)

def rotate(event=None, rotation_modifier=0):
    global rotation
    if event:
        char = event.char
    else:
        char = ""
    if (rotation_modifier == -1 or char == 'q'):
        rotation -= 1
    elif (rotation_modifier == 1 or char == 'e'):
        rotation += 1
    rotation = rotation % 4
    update()

def count_corners(field):   # Counts squares for each player
                            # where he can place tiles on
                            # (Corners to previous tiles).
                            # Saves result to player{id}_corners
    for player in range(len(players)):
        globals()[f"Player{player}_corners"] = []
        if (move_count // len(players) == 0 and move_count <= player):
            if (player == 1):
                if (field[0][0] != "#"):
                    globals()[f"Player1_corners"].append(f"{field_size-1}_{field_size-1}")
                elif (field[field_size-1][0] != "#"):
                    globals()[f"Player1_corners"].append(f"{field_size-1}_0")
                elif (field[0][field_size-1] != "#"):
                    globals()[f"Player1_corners"].append(f"0_{field_size-1}")
                else:
                    globals()[f"Player1_corners"].append("0_0")
            else:
                globals()[f"Player{player}_corners"].append("0_0")
                globals()[f"Player{player}_corners"].append(f"{field_size-1}_0")
                globals()[f"Player{player}_corners"].append(f"0_{field_size-1}")
                globals()[f"Player{player}_corners"].append(f"{field_size-1}_{field_size-1}")
        else:
            for row, y in enumerate(field):
                for column, x in enumerate(y):
                    if(check_corners(player, column, row)):
                        globals()[f"Player{player}_corners"].append(f"{column}_{row}")

def check_corners(id, x, y):
    edge_flag = True
    corner_flag = False
    if (field[y][x] == "#"):
        if (y != 0):
            if (field[y-1][x] == id):
                edge_flag = False
        if (y != field_size-1):
            if (field[y+1][x] == id):
                edge_flag = False
        if (x != 0):
            if (field[y][x-1] == id):
                edge_flag = False
        if (x != field_size-1):
            if (field[y][x+1] == id):
                edge_flag = False
        if (y != 0 and x != 0):
            if (field[y-1][x-1] == id):
                corner_flag = True
        if (y != 0 and x != field_size-1):
            if (field[y-1][x+1] == id):
                corner_flag = True
        if (y != field_size-1 and x != 0):
            if (field[y+1][x-1] == id):
                corner_flag = True
        if (y != field_size-1 and x != field_size-1):
            if (field[y+1][x+1] == id):
                corner_flag = True
    if (corner_flag and edge_flag):
        return True
    return False

def undo(event=None):
    if (len(log) >= 1):
        global player_id
        global move_count
        global moves
        global sidepanel_id
        last_move = log.pop()
        player, name, x, y, rotation, mirror, field_rotation = last_move.split('_')
        tiles = globals()[f'{name}']
        rotation = int(rotation)
        tiles = apply_rotation(tiles, int(rotation))
        tiles = apply_mirror(tiles, int(mirror))
        if player_types[int(player)][0:2] != "AI":
            tiles = apply_rotation(tiles, (4-int(field_rotation))%4)
        draw_tile("#", field, tiles, int(x), int(y))
        player_id = int(player)
        globals()[f'player{player_id}_tiles'][f'{name}'] += 1
        move_count -= 1
        sidepanel_id = player_id
        print("Reverted the last move!")
        update()
        moves = check_for_moves(player_id, field)
        if player_types[player_id][0:2] == "AI":
            undo()
    else:
        print("There is nothing to undo!")
        AI_move()

def apply_mirror(tiles, mirror):
    if (mirror == 0):
        return tiles
    mirrored_tiles = []
    for tile in tiles:
        vx = (tile % 5) -2
        vx = -vx
        vy = (tile // 5) -2
        new_tile = 12 +vx+vy*5
        mirrored_tiles.append(new_tile)
    return mirrored_tiles

def change_mirror(event):
    global mirror
    mirror += 1
    mirror %= 2
    update()

def check_for_moves(player_id, field):  # Checks for moves for a player id.
                                        # Returns False if 0, moves if at least 1 move.
                                        # Appends moves to moves=[] for AI and hint()
    global moves
    moves = []
    #print(f"""Player {player_id} corners: {globals()[f"Player{player_id}_corners"]}""")
    corners = globals()[f"Player{player_id}_corners"]
    for name in tiles_list:  # goes through every tile name in tile_list
        tiles = globals()[f"{name}"]
        for str in corners: # tries to place that tile into all possible locations
            x, y = str.split("_")
            x = int(x)
            y = int(y)
            for rotation in range(4):   # cycles through 4 rotations
                rotated_tiles = apply_rotation(tiles, rotation)
                if rotation != 0 and compare_arrays(tiles, rotated_tiles): # exludes X5 and I1
                    #print(f"tile: {name}_{rotation}_{mirror}, {tiles} and {rotated_tiles} are the same, no need to rotate")
                    continue
                if rotation > 1 and compare_arrays(apply_rotation(tiles, 1), rotated_tiles):
                    #print(f"tile: {name}_{rotation}_{mirror}, rotation 1 and {rotated_tiles} are the same, no need to rotate ####")
                    continue
                for mirror in range(2): # checks both mirror possibilities
                    mirrored_tiles = apply_mirror(rotated_tiles, mirror)
                    if mirror != 0 and compare_arrays(mirrored_tiles, rotated_tiles): # excludes tiles with y-symmetry on any rotation
                        #print(f"tile: {name}_{rotation}_{mirror}, {mirrored_tiles} and {rotated_tiles} are the same, no need to mirror#")
                        continue
                    if rotation % 2 == 1 and mirror == 1 and (compare_arrays(mirrored_tiles, apply_rotation(tiles, 1)) or compare_arrays(mirrored_tiles, apply_rotation(tiles, 3))):
                        #print(f"tile: {name}_{rotation}_{mirror}, {mirrored_tiles} and {rotated_tiles} are the same, no need to mirror#")
                        continue
                    for square in mirrored_tiles:
                        vx = (square % 5) -2
                        vy = (square // 5) -2
                        if (check_tile(player_id, field, mirrored_tiles, name, x-vx, y-vy)):
                            if ((x-vx) // 10 == 0):
                                lx = f"0{x-vx}"
                            else:
                                lx = f"{x-vx}"
                            if ((y-vy) // 10 == 0):
                                ly = f"0{y-vy}"
                            else:
                                ly = f"{y-vy}"
                            moves.append(f"{name}_{lx}_{ly}_{rotation}_{mirror}")
                            #print(f"Tile {name} successfully fit in {x-vx}, {y-vy} with rotation: {rotation} and mirror: {mirror}")
                        else:
                            #print(f"Tile {name} does not fit in {x-vx}, {y-vy} with rotation: {rotation} and mirror: {mirror}")
                            pass

    #print(f"moves = {moves}")
    #print(f"Amount of moves: {len(moves)}")
    if ((not moves) and move_count // len(players) != 0):
        return False
    return moves

def compare_arrays(x, y):
    for tile in x:
        if tile not in y:
            return False
    return True

def count_score():
    score_list = []
    for id in range(len(players)):
        locals()[f"Player{id}_score"] = 0
        all_pieces_placed = True
        for item in globals()[f"player{id}_tiles"].items():
            if (item[1] == 1):
                locals()[f"Player{id}_score"] -= int(item[0][1])
                all_pieces_placed = False
        if (all_pieces_placed):
            for str in reversed(log):
                pl, name, *_ = str.split("_")
                if (int(pl) == id):
                    if (name == "I1"):
                        locals()[f"Player{id}_score"] = 20
                    else:
                        locals()[f"Player{id}_score"] = 15
                    break
        score_list.append(locals()[f"Player{id}_score"])
    return score_list

def game_over(event=None):
    print("Its game over!")
    print(f"""Score:""")
    score_list = count_score()
    for id, score in enumerate(score_list):
        print(f"{players[id]}: {score}")
    if (not team_mode):
        highest = max(score_list)
        winner_id = score_list.index(highest)
        winners = [players[winner_id]]
        for id, score in enumerate(score_list):
            if (id == winner_id):
                continue
            if (score == highest):
                winners.append(players[id])
        if (len(winners) == 1):
            print(f"{winners[0]} won with {highest} points!")
        elif (len(winners) == 2):
            print(f"It is a tie beetween {winners[0]} and {winners[1]} \
with {highest} points!")
        elif (len(winners) == 3):
            print(f"It is a tie beetween {winners[0]}, {winners[1]} \
and {winners[2]} with {highest} points!")
        else:
            print(f"It is a tie beetween {winners[0]}, {winners[1]}\
, {winners[2]} and {winners[3]} with {highest} points!")
    else:
        team1_score = score_list[0] + score_list[2]
        print(f"Team 1 score: {team1_score}")
        team2_score = score_list[1] + score_list[3]
        print(f"Team 2 score: {team2_score}")
        if (team1_score > team2_score):
            print(f"Team 1 ({players[0]} and {players[2]}) won with {team1_score} points!")
        elif (team1_score < team2_score):
            print(f"Team 2 ({players[1]} and {players[3]}) won with {team2_score} points!")
        else:
            print(f"It is a tie beetween Team 1 ({players[0]} and {players[2]}) and Team 2 ({players[1]} and {players[3]}) with {team1_score} points!")

def new_game():
    print("New Game")

def hint():
    print("Giving a hint!")

def combobox_field_selected(event=None):
    options_field_size = combobox_field.get()
    check_apply_button_state()

def check_apply_button_state(event=None):
    options_field_size = combobox_field.get()
    if field_size != int(options_field_size[0:2]):
        apply["state"] = 'disabled'
        return
    if len(players) != int(radio_players.get()):
        apply["state"] = 'disabled'
        return
    if (options_team_mode.get() and not team_mode) or (not options_team_mode.get() and team_mode):
        apply["state"] = 'disabled'
        return
    for id, type in enumerate(player_types):
        if type != globals()[f'combobox_player_type_{id}'].get():
            apply["state"] = 'disabled'
            return
    apply["state"] = 'normal'

def create_menu():
    menu_game = Menu(menubar)
    menubar.add_cascade(menu=menu_game, label='Game')
    menu_game.add_command(label='New Game', command=new_game)
    menu_game.entryconfigure('New Game', accelerator='Control+N')

    map_size = IntVar()
    map_size.set(14)
    menu_map_size = Menu(menubar)
    menu_map_size.add_radiobutton(label='10x10 (very small)', variable=map_size, value=10)
    menu_map_size.add_radiobutton(label='12x12 (small)', variable=map_size, value=12)
    menu_map_size.add_radiobutton(label='14x14 (standard)', variable=map_size, value=14)
    menu_map_size.add_radiobutton(label='16x16 (big)', variable=map_size, value=16)
    menu_map_size.add_radiobutton(label='18x18 (large)', variable=map_size, value=18)
    menu_map_size.add_radiobutton(label='20x20 (extra large)', variable=map_size, value=20)

    menu_options = Menu(menubar)
    menubar.add_cascade(menu=menu_options, label='Options')
    menu_options.add_cascade(menu=menu_map_size, label='Map Size')

    menu_help = Menu(menubar)
    menu_help.add_command(label='Hint', command=hint)
    menubar.add_cascade(menu=menu_help, label='Help')

def change_game_state(event=None):
    global game_state
    if (game_state == "Game"):
        game_state = "Options"
        canvas.pack_forget()
        draw_options()
    else:
        game_state = "Game"
        rezoom()
        frame.pack_forget()
        canvas.pack(anchor = 'nw')
    update()

def check_team_mode():
    if (radio_players.get() == "4"):
        if (checkbox_team_mode not in frame.place_slaves()):
            checkbox_team_mode.place(anchor="nw", relx=0.21, rely=0.11, relwidth=0.19, relheight=0.18)
    else:
        checkbox_team_mode.place_forget()
        options_team_mode.set(0)
    check_apply_button_state()

def radiobutton_player():
    check_team_mode()
    draw_entries()

def draw_entries(rewrite=False):
    i = int(radio_players.get())
    entry_player_0.place_forget()
    entry_player_1.place_forget()
    entry_player_2.place_forget()
    entry_player_3.place_forget()
    combobox_player_type_0.place_forget()
    combobox_player_type_1.place_forget()
    combobox_player_type_2.place_forget()
    combobox_player_type_3.place_forget()
    team = options_team_mode.get()
    if not team:
        label_team_1.place_forget()
        label_team_2.place_forget()
    else:
        label_team_1.place(anchor = "nw", relx=0.65, rely=0.43, relwidth=0.2, relheight=0.12)
        label_team_2.place(anchor = "nw", relx=0.65, rely=0.58, relwidth=0.2, relheight=0.12)
    while i != 0:
        if not team:
            globals()[f"combobox_player_type_{i-1}"].place(anchor = "nw", relx=0.05, rely=0.43+0.06*(i-1), relwidth=0.3, relheight=0.06)
            globals()[f"entry_player_{i-1}"].place(anchor = "nw", relx=0.35, rely=0.43+0.06*(i-1), relwidth=0.3, relheight=0.06)
        else:
            globals()[f"combobox_player_type_{i-1}"].place(anchor = "nw", relx=0.05, rely=0.43+0.15*((i-1)%2)+0.06*((i-1)//2), relwidth=0.3, relheight=0.06)
            globals()[f"entry_player_{i-1}"].place(anchor = "nw", relx=0.35, rely=0.43+0.15*((i-1)%2)+0.06*((i-1)//2), relwidth=0.3, relheight=0.06)
        if rewrite:
            if len(players) >= i and globals()[f"entry_player_{i-1}"].get() == players[i-1]:
                i -= 1
                continue
            elif len(players) >= i:
                globals()[f"entry_player_{i-1}"].delete(0, END)
                globals()[f"entry_player_{i-1}"].insert(0, players[i-1])
                i -= 1
                continue
        if len(players) < i:
            globals()[f"entry_player_{i-1}"].delete(0, END)
            globals()[f"entry_player_{i-1}"].insert(0, f"Player {i}")
        i -= 1

def checkbox_team():
    check_apply_button_state()
    draw_entries()

def button_cancel():
    radio_players.set(str(len(players)))
    for id, value in enumerate(field_values):
        if value[0:2] == str(field_size):
            combobox_field.current(id)
    options_team_mode.set(team_mode)
    change_game_state()

def button_apply():
    change_player_names()
    change_game_state()

def button_apply_and_restart():
    global field
    global field_size
    global move_count
    global mirror
    global rotation
    global log
    global team_mode
    global player_types
    global moves
    global sidepanel_id
    reset_player_tiles()
    change_player(0)
    field_size = int(combobox_field.get()[0:2])
    field = generate_field(field_size, field_size)
    sidepanel_id = 0
    move_count = 0
    rotation = 0
    mirror = 0
    log = []
    team_mode = options_team_mode.get()
    change_player_names()
    change_game_state()
    player_types = []
    for id, player in enumerate(players):
        player_types.append(globals()[f'combobox_player_type_{id}'].get())
    count_corners(field)
    moves = check_for_moves(0, field)
    AI_move()

def change_player_names():
    global players
    players = []
    for id in range(int(radio_players.get())):
        players.append(globals()[f"entry_player_{id}"].get())

def reset_player_tiles():
    for id, player in enumerate(players):
        for tile in tiles_list:
            globals()[f"player{id}_tiles"][tile] = 1

field = generate_field(field_size, field_size)
win = Tk()

win.option_add('*tearOff', False)
menubar = Menu(win)
win['menu'] = menubar
create_menu()

text_font = font.Font(size=int(10*scale))
combobox_font = font.Font(size=int(13*scale))
frame_bg = "#cccccc"
radio_players = StringVar()
options_team_mode = IntVar()

canvas = Canvas(win, width = startX, height = startY, bg = "#cccccc", confine = False)
frame = Frame(win, width=startX, height=startY, bg=frame_bg)
cancel = Button(frame, text="Cancel", font=text_font, padx = 10, pady = 10, command=button_cancel)
apply = Button(frame, text="Apply", font=text_font, padx = 10, pady = 10, command=button_apply)
apply_and_restart = Button(frame, text="Apply and Restart", font=text_font, padx = 10, pady = 10, command=button_apply_and_restart)
label_amount = Label(frame, text="Amount of Players", font=text_font, bg=frame_bg, padx = 5*scale, pady = 5*scale, relief="raised")
radio_2 = Radiobutton(frame, text="2 Players", value="2", variable=radio_players, font=text_font, indicatoron=0, command=radiobutton_player)
radio_3 = Radiobutton(frame, text="3 Players", value="3", variable=radio_players, font=text_font, indicatoron=0, command=radiobutton_player)
radio_4 = Radiobutton(frame, text="4 Players", value="4", variable=radio_players, font=text_font, indicatoron=0, command=radiobutton_player)
entry_player_0 = Entry(frame, font = text_font)
entry_player_1 = Entry(frame, font = text_font)
entry_player_2 = Entry(frame, font = text_font)
entry_player_3 = Entry(frame, font = text_font)
label_team_1 = Label(frame, text="Team 1", font=text_font, bg=frame_bg, padx = 5*scale, pady = 5*scale, relief="raised")
label_team_2 = Label(frame, text="Team 2", font=text_font, bg=frame_bg, padx = 5*scale, pady = 5*scale, relief="raised")
label_field = Label(frame, text="Field size", font=text_font, bg=frame_bg, padx = 5*scale, pady = 5*scale, relief="raised")
label_player_names = Label(frame, text="Player/AI names", font=text_font, bg=frame_bg, padx = 5*scale, pady = 5*scale, relief="raised")
checkbox_team_mode = Checkbutton(frame, text="Team mode", onvalue=1, offvalue=0, variable=options_team_mode, font=text_font, indicatoron=0, command=checkbox_team)
combobox_field = ttk.Combobox(frame, values=field_values, state='readonly', font=combobox_font)
combobox_player_type_0 = ttk.Combobox(frame, values=player_values, state='readonly', font=combobox_font)
combobox_player_type_1 = ttk.Combobox(frame, values=player_values, state='readonly', font=combobox_font)
combobox_player_type_2 = ttk.Combobox(frame, values=player_values, state='readonly', font=combobox_font)
combobox_player_type_3 = ttk.Combobox(frame, values=player_values, state='readonly', font=combobox_font)

combobox_field.bind("<<ComboboxSelected>>", combobox_field_selected)
combobox_player_type_0.bind("<<ComboboxSelected>>", check_apply_button_state)
combobox_player_type_1.bind("<<ComboboxSelected>>", check_apply_button_state)
combobox_player_type_2.bind("<<ComboboxSelected>>", check_apply_button_state)
combobox_player_type_3.bind("<<ComboboxSelected>>", check_apply_button_state)
combobox_player_type_0.current(0)
combobox_player_type_1.current(0)
combobox_player_type_2.current(0)
combobox_player_type_3.current(0)
win.option_add('*TCombobox*Listbox.font', combobox_font)
combobox_field.current(2)
radio_players.set(str(len(players)))
update()
draw_options()
"""count_corners()
check_for_moves(0)"""
win.bind("<Configure>", rezoom)
win.bind("<Button-1>", click_event)
win.bind("q", rotate)
win.bind("e", rotate, add = "+")
win.bind("c", turn_field)
win.bind("v", turn_field, add = "+")
win.bind("<Control-z>", undo)
win.bind("s", change_mirror)
win.bind("<Escape>", change_game_state)
win.minsize(400, 320)
win.geometry("404x324")
win.title("Blokus game")
win.bind("g", game_over)
win.mainloop()
