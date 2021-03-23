# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 06:34:01 2021

@author: Altair
"""

# 数值类型：整数类型，浮点数类型，复数类型
# 类型之间互相转化: int() float() complex()
'''数值计算语法
x+y
x-y
x*y
x/y
x//y 不大于x与y之商的最大整数
x%y  x与y之商的余数
+x
-x
x**y  x的y次幂
abs(x) x的绝对值
divmod(x,y)  (x//y, x%y)
pow(x,y)  即x**y
'''

# 字符串
'''索引值正向要+1，反向不需要'''
print('pine'+'apple')
print(3*'pineapple')
print(len('wwe'))
print(str(123e+10)) # 将格式转化成浮点数
print(type(str(123e+10)))


# 字符串实战：
months="JanFebMarAprMayJunJulAugSepOctNovDec"
n=input('请输入月份数(1-12):')
pos=(int(n)-1) * 3
monthAbbrev=months[pos:pos+3]
print("月份简写是"+monthAbbrev+".")


''' 字符串操作
<string>.upper()        #大写
<string>.lower()        #小写
<string>.capitalize()   #首字母大写
<string>.strip()        #去空格/去指定字符
<string>.split()        #按指定字符分割字符串为数组
<string>.isdigit()      #判断是否是数字类型，返回bool
<string>.find()         #搜索指定字符串
<string>.replace()      #字符串替换
'''

# 元组
# 元组中的元素可以是不同类型
t1= 123, 456, "wwe"
print(t1)
# 索引方式一样；可以进行运算；不可以修改元组


# 列表
# 列表可以修改
'''
<seq> + <seq>                 #连接两个序列
<seq> * <整数类型>             #对序列进行整数次重复
<seq> [<整数类型>]             #索引序列中的元素
len(<seq>)                    #取序列的一个子序列
<seq> [<整数类型> : <整数类型>] #对序列进行循环列举
For <var> in <seq> :          #对序列进行循环列举
<expr> in <seq>               #成员检查，判断前者是否在序列中
<list>.append(x)              #将元素x增加到列表的最后
<list>.sort()                 #将列表排序
<list>.reverse()              #将列表反转
<list>.index()                #返回第一次出现元素x的索引值
<list>.insert(i,x)            #在位置i处插入新元素x
<list>.count(x)               #返回元素x在列表中的数量
<list>.remove(x)              #删除列表中第一次出现的元素x
<list>.pop(i)                 #取出列表中位置i的元素，并删除它
'''


# math库
import math
'''
math.ceil(x)            返回 x 的上限，即大于或者等于 x 的最小整数
math.comb(n, k)         返回不重复且无顺序地从 n 项中选择 k 项的方式总数
math.copysign(x, y)     返回一个基于 x 的绝对值和 y 的符号的浮点数
math.fabs(x)            返回 x 的绝对值
math.factorial(x)       以一个整数返回x的阶乘,如果 x 不是整数或为负数时则将引发 ValueError
math.floor(x)           返回 x 的向下取整，小于或等于 x 的最大整数
math.fmod(x, y)         Python表达式 x % y 可能不会返回相同的结果
math.frexp(x)           以 (m, e) 对的形式返回 x 的尾数和指数, m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e
math.fsum(iterable)     返回迭代中的精确浮点值
math.gcd(*integers)     返回给定的整数参数的最大公约数

math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
                        若 a 和 b 的值比较接近则返回 True，否则返回 False
                        rel_tol 是相对容差 —— 它是 a 和 b 之间允许的最大差值，相对于 a 或 b 的较大绝对值。
                        例如，要设置5％的容差，请传递 rel_tol=0.05 。默认容差为 1e-09，确保两个值在大约9位十进制数字内相同。 rel_tol 必须大于零。
                        abs_tol 是最小绝对容差 —— 对于接近零的比较很有用。 abs_tol 必须至少为零

math.isfinite(x)        如果 x 既不是无穷大也不是NaN，则返回 True ，否则返回 False 
math.isinf(x)           如果 x 是正或负无穷大，则返回 True ，否则返回 False
math.isnan(x)           如果 x 是 NaN（不是数字），则返回 True ，否则返回 False
math.isqrt(n)           返回非负整数 n 的整数平方根。 这就是对 n 的实际平方根向下取整，或者相当于使得 a² ≤ n 的最大整数 a
math.lcm(*integers)     返回给定的整数参数的最小公倍数
math.ldexp(x, i)        返回 x * (2**i)
math.modf(x)            返回 x 的小数和整数部分
math.nextafter(x, y)    返回 x 趋向于 y 的最接近的浮点数值，如果 x 等于 y 则返回 y
math.perm(n, k=None)    返回不重复且有顺序地从 n 项中选择 k 项的方式总数
math.prod(iterable, *, start=1)
                        计算输入的 iterable 中所有元素的积
                        
math.remainder(x, y)    返回 IEEE 754 风格的 x 相对于 y 的余数
math.trunc(x)           返回 Real 值 x 截断为 Integral
math.ulp(x)             返回浮点数 x 的最小有效比特位的值:
math.exp(x)             返回 e 次 x 幂
math.expm1(x)           返回 e 的 x 次幂，减1
math.log(x[, base])     使用一个参数，返回 x 的自然对数（底为 e ）
math.log1p(x)           返回 1+x (base e) 的自然对数
math.log2(x)            返回 x 以2为底的对数
math.log10(x)           返回 x 底为10的对数
math.pow(x, y)          将返回 x 的 y 次幂
math.sqrt(x)            返回 x 的平方根
math.acos(x)            返回以弧度为单位的 x 的反余弦值
math.asin(x)            返回以弧度为单位的 x 的反正弦值
math.atan(x)            返回以弧度为单位的 x 的反正切值
math.atan2(y, x)        以弧度为单位返回 atan(y / x)
math.cos(x)             返回 x 弧度的余弦值
math.dist(p, q)         返回 p 与 q 两点之间的欧几里得距离
math.hypot(*coordinates)返回欧几里得范数
math.sin(x)             返回 x 弧度的正弦值
math.tan(x)             返回 x 弧度的正切值
math.degrees(x)         将角度 x 从弧度转换为度数
math.radians(x)         将角度 x 从度数转换为弧度
math.acosh(x)    返回 x 的反双曲余弦值。
math.asinh(x)    返回 x 的反双曲正弦值。
math.atanh(x)    返回 x 的反双曲正切值。
math.cosh(x)     返回 x 的双曲余弦值。
math.sinh(x)     返回 x 的双曲正弦值。
math.tanh(x)     返回 x 的双曲正切值。
math.erf(x)      返回 x 处的 error function
math.erfc(x)     返回 x 处的互补误差函数。 互补错误函数 定义为 1.0 - erf(x)
math.gamma(x)    返回 x 处的 伽马函数 值
math.lgamma(x)   返回Gamma函数在 x 绝对值的自然对数
math.pi          数学常数 π = 3.141592...，精确到可用精度。
math.e           数学常数 e = 2.718281...，精确到可用精度。
math.tau         数学常数 τ = 6.283185...
math.inf         浮点正无穷大（对于负无穷大，使用 -math.inf 。
math.nan         浮点“非数字”（NaN）值
'''

# random库
from random import random
'''同样的一堆语句
seed(x)            给随机数一个种子值
random()           生成0到1之间的随机小数
uniform(a,b)       生成a到b之间的随机小数
randint(a,b)       生成a到b之间的随机整数
randrange(a,b,c)   随机生成一个从a开始到b以c递增的数
choice(<list>)     从列表中随机返回一个元素
shuffle(<list>)    将列表中元素随机打乱
sample(<list>,k)   从指定列表随机获取k个元素
'''


# random库与math库的应用：蒙特卡罗尔模拟求圆周率
from random import random
from math import sqrt
from time import clock
DARTS = 12000
hits = 0
clock()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print('pi的值是 %s' % pi)
print('程序运行的时间是 % -5.5ss' % clock())