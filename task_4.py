#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    def check_out():
        if wall_is_above() and wall_is_beneath() and wall_is_on_the_left() == True:         # проверка наличия стен и движения в сторону где стен нет
            move_right()
        elif wall_is_above() and wall_is_beneath() and wall_is_on_the_right() == True:
            move_left()
        elif wall_is_beneath() and wall_is_on_the_left() and wall_is_on_the_right() == True:
            move_up()
        elif wall_is_above() and wall_is_on_the_left() and wall_is_on_the_right() == True:
            move_down()
    for i in range(1):               # однократное выполнение функции check_out
        check_out()
    pass


if __name__ == '__main__':
    run_tasks()
