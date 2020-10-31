#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    def search_out():                       # поиск выхода из ловушки0
        while wall_is_above():
            if not wall_is_on_the_right():
                move_right()
            else:
                while wall_is_above():
                    if not wall_is_on_the_left():
                        move_left()
    search_out()
    while not wall_is_above():              # после выхода, движется в верхний левый угол
        move_up()
    while not wall_is_on_the_left():
        move_left()
    pass


if __name__ == '__main__':
    run_tasks()
