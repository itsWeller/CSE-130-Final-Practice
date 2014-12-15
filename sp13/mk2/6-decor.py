def print_some(l):
    def wrapper(f):
        def wrapped(*args):
            for i in l:
                if i < 0:
                    print_flag = True
                else:
                    if i < len(args):
                        print "Arg " + str(i) + ": " + str(args[i])
            rv = f(*args)
            if print_flag:
                print "Return: " + str(rv)
            return rv
        return wrapped
    return wrapper

@print_some([-1,1,0])
def plus(x,y):
    print "-- plus called --"
    return x+y

print plus(1,2)

@print_some([-2,100])
def plus(x,y):
    print "-- plus called --"
    return x + y

print plus(1,2)



