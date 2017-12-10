from pico2d import *
import vector_class
import math

class Bike:

    IDLE1,IDLE2 ,UP1,UP2,DOWN1,DOWN2 = 0,1,2,3,4,5
    
    def __init__(self):
        self.degree = 0
        self.state = self.IDLE1
        self.x,self.y = 200,200
        self.idle1 = load_image('resource\\idle1.png')
        self.idle2 = load_image('resource\\idle2.png')
        self.up1 = load_image('resource\\up1.png')
        self.up2 = load_image('resource\\up2.png')
        self.down1 = load_image('resource\\down1.png')
        self.down2 = load_image('resource\\down2.png')
        self.vec = vector_class.Vector()
        self.LWx , self.LWy = self.x - 58 , self.y + 12
        self.toLW = 74
        self.Wsize = 23  # W = Wheel
        self.RWx , self.RWy = self.x + 72 , self.y + 12
        self.toRW = 86
        
    def draw(self):
        radi = 3.14/180.0 * self.degree
        if self.state == self.IDLE1:
            self.idle1.rotate_draw(radi,self.x,self.y)
        elif self.state == self.IDLE2:
            self.idle2.rotate_draw(radi,self.x,self.y)
        elif self.state == self.UP1:
            self.up1.rotate_draw(radi,self.x,self.y)
        elif self.state == self.UP2:
            self.up2.rotate_draw(radi,self.x,self.y)
        elif self.state == self.DOWN1:
            self.down1.rotate_draw(radi,self.x,self.y)
        elif self.state == self.DOWN2:
            self.down2.rotate_draw(radi,self.x,self.y)
            
        draw_rectangle(self.LWx - self.Wsize , self.LWy - self.Wsize
                       ,self.LWx + self.Wsize , self.LWy + self.Wsize)
        
        draw_rectangle(self.RWx - self.Wsize , self.RWy - self.Wsize
                       ,self.RWx + self.Wsize , self.RWy + self.Wsize)

    def update(self):
        #manage state
        if self.state %2 == 0:
            self.state+=1
        else:
            self.state-=1
        if self.state in (self.UP1,self.UP2):
            self.degree+=2
        elif self.state in (self.DOWN1,self.DOWN2):
            self.degree-=2


        #manage speed
        vecx , vecy = self.vec.getVector()
        self.x += vecx
        self.y += vecy

        #collision box
        radi = 3.14/180.0
        LWdegree = self.degree + 218
        RWdegree = self.degree + 328
        
        self.LWx = self.x + self.toLW * math.cos(LWdegree*radi) 
        self.LWy = self.y + self.toLW * math.sin(LWdegree*radi)
        self.RWx = self.x + self.toRW * math.cos(RWdegree*radi)
        self.RWy = self.y + self.toRW * math.sin(RWdegree*radi)

        
        

    def handle_events(self,event):
        if (event.type,event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP1
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.DOWN1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.IDLE1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.IDLE1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.vec.Plus(1,0)
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.vec.Minus(1,0)

    def get_x(self):
        return self.x
