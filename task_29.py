#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x = 0
    y = 0
    if cell_is_filled():
        y += 1
    while not y == 3 and not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            y += 1
        else:
            y = 0
    pass


if __name__ == '__main__':
    run_tasks()
