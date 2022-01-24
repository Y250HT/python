import shutil
import os
def move():
    path = "C:/Users/86198/PycharmProjects/pythonProject/课程设计"
    datanames = os.listdir(path)
    for i in datanames:
        if len(i)==23:
            path = "C:/Users/86198/PycharmProjects/pythonProject/课程设计/"
            dst = "C:/Users/86198/PycharmProjects/pythonProject/课程设计/Picture/"
            old = path + i
            goto = dst + i
            shutil.move(old, goto)


