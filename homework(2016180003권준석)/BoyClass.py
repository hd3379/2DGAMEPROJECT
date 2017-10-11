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
        self.state = self.RIGHT_RUN
        self.run_frames = random.randint(0,99)
        self.stand_frames =random.randint(0,49)
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        

    def handle_left_run(self):
        self.x -=5
        self.run_frames +=1
        if self.x <0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames +=1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
        
    def handle_right_run(self):
        self.x += 5
        self.run_frames +=1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0
        
    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame +1) %8
        self.handle_state[self.state](self)
        
    def SetPoint(self,X,Y):
        self.x = X
        self.y = Y

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
