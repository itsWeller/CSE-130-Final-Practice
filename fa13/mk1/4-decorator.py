def in_range(a,(b,c)):
    def wrapper(f):
        def wrapped(*args):
            rv = f(*args)
            if a < 0:
                if rv > c:
                    syn = "big"
                else:
                    syn = "small"
                if not (b <= rv <= c):
                    raise Exception("Return value "+rv+"too "+syn)
            elif a < len(args):
                if args[a] > c:
                    syn = "big"
                else:
                    syn = "small"
                if not (b <= args[a] <= c):
                    raise Exception(""+str(a)+"th argument " +str(args[a])+ " too " + syn)
            else:
                return rv
        return wrapped
    return wrapper

                
@in_range(0, (0,10))
@in_range(1, (-10,20))
def plus(a,b): return a+b

print plus(10,-5)
