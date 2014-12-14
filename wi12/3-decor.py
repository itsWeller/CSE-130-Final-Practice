def derivative(delta):
    def wrapper(f):
        def wrapped(*args):
            return (f(args[0] + delta) - f(args[0]))/delta
        return wrapped
    return wrapper

@derivative(0.0001)
def double(x): return 2*x

print double(10.0)
print double(20.0)
print double(30.0)

@derivative(0.0001)
def square(x): return x*x

print square(10.0)
print square(20.0)
print square(30.0)
