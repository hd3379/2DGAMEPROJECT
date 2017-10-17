from pico2d import *
import game_framework

def enter():
    global paco
    paco = Bike()
    open_canvas()
    

def exit():
    global paco
    del(paco)
    close_canvas()


def update():
    delay(0.05)


def draw():
    clear_canvas()
    paco.draw()


def handle_events():pass


def pause(): pass


def resume():pass

class Bike:
    image = None

    def __init__(self):
        self.x,self.y = 300,300
        self.image = load_image('resource\\idle1.png')
    def draw(self):
        self.image.draw(self.x,self.y)

