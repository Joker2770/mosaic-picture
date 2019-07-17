from pygame import *
from math import *
import sys
import os

if not os.path.exists(sys.argv[1]):
    raise FileNotFoundError
screen = display.set_mode((1366,768))
m = image.load(sys.argv[1])

screen.blit(m,(0,0))                            #将打开的图片m显示在左上角
mon = open(r"./TagPic.py","w")    #创建马赛克文件

mon.write("""from pygame import *
from math import *
import os

screen = display.set_mode((1366,768))
""")                                            #写入到mon，用三层引号来分开写入代码
running = True                                  #运行程序
display.flip()                                  #显示图片

for x in range(0,1366,5):
    for y in range(0,768,5):
        c = str(screen.get_at((x,y)))           #获得每个x,y坐标上颜色
        mon.write("draw.rect(screen,"+c+",("+str(x)+","+str(y)+",4,4))\n")
                                                #将像素位置写入mona.py,形状为矩形
    mon.write("display.flip()\n")               #展示图片

mon.write("""os.system(\"pause\")\n""") 
mon.close()                                     #保存关闭mon.py
