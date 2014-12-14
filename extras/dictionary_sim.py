d = [("a",10),("b",20),("c",30),("a",40)]

def lookup(d,k):
    return [x for (a,x) in d if a == k]

print lookup(d,"a")

def cond(b,t,f):
    if b: return t
    else: return f

def update(d,k,v):
    return [(a,cond(a==k,v,x)) for (a,x) in d]

print update(d,"b","CSE130")

def delete(d,k):
    return [(a,x) for (a,x) in d if a!=k]

print delete(d,"b")

def update2(d,k,v):
    l = []

    for (a,x) in d:
        if a == k:
            l.append((a,v))
        else:
            l.append((a,x))

    return l

print update2(d,"b","FUCK")
