#!/usr/bin/env python
#coding:utf-8
from macpath import split
'''
data = raw_input('请输入地址')
array = data.split('/')

try:
    userspace = __import__('backcount.'+array[0])
    model = getattr(userspace, array[0])
    func = getattr(model, array[1])
    func()
except ImportError,f:
    print f
    print '404'
except AttributeError,f:
    print f
    print '404sdf'
except Exception,r:
    print 5,r
    print 'sdfsa'
#没有出现异常的时候执行   
else:
    print '没有出错'
    
finally:
    print '无论异常与否都会执行'
'''
'''
class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg

    def __str__(self, *args, **kwargs):
        return '该对象是MyException实例化的一个对象'



obj = MyException('错误')
print obj
'''


'''
class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg

    def __str__(self, *args, **kwargs):
        return self.error



#obj = MyException('自定义错误信息')
#print obj

raise MyException('自定义错误')

'''

def Validate(name,pwd):
    
    if name == 'alex' and pwd == '123'
        return True
    else:
        return False

try:
    









