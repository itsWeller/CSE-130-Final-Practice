def rev_1(l):
    return l[::-1]

def rev_2(l):
    def fold_fn(acc,elm): return [elm] + acc
    return reduce(fold_fn,l,[])

print rev_2([1,2,3,4,5])
