#!/usr/bin/env python
#coding:utf-8

'''
class Alex:
    xx = '没心没肺'
class Person:
    xue = '血'
    def __init__(self,name,age):
        self.name = name
        self.agexx = age

p1 = Person('liyang',18)    
print p1.name
print p1.agexx
p2 = Person('laogou',11)    
print p2.name

'''

class Province(object):
    #静态字段
    memo = '中国的23个省之一'
    
    
    def __init__(self,name,capital,leader,flag):
        #动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        
        self.__Thailand = flag
    
    #动态方法
    def sports_meet(self):
        print self.Name + '正在开运动会'
    
    @staticmethod
    def Foo():
        print '每个省要带头反腐'
    
    @property
    def Bar(self):
        print self.Name
        
    def show(self):
        print self.__Thailand
    
    def __sha(self):
        print '我是Alex'

    def Foo2(self):
        self.__sha()
    #只读
    @property
    def Thailand(self):
        return self.__Thailand
    
    #只写
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value
    
#hb = Province('河北','石家庄','luyang')
#sd = Province('shangdong','jinan','wangshenghui')   
#japan = Province('日本','东京','luyang',True)
#print japan.__Thailand
#japan.show()
#japan.Foo2()
#print japan.Tailand
#japan._Province__sha()

#print hb.Capital
#print Province.memo
#静态类不能访问动态字段
#print Province.Name  error 

#对象可以访问静态对象
#print hb.memo

#hb.sports_meet()
#sd.sports_meet()
#Province.Foo()

#hb.Bar
japan = Province('日本','东京','luyang',True)
print japan.Thailand
japan.Thailand = False
print japan.Thailand




