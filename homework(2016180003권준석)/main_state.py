import game_framework
from pico2d import *
import random
import numbers
import BoyClass
import json_player

def enter():
    global boy,grass
    global team , num,running
    open_canvas()
    boy = BoyClass.Boy()
    grass = Grass()
    team = json_player.create_team()
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
    numbers.draw(num+1,740,540)
    update_canvas()


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)




def handle_events():
    global num
    global running
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
             running = False
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_DOWN):
                num = num+1
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_UP):
                num = num-1
        else:
            team[num].handle_event(event)


