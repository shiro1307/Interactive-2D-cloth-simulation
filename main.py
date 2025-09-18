import math

points = []
lines = []
dt = 0.005
g = 9.8
m = 0.25

k = 5

running = False

def addPoint(x,y,hooked=False):
    points.append([x,y,0,0,0,0,hooked])

def dist(a,b,c,d):
    return math.sqrt( (a-c)**2 + (b-d)**2 )

def addLine(i,j):
    lines.append( [i,j, math.hypot( points[i][0] - points[j][0] , points[i][1] - points[j][1] ) ] )

def applyForceToPoint(i):

    if running:
        points[i][2] += (points[i][4]/m)*dt
        points[i][3] += (points[i][5]/m)*dt

        dampvel = 1
        points[i][0] += points[i][2]*dt*dampvel
        points[i][1] += points[i][3]*dt*dampvel

        points[i][4],points[i][5] = 0,(0 if points[i][6] else g)

def applySpringToEdge(j):

    if running:

        pi , pj = lines[j][0],lines[j][1]

        dx = points[pj][0] - points[pi][0]
        dy = points[pj][1] - points[pi][1]
        dist = math.hypot(dx,dy)

        relvx = points[pj][2] - points[pi][2]
        relvy = points[pj][3] - points[pi][3]

        if dist==0:
            dist += 0.01

        ux,uy = dx/dist,dy/dist

        rel_v_spring = relvx*ux + relvy*uy

        damp =0.5

        f = k * (dist - lines[j][2]) + damp * rel_v_spring
        fx,fy = -f*ux,-f*uy

        points[pi][4] -= fx/m
        points[pi][5] -= fy/m

        points[pj][4] += fx/m
        points[pj][5] += fy/m
