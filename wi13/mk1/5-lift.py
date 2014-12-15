def lift_1(f):
    def decorated(x):
        return [f(i) for i in x]
    return decorated

def lift_2(f):
    def decorated(x,y):
        return [f(i,j) for (i,j) in zip(x,y)]


