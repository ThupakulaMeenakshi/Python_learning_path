print("Hi i'm meenakshi",end=" ")
print("Have a nice day!")
#printing the number and the text mix
print("I am Meenakshi",21,"Years old")

#Variables in python
x=25
y="Sally"
print(type(x))
print(type(y))

#variable naming
carname='Volva'
print(type(carname))
print(carname)

#Assigning many variable to many values
x,y,z="orange","banana","grapes"
print(x,y,z)

#Assigning one value to many variables
x=y=z="Apple"
print(x)
print(y)
print(z)

#Unpacking variables
fruits=['apple','banana','grapes']
x,y,z=fruits
print(x,y,z)

#creating a variable inside a function
x="Fantastic"
def MyFun():
    x="awesome"
    print("I'm beautiful and "+x)
MyFun()

