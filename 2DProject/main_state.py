import game_framework
from pico2d import *
import time
import map_class
import bike_class

def enter():
    global paco
    global ground
    global old_time
    open_canvas()
    paco = bike_class.Bike()
    ground = map_class.Map()
    old_time = get_time()
    ground.CreateMap()

def exit():
    global paco ,ground
    del(paco)
    del(ground)
    close_canvas()


def update():
    global old_time, now , delta_time
    now = get_time()
    delta_time = now - old_time
    old_time = now
    
    paco.update(delta_time)
    
    x , y = paco.get_xy()
    vecx ,vecy = paco.get_vec()
    ground.update(x,y,vecx,vecy,delta_time)
    camarax , camaray = ground.get_map()
    paco.set_camara(camarax,camaray)


def draw():
    global paco, ground
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


