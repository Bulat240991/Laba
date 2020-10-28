#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    def colors():                                          # функция закрашивает клетку, если сверху нет стены, а после движется вправо
        if wall_is_above() == False:
            fill_cell()
    while wall_is_beneath() * wall_is_on_the_right() == False:   # если снизу есть стена то выполняется функция colors
        colors()
        move_right()
    else:
        colors()

    pass


if __name__ == '__main__':
    run_tasks()
