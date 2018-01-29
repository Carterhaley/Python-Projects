#Calculates the Area of a Rectangle 
def calcRectArea():
    print("Calculates the area of a Rectangle")
    length=eval(input("Enter length: "))
    width=eval(input("Enter width: "))
    area=length*width
    print("Area:", area)
    print()

    name=input("Enter your name: ")
    print("Hi,", name)


#Calculates the Area of a Circle
def calcCircleArea():
    print("Calculates the area of a Circle")
    radius = eval(input("enter radius: "))
    PI = 3.14 #Value of pi
    area = PI * radius ** 2
    print("area: ", area)
    print()

    
