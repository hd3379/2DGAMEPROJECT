import game_framework
from pico2d import *
import random
class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN , LEFT_STAND, RIGHT_STAND = 0,1,2,3
   

    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = random.randint(0,99)
        self.stand_frames =random.randint(0,49)
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        

    def handle_left_run(self):
        self.x -=5
        self.run_frames +=1

    def handle_left_stand(self):
        self.stand_frames +=1
        
    def handle_right_run(self):
        self.x += 5
        self.run_frames +=1

    def handle_right_stand(self):
        self.stand_frames += 1
        
    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def handle_event(self , event):
        if (event.type,event.key) == (SDL_KEYDOWN,SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
            elif self.state == self.RIGHT_RUN:
                self.state = self.RIGHT_STAND
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
            elif self.state == self.LEFT_RUN:
                self.state = self.LEFT_STAND
        elif (event.type,event.key) == (SDL_KEYUP,SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type,event.key) == (SDL_KEYUP,SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND

    def update(self):
        self.frame = (self.frame +1) %8
        if self.state == self.RIGHT_RUN:
            self.x = min(800,self.x +5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0,self.x -5)
        
    def SetPoint(self,X,Y):
        self.x = X
        self.y = Y

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
