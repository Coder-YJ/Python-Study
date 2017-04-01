# -*- coding: utf-8 -*-
# map/reduce   pratice 1
def normalize(name):
    n = 1
    na = name[0].upper()
    while n < len(name):
        na = na + name[n].lower()
        n = n + 1
    return na
'''    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

def is_palindrome(n):
    s = str(n)
    l = len(s)
    l2 = int(l/2)
    if l == 1:
        return False
    elif l % 2 == 0:
        return False
    else:
        n = 0
        while n < l/2:
            if s[n] != s[l-n-1]:
                return False
            n = n + 1
        return True
        
 
 L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
 L.keys()
 
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width*self._height

