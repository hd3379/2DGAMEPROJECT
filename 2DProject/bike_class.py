from pico2d import *
import vector_class
import math
import collision
import game_framework
import game_over

class Bike:

    IDLE1,IDLE2 ,UP1,UP2,DOWN1,DOWN2 = 0,1,2,3,4,5
    
    def __init__(self):
        global stacked_time
        stacked_time = 0
        self.degree = 0
        self.state = self.IDLE1
        self.x,self.y = 300,500
        self.mapx, self.mapy = 200,300
        self.drawx, self.drawy = 200,300
        self.idle1 = load_image('resource\\idle1.png')
        self.idle2 = load_image('resource\\idle2.png')
        self.up1 = load_image('resource\\up1.png')
        self.up2 = load_image('resource\\up2.png')
        self.down1 = load_image('resource\\down1.png')
        self.down2 = load_image('resource\\down2.png')
        
        self.vec = vector_class.Vector()
        self.RightMove = False
        self.LeftMove = False
        self.headx, self.heady = self.x , self.y -30
        self.headSize = 25
        self.tohead = 30
        self.LWx , self.LWy = self.x - 58 , self.y + 12
        self.toLW = 74
        self.Wsize = 23  # W = Wheel
        self.RWx , self.RWy = self.x + 72 , self.y + 12
        self.toRW = 86
        
    def draw(self):
        radi = 3.14/180.0 * self.degree
        self.drawx = self.x - self.mapx + 200
        self.drawy = self.y
        if self.state == self.IDLE1:
            self.idle1.rotate_draw(radi,self.drawx, self.drawy)
        elif self.state == self.IDLE2:
            self.idle2.rotate_draw(radi,self.drawx, self.drawy)
        elif self.state == self.UP1:
            self.up1.rotate_draw(radi,self.drawx, self.drawy)
        elif self.state == self.UP2:
            self.up2.rotate_draw(radi,self.drawx, self.drawy)
        elif self.state == self.DOWN1:
            self.down1.rotate_draw(radi,self.drawx, self.drawy)
        elif self.state == self.DOWN2:
            self.down2.rotate_draw(radi,self.drawx, self.drawy)
            
        draw_rectangle(self.LWx - self.Wsize , self.LWy - self.Wsize
                       ,self.LWx + self.Wsize , self.LWy + self.Wsize)
        
        draw_rectangle(self.RWx - self.Wsize , self.RWy - self.Wsize
                       ,self.RWx + self.Wsize , self.RWy + self.Wsize)

        draw_rectangle(self.headx - self.headSize , self.heady - self.headSize
                       ,self.headx + self.headSize , self.heady + self.headSize)

    def update(self,delta_time):
        global stacked_time
        stacked_time += delta_time
        radi = 3.14/180.0

        if(stacked_time > 0.01):
            stacked_time -= 0.01
            
            #manage state
            if self.state %2 == 0:
                self.state+=1
            else:
                 self.state-=1
            if self.state in (self.UP1,self.UP2):
                self.degree+= 2.5
                if(self.degree > 360):
                    self.degree -= 360
            elif self.state in (self.DOWN1,self.DOWN2):
                self.degree-= 2.5
                if(self.degree < -360):
                    self.degree += 360

            
            vecx , vecy = self.vec.getVector()
            
            if self.RightMove:
                if vecx < 10:
                    self.vec.Plus(0.05,0)
            if self.LeftMove:      
                if vecx > -5:
                    self.vec.Minus(0.05,0)
    

            #manage speed

            self.y += vecy

            self.drawx = self.x - self.mapx + 200
            self.drawy = self.y
            
            #collision box
            LWdegree = self.degree + 218
            RWdegree = self.degree + 328
            headDegree = self.degree + 90
            
            self.LWx = self.drawx + self.toLW * math.cos(LWdegree*radi) 
            self.LWy = self.drawy + self.toLW * math.sin(LWdegree*radi)
            self.RWx = self.drawx + self.toRW * math.cos(RWdegree*radi)
            self.RWy = self.drawy + self.toRW * math.sin(RWdegree*radi)
            self.headx = self.drawx + self.tohead * math.cos(headDegree*radi)
            self.heady = self.drawy + self.tohead * math.sin(headDegree*radi)

            #collision
            global map_height
            Lcheck , Rcheck = 0 , 0
            Lcheck = collision.WheelWithGround(self.LWx + self.mapx - 100,self.LWy,
                                                self.Wsize,map_height)
            Rcheck = collision.WheelWithGround(self.RWx + self.mapx - 100,self.RWy,
                                                self.Wsize,map_height)
            Hcheck = collision.WheelWithGround(self.headx + self.mapx - 100,self.heady,
                                                self.headSize,map_height)

            if(Hcheck):
                game_framework.push_state(game_over)

            if(Lcheck and Rcheck):
                self.y -= vecy
                self.vec.setVector(vecx,0)
                self.y += 1
            elif(Lcheck):
                self.y -= vecy
                if abs(self.degree) < 90 or abs(self.degree) > 270:
                    self.degree -= 1
                else:
                    self.degree += 1
                self.y += 1
            elif(Rcheck):
                self.y -= vecy
                if abs(self.degree) < 90 or abs(self.degree) > 270:
                    self.degree += 1
                else:
                    self.degree -= 1
                self.y += 1
            else:
                self.vec.gravity()

            self.x += vecx

            while 1:

                self.drawx = self.x - self.mapx + 200
                self.drawy = self.y
                
                #collision box
                LWdegree = self.degree + 218
                RWdegree = self.degree + 328
                headDegree = self.degree + 90
                
                self.LWx = self.drawx + self.toLW * math.cos(LWdegree*radi) 
                self.LWy = self.drawy + self.toLW * math.sin(LWdegree*radi)
                self.RWx = self.drawx + self.toRW * math.cos(RWdegree*radi)
                self.RWy = self.drawy + self.toRW * math.sin(RWdegree*radi)
                self.headx = self.drawx + self.tohead * math.cos(headDegree*radi)
                self.heady = self.drawy + self.tohead * math.sin(headDegree*radi)

                #collision
                Lcheck , Rcheck = 0 , 0
                Lcheck = collision.WheelWithGround(self.LWx + self.mapx - 100 ,self.LWy,
                                                self.Wsize,map_height)
                Rcheck = collision.WheelWithGround(self.RWx + self.mapx - 100,self.RWy,
                                                self.Wsize,map_height)
                if(Lcheck and Rcheck):
                    self.y += 1
                elif(Lcheck):
                    self.degree -=1
                    self.y += 0.2
                elif(Rcheck):
                    self.degree +=1
                    self.y +=0.2
                else:
                    break
            self.vec.friction()
                    

        

    def handle_events(self,event):
        if (event.type,event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP1
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.DOWN1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.IDLE1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.IDLE1
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.RightMove = True
            self.LeftMove = False
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.LeftMove = True
            self.RightMove = False
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.RightMove = False
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.LeftMove = False
    def get_xy(self):
        return self.x , self.y

    def get_vec(self):
        vecx , vecy = self.vec.getVector()
        return vecx , vecy

    def set_camara(self , x , y):
        self.mapx = x
        self.mapy = y

    def set_map(self,Map_height):
        global map_height
        map_height = Map_height
