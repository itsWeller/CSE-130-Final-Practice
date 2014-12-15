d = [ ("a", 10), ("b", 20), ("c", 30), ("a", 40) ]

def lookup(d,k):
    return [v for (kd,v) in d if kd==k]

print lookup(d,"d")

def cond(b,t,f):
    if b: return t
    else: return f

def update(d,k,v):
    return [(a,cond(a == k,v,b)) for (a,b) in d]

print update(d, "a", "CSE130")

def delete(d,k):
    return [(a,b) for (a,b) in d if k != a]

print delete(d,"a")

def add(d,k,v):
    return d + [(k,v)]

def update2(d,k,v):
    l = []
    for (a,b) in d:
        if a == k:
            l.append(k,v)
        else:
            l.append(a,b)
    return l

