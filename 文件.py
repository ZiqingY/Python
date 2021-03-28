# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 05:57:03 2021

@author: Altair
"""

'''Python常用的编码为ASCII'''
print(ord('A'))
print(ord('a'))
print(chr(65))
print(chr(97))
# ord与chr函数用于字符与ASCII码的转换
# 文本文件是以ASCII编码的文件


'''其他的编码方式：Unicode，UTF-8'''
# encode() 对字符串编码
# decode() 对字符串解码
s='wwe'
bs=s.encode("utf-8")
print(bs)
print(bs.decode('utf-8'))


'''换行符 \n '''
print('Hey! \nyou \nmotherfucker!')


'''打开文件'''
# open(<name>, <mode>)
# mode的可选参数: r, w, a, rb, wb, ab, r+
# 例： infile=open('numbers.dat', 'r')
#      infle=open('music.mp3', 'rb')  打开二进制文件需要rb模式

# read()      读取整个文件内容为字符串 
# readline()  文件下一行内容的字符串
# readlines() 返回值为整个文件内容的列表形式
# 例:  infile=open(someFile, "r")
#      for i in range(5):
#          line=infile.readline() 
#          print(line[:-1])

# 文件输出例:  outfile=open("outfile.txt", "w")
#             outfile.writelines(["Hello", " ", "world"])
#             outfile.close()
#             infile=open("outfile.txt", "r")
#             infile.read()
              # 运行结果为'Hello world'

# 通用读取文件框架: file=open(someFile, 'r')
#                 For line in file.readlines():
#                     # 处理一行文件内容
#                 file.close()
    
# 简化版读取文件框架: file = open(someFile, "r")
#                   For line in file:
#                        # 处理一行文件内容
#                   file.close()
       














              