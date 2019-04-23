# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:38:43 2019

@author: Gyan
"""
list1 = ["hi",12,30.12]
print(list1)

print(list1[2])

list2 = ["Apple",'mac',69]

new = list1 + list2

print(new)


#empty list

emp_list = []
print(emp_list)

#different functions
emp_list.append(1)
emp_list.append(12.3)
emp_list.append('qw')

print(emp_list) 

emp_list.pop()
print(emp_list) 
emp_list.extend(list1)
print(emp_list) 
emp_list.remove(12.3)
print(emp_list) 

even = [2,4,8,6]
odd = [1,3,7,9,5]

combine = even+odd
print(combine)
print(sorted(combine))
print(len(combine))
print(max(combine))
print(min(combine))








