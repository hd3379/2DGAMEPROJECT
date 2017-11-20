from pico2d import *
import json

class Map:

    def __init__(self):
        self.map_height = []
        
    def CreateMap(self):
        map_data_file = open('map_data.txt','r')

        lines = map_data_file.readlines()
        
        for line in lines:
            num = int(line)
            self.map_height.append(num)

        print(self.map_height)
        map_data_file.close()



ground = Map()
ground.CreateMap()
