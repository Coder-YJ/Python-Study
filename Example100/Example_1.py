# -*- coding: utf-8 -*-
# build in 2017/3/31 by QianYuanJing

def example_1():
    numGroup = ['']
    counter = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if (i != j) and (i != k) and (k != j):
                    numGroup[counter] = str(i) + str(j) + str(k)
                    numGroup[counter] = int(numGroup[counter])
                    numGroup.append('')
                    counter += 1
    return numGroup,counter
    
def example_2():
    profit = int(input("Please Enter your profit:"))
    bonus = 0
    if profit > 100:
        bonus += (profit - 100)*0.01
        profit = 100
    if profit > 60:
        bonus += (profit - 60)*0.015
        profit = 60
    if profit > 40:
        bonus += (profit - 40)*0.03
        profit = 40
    if profit > 20:
        bonus += (profit - 20)*0.05
        profit = 20
    if profit > 10:
        bonus += (profit - 10)*0.075
        profit = 10
    bonus += profit*0.1
    return bonus
            
            
def example_3():
    from math import sqrt
    for i in range(1,100000):
        x = int(sqrt(i + 100))
        y = int(sqrt(i + 268))
        if (x * x == i + 100) and (y * y == i + 268):
            print(i)

def example_4():
    print("example is not exit!")
    

def example_5():
    print("Enter the num you want to sort, enter 'q' to end")
    l = []
    i = 0
    temp = 0
    x = 0
    y = 0
    counter = 0
    while(True):
        i += 1
        num = input('请输入第%2d个数字--> '%i)
        try:
            if num != 'q':
                l.append(int(num))
            else:
                break
        except Exception as e:
            print(e,"\n请不要输入整数以外的其他数字或字符")
            i -= 1
            continue
    print(len(l))
    #擂台法排序
    
    while x < len(l):
        while y < len(l):
            if l[x] > l[y]:
                temp = l[y]
                l[y] = l[x]
                l[x] = temp
                print("exachange %d 、%d"%(l[y],l[x]))
                print(l,'  x = %d'%x)
            y += 1
            counter += 1
        x += 1
        y  = x 
    
    #冒泡法排序
    '''
    while x < len(l):
        while y < len(l) - 1:
            if l[y] > l[y+1]:
                temp = l[y + 1]
                l[y + 1] = l[y]
                l[y] = temp
                print("exachange %d 、%d"%(l[y + 1],l[y]))
                print(l,'  x = %d'%x)
            y += 1
            counter += 1
        x += 1
        y = 0 '''
     
    return l , counter
                    