import game_framework
from pico2d import *
import random

def enter():
    global boy,grass
    global team , num,running
    boy = Boy()
    grass = Grass()
    open_canvas()
    team = [Boy() for i in range(11)]
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
    update_canvas()


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
        

    def update(self):
        self.frame = (self.frame +1) % 8
        self.x +=5
        if self.x > 800:
            self.x=0
    def SetPoint(self,X,Y):
        self.x = X
        self.y = Y

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
            



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
            elif event.key == SDLK_1:
                num = 1
            elif event.key == SDLK_2:
                num = 2
            elif event.key == SDLK_3:
                num = 3
            elif event.key == SDLK_4:
                num = 4
            elif event.key == SDLK_5:
                num = 5
            elif event.key == SDLK_6:
                num = 6
            elif event.key == SDLK_7:
                num = 7
            elif event.key == SDLK_8:
                num = 8
            elif event.key == SDLK_9:
                num = 9
            elif event.key == SDLK_0:
                num = 0



