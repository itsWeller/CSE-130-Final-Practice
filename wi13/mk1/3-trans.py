A=[[1,2,3],
   [4,5,6]]

def transpose(m):
    height = len(m)
    width = len(m[0])
    return[[m[row][col] for row in range(height)] for col in range(width)]

print transpose(A)
