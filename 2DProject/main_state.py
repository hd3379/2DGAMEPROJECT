import game_framework
from pico2d import *
import time
import map_class
import bike_class

def enter():
    global paco
    global ground
    global current_time
    open_canvas()
    paco = bike_class.Bike()
    ground = map_class.Map()
    current_time = get_time()

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
    ground.draw()
    update_canvas()


def handle_events():
    global paco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            paco.handle_events(event)


