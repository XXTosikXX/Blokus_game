from tkinter import *

yes = 1
field_size = 14
scale = 1.0
canvasX = 400
canvasY = 320
startX = 400 - 4
startY = 320 - 4
player = "Player 1"
player1_color = "#ff6666"
player2_color = "#66ff66"
active_tile = "None"
move_count = 0
rotation = 0
log = []

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

player1_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

player2_tiles = {"I5" : 1, "I4" : 1, "I3" : 1, "I2" : 1, "I1" : 1,
"U5" : 1, "O4" : 1, "X5" : 1, "P5" : 1, "W5" : 1, "T5" : 1, "T4" : 1,
"V5" : 1, "V3" : 1, "Z5" : 1, "Z4" : 1, "F5" : 1, "L5" : 1, "L4" : 1,
"N5" : 1, "Y5" : 1}

def rezoom(event):
    global scale
    global canvasX
    global canvasY
    global startX
    global startY
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
        canvas.config(width = canvasX, height = canvasY)
    elif (x/canvasX > y/canvasY):
        #canvas.scale("all", 2, 2, y/canvasY, y/canvasY)
        canvasX = canvasX*y/canvasY
        canvasY = canvasY*y/canvasY
        canvas.config(width = canvasX, height = canvasY)
    scale = canvasX/startX
    update()

def generate_field(x, y):
    field = []
    for i in range(y):
        field.append([0,]*x)
    return field

def draw_field(field, canvas):
    row = 0
    column = 0
    for y in field:
        for x in y:
            if (x == 0):
                if ((column + row) % 2 == 0):
                    color = "#fafafa"
                else:
                    color = "#eeeeee"
            elif (x == 1):
                color = player1_color
            elif (x == 2):
                color = player2_color
            draw_square(column, row, color, canvas)
            column += 1
        row += 1
        column = 0

def draw_square(x, y, color, canvas):
    a = 260/field_size * scale
    coords = 2+x*a, 2+y*a, 2+(x+1)*a, 2+(y+1)*a
    canvas.create_rectangle(coords, fill = color)

def click_event(event):
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
            id = int(player[-1])
            tile_list = list(globals()[f'player{id}_tiles'].items())
            tile_name = tile_list[vy*3+vx][0]
            if (active_tile != tile_name):
                active_tile = tile_name
            else:
                active_tile = "None"

    else: #field gets clicked
        if (active_tile != "None"):
            place_tile(active_tile, SqX, SqY)
        else:
            print("Select the tile first")
    update()

def place_tile(name, x, y):
    global log
    global player
    global move_count
    global active_tile
    if (player == "Player 1"):
        color = "#ff6666"
    else:
        color = "#66ff66"
    if(check_piece(name)):
        tiles = globals()[f'{name}']
        tiles = apply_rotation(tiles, rotation)
        if (check_move(tiles, x, y)):
            id = int(player[-1])
            globals()[f'player{id}_tiles'][f'{name}'] = 0
            draw_tile(player, tiles, x, y)
            move_count += 1
            if id == 1:
                player = "Player 2"
            else:
                player = "Player 1"
            active_tile = "None"
            count_corners()
            log.append(f"{name}_{x}_{y}_{rotation}")
    else:
        print(f"{player} has no more pieces of that kind!")

def check_piece(name):
    id = int(player[-1])
    if globals()[f"player{id}_tiles"][f"{name}"] == 1:
        return True
    return False

def check_move(tiles, x, y):
    if (move_count // 2 == 0):
        valid_first_move = check_first_move(tiles, x, y)
        if (valid_first_move == False):
            print("First tile should occupy square in a corner!")
            return False
    valid_boundaries = check_boundaries(tiles, x, y)
    if (valid_boundaries):
        valid_CAE = check_CAE(player, tiles, x, y) #CAE = Corners And Edges
        if (valid_CAE):
            return True
    return False

def check_first_move(tiles, x, y):
    bottom_left = True
    bottom_right = True
    top_left = True
    top_right = True
    id = int(player[-1])
    if (field[0][field_size-1] != 0):               # top_right
        bottom_right = top_left = top_right = False
    elif (field[0][0] != 0):                        # top_left
        top_left = bottom_left = top_right = False
    elif (field[field_size-1][0] != 0):             # bottom_left
        bottom_right = top_left = bottom_left = False
    elif (field[field_size-1][field_size-1] != 0):  # bottom_right
        top_right = bottom_right = bottom_left = False
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

def check_CAE(player, tiles, x, y):
    edge_flag = True
    corner_flag = False
    id = int(player[-1])
    for tile in tiles:
        vx = (tile % 5) - 2
        vy = (tile // 5) - 2
        if (field[y+vy][x+vx] == 0):
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
            print("Cannot place over other tiles!")
            return False
    if (edge_flag):
        if (corner_flag):
            return True
        elif (move_count // 2 == 0):
            return True
        else:
            print("Tiles have to touch each other with at least 1 corner!")
            return False
    else:
        print("Edges of your tiles should not touch each other!")
        return False

def check_boundaries(tiles, x, y):
    valid = True
    for tile in tiles:
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
        print("Invalid location, out of map")
        return False

def draw_tile(player, tiles, x, y):
    for tile in tiles:
        vx = (tile % 5)-2
        vy = (tile // 5)-2
        field[y+vy][x+vx] = int(player[-1])

def draw_sidepanel():
    coords = 260*scale, 2, 396*scale, 316*scale
    canvas.create_rectangle(coords, fill = "#cccccc", outline = "#000000")
    coords = (8+260)*scale, 2.5*scale, (8+260+120)*scale, (2.5+36)*scale
    canvas.create_rectangle(coords, fill = "#eeeeee")
    """l = Label(win, width = int(10), height = int(1), text = "player")
    l.place(x=260, y=20)""" # LABEL TODO
    id = int(player[-1])
    tile_list = list(globals()[f'player{id}_tiles'].items())
    for ny in range(7):
        for nx in range(3):
            coords = (260+nx*40+8)*scale, (40+ny*38)*scale, (260+(nx+1)*40+8)*scale, (40+(ny+1)*38)*scale
            tile_name = tile_list[ny*3+nx][0]
            tile = globals()[f'{tile_name}']
            rotated_tile = apply_rotation(tile, rotation)
            if (active_tile == tile_name):
                outline_color = '#999999'
                border = 2*scale
                coords = (260+nx*40+8+1)*scale+1, (40+ny*38+1)*scale+1, (260+(nx+1)*40+8-1)*scale, (40+(ny+1)*38-1)*scale
            else:
                border = 1
                outline_color = '#000000'
            canvas.create_rectangle(coords, fill = "#ffffff", outline = outline_color, width = border)
            if (globals()[f"player{id}_tiles"][f'{tile_name}'] == 0):
                color = "#aaaaaa"
            else:
                color = globals()[f'player{id}_color']
            for square in rotated_tile:
                vx = (square % 5)
                vy = (square // 5)
                coords = (260+nx*40+8+vx*8)*scale, (40+ny*38+vy*38/5)*scale, (260+nx*40+8+(vx+1)*8)*scale, (40+ny*38+(vy+1)*38/5)*scale
                canvas.create_rectangle(coords, fill = color, outline = "#000000")
            coords = (260+nx*40+8+18.5)*scale, (40+ny*38+(18.5/40*38))*scale, (260+nx*40+8+21.5)*scale, (40+ny*38+(21.5/40*38))*scale
            canvas.create_oval(coords, fill = "#000000")

def draw_scoreboard():
    coords = 2, (260)*scale+2, (260)*scale, (316)*scale
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
    Player1_corners = 0
    Player2_corners = 0
    row = 0
    column = 0
    for y in field:
        for x in y:
            if(check_corners("Player 1", row, column)):
                Player1_corners += 1
            if(check_corners("Player 2", row, column)):
                Player2_corners += 1
            column +=1
        column = 0
        row += 1
    #print(f"Player1_corners: {Player1_corners}\nPlayer2_corners: {Player2_corners}")

def check_corners(player, x, y):
    id = player[-1]
    edge_flag = True
    corner_flag = False
    if (field[y][x] == 0):
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
    global player
    global move_count
    last_move = log.pop()
    name, x, y, rotation = last_move.split('_')
    tiles = globals()[f'{name}']
    tiles = apply_rotation(tiles, int(rotation))
    #print(f"name: {name}, tiles: {tiles} x: {x}, y: {y}, rotation: {rotation}")
    draw_tile("Player 0", tiles, int(x), int(y))
    if (player == "Player 1"):
        globals()[f'player2_tiles'][f'{name}'] += 1
        player = "Player 2"
    else:
        globals()[f'player1_tiles'][f'{name}'] += 1
        player = "Player 1"
    move_count -= 1
    update()

field = generate_field(field_size, field_size)
win = Tk()
canvas = Canvas(win, width = startX, height = startY, bg = "#cccccc", confine = False)
canvas.pack(anchor = 'nw')
draw_field(field, canvas)
draw_sidepanel()
win.bind("<Configure>", rezoom)
win.bind("<Button-1>", click_event)
win.bind("q", rotate)
win.bind("e", rotate, add = "+")
win.bind("<Control-z>", undo)
win.minsize(400, 320)
win.mainloop()
