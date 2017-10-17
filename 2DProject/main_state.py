import game_framework
from pico2d import *
import time

def enter():
    global paco
    open_canvas()
    paco = Bike()

def exit():
    global paco
    del(paco)
    close_canvas()


def update():
    global oldtime, now
    paco.update()
    delay(0.03)


def draw():
    clear_canvas()
    paco.draw()
    update_canvas()


def handle_events():
    global paco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            paco.handle_events(event)


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
    def draw(self):
        if self.state == self.IDLE1:
            self.idle1.draw(self.x,self.y)
        elif self.state == self.IDLE2:
            self.idle2.draw(self.x,self.y)
        elif self.state == self.UP1:
            self.up1.draw(self.x,self.y)
        elif self.state == self.UP2:
            self.up2.draw(self.x,self.y)
        elif self.state == self.DOWN1:
            self.down1.draw(self.x,self.y)
        elif self.state == self.DOWN2:
            self.down2.draw(self.x,self.y)

    def update(self):
        if self.state %2 == 0:
            self.state+=1
        else:
            self.state-=1
        if self.state in (self.UP1,self.UP2):
            degree+=2
        elif self.state in (self.DOWN1,self.DOWN2):
            degree-=2

    def handle_events(self,event):
        if (event.type,event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP1
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.DOWN1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.IDLE1
        elif (event.type,event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.IDLE1