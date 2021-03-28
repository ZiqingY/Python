# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:11:46 2021

@author: Altair
"""

'''dictionary操作'''
students = {"203-2012-045":'John', "204-2012-037":'Peter'}
print(students)
print(students['203-2012-045'])  #访问dic中的值
students['202-2011-121']="Susan" #添加Susan
print(students)
del students['202-2011-121']     #删除Susan

for key in students:
    print(key + "--------" + str(students[key]))
                                 # 遍历dic

print('203-2012-045' in students)

# 注：dic是无序的，即只要键值相等即dic相等

print()
print(tuple(students.values()))     #返回所有values
print(tuple(students.items()))      #将dic变成list
print(students.get("203-2012-045")) #返回key对应的value
print(students.pop("203-2012-045")) #删除并返回key的对应值
print(students)
students.clear()                    #清空dic
print(students)
teachers={"203-2012-045":'Dr.Yan', "204-2012-037":'Dr.Li'}
students.update(teachers)           #将另一个dic加入现在这个dic中
print(students)



'''统计文章重复词汇,利用文本文件dic_example.txt'''
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/.,:;{}[]|\'""":
            line = line.replace(ch, "")
    return line
        
def processLine(line, wordCounts):
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

filename = input("enter a filename:").strip()
infile = open(filename, "r", encoding="utf8")

wordCounts={}
for line in infile:
    processLine(line.lower(), wordCounts)
    
pairs = list(wordCounts.items())
items = [[x,y]for (y,x)in pairs]
items.sort()

import pandas as pd
result=pd.Series(items)
print(result)



'''用dic合并两个文本文件数据'''
ftele1=open('TeleAddressBook.txt', 'rb')
ftele2=open('EmailAddressBook.txt', 'rb')

ftele1.readline()
ftele2.readline()
lines1=ftele1.readlines()
lines2=ftele2.readlines()

dic1={}
dic2={}

for line in lines1:
    elements = line.split()
    dic1[elements[0]] = str(elements[1].decode('utf-8'))

for line in lines2:
    elements = line.split()
    dic2[elements[0]] = str(elements[1].decode('utf-8'))
    
lines=[]
lines.append('姓名\t        电话    \t      邮箱\n')

for key in dic1:
    s=''
    if key in dic2.keys():
        s='\t'.join([str(key.decode('utf-8')), dic1[key], dic2[key]])
        s+='\n'
    else:
        s='\t'.join([str(key.decode('utf-8')), dic1[key], str(' ------- ')])
        s+='\n'
    lines.append(s)

for key in dic2:
    s=''
    if key not in dic1.keys():
        s='\t'.join([str(key.decode('utf-8')), str(' ------- '), dic2[key]])
        s+='\n'
    lines.append(s)

ftele3=open('AddressBook.txt', 'w')
ftele3.writelines(lines)

ftele3.close()
ftele1.close()
ftele2.close()

print("The addressBooks are merged!")
