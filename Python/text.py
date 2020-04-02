# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def text1():
    print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xef\xbc\x81'.decode('utf-8'))
    print(b'\xe7\x94\x9f\xe6\x97\xa5\xe5\xbf\xab\xe4\xb9\x90\xef\xbc\x81'.decode('utf-8'))

    # Output: 我爱你！
    #         生日快乐！


def text2():
    print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


if __name__ == '__main__':
    # text1()
    text2()