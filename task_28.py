#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    x = 0
    while not x == 5:
        move_right()
        if cell_is_filled():
            x += 1

    pass


if __name__ == '__main__':
    run_tasks()
