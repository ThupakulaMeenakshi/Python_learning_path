#Day 02 Data Types
#string data type
text='Meenakshi'
print(type(text))
print(text)

#integer data type
a ,b=5,3
print("The sum is ",a+b)
print(type(a))

#float data type
x=4.56
y=2.31
print("The division result is",x/y)
print(type(x))

#complex data type
P=5+1j
Q=2+3j
print("The addition is",P+Q)
print(type(P))

#List data type 
k=['Meenakshi',21,'btech']
print("my name is "+k[0]+"I'm "+str(k[1]),"and I'm "+k[2]+"Undergraduate")
print(type(k))

#tuple data type
M=("Apple","Banana","orange")
print(type(M))
print(M)

#Boolean data type
a=3
b=6
if(a>b):
    print(bool(a))
else:
    print(bool(b))

#Set Datatype
Items={"brinjal","tamrind","tomato"}
print(type(Items))
print(Items)

#Dict datatype
PersonData={'name': "Meenakshi",'age':21,'qual':"Btech"}
print(PersonData)
print(type(PersonData))

#FrozenSet data type
listOfItems=frozenset({"bitterguard","potato"})
print(listOfItems)
print(type(listOfItems))

#Bytearray datatype
x=bytes(5)
print(x)
y=bytearray(6)
print(y)

#Range data type
x=range(5)
print(list(x))


#importing random function
import random
num=random.randrange(1,50)
print(num)
