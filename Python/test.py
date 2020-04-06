# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    :
import threading
import turtle
import random
import time
import cv2

DISTANCE = 65  # 设置一个固定距离
BRANCH = 65  # 设置分支量


def add_text_openCv():
    bk_img = cv2.imread("qq_head_portrait.jpg")
    # cv2.putText(bk_img, "HI RICHARD cats_under_the_moon.gif", (200, 100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("text", bk_img)
    cv2.waitKey()
    cv2.imwrite("cats_under_the_moon_add.jpg", bk_img)


def add_text_turtle(t):
    """
    通过turtle库实现线程同步添加文字
    :return:
    """

    title = "Friday, April 10, 2020   多云：☁☂\n"
    middle_1 = "今天是一条调皮小蛇的19岁破壳日\n"
    middle_21 = "纵有灼灼桃花十里，十里桃花不如你。"
    middle_31 = "你眼中倒映的是星河漫漫，是我见过最美的世外梦幻。"
    middle_41 = "灼灼桃花  三千繁华\n "
    middle_42 = "      却似人间只有你\n"
    ending_1 = "临水而立，波光淋漓。此刻只想把你拥在怀中，与你静听流水清风的欢歌。"
    ending_2 = "一笔一划诉春秋，一撇一捺绣温柔，一动一静情无限，一生一世牵你手。"

    name_1 = "\n" + " "*36 + "刘晨旭ღ卜宇 "
    name_2 = "\n" + " "*36 + "刘晨旭❤卜宇 "

    t.write(title + middle_1 + middle_21 + middle_31, True, 'left')
    # t.write(middle_3, True, 'right')
    t.write(name_1, True, 'right')


def draw_tree(t, brance):  # 画树枝部分  分支量
    """
    一种递归实现（关键就是顺序执行）
    :param brance:
    :return:
    """
    if brance > 4:  # 设置一个最小分支量 可以自己改  否者长度不够就停止
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
        b = 1.5 * random.random()  # 随机长度因子

        t.right(20 * a)  # 右转随机角度
        # print(brance)
        draw_tree(pen1, brance - 10 * b)

        t.left(40 * a)  # 左转随机角度
        draw_tree(pen1, brance - 10 * b)  # 往左画，直到画不动为止，然后右转随机度数
        # time.sleep(2)
        t.right(20 * a)  # 右转一定角度

        t.penup()
        t.backward(brance)  # 递归结束回到上一个节点（相当于回到开叉那里）
        t.pendown()


def draw_fallenflower(t, brance):
    t.penup()  # 抬笔  缩写：pu

    t.speed(0)  # 画笔移动速度
    t.backward(4 * DISTANCE)
    t.right(90)  # 顺时针旋转角度
    t.forward(3 * DISTANCE)  # 缩写：fd
    t.left(180)

    t.pendown()  # 落笔  缩写：pd

    for i in range(156):  # 循环150次 绘制 掉落的花瓣
        a = 300 - 600 * random.random()  # 花瓣整体长度，有正有负就可以让海龟往二个方向走
        b = 10 - 20 * random.random()  # 花瓣整体宽度，正负道理一致，数值可以根据实际输入

        t.penup()  # 抬笔向前随机走b个宽度，左转90，随机走a个长度，落笔，跟我画一个小圈圈
        t.fd(b)
        t.left(90)
        t.fd(a)
        t.pendown()

        t.pencolor("lightcoral")  # 珊瑚色
        # t.pencolor("green")
        t.circle(1)  # 画出小圆形花瓣

        t.penup()  # 跟我左边抬个笔，后退个a的长度，右边转个90，后退个b的宽度，这样可以
        t.backward(a)  # 让海龟回到和刚出发位置差不多的水平线上，所以上面的b设置最好小一点
        t.right(90)
        t.backward(b)

        # 又回到最初的起点


def run(t):
    t.penup()  # 抬笔  缩写：pu

    t.backward(4 * DISTANCE)
    t.right(90)  # 顺时针旋转角度
    t.forward(3 * DISTANCE)  # 缩写：fd
    t.left(180)

    t.pendown()  # 落笔  缩写：pd


if __name__ == '__main__':
    # turtle.bgpic(r'./image/1586171365320.gif')
    turtle.bgpic(r"cats_under_the_moon.gif")
    turtle.screensize(500, 500, "pink")  # 设置尺寸与背景颜色

    pen1 = turtle.Pen()
    pen2 = turtle.Pen()
    pen3 = turtle.Pen()

    pen1.speed(9.9)  # 画笔移动速度
    pen2.speed(9.9)
    pen3.speed(9.9)

    run(pen1)
    t1 = threading.Thread(target=draw_tree, name="Threading_1", args=(pen1, BRANCH,))
    t2 = threading.Thread(target=add_text_turtle, name="Threading_2", args=(pen2,))
    t3 = threading.Thread(target=draw_fallenflower, name="Threading_3", args=(pen3, BRANCH))

    t1.start()
    time.sleep(0.5)
    t2.start()

    time.sleep(0.5)
    t3.start()

    # t1.join()  # 线程同步，进入阻塞状态
    # t2.join()

    turtle.done()
