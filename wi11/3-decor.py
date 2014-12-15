def print_first_k_args(k):
    def wrapper(f):
        def wrapped(*args):
            for i in range(k):
                if i < len(args):
                    print "Arg " + str(i+1) + ": " + str(args[i])
            rv = f(*args)
            print "Return: " + str(rv)
            return rv
        return wrapped
    return wrapper

@print_first_k_args(1)
def sum(a,b): return a + b
print sum(3,4)

@print_first_k_args(2)
def sum(a,b): return a + b
print sum(3,4)

@print_first_k_args(3)
def sum(a,b): return a + b
print sum(3,4)

@print_first_k_args(1)
def fac(n):
    if n <= 0: return 1
    else: return n*fac(n-1)

print fac(3)

