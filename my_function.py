def greet():
    print("Hello!")
greet()
greet()

#------------------------------------

def greet2(name):
    print(f"Hello {name}")
greet2("Carlos")
greet2("Fool")

#------------------------------------

def average(a,b):
    return (a+b)/ 2 #this is how the function gives back the value
print(average(10,20))

#------------------------------------

def divide(x,y):
    """
    :param x: first number
    :param y: second number
    :return: float, the division of x by y
    """
    if y == 0:
        return None
    return x/y

print(divide(10,2))
print(divide(10,0))
print(divide(y=10,x=2))

#------------------------------------

def bond(first_name, last_name):
    return f"{first_name}, {first_name} {last_name}"

def introduce(name):
    print(f"The name is: {name}")

print(bond("Carlos","Fool"))
print(introduce(bond("Carlos","Fool")))

#------------------------------------

import random
def CarlosFoolish():
    s= 0
    count = 0
    while True:
        try:
            s = s + random.randint(1, 101)
            count += 1
            if s > 900:
                print(s)
                print(count)
                break
        except ValueError:
            print("fool")
CarlosFoolish()

