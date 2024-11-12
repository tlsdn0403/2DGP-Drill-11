import random

from pico2d import *
import game_framework

import game_world
from game_world import collide,handle_collisions
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global balls
    


    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    global balls
    balls = [Ball(random.randint(100, 1600-100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)
    
    global zombies
    zombies= [Zombie() for i in range(5)]
    game_world.add_objects(zombies)




    #충돌 정보를 등록합니다
    game_world.add_collision_pair('boy:ball',boy, None)  #보이를 한 번만 넣도록 만듦
    for ball in balls:
        game_world.add_collision_pair('boy:ball',None, ball)

    game_world.add_collision_pair('boy:zombie', boy, None)
    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie) 

    for zombie in zombies:
        game_world.add_collision_pair('ball:zombie', None, zombie) 

    # fill here




def finish():
    game_world.clear()
    pass


def update():
    game_world.update() #소년과 볼 위치가 다 업데이트 완료
    
    game_world.handle_collisions()
    
    


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

