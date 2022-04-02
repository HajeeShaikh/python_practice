# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# for i in range(10):
#   if not i % 2 == 0:
#     print(i+1)

# while not False:
#   print("Looping...")
#   continue
# n = int(input("Enter Number:-  "))

# for x in range(1, n):
#     print(x)
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x%2 ==0:
#         continue
#     elif x % 3 == 0:
#         print("Solo")
#     elif x % 5 == 0:
#         print("Learn")
#     else:
#         print(x)
# def double(x , y ):
#     print(x == y)   
#     print(x+y)



# double(12 , 4)
# def shortest_string(x, y):

#   if len(x) <= len(y):
#     return x

#   else:

#     return y


# x= "hajee,r"
# y= "shaikh,g"
# shortest_string(x, y)

# name = ""

# if name:
#     print("Not empty")
# else:
#     print("empty")

# for x in range(1,11):
#     v =int(input())
#     y = int(x)*int(v)
#     print(y)  
# x=0
# while x<=10:
#     print(f"Hello {x}")
#     x+=1
# print(" Multiplication Table ")
# t= (input())
# for i in t:
    
#     for j in range(1, 11):
#         print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
#     print('==============')

# Multiplication table in Python
# using for loop
# def table():
#     num = int(input("Enter the number : "))    
#     i = 1
#     for i in range(1, 11):
#         p=num*i
#         print(num,'x',i,'=',p) 
# table()
# # num = int(input())
# i =1
# while i<=10:
#     p=num*i
#     print ( num,"x",i,"=",p )
#     i+=1

# total = 0
# i =1
# N=int(input())
# while i<=N:
#     total+=i 
#     i+=1
# print(total)

# n = input("Enter a number: ")
# total = 0
# i=0
# while i<len(n):
#     total+=int(n[i])
#     i+=1
# print(i)
# print(total)

# def shout(word):
#    return word + "!❤🤣😂😁"
# speak = shout
# output = speak("shout")
# print(output)
# def square(x):
#     return x * x
# def test(func, x):
#     print(func(x))
#     test(square, 42)

# import random
# for i in range(9):
#     value = random.randint(1,9)
#     print(value)
# import math
# num = 10
# print (math.sqrt(num))

# from math import pi, sqrt
# x=pi
# print(pi)

# n = int(input("Enter a number:  "))
# total = 0
# i = 0
# while i<=n:
#     total+=i
#     i+=1
# print(total)

# n = input("Enter a number:  ")
# total = 0
# i=0
# while i<len(n):
#     total+=int(n[i])
#     i+=1
# print (total)
# temp=""
# n = input("Enter your name:  ")
# i = 0
# while i<len(n):
#     if n[i] not in temp:
#         temp+=n[i]
#         print(f"{n[i]}:{n.count(n[i])}")
#     i+=1
        
# i=10
# while i<=10:
#     pass
#     print("Hello world....!")

# from asyncio.windows_events import INFINITE


# total=0
# for i in range(1, (INFINITE)):
#     total+=i
#     print("Hello World")
# n=int(input("Enter a number:  "))
# total=0
# for i in range(1, n+1):
#     total+=i
# print(total)

# n = input("enter your number: ")
# total=0
# for i in range(0, len(n)):
#     total+=int(n[i])
# print(total)

# temp=""
# n = input("enter your name: ")
# for i in range(0, len(n)):
#     if n[i] not in temp:
#         print(f"{n[i]}:{n.count(n[i])}")
#         temp+=n[i]

"""NUMBER GUESSING GAME"""

'''Manual input number'''

# winning_number = 56
# guess = 1
# number = int(input("Guess a number between 1 and 100:  "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win and you guessed in {guess} attempts")
#         game_over = True
    
#     else:
#         if number < winning_number:
#             print("too low")
#             guess+=1
#             number = int(input("Guess again: "))
#         else:
#             print("too high")
#             guess+=1
#             number = int(input("Guess again: "))

# '''Auto generated number game'''

# import random
# winning_number = random.randint(1,100)
# guess = 1
# number = int(input("Guess a number between 1 and 100:  "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win and you guessed in {guess} attempts")
#         game_over = True
    
#     else:
#         if number < winning_number:
#             print("too low")
#             guess+=1
#             number = int(input("Guess again: "))
#         else:
#             print("too high")
#             guess+=1
#             number = int(input("Guess again: "))

# num = input("Enter a number: ")
# total = 0
# for i in num:
#     total+=int(i)
# print(total)

# Printing last two places

# N = input("Enter your number/character: ")

# if len(N)>=2:
#     print(f"On the last two places you have : {(N[-2])+(N[-1])}")
# else:
#     if len(N)==1:
#         print(f"You have Entered this : {N}")
#     else:
#         pass

# def is_even(num):
#     return num%2 == 0

# print(is_even(12.5))
# def value(_1,_2):

#     if N1>N2:
#         return "first is greater"
#     elif N1==N2:
#         return "Both are same"
    
# N1 = int(input("Enter first number : "))
# N2 = int(input("Enter second number : "))
# print(value(N1, N2))

# a= 1,2,3,4,5,6

# b =int(input("Enter second number : "))
# # print(f"{greatest(a,b,c)} is greatest among three")
# print(min(a))# a =int(input("Enter first number : "))
# print(max(a,b,c))

'''Finding greatest among three numbers method number one'''
# c =int(input("Enter third number : "))
# def greatest(a,b,c):
#     return max(a,b,c)

# a =int(input("Enter first number : "))
# b =int(input("Enter second number : "))
# c =int(input("Enter third number : "))

# print(f"{greatest(a,b,c)} is greatest among you have entered")

'''Finding greatest among three numbers method  number two'''


# def greatest(a,b,c):
#     if a>(b and c):
#         return a
#     elif b>(a and c):
#         return b
#     return c

# a =int(input("Enter first number : "))
# b =int(input("Enter second number : "))
# c =int(input("Enter third number : "))

# print(f"{greatest(a,b,c)} is greatest among you have entered")

# '''Finding greatest among three numbers method  number three'''
# """ # function in function method #'''

# a =int(input("Enter first number : "))
# b =int(input("Enter second number : "))
# c =int(input("Enter third number : "))
# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def new_greatest(a,b,c):
#     # ng = greater(a,b)
#     return greater(greater(a,b),c)
   

# print(f"{new_greatest(a,b,c)} is greatest among you have entered")

# w = "hajee"
# print(w[::-1])

'''PALINDROME'''

# def is_palindrome(word):
#     word = input("Enter any word : ")
#     rev = word[::-1]
#     a=word.lower()   # To avoid case sensitiveness
#     b = rev.lower()  # To avoid case sensitiveness
#     if a ==b :
#         print(f"{word} is palindrome")
#     else:
#         print(f"{word} is not palindrome")

# is_palindrome("word")

# SHORTCUT TO PALINDROME

# word = input("Enter a word : ")
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome(word))

# Python program to display all the prime numbers within an interval

# lower = int(input("lower limit : "))
# upper = int(input("Upper limit : "))

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

"""# fibnonacci series"""

# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print ( a ,b, end=" " )
#         for i in range (n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end = " ")

# fibonacci_seq(10)

# a=[1,2,3,4,5]
# a[1,3]=(0,0)
# print (a)

# x = 7
# def variable( ):
#     global x
#     # x = 5
#     print(x)
#     return x

# variable ( )

''' methods to add data'''

# v = ['sammy', 'aniruddha', 'muddassir', '0hajee']
# w = ['salman','shahrukh','aamer']

# append,extend,insert

# v.append('mahesh')
# print(v+w)
# print(v)
# v.append(w)
# print(v)
# v.extend(w)
# print(v)
# v.insert(0,w)
# v.insert(0,'watson')
# print(v)

'''methods to remove data'''
# del, remove, pop
# v.pop(0)
# print(v)
# del v[0]
# print(v)
# v.remove('sammy')
# print(v)

# if 'salman' in v:
#     print("sammy is present")
# else:
#     print("not present")
# print(v.count("sammy"))
# v.sort()
# print(v)
# v.clear()
# print(v)
# print(sorted(v))
# print(v)
# v.reverse()
# copy = v.copy()
# print(copy)

'''split and join method'''
# split converts string to list
# v = 'sammy, aniruddha, muddassir, 0hajee'.split(" , ")
# print(v)
# join converts list to string 
# v = ['sammy', 'aniruddha', 'muddassir', '0hajee']
# print(" , ".join(v))

'''LOOPING IN LIST'''

#for loop



from ast import comprehension, operator


v = ['sammy', 'aniruddha', 'muddassir', '0hajee']
# for name in v:
#     print(name)

#while loop

# i = 0

# while i<len(v):
#     print(v[i])
#     i+=1

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][0])
# for sublist in matrix:
#     print(sublist)
    # for m in sublist:

#     print(type(matrix))

# name = "Shaikh Hajee"
# print(type(matrix))

# for i in range (1,11):
    # print(i, end = " ")     #only checked
    # p = (list(i))
    # print(p)

# nums = list(range(1,11))
# print(nums)

# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#         return negative
# print(negative_list(nums))

# numbers = list(range(int(input("Enter num1: "),int(input("Enter num2: ")))))
# print(numbers)
'''list examples'''
#wrong way

# num = list(range(int(input("start: ")),int(input("stop: "))))
# def square(num):
#     for i in num :
#         i = (i**2)
#         print(i)
# square(num)

# solution

# first

# def square(l):
#     numb=[]
#     for i in range(len(l)):
#         numb.append(i**2)
#     return numb


# value=int(input("enter valaue from where you start? : "))
# stopping_val=int(input("enter stopping range or the end of value? : "))
# numer=list(range(value,stopping_val+1))
# print(square(numer))

# second

# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
# numbers = list(range(1,11))
# print(square_list(numbers))

'''reverse list'''

# def reverse_list(l):
#     r_list = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#     return r_list

# numbers = [1,2,3,4]
# print(reverse_list(numbers))

"""reverse element"""

# def reverse_element(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements

# v = ['sammy', 'aniruddha', 'muddassir', '0hajee']
# print(reverse_element(v))

'''Odd and even function'''

# def even_odd(l):
#     even = []
#     odd = []
#     for n in l:
#         if n % 2 ==0:
#             even.append(n)
#         else:
#             odd.append(n)
#     p = [odd , even]
#     return p
# num = [1,2,3,4,5,6,7,8,9,10]
# print(even_odd(num))

'''common elements'''
# def common(l1,l2):
#     common=[]
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 common.append(i)
#     return common

# l1 = list(range(1 , 28))
# l2 = list(range(14 , 28))
# l1 = [1,2,3,4,5,6,7]
# l2 = [7,6,5,4,3,2,1]
# print(common(l1,l2))

'''use of min and max in function'''

# def greatest_diff(l):
#     p = max(l) - min(l)
#     return p
# print(greatest_diff([1,2,3,45,15,345,4,5,43545,34,24,0]))

'''sublist counter'''
# def sublist_counter(l):
#     counter = 0
#     for i in l:
#         if type(i)==list:
#             counter+=1
#     return counter

# l=[1,2,3,4,[12,3,43],[12,4,5,6,6,7,8],["hajee",";"]]            
# print(sublist_counter(l))

'''tuples'''

# tup = (1,3,4,5,6,7,["sammy","aniruddha","muddassir"] )

# print(type(tup))
# print(tup.index("sammy"))
# print(tup.index(7))
# tup[6].pop()
# tup[6].insert(1, "inserted")
# del tup[7] can't be done
# print(len(tup))

# a,b,c,d,e,f,g = (1,3,4,5,6,7,["sammy","aniruddha","muddassir"] )
# for h in a,b,c,d,e,f,g:
#     print(h)

# def func(a,b):
#     c = a+b
#     d = a//b
#     E = a/b
#     e = a%b
#     return c,d,E,e
# print(func(3,8), end=",")
# a = func(3,2)
# print(a)
# for i in a:
#     for j in a:
#         print(a)

"tuple's some other things"

# a = list(range(1,11))
# print(list(a))
# print(tuple(a))
# print(str(a))
# print(sum(a))

"simplest program for addition of numbers"

# b= int(input("start:  "))
# c= int(input("stop:  "))
# a = range(b,c+1)
# print(sum(a))

"Dictionaries"
#first method

# Aniruddha = {"Name" : "Aniruddha","Age":"22"}
# print(type(Aniruddha))
# print(Aniruddha)

#second method
# user = dict ( Name="Aniruddha",Age="22" )
# print(user)

# user_info = {
#     "name" : "Harry",
#     "Age" : 21 ,
#     "fav_place" : 'house',
#     "fav_subject" : "Physics"
# }
# print(user_info["name"])

"Adding to empty dictionaries"

# user = {}
# user["name"] = "Harry"
# user["age"] = 25
# user["place"] = "Pune"
# print(user)

# "if method to check keys"

# if "name" in user:
#     print("present")
# else:
#     print("not present")

# "if method to check values"

# if 25 in user.values():
#     print("present")
# else:
#     print("not present")

"looping in dictionaries"

# for i in user:
#     for j in user.values():
#         print(f"{i}:{j}")

# for i in user_info:
#     print(user_info[i])

# user_info = {
#     "name" : "Harry",
#     "Age" : 21 ,
#     "fav_place" : 'house',
#     "fav_subject" : "Physics"
# }

# items method

# user_items = user_info.items()
# print(user_items)

# for i, j in user_info.items():
#     print(f"key is {i} and it's value is {j}")

# adding data

# user_info['fav_songs'] = ["a","b","c"]
# print(user_info)

"popping methods"

# pop method

# pooped_item = user_info.pop("fav_place")
# print(f"popped item is {pooped_item}")
# print(user_info)

# popitem() method 

# popped_item = user_info.popitem()
# print(f"popped item is {popped_item}")
# print(type(popped_item))

# update method

# more_info = {"fav_tunes":("x","y","z")}
# user_info.update(more_info)
# print(user_info)

'fromkeys method'

# d = dict.fromkeys(["name" , "age"],"unknown")
# print(d)

# d = {
#     "name":"Nimit",
#     "age":30,
#     "place":"lodha",
#     "partner":"danny",
#     "employee":"nilesh",
#     "company":"ONN bikes"
    
#     }


# print(d['name'])
# print(d.get("age"))
# if d.get("names"):
#     print("present")
# else:
#     print("not present")

# d.clear()
# print(d)

# d1 = d.copy()
# print(d1)

# d = d1
# print(d1)

# print(d.get("names", "not found"))

"cube finder exercise"

# def cube_finder(n):
#     cubes = {}
#     for i in range(1,1+n):
#         cubes[i] = i**3
#     return cubes

# print(cube_finder(10))

'''Word counter'''

# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char]=s.count(char)
#     return count
# print(word_counter("Harshit Vashistha"))

'''User values input'''


# user = {}
# name = input ("What is your name: ")
# age = input ("What is your age: ")
# fav_place = input ("What is your fav_place: ")
# fav_subject = input ("What is/are your fav_subjects comma separated: ").split(" , ")
# fav_movies = input ("What is/are your fav_movies comma separated: ").split(" , ")

# user["name"] = name
# user["age"] = age
# user["fafav_place"] = fav_place
# user["fav_subject"] = fav_subject
# user["fav_movies"] = fav_movies
# # print(user)

# for key, value in user.items():      # """Don't forget to write items()"""
    # print(f"{key} : {value}")

# Set data type

# set = {1,2,2,3,4,4,5,5,54,56,67,77,77}
# print(list(set))
# set.add(0)
# set.clear()
# w = set.copy()
# set.remove(70)
# w = set.di

# union "|" and intersection "&"

# A = {1,2,3,4,5,6}
# B = {7,8,9,0,1,2,3}
# print(A|B)
# print(A&B)

# list comprehension

'''comprehension makes our code short'''

# regular method

# squares = []
# for i in range(1,11):
#     i = i**2
#     squares.append(i)
    
# print(squares)

# using comprehension

# squares = [i**2 for i in range(1,11)]
# print(squares)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# negative = [-i for i in range(1,11)]
# print(negative)

# l = ["abc","def","ghi","jkl"]
# rev = [n[::-1] for n in l]
# print(rev)

# def rev(l):
#     return[n[::-1] for n in l]
# l = ["abc","def","ghi","jkl"]
# print(rev(["abc","def","ghi","jkl"]))

l = [0,1,2,3,4,5,6,7,8,9,10]

# regular method
# even = []
# for i in l:
#     if i%2==0:
#         even.append(i)
# print(even)

# even = [i for i in l if i%2 == 0]
# odd = [i for i in l if i%2 != 0]
# print(even)
# print(odd)

# def stringify(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)] 

# l = [True, False, "right",1,1.0,2]
# print(stringify(l))

# nested_comp = [[i for i in range(1,4) ] for j in range(3)]
# print(nested_comp)

"""Dictionary comprehension"""

# square = {num:num**2 for num in range(1,11)}
# print(square)

# name = "Hajee"
# dicti = {char:name.count(char) for char in name}
# print(dicti)

# even_odd = {i:("even" if i%2==0 else "odd") for i in range(1,11)}
# print(even_odd)

"""set comprehension"""
# s = {k**3 for k in range(1,11)}
# print(s) 

n = ["Aniruddha","Hajee","Muddassir"]
# ss = {n[0] for n in n}
# print(ss)

# *args or * operator
# def sum(*args):
#     t = 0
#     for a in args:
#         t += a
#     print(t)

# sum(1,2,3,4,5,6)

# args with normal argument
'remember num first and args second'
# def sum(num,*args):    
#     t = 0
#     for a in args:
#         t += a
#     print(t)

# sum(1,2,3,4,5,6)

'''while passing list'''

# *args as argument

# def multiply(*args):
#     multiply = 1
#     # print(args)
#     for i in args:
#         multiply *=i
#     return multiply

nums = [1,2,3,4,5]   # list or tuple can be passed
# print(multiply(nums))  #here list will get completely passed instead of items

#to overcome this use as follows
# print(multiply(*nums))

# def to_power(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "you didn't passed any argument"

# print(to_power(3,*[3,4,5]))
# print(to_power(3,*[]))

"""kwargs (keyword argument)
double star oprerator (**)"""


# def func(**kwargs):
#     print(kwargs)  # it produces dictionary

# func(name="sameer", standard = "9", village = "udgir")

# looping in kwargs
# def func(**kwargs):
#     for i,j in kwargs.items():
#       print(f"{i}:{j}")
# func(name="sameer", standard = "9", village = "udgir")  

"order of parameters in function"
"""
PADK

P = parameter
A = *args
D = default parameters
K = **kwargs
"""

# def func(name, *args , age =25, **kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
# func("Hajee",*[1,2,3],names= "sameer",age =22)

# def cap (l,**kwargs):
#     if kwargs.get("reverse_str")==True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]

# names= ["hajee","calvin"]
# print(cap(names,reverse_str=True))

"""lambda function"""
# general function

# def add(a,b):
#     return a+b

# lambda style

# add2 = lambda a,b : a+b

# print(add2(2.4,2))

# multiply = lambda a,b : a**b
# print(multiply(4,5))

"lambda function has no name"
# print(add2)
# print(add)
# print(multiply)

"lambda fuction with if, else statement"

# def func(s):
#     return s%2 == 0

# func2 = lambda s : True if s%2==0 else False
# print(func(0.8753827348750))
# print(func2(0.5432435))

"Enumerate function"
# Q - show name and their position .

# without enumerate function

# names = ["abc","def","ghi","Hajee","sameer","chand"]
# def position(l):
#     pos = 0
#     for name in names:
#         print(f"{pos}---->{name}")
#         pos+=1
# position(names)

# with enumerate fuction
# names = ["abc","def","ghi","Hajee","sameer","chand"]
# for pos, name in enumerate(names):
#     print(f"{pos}---->{name}")

# find position with index() function

# names = ["abc","def","ghi","Hajee","sameer","chand"]
# print(names.index("chand"))

# find position with enumerate() function
# names = ["abc","def","ghi","Hajee","sameer","chand"]
# def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if name == target:
#             return pos
#     return -1
# print(find_pos(names,'Hajeedfg'))

"map function"

# make a list of  square of each element of the given list:

num = [1,2,3,4]

# general method

# def square(a):
#     return(a**2)
# print(map(square, num))
# squares = list(map(lambda a:a**2, num))
# print(squares)

#by using list comprehension

# square = [i**2 for i in num]
# print(square)

# old method-1

# square = []
# for i in num:
#     square.append(i**2)
# print(square)

# old method-2
# s = []
# for a in num:
#     s.append(square(a))
# print(s)

# names = ["Humer","Aamer","Sunny","Godikat"]
# # a=list(map(len , names))
# a=map(len , names) #map object is iterable
# for i in a:
#     print(i)

# def add(a,b):