import math


def BoxWithGround(x1,y1,x2,y2,height):
    if y2 < height or y1 < height:
        return True
    else:
        return False
