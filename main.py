if 5 > 2:
    print("five is greater than two")
print("no yes ctrl ")  # this is comment
""" this is a comment"""
"""this is comment"""

x = 4
x = "Sally"
print(x)

# Casting
x = str(3)
print(x)
print(type(x))

x, y, z = "orange", "Banana", "Cherry"
print(x)
print(z)
print(y)
print(x)

# rules of variable naming
# no other than alphanumeric character
# variable can't start with number


# Assigning same value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variable
x = "python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

# different type outputs collectively
x = 5
y = "john"
print(x, y)
print(str(x) + y)

# Global Variable
x = "awesome"


def myfunc():
    global x
    x = "fantastic"
    print("python is " + x)


myfunc()
print("python is " + x)

# Data type
# setting the specific data type

x = str("Hello World")  # str
x = int(20)
x = float(20.5)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "cherry", "banana"))
x = range(6)
x = dict(name="john", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

# python numbers
# int float complex
# type conversions int float complex

x = complex(1)
print(x)

import random

print(random.randrange(1, 10))

# multiline strings
a = """ lorem ipsum dolor sit amet consectetur
 adipscing elit, sed do eiusmod tempor"""

print(a)

for i in range(len(a)):
    print(a[i])

for x in "banana":
    print(x)

# check string
text = "the best things in life are free!"
print("arefree!" in text)

# use if in an statement:
text = "the best things in life are free!"
if "free" in text:
    print("yes, 'free' is present.")

txt = "the best things in life are free!"
print("expensive" not in text)

# python slicing strings

b = "HelloWorld"
print(b[:6])
print(b[-5:-2])

# modifying strings

a = "helloworld"
print(a.upper())

# removing white spaces
a = "     Hello, world"
print(a.strip())

# replacing strings
a = "Hello, Wor ld!"
print(a.replace("H", "J"))
print(a.split(" "))

# string format
age = 36
txt = ("My name is John, I am ", age)
print(txt)

age = 37
txt = "My  name is {} John, and I am "
print(txt.format(age))

age = 37
txt = "My  name is {} {} {} John, and I am "
print(txt.format("john abraham", "agent 50", 90.13))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {1} dollars for {2} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape characters
txt = "We are the so-called \"vikings\" from the north"
print(txt)


# booleans
def myFunction():
    return False


if myFunction():
    print("YES!")
else:
    print("NO!")

print(5 ^ 6)

# lists index starts from 0, range of indexes

thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("yes, apple is in this list")

# changing item value
thisList[1:3] = ["blackcurrant", "kiwi"]
print(thisList)

thisList[1:3] = ["yesyes"]
print(thisList)

thisList = ["apple", "mango", "banana", "cherry"]
thisList.insert(5, "watermelon")
print(thisList)

# removin from list

thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList, "this is del list")

thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList, "this is remove list")

print(thisList.pop(), "this is pop list")

# loop through lists

thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# differnce between different looping
bb = """this is haseeb at viteace solutions"""

for i in range(len(bb)):
    print(bb[i])  # range need number

xx = " banana"
for i in xx:
    print(i)

for i in " banana":
    print(i)

# looping using while loop
thislist = ["apple", "banana", "cherry"]
i = 0;
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# looping using list comprehension
thislist = ["yes yes apple", "banana", "cherry"]
[print(x) for x in thislist]

"""List comprehension offers a shorter syntax when 
you want to create a new list based on the values of
 an existing list.
Example:
Based on a list of fruits, you want a new list,
containing only the fruits with the letter "a" in the name.
Without list comprehension you will have
to write a for statement with a conditional test inside:

"""

# list comprehension

# for quickly creating new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "r" in x]
print(newlist)

# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if x != "apple"]

print(newlist)


# customize sort function
def myfunc(n):
    return abs(n - 50)


thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key=myfunc)
print(thislist2)

# case insensitive sort
fruits = ["apple", "banana", "Cherry", "kiwi", "mango"]
fruits.sort(key=str.lower)
print(fruits)

fruits = ["apple", "banana", "Cherry", "kiwi", "mango"]
fruits.reverse()
print(fruits)

# copy list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

mylist22 = list(thislist)
print(mylist)

# append extend list+list for joining two list

# tuples  unchangeable, ordered for single item tuples add a comma
# after the items so that python can recognize it as a tuple


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# del thistuple
print(thistuple)

# python if ... Else
# short hand if
# if only one statement to execute  you can put it on the
# same line as the if statement

a = 300
b = 200
if a > b: print("a is greater than b")

# short hand if... else

a = 2
b = 330
print("a") if a > b else print("b")  # ternary operators or conditional
# expressions


# multiple else statements on the same line
a = 330
b = 330
print("a") if a > b else print("=") if a == b else print("b")

# and
a = 200
b = 33
c = 500
if b < a < c:
    print("both conditions are true")

# nested if

x = 41
if x > 10:
    print("above ten,")
    if x > 20:
        print(" and also above 20!")
    else:
        print("but not above 20.")

# pass statement

a = 33
b = 200
if b > a:
    pass

# python loops

# when condition remains true we can run while
i = 1
while i < 6:
    print(i)
    i += 1

# break statement for breaking the loop even the
# condition remains true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# with continue statement we can stop
# with current iteration and continue with the
# next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i is no longer less than 6")

# for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through strings
for x in "banana":
    print(x)

# break state in for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# the range() funciton
# to loop through a set of code a specified number
# we can use the range() funciton

# range gives the iteration control over  number.
for x in range(6):
    print(x)

for x in range(2, 200, 3):
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")  # The else block
    # will NOT be executed
    # if the loop is stopped by a break statement.

i = 0
while i < 15:
    print(i)
    if i == 7:
        break
    i += 1
    print("the loops is not finished yet")
else:
    print("may be the looop is break")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("finally finished")

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# pass statement
for x in [0, 1, 2]:
    pass


# python functions

# python function is defined using def keyword

def my_function():
    print("Hellow from a funciton")


my_function()


def my_function2(fname):
    print(fname + " refsnes")


my_function2("emil")
my_function2("tobias")
my_function2("linus")


# argument shortened as args
# argument when fucniton is called with data
# parameter is fucntion defination with data or variable
# in it defination

def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emilia", "Refsnes")


def kids_func(*kids):
    print(" the youngest child is " + kids[0])


kids_func("emilia", "Tobias", "Linus")


def my_function(child3, child2, child1):
    print("the youngest child is " + child3)


my_function(child1="emil", child2="Tobias", child3="linus")


# arb arg is *arg
# keyword argusment **kwargs

def my_function(**kid):
    print("His last name is " + kid["fname"])


my_function(fname="tobias ", lname="rufus")


# default parameter
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing list as argument
def my_function(food):
    print(food)
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# pass function
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# recursion

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

print("lamda\nfunctions calling")

# python lambda
y = lambda a: a + 10
print(y(5))  # 5 is pass as argument

xx = lambda a, b: a * b
print(xx(5, 6))

print(type(xx))


# lamda doubler or tripler
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# string format
price = 49
txt = "the price is {:.3f} dollars"
print(txt.format(price))

# index numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))


# # input
# username = input("enter username")
# print("username is " + username)


# python classes and objects
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(selfi, name, age):
        selfi.name = name
        selfi.age = age


p1 = Person("john", 36)
print(p1.name)
print(p1.age)


class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Persona("John", 36)
p1.myfunc()


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p11 = Person("John", 36)
p11.myfunc()
p11.age = 40


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Mike student", "Olsen")
x.printname()


# super funciton

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = Student("Mike", "Olsen")
print(x.graduationyear)


# method to the child class

class Personwho:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Studentwho(Personwho):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)


x = Studentwho("Mike", "Olsen", 2019)
x.welcome()

# iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# looping through an Iterator

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

import datetime as dt
xxx = dt.datetime.now()
print (xxx.strftime("%C"))