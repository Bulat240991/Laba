#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    def wall():
        if wall_is_beneath() == True:   # проверка наличия стены снизу
            move_right()                # движемся в право, покка стена есть
    for i in range(9):
        wall()
    pass


if __name__ == '__main__':
    run_tasks()
