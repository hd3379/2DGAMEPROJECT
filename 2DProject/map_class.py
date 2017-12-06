from pico2d import *
import json

class Map:

    def __init__(self):
        self.map_height = []
        self.map_left = 0
        self.map_right = 8
        
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
        for height in self.map_height:
            draw_line(i*100,oldheight,(i+1)*100,height)
            i = i+1
            oldheight = height
