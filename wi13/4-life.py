def access(g,x,y):
    try: return g[y][x]
    except: return 0

def count_live_neighbours(g,x,y):
    live = 0
    for x_delta in [-1,0,1]:
        for y_delta in [-1,0,1]:
            if access(g,x+x_delta,y+y_delta) and x!=x_delta and y!=y_delta:
                live += 1
    return live

def new_val(g,x,y):
    homies = count_live_neightbours(g,x,y)

    if access(g,x,y):   #Alive
        if 2 <= homies <= 3:
            return 1
    else:
        if homies == 3:
            return 1
    return 0

def step(g):
    height = len(g)
    width = len(g[0])
    return [[new_val(g,col,row) for col in range(width)] for row in range(height)]
