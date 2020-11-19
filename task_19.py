#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():

    if wall_is_above():
        while not wall_is_on_the_left():
            move_left()
    if wall_is_above():
        while not wall_is():
            move_right()
    if wall_is_above():
        B = True

    pass


if __name__ == '__main__':
    run_tasks()
