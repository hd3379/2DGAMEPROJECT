from pico2d import *
import json

class Map:

    def __init__(self):
        self.map_height = []
        self.map_left = 0
        self.map_right = 8
        self.mapx , self.mapy = 200,300
        self.cloudx = 0
        self.apartx = 0
        self.Treex = 0
        self.cloud = load_image('resource\\cloud.png')
        self.apart = load_image('resource\\apart.png')
        self.Tree = load_image('resource\\Tree.png')
        self.bgm = load_music('sound\\(Yoshis Island) - Athletic.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        global stacked_time
        stacked_time = 0

    def exit(self):
        del(self.cloud)
        del(self.Tree)
        del(self.apart)
        self.bgm.stop()
        del(self.bgm)
        
    def CreateMap(self):
        map_data_file = open('map_data.txt','r')

        lines = map_data_file.readlines()
        
        for line in lines:
            num = int(line)
            self.map_height.append(num)

        map_data_file.close()
        
    def draw(self):
        i = 0
        oldheight = 500
        self.cloud.clip_draw_to_origin(int(self.cloudx),0,800,600,0,0)
        self.apart.clip_draw_to_origin(int(self.apartx),0,800,600,0,0)
        if self.Treex < 1600:
            self.Tree.clip_draw_to_origin(int(self.Treex),0,800,600,0,0)
        else:
            self.Tree.clip_draw_to_origin(int(self.Treex),0,int(2400 - self.Treex),600,0,0)
            self.Tree.clip_draw_to_origin(0,0,int(self.Treex - 1600),600,int(2400 - self.Treex),0)
        if self.Treex >=2400:
            self.Treex-=2400
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
                self.cloudx += vecx*(pacoX - self.mapx)/10000.0
                self.apartx += vecx*(pacoX - self.mapx)/5000.0
                self.Treex += vecx*(pacoX - self.mapx)/500.0
            elif self.mapx  > pacoX + 1:
                self.mapx += -1 + vecx*(self.mapx - pacoX)/200
                self.cloudx -= vecx*(pacoX - self.mapx)/10000.0
                self.apartx -= vecx*(pacoX - self.mapx)/2000.0
                self.Treex -= vecx*(pacoX - self.mapx)/500.0             

            if self.mapy + 1 < pacoY:
                self.mapy += vecy*(pacoY - self.mapy)/100
            elif self.mapy > pacoY + 1:
                self.mapy += vecy*(self.mapy - pacoY)/100

    def get_map(self):
        return self.map_height

    def get_maplocation(self):
        return self.mapx, self.mapy
