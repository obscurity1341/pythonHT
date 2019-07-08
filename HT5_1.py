# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
dir_path =[('dir_' + str(i + 1)) for  i in range(9)]
def make_dir(new_dir):
    new_dir = os.path.join(os.getcwd(), 'NewDir')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print("Wrong name")

old_dir = [('dir_' + str(i+1)) for i in range(9)]
def remove_dir(old_dir)
    try:
        os.removedirs(dir_path)
    except FileExistsError:
        print("Wrong name")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
def folders(dir_path):
    for _ in os.listdir(dir_path):
        print(_)
dir_path = os.getcwd()



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import sys
def file_copy():
    