from pyray import *

import math
import main

sx,sy = 1700,900
r = 10
showlabel = False

is_drawing_line = False
last_point = None

def point_line_distance(x0, y0, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    numerator = abs(dy*x0 - dx*y0 + x2*y1 - y2*x1)
    denominator = math.hypot(dx,dy)
    return numerator / denominator

def handle_force_and_springs():

    #handlelines
    for i,l in enumerate(main.lines):
        a = main.points[l[0]]
        b = main.points[l[1]]
        draw_line_ex( [int(a[0]),int(a[1])] , [int(b[0]),int(b[1])] , 2 ,WHITE)

        main.applySpringToEdge(i)

    #handlepoints
    for i,p in enumerate(main.points):
        if not p[6]:
            main.applyForceToPoint(i)

        if showlabel:
            draw_text(str(i) , int(p[0])+10 , int(p[1])+10 , 30 , WHITE)

        if not main.running:
            draw_circle( int(p[0]) , int(p[1]) , r , RED if p[6] else (BLUE if i==last_point and is_drawing_line else WHITE) )

def handle_line_deletion():
    global last_point

    m = get_mouse_position()
    mx,my = m.x,m.y

    #handle line deletion
    it = 0
    while it < len(main.lines):
        l = main.lines[it]
        p1,p2 = main.points[l[0]],main.points[l[1]]

        borderbuff = 4

        minx,maxx = min(p1[0],p2[0]) - borderbuff ,max(p1[0],p2[0]) + borderbuff
        miny,maxy = min(p1[1],p2[1]) - borderbuff ,max(p1[1],p2[1]) + borderbuff

        ldis = point_line_distance(mx,my,p1[0],p1[1],p2[0],p2[1])

        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT) and ldis<=borderbuff and mx >= minx and mx <= maxx and my >= miny and my <= maxy:
            del main.lines[it]
        else:
            it+=1

def handle_point_interaction():

    global is_drawing_line
    global last_point

    m = get_mouse_position()
    mx,my = m.x,m.y

    if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):

        isonpoint = False
        point_index = -1

        for i,p in enumerate(main.points):
            dis = math.hypot( p[0]-mx , p[1]-my )

            if dis<=r:
                isonpoint=True
                point_index = i

        if not isonpoint:
            if not is_drawing_line:
                main.addPoint(mx,my, is_key_down(KeyboardKey.KEY_LEFT_SHIFT) )
            else:
                if not is_key_down(KeyboardKey.KEY_LEFT_CONTROL):
                    is_drawing_line = False
                    last_point = -1
                    print("Stopped drawing line cus you clicked in the void.")
                else:
                    main.addPoint(mx,my, is_key_down(KeyboardKey.KEY_LEFT_SHIFT) )

                    main.addLine( len(main.points) - 1 ,last_point )

                    last_point = len(main.points) - 1
                    print("Polygon tool")

        else:
            if (not is_drawing_line) and last_point!=point_index:
                is_drawing_line = True
                last_point = point_index
                print("started drawing the line!")
            elif is_drawing_line and last_point!=point_index:

                main.addLine( point_index,last_point )

                is_drawing_line = False
                last_point = -1
                print("done drawing the line!")
            else:
                is_drawing_line = False
                last_point = -1
                print("cancelled the line. Same point clicked")

def drawline_preview():
    if is_drawing_line:

        m = get_mouse_position()
        mx,my = m.x,m.y            

        p = main.points[last_point]

        draw_line_ex( [int(p[0]),int(p[1])] , [int(mx),int(my)] , 2 ,WHITE)

def extrude_shortcut():

    if is_key_pressed(KeyboardKey.KEY_E):

        n = len(main.points)
        base_row = main.points[:n]

        rows = 8
        spacing = 40

        for y in range(1,rows+1):
            for p in base_row:
                main.addPoint(p[0],p[1]+(y*spacing), False)

        total_points = len(main.points)
        cols = n
        for row in range(1+rows):
            for col in range(cols):
                i = row * cols + col
                
                if i>=cols:
                    up = (row-1)*cols + col
                    main.addLine(i,up)

                    if (not is_key_down(KeyboardKey.KEY_LEFT_SHIFT)) and col<cols-1:
                        main.addLine(i,up+1)
                
                if col<cols-1:
                    right = i+1
                    main.addLine(i,right)

def frame():

    extrude_shortcut()

    drawline_preview()

    handle_line_deletion()

    handle_force_and_springs()

    handle_point_interaction()

    if is_key_pressed(KeyboardKey.KEY_SPACE):
        main.running = not main.running      

init_window(sx,sy, "Cloth sim")
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    
    frame()

    end_drawing()
close_window()

