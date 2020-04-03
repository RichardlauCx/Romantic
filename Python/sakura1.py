# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import turtle as t
import random

from copy import deepcopy

brance = 65
BRANCE = 65


def draw_tree(brance):  # 画树枝部分  分支量
    if brance > 4:  # 设置一个最小分支量 可以自己改
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
        draw_tree(brance - 10 * b)  # 往右画，直到画不动为止，然后左转随机度数

        t.left(40 * a)  # 左转随机角度
        draw_tree(brance - 10 * b)  # 往左画，直到画不动为止，然后右转随机度数

        t.right(20 * a)  # 右转一定角度

        t.penup()
        t.backward(brance)  # 递归结束回到上一个节点
        t.pendown()


def draw_fallenflower(brance):
    for i in range(150):  # 循环150次 绘制 掉落的花瓣
        a = 250 - 500 * random.random()  # 花瓣整体长度，有正有负就可以让海龟往二个方向走
        b = 10 - 20 * random.random()  # 花瓣整体宽度，正负道理一致，数值可以根据实际输入

        t.penup()  # 抬笔向前随机走b个宽度，左转90，随机走a个长度，落笔，跟我画一个小圈圈
        t.fd(b)
        t.left(90)
        t.fd(a)
        t.pendown()

        t.pencolor("lightcoral")  # 珊瑚色
        # t.pencolor("green")
        t.circle(1)

        t.penup()  # 跟我左边抬个笔，后退个a的长度，右边转个90，后退个b的宽度，这样可以
        t.backward(a)  # 让海龟回到和刚出发位置差不多的水平线上，所以上面的b设置最好小一点
        t.right(90)
        t.backward(b)


def main():
    t.bgpic(r'cats_under_the_moon.gif')

    t.screensize(500, 500, "pink")
    t.speed(0)
    t.penup()
    t.backward(4 * BRANCE)
    t.right(90)
    t.fd(3*BRANCE)
    t.pendown()
    t.left(180)

    draw_tree(brance)

    draw_fallenflower(brance)

    t.done()


main()

