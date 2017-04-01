# -*- coding: utf-8 -*-
# build in 2017/3/25 by QianYuanJing
'create a doublecolorball '
import random

def isBallValid(num,redBall):
    for ball in redBall:
        if num == ball:
            return False
    return True

def getRedBall():
    redball = []
    n = 0
    while n < 6:
        x = random.randint(1,34)
        if isBallValid(x,redball):
            redball.append(x)
        else:
            continue
        n += 1
        redball.sort()
    return redball

def getBlueBall():
    blueball = []
    n = 0
    while n < 1:
        x = random.randint(1,17)
        if isBallValid(x,blueball):
            blueball.append(x)
        else:
            continue
        n += 1
    return blueball

def getDoubleColorBall():
    return [getRedBall(),getBlueBall()]
    
