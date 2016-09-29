#!/usr/bin/env python
#coding:utf-8
'''
class Foo:
    def __init__(self):
        pass
    def __del__(self):
        print '解释器 要销毁我了 '
    def Go(self):
        print 'Go'
    def __call__(self):
        print 'call'

f1 = Foo()
f1.Go()
f1()

'''
class Father:
    
    def __init__(self):
        self.name = 'ffff'
        
    def Func(self):
        print 'father.Func'
    
    def Bad(self):
        print 'father.bad'

class Son(Father):
    def __init__(self):
        self.Sname = 'ssss'
        Father.__init__(self)
        
    def Bar(self):
        print 'son.bar'

    def Bad(self):
        print 'son.some'

s1 = Son()
s1.Bar()
s1.Func()
s1.Bad()
