#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    def wall():
        while wall_is_beneath() == True:  # проверка наличия стены снизу
            move_right()  # движется вправо, пока стена есть

    while wall_is_beneath() == False:       # движется вправо, пока не встретит стену снизу
        move_right()

    wall()
    pass

if __name__ == '__main__':
    run_tasks()
