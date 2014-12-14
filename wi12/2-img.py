img1=[[ 11,  0, 12],
      [  0,  0,  0],
      [ 13,  0, 14],
      [ 15, 16, 17]]

def square_img(img):
    return [[i**2 for i in l] for l in img]

print square_img(img1)

def crop_img(img,x1,y1,x2,y2):
    return [i[x1:x2] for i in img[y1:y2]]

print crop_img(img1,0,1,2,4)

def zip(l1,l2):
    min_len = min(len(l1),len(l2))
    l = []

    for x in range(min_len):
        l.append((l1[x],l2[x]))

    return l

def zip2(l1,l2):
    return [(l1[x],l2[x]) for x in range(min(len(l1),len(l2)))]

print zip2([1,2,3], [4,5]) 

def add_imgs(img1,img2):
    return [[L1+L2 for (L1,L2) in zip(l1,l2)] for (l1,l2) in zip(img1,img2)]

print add_imgs(img1,img1)
