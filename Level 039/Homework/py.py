def function (number = 5):
    return number * 25
print (function(10))


def function2 (name = "Nikoloz"):
    return "My name is " + name
print (function2())

def phones(samsung, iphone, android):
    return samsung, iphone, android
s, i, a = phones("Samsung Galaxy S25 Ultra", "iPhone 17 Pro Max", "Andoid")
print(s)
print(i)
print(a)


def Rectangle(width, length):
    area = width * length
    perimeter = width * 2 + length * 2
    return area, perimeter
area, perimeter = Rectangle(10, 20)
print(area)
print(perimeter)