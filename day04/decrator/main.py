#!/usr/bin/env python
#coding:utf-8

def outer(fun):
    def wrapperqq(arg):
        print '验证'
        result = fun(arg)
        print '追加'
        return result
    return wrapperqq



@outer
def Func1(arg):
    print 'func1',arg
    return 'return'


    
response = Func1('alex')
print response