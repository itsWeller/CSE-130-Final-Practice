g = [[ 0, 0, 0, 0, 0 ],
     [ 0, 0, 0, 0, 0 ],
     [ 0, 1, 1, 1, 0 ],
     [ 0, 0, 0, 0, 0 ],
     [ 0, 0, 0, 0, 0 ]]

height = len(g)
width = len(g[0])

def access(g, x, y):
    try: return g[y][x]
    except: return 0

def count_live_neightbours(g,x,y):
    live = 0
    for x_delta in [x-1,x,x+1]:
        for y_delta in [y-1,y,y+1]:
            if access(g,x_delta,y_delta) and x_delta!= x and y_delta != y:
                live+=1
        return live

def new_val(g,x,y):
    homies_still_kickin = count_live_neightbours(g,x,y)

    if access(g,x,y):
        if homies_still_kickin < 2 or homies_still_kickin > 3:
            return 0
        elif 2 <= homies_still_kickin <= 3:
            return 1
    else:
        if homies_still_kickin == 3:
            return 1

def step(g):
    height = len(g)
    width = len(g[0])
    return [[new_val(g,col,row) for col in range(width)]for row in range(height)]

while any(g[y][x] == 1 for y in range(width) for x in range(height)):
    print g
    g = step(g)


