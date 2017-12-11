from pico2d import *
import json

class Map:

    def __init__(self):
        self.map_height = []
        self.map_left = 0
        self.map_right = 8
        self.mapx , self.mapy = 200,300
        global stacked_time
        stacked_time = 0
        
    def CreateMap(self):
        map_data_file = open('map_data.txt','r')

        lines = map_data_file.readlines()
        
        for line in lines:
            num = int(line)
            self.map_height.append(num)

        print(self.map_height)
        map_data_file.close()
        
    def draw(self):
        i = 0
        oldheight = 500
        map_scrollx = self.mapx
        map_scrolly = self.mapy
        for height in self.map_height:
            draw_line(int(i*100 - map_scrollx),oldheight,
                      int((i+1)*100 - map_scrollx),height)
            i = i+1
            oldheight = height


    def update(self,pacoX,pacoY, vecx,vecy, delta_time):
        global stacked_time
        stacked_time += delta_time
        
        if(stacked_time > 0.01):
            stacked_time -= 0.01

            if self.mapx + 1 < pacoX:
                self.mapx += 1 + vecx*(pacoX - self.mapx)/200
            elif self.mapx  > pacoX + 1:
                self.mapx += -1 + vecx*(self.mapx - pacoX)/200

            if self.mapy + 1 < pacoY:
                self.mapy += vecy*(pacoY - self.mapy)/100
            elif self.mapy > pacoY + 1:
                self.mapy += vecy*(self.mapy - pacoY)/100


    def get_map(self):
        return self.mapx, self.mapy
