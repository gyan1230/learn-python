# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:48:32 2019

@author: Gyan
"""
#concatinating string
greet = "hi"
name = 'Gyan'
print(greet+" "+name)

name = input("What is your name?")
print(greet+" "+name)

#indexing of string

color = "Orange"
print("length of 'color' string is "+str(len(color)))

print(color[2],color[3],color[4]+color[3])
print(color[-5],color[-4],color[-3],color[-2])

print(color[:3])
print(color[3:])
print(color[:3]+color[4:])

#string formatting

salary = 38457
print(salary)

#TypeError: can only concatenate str (not "int") to str
#print("My salary is"+salary)

print("My salary is "+str(salary))

# .format 

print("the colors are {},{},{}.".format("red","green","blue"))
print("the colors are {0},{1},{2}.".format("red","green","blue"))

print("the colors are {0},{1},{0}.".format("red","green","blue"))

print("the colors are {b},{g},{r}.".format(r="red",g="green",b="blue"))

pie = 3.14
print("The value of pi is {}".format(pie))





















