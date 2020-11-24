#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x = 1
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_on_the_right():
            fill_cell()
        x += 1
    x -= 2
    while x > 0:
        for i in range(x):
            move_down()
            fill_cell()
        move_down()
        for i in range(x):
            move_left()
            fill_cell()
        move_left()
        for i in range(x):
            move_up()
            fill_cell()
        move_right()
        x -= 2
        for i in range(x):
            move_right()
            fill_cell()
        move_right()
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()

    pass


if __name__ == '__main__':
    run_tasks()
