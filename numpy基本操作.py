# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

######## Ipython: Python的交互式调试环境（就是右边展示输出结果那一块）#######
# 在变量后面加？显示变量的相关信息
# In Out 分别表示输入指令和输出指令
# 魔术命令例子：%run xx.py 运行xx.py程序...
# %magic 显示所有IPython的魔术命令


###########################      numpy库     ###########################
import numpy as np

# 展示一下numpy的强大功能
def pySum():
    a=[0,1,2,3,4]
    b=[9,8,7,6,5]
    c=[]
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
    return c
print(pySum())

def npSum():
    a=np.array([0,1,2,3,4])
    b=np.array([9,8,7,6,5])
    c=a**2+b**3
    return c
print(npSum())
# 比上面pySum的语法简单得多


#____________ndarray数组属性______________
print(" ")
x=np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(x)
print(x.ndim) #维度
print(x.shape) #多少行多少列
print(x.size) #元素个数，即行乘以列
print(x.dtype) #元素类型
print(x.itemsize) #每个元素的大小（单位为字节）



# ndarray中的元素类型：bool, intc, inp, int8, int16...（很多很多类型）
# ndarray也可以由非同质对象组成，但会被强行转化成同质，无法有效发挥numpy优势。例：
print(" ")
y=np.array([[0,1,2,3,4],[1,2,3,4]])
print(y.shape) #变成1行1列
print(y.size) #元素个数变成2个
print(y.dtype) #元素类型为object
print(y.itemsize) #每个元素的大小（单位为字节），发现为8字节，较大




#_____________ 创建和变幻ndarray_______________________
# 1.x=np.array() 括号中输入list[], tuple(), list[]&tuple()都可,只要维度相同就行

# 2.1 np.arange(n)  np.ones(shape)  np.zeros(shape)  np.zeros(shape)  np.full(shape,value)   np.full(shape,value)  np.eye(n)
print(" ")
print(np.arange(10))
print(np.ones((1,10)))
print(np.zeros((10,1)))
print(np.full((4,4),99999))
print(np.eye(6))

# 2.2 np.ones_like(x)  np.zeros_like(x)  np.full_like(x,value) #根据给定数组生成同形状数组

# 2.3 np.linspace()均匀取值  np.concatenate()合并数组
a=np.linspace(1,10,4)
print(a)
b=np.linspace(1,10,4,endpoint=False)
print(b)
print(np.concatenate((a,b)))

# 3.1  .reshape(shape)     .resize(shape)     .swapaxes(ax1,ax2)      .flatten()
# reshape和flatten生成新数组不改变原数组，resize改变原数组
print(x)
print(x.flatten())
print(x.reshape(5,2))

# 3.2 new_x=x.astype(new_type) 改变数组类型
w=np.ones((2,3,4),dtype=np.int)
print(w)
print(w.astype(np.float))

# 3.3 x.tolist()  将ndarray转化成list
v=np.full((2,3,4), 25, dtype=np.int32)
print(v)
print(v.tolist())
print(v.flatten())



#_____________对ndarray的操作__________________
q=np.array([9,8,7,6,5])
print(q[2])  #q中的第三个元素
q[1:4:2] #起始编号 到 终止编号（不含）之间，间隔为2的元素组成组成的ndarray
print(q[1:4:2]) 
# 切片操作可以用冒号选取整个维度，双冒号表示用特定步长跳跃切片

r=np.arange(24).reshape((2,3,4))
print(r)
print(r[-1,-2,-3]) # 倒数的元素
print(r[:,1,-3]) # 覆盖第一个维度,只选取满足 在第二个维度1位置和第三个维度-3位置 的元素
print(r[:, 1:3, :]) # 覆盖第一、三维度，只选取满足 在第二个维度1、2位置 的元素
print(r[:, :, ::2]) # 覆盖一、二维度，只在三维度进行间隔为2的切片

print(r.mean()) # 求所有元素均值


#________________numpy对ndarray元素的计算_______________
# np.square(x)  np.sqrt(x)  np.abs(x)  np.fabs(x)  np.log(x)  np.ceil(x)  np.floor(x)
# np.rint(x)  np.modf(x)   np.cos/sin/tan(x)  np.exp(x)   np.sign(x)
print(" ")
print(np.square(r))
print(np.sqrt(r))
s=np.sqrt(r)
print(np.modf(s)) #区分整数和小数部分,生成两个数组



#___________________数组x和数组y的二元运算________________
# x+y  x-y  x*y  x/y  x**y  np.maximum(x,y)  np.minimum(x,y)  np.mod(x,y)  np.copysign(x,y)  算数比较(产生True or False)
t=np.arange(24).reshape((2,3,4))
o=np.sqrt(t)
print(np.maximum(t,o))
print(t>o)


























