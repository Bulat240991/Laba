#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    a = 0
    while wall_is_beneath() == False:       # спускается вниз до стены
        move_down()
    while wall_is_beneath() == True:        # движется вправо и считает шаги
        move_right()
        a += 1
    move_down()
    move_left(a)                            # движется влево по просчитаным шагам
    pass


if __name__ == '__main__':
    run_tasks()
