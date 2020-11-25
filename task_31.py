#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    x = 0
    while x < 2:
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
            x = 0
        if wall_is_beneath():
            while wall_is_beneath() and not wall_is_on_the_right():
                move_right()
            while wall_is_beneath() and not wall_is_on_the_left():
                move_left()
        X += 1



    pass


if __name__ == '__main__':
    run_tasks()
