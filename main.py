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
    print(bb[i]) # range need number

xx = " banana"
for i in xx:
    print(i)

for i in " banana":
    print(i)

# looping using while loop
thislist = ["apple", "banana", "cherry"]
i=0;
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
thislist2.sort(key = myfunc)
print(thislist2)

#case insensitive sort
fruits = ["apple", "banana", "Cherry", "kiwi", "mango"]
fruits.sort(key = str.lower)
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

del thistuple
print(thistuple)