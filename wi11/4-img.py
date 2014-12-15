img1=[[255,255,  0,  0,255,255],
      [255,255,  0,  0,255,255],
      [  0,  0,255,  0,  0,  0],
      [  0,  0,255,255,  0,  0],
      [255,  0,  0,  0,  0,255],
      [  0,255,255,255,255,  0]]

def create_image(w,h,c):
    return [[c for x in range(w)] for y in range (h)]

gi = create_image(3,2,27)

def well_formed(img):
    try: w = len(img[0])
    except: return False

    try: c = img[0][0]
    except: c = None

    for x in img:
        if len(x) != w:
            return False
    for x in img:
        for y in x:
            if y != c:
                return False
    return True

def fill_rect(img,x0,y0,x1,y1,c):
    min_x = max(0,x0)
    min_y = max(0,y0)
    max_x = min(len(img[0]))

