#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2020/4/16 下午 08:11
# @Author : ClancyHe
# @Email : 10512091@qq.com
# @Software: PyCharm
for value in range(1,11):
    print(value)

numbers = list(range(1,11))
print(numbers)

numbers2 = list(range(2,11,2))
print(numbers2)

sqs=[]
for value in range(1,11):
    sq=value**2
    sqs.append(sq)
print(sqs)

aaa=[]
for value in range(1,21):
    aaa.append(value**2) # 2是乘方
print(aaa)

aaa=[]
for value in range(1,101):
    aaa.append(value**3) # 3是立方
print(aaa)
print(sum(aaa))
print(min(aaa))
print(max(aaa))