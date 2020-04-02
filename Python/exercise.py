# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import turtle as t
import random

DISTANCE = 65  # 设置一个固定距离
BRANCH = 65  # 设置分支量


def draw_tree(brance):  # 画树枝部分  分支量
    if brance > 4:  # 设置一个最小分支量 可以自己改  否者就停止
        if 8 <= brance <= 16:  # 分支量在这个范围内，画笔大小缩小四倍，画中等细小的树枝
            t.pencolor("lightcoral")  # 珊瑚色
            # t.pencolor("green")
            t.pensize(brance / 4)
        elif brance < 8:  # 分支量在这个范围内，画笔大小缩小二倍 ， 画细小的树枝
            t.pencolor("lightcoral")  # 珊瑚色
            # t.pencolor("green")
            t.pensize(brance / 2)
        else:  # 其他范围内，我们让程序画树干部分
            t.pencolor("Tan")  # 褐色
            t.pensize(brance / 10)  # 缩小支柱  设置画笔宽度

        t.fd(brance)  # 最开始的树干部分
        a = 1.5 * random.random()  # 随机度数因子

        t.right(20 * a)  # 右转随机角度

        b = 1.5 * random.random()  # 随机长度因子
        print(brance)
        draw_tree(brance - 10 * b)  # TODO 往右画，直到画不动为止，然后左转随机度数


def run():
    t.bgpic(r'cats_under_the_moon.gif')
    t.screensize(500, 500, "pink")  # 设置尺寸与背景颜色

    t.penup()  # 抬笔  缩写：pu

    t.speed(0)  # 画笔移动速度
    t.backward(4 * DISTANCE)
    t.right(90)  # 顺时针旋转角度
    t.forward(3*DISTANCE)  # 缩写：fd
    t.left(180)

    t.pendown()  # 落笔  缩写：pd

    draw_tree(BRANCH)



    t.done()


if __name__ == '__main__':
    run()
