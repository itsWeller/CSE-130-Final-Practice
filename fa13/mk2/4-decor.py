def in_range(i, (a,b)):
    def wrapper(f):
        def wrapped(*args):
            rv = f(*args)
            syn = "big"

            if i < 0:
                if not(a <= rv <= b):
                    if rv < a:
                        syn = "small"
                    raise Exception("Return value "+str(rv)+" too "+syn)
                else:
                    return rv
            else:
                if i < len(args):
                    if not(a<=args[i]<=b):
                        if args[i] < a:
                            syn = "small"
                        raise Exception(str(i)+"th arg " + str(args[i]) + " too " + syn)
                return rv
        return wrapped
    return wrapper

@in_range(0, (0,10))
@in_range(1, (-10,20))
def plus(a,b): return a+b

print plus(-1,3)

                
