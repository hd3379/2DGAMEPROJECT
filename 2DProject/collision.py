import math


def WheelWithGround(x1,y1,size,map_height):
    # ax + by + c ,  -by = ax + c
    c = 600 - map_height[int(x1/100)]
    a = (map_height[int(x1/100)] -map_height[int(x1/100)+1])/100.0
    b = -1
    x = x1 - int(x1/100)*100
    d = abs(a*x + b*y1 + c)/ math.sqrt(pow(a,2)+pow(b,2))
    if d < size:
        return 1

    if int(x1/100) >= 1:
        c = 600 - map_height[int(x1/100)-1]
        a = (map_height[int(x1/100)-1] -map_height[int(x1/100)])/100
        b = -1
        x = x1 - int(x1/100)*100 - 100
        d = abs(a*x + b*y1 + c)/ math.sqrt(pow(a,2)+pow(b,2))
        if d < size:
            return 1

    return 0
