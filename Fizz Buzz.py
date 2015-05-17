# -*- coding:utf-8 -*-
class Solution:
	def fizzBuzz(self,x):
		s=[]
		for i in range(1,n+1):
			if(i%3==0 and i%5==0):
				s.append("fizz buzz")
			elif i%3==0:
				s.append("fizz")
			elif i%5==0:
				s.append("buzz")
			else:
				s.append(str(i))

		return s