# #1)
# # თუ რიცხვი იყოფა 3-ზეც და 5-ზეც — დაბეჭდე "FizzBuzz".
# #    თუ მხოლოდ 3-ზე — "Fizz".
# #    თუ მხოლოდ 5-ზე — "Buzz". 
# #    სხვა შემთხვევაში — თავად რიცხვი. 


# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)
    
    
    
# #2)

# #იყოპა თუ არა რიცხვი 2ზე

# a = int(input("Enter a: "))

# i = 1
# while i <= a:
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print(i)
#     i += 1
    
    
    
# #3)printing odd numbers

# i = 1

# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#     i += 1
    
    
#4)total odd and even numbers

odd_count = 0
even_count = 0

print("Odd numbers:")

for i in range(1, 101):
    if i % 2 != 0:
        print(i)
        odd_count += 1

print("Total odd numbers:", odd_count)

print("Even numbers:")

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
        even_count += 1

print("Total even numbers:", even_count)