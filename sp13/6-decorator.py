def print_some(l):
    def wrapper(f):
        rv = None
        print_fag = False
        def wrapped(*args):
            rv = f(*args)
            if i < 0:
                print_fag = True
                return rv
            else:
                for i in l:
                    if l[i] < len(args):
                        print args[l[i]]
                return rv
        if print_fag:
            print str(rv)
        return wrapped
    return wrapper

