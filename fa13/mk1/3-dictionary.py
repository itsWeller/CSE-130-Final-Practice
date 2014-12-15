def cond(b, t, f):
    if b: return t
    else: return f

def lookup(d,k):
    return [x for (a,x) in d if k == a]

def update(d,k,v):
    return [(a,cond(a == k,v,x)) for (a,x) in d]

def delete(d,k):
    return [(a,x) for (a,x) in d if a != k]

def add(d,k,v):
    return d.append((k,v))

def update2(d,k,v):
    l = []
    for (a,x) in d:
        if a == k:
            l.append((a,v))
        else:
            l.append((a,x))
    return l
d = [ ("a", 10), ("b", 20), ("c", 30), ("a", 40) ]
print update(d, "a", "CSE130")
d = [ ("a", 10), ("b", 20), ("c", 30), ("a", 40) ]
print update2(d, "a", "CSE130")
d = [ ("a", 10), ("b", 20), ("c", 30), ("a", 40) ]
add(d,"d","FUCK")
print d
