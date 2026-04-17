#function გამოიყენება რომ მივანიჭოთ ელემენტებს ფუნქციები.
#არგუმენტი პითონში არის პუნქცია

def function(List):
    number = 0
    for i in List:
        number += 1
    return number
print (function(["car", "plane", "table", "number"]))



def fun1(a, b):
    return a + b
print (fun1(9, 4))

def fun2(a, b):
    return a - b
print (fun2(10, 6))

def fun3(a, b):
    return a * b
print (fun3(2, 2))

def fun4(a, b):
    return a / b
print (fun4(10, 2))

#function აბრუნებს და გამოაქვს ბრძანება.