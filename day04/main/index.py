#!/usr/bin/env python
#coding:utf-8

str1 = 'demo'
str2 = 'Foo'

module = __import__(str1)
func = getattr(module, str2)

print func