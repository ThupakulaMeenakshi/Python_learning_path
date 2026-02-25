#NUMERIC DATA TYPE
a=12
b=5.63
c=3+2j
x=float(a)
y=int(b)
print(type(a))
print(type(b))
print(type(c))
print(type(x))
print(type(y))
print(x)
print(y)
#importing random function
import random
A=random.randrange(1,10)
print(A)
#using E function
Q=2.e2
print(Q)
#Data Type Casting
a=int(3.14)
b=float('3')
c=str(6.23)
print(a)
print(b)
print(c)
#Strings
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Accessing the string
A="Hello World"
print(A[0])
print(A[1])
#Looping through the string
for x in "Hello world!":
    print(x)
x="Hello World!"
print(len(x))
#checking the str value is present in or not by using the keyword
A="I'm the best in SQL"
print('best' in A)
if('best' in A):
    print("YES it is present")
B="Now things are going to very expensive"
if('going' not in B):
    print("It's not available")
else:
    print("It's available")
#Slicing string
A="Hello World!"
#range of the string from starting position to ending position
print(A[1:8])
#start to upto end postion
print(A[1:])
#slice to the start position
print(A[:13])
#Negative slicing
print(A[-1:-12])
#convertig the string
#lower()
A="Hello World!"
print(A.lower())
#Upper
print(A.upper())
#strip() remove white spaces
print(A.strip())
#Replace
#syntax:variable.replace("old","New")
print(A.replace("H",'B'))
#Split function
#syntax: variable.split() Or variable.split("Seperator")
print(A.split())
print(A.split('_'))
