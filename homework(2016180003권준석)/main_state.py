import game_framework
from pico2d import *
import random

def enter():
    global boy,grass
    global team , num,running
    open_canvas()
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(1000)]
    num = 0
    running = True;

def exit():
    global boy, grass
    del(boy)
    del(grass)
    close_canvas()

        
def update():
    for boy in team:
        boy.update()
    delay(0.05)


def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    print(num+1)
    update_canvas()


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN , LEFT_STAND, RIGHT_STAND = 0,1,2,3
   

    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.state = self.RIGHT_RUN
        self.run_frames = 0
        self.stand_frames =0
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
            



def handle_events():
    global num
    global running
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x,600 - event.y
            team[num].SetPoint(x,y)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x,y = event.x,600 - event.y
            team[num].SetPoint(x,y)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == SDLK_DOWN:
                num = num+1
            elif event.key == SDLK_UP:
                num = num-1


