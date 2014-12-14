def lift_1(f):
    def decorated(x):
        return [f(y) for y in x]
    return decorated

@lift_1
def inc(x): return x+1

print inc([1,2,3])

def lift_2(f):
    def decorated(x,y):
        return [f(a,b) for a,b in zip(x,y)]
    return decorated

@lift_2
@lift_2
def plus(x,y): return x+y

print plus([1,2,3,4],[4,5,6,7])
