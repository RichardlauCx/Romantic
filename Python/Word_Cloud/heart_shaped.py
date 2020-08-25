# -*- coding: utf-8 -*-
#  @ Date   : 2020/8/25 18:46
#  @ Author : RichardLau_Cx
#  @ Project: Romantic
#  @ File   : heart_shaped
#  @ IDE    : PyCharm


# 导入matplotlib模块pyplot函数并使用as给函数起个别名plt
import matplotlib.pyplot as plt
import jieba  # jieba是优秀的中文分词第三方库
import wordcloud  # 导入词云图模块
from matplotlib import colors
# from scipy.misc import imread  # 此方法已经被弃用，用imageio库来代替
from imageio import imread  # 此方法已经被弃用，用imageio库来代替

# 读取文本文件
str1 = open('words.txt', 'r', encoding="utf-8").read()
cut_text = jieba.cut(str1)  # 智能分词处理
word = ' '.join(cut_text)  # 以空格来分割文本

# 红、粉色值
color_list = ['red', 'pink']
colorMap = colors.ListedColormap(color_list)  # 色谱图

# 七夕版
pic = imread('./image/love.png')
# pic = imread('F:\Computer\Computer_Python\Romantic\Python\Word_Cloud\image\magpie_bridge_tanabata.jpg')

wc = wordcloud.WordCloud(
    mask=pic,  # 背景图形(轮廓), 若根据图片绘制，则需要设置
    font_path='simhei.ttf',  # 可以改成自己喜欢的字体
    background_color='white',  # 词云图背景颜色, 可以换成自己喜欢的颜色
    colormap=colorMap
)

wc.generate(word)  # 生成词云

# 显示词云图
plt.imshow(wc)  # 只是画出该图
plt.axis('off')
plt.show()  # 显示出来
