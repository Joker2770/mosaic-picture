#-*-coding:utf-8-*-
#date:2019/07/19
'''
MIT License

Copyright (c) 2019 Joker2770

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
