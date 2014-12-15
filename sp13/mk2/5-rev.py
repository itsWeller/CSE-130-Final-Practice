def rev(l):
    return [l[-x] for x in range(1,len(l)+1)]

def rev2(l):
    def fold_fn(acc,elm):return [elm]+acc
    return reduce(fold_fn, l, [])

print rev2([1,2,3])
