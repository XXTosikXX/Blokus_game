from tkinter import *

field_size = 14
scale = 1.0
canvasX = 400
canvasY = 320
startX = 400 - 4
startY = 320 - 4
players = ["Anton", "Peter", "Niclas", "Lorenz"]
player_id = 0
colors = ["#6666ff", "#ffff66", "#ff6666", "#66ff66"]
active_tile = "None"
move_count = 0
rotation = 0
mirror = 0
log = []
team_mode = False
tiles_list = ["I5", "I4", "I3", "I2", "I1", "U5", "O4", "X5", "P5", "W5",
"T5", "T4", "V5", "V3", "Z5", "Z4", "F5", "L5", "L4", "N5", "Y5"]
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

def rezoom(event):
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
    canvas.config(width = canvasX-4, height = canvasY-4)
    scale = canvasX/startX
    update()

def generate_field(x, y):
    field = []
    for i in range(y):
        field.append(["#",]*x)
    return field

def draw_field(field, canvas):
    row = 0
    column = 0
    for y in field:
        for x in y:
            if (x == "#"):
                if ((column + row) % 2 == 0):
                    color = "#fafafa"
                else:
                    color = "#eeeeee"
            else:
                color = colors[x]
            draw_square(column, row, color, canvas)
            column += 1
        row += 1
        column = 0

def draw_square(x, y, color, canvas):
    a = 260/field_size * scale
    coords = 2+x*a, 2+y*a, 2+(x+1)*a, 2+(y+1)*a
    canvas.create_rectangle(coords, fill = color)

def click_event(event):
    global player_id
    global active_tile
    x = event.x
    y = event.y
    a = 260/field_size * scale
    SqX = int((x-1)//a)
    SqY = int((y-1)//a)
    #print(f"Coords: {SqX}, {SqY}")
    if (SqX >= field_size or SqY >= field_size or SqX < 0 or SqY < 0):
        if (x >= 268*scale and x <= 388*scale and y >= 40*scale and y <= (40+38*7)*scale):  #sidepanel gets clicked
            vx = int((x/scale - 260 - 8) / 40)
            vy = int((y/scale - 40) / 38)
            id = player_id
            tile_list = list(globals()[f'player{id}_tiles'].items())
            tile_name = tile_list[vy*3+vx][0]
            if (active_tile != tile_name):
                active_tile = tile_name
            else:
                active_tile = "None"

    else: #field gets clicked
        if (active_tile != "None"):
            if (place_tile(active_tile, SqX, SqY)):
                id = player_id+1
                for vid in range(len(players)):
                    next_id = (id+vid) % len(players)
                    print(f"next_id: {next_id}")
                    if (check_for_moves(next_id)):
                        change_player(next_id)
                        break
                    else:
                        print(f"{players[next_id]} has no more moves!")
                else:
                    game_over()
        else:
            print("Select the tile first")
    update()

def place_tile(name, x, y):
    global log
    global player_id
    global move_count
    global active_tile
    color = colors[player_id]
    if(check_piece(name, player_id)):
        tiles = globals()[f'{name}']
        tiles = apply_rotation(tiles, rotation)
        tiles = apply_mirror(tiles, mirror)
        if (check_move(player_id, tiles, x, y, True)):
            globals()[f'player{player_id}_tiles'][f'{name}'] = 0
            draw_tile(player_id, tiles, x, y)
            move_count += 1
            log.append(f"{player_id}_{name}_{x}_{y}_{rotation}_{mirror}")
            active_tile = "None"
            #count_corners()
            return True
    else:
        print(f"{players[player_id]} has no more pieces of that kind!")
        return False

def check_tile(player_id, tiles, name, x, y):
    if (check_piece(name, player_id) and check_move(player_id, tiles, x, y, False)):
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

def check_move(player_id, tiles, x, y, msg):
    if (move_count // len(players) == 0):
        valid_first_move = check_first_move(tiles, x, y)
        if (valid_first_move == False):
            if (msg):
                print("First tile should occupy square in a corner!")
            return False
    valid_boundaries = check_boundaries(tiles, x, y, msg)
    if (valid_boundaries):
        valid_CAE = check_CAE(player_id, tiles, x, y, msg) #CAE = Corners And Edges
        if (valid_CAE):
            return True
    return False

def check_first_move(tiles, x, y):
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
            bottom_left = top_right = True
            top_left = bottom_right = False
        if (bottom_left and top_right):
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
            print("Invalid rotation")
            break
        new_tile = (2+vy)*5 + (vx+2)
        rotated_tiles.append(new_tile)
    return rotated_tiles

def check_CAE(id, tiles, x, y, msg):
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

def draw_tile(player_id, tiles, x, y):
    for tile in tiles:
        vx = (tile % 5)-2
        vy = (tile // 5)-2
        field[y+vy][x+vx] = player_id

def draw_sidepanel():
    coords = 260*scale+2, 2, 394.5*scale, 315.5*scale
    canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
    coords = (8+260)*scale, 2.5*scale, (8+260+120)*scale, (2.5+36)*scale
    canvas.create_rectangle(coords, fill = "#eeeeee")
    """l = Label(win, width = int(10), height = int(1), text = "active_player")
    l.place(x=260, y=20)""" # LABEL TODO
    tile_list = list(globals()[f'player{player_id}_tiles'].items())
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
            if (globals()[f"player{player_id}_tiles"][f'{tile_name}'] == 0):
                color = "#aaaaaa"
            else:
                color = colors[player_id]
            for square in tile:
                vx = (square % 5)
                vy = (square // 5)
                coords = (260+nx*40+8+vx*8)*scale, (40+ny*38+vy*38/5)*scale, (260+nx*40+8+(vx+1)*8)*scale, (40+ny*38+(vy+1)*38/5)*scale
                canvas.create_rectangle(coords, fill = color, outline = "#000000")
            coords = (260+nx*40+8+18.5)*scale, (40+ny*38+(18.5/40*38))*scale, (260+nx*40+8+21.5)*scale, (40+ny*38+(21.5/40*38))*scale
            canvas.create_oval(coords, fill = "#000000")

def draw_scoreboard():
    coords = 2, (260)*scale+2, (260)*scale+2, (315.5)*scale
    canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")

def update():
    canvas.delete('all')
    draw_field(field, canvas)
    draw_sidepanel()
    draw_scoreboard()

def rotate(event):
    global rotation
    char = event.char
    if (char == 'q'):
        rotation -= 1
    elif (char == 'e'):
        rotation += 1
    rotation = rotation % 4
    update()

def count_corners():
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

def undo(event):
    if (len(log) >= 1):
        global player_id
        global move_count
        last_move = log.pop()
        player, name, x, y, rotation, mirror = last_move.split('_')
        tiles = globals()[f'{name}']
        tiles = apply_rotation(tiles, int(rotation))
        tiles = apply_mirror(tiles, int(mirror))
        draw_tile("#", tiles, int(x), int(y))
        player_id = int(player)
        globals()[f'player{player_id}_tiles'][f'{name}'] += 1
        move_count -= 1
        print("Reverted the last move!")
        update()
    else:
        print("There is nothing to undo!")

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
    mirror = mirror % 2
    update()

def check_for_moves(player_id):
    moves = []
    count_corners()
    print(f"""Player {player_id} corners: {globals()[f"Player{player_id}_corners"]}""")
    corners = globals()[f"Player{player_id}_corners"]
    for name in tiles_list:  # goes through every tile name in tile_list
        tiles = globals()[f"{name}"]
        for str in corners:
            x, y = str.split("_")
            x = int(x)
            y = int(y)
            for rotation in range(4):   # cycles through 4 rotations
                tiles = apply_rotation(tiles, rotation)
                for mirror in range(2): # checks both mirror possibilities
                    tiles = apply_mirror(tiles, mirror)
                    for square in tiles:
                        vx = (square % 5) -2
                        vy = (square // 5) -2
                        if (check_tile(player_id, tiles, name, x-vx, y-vy)):
                            if ((x-vx) // 10 == 0):
                                lx = f"0{x-vx}"
                            else:
                                lx = f"{x-vx}"
                            if ((y-vy) // 10 == 0):
                                ly = f"0{y-vy}"
                            else:
                                ly = f"{y-vy}"
                            moves.append(f"{name}_{lx}_{ly}_{rotation}_{mirror}")

    print(f"moves = {moves}")
    print(f"Amount of moves: {len(moves)}")
    if ((not moves) and move_count // len(players) != 0):
        return False
    return True

def game_over(event=None):
    print("Its game over!")
    print(f"""Score:""")
    score_list = []
    for id, player in enumerate(players):
        locals()[f"Player{id}_score"] = 0
        all_pieces_placed = True
        for item_id, item in enumerate(globals()[f"player{id}_tiles"].items()):
            if (item[1] == 1):
                locals()[f"Player{id}_score"] -= int(item[0][1])
                all_pieces_placed = False
        if (all_pieces_placed):
            for str in reverse(log):
                pl, name, x, y, rotation, mirrored = str.split("_")
                if (pl == id):
                    if (name == "I1"):
                        locals()[f"Player{id}_score"] = 20
                    else:
                        locals()[f"Player{id}_score"] = 15
                    break

        score = locals()[f"Player{id}_score"]
        print(f"{player}: {score}")
        score_list.append(score)
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
        else:
            print(f"Team 2 ({players[1]} and {players[3]}) won with {team2_score} points!")

field = generate_field(field_size, field_size)
win = Tk()
canvas = Canvas(win, width = startX, height = startY, bg = "#cccccc", confine = False)
canvas.pack(anchor = 'nw')
update()
count_corners()
check_for_moves(0)
win.bind("<Configure>", rezoom)
win.bind("<Button-1>", click_event)
win.bind("q", rotate)
win.bind("e", rotate, add = "+")
win.bind("<Control-z>", undo)
win.bind("s", change_mirror)
win.minsize(400, 320)
win.title("Blokus game")
win.bind("g", game_over)
win.mainloop()
