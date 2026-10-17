# #1)სისტემაში დაყენებულია სწორი pin: "1234".მომხმარებელს აქვს მაქსიმუმ 3 მცდელობა რომ შეიყვანოს სწორი კოდი.თუ შეიყვანს სწორად - დაიბეჭდოს f"Access Granted" და ციკლი გაჩერდეს.თუ არასწორად შეიყვანს - დაბეჭდოს f"Incorrect PIN, attempts left: {დარჩენილი მცდელობები}".თუ 3 - ჯერვე არასწორად შეიყვანს - დაიბეჭდოს "Account Locked" და ციკლი დასრულდეს.



# pin = "1234"
# attempts = 3
# while True:
#     user_attempt = input("enter pin: ")
    
#     if user_attempt == pin:
#         print(f"Access Granted")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect PIN, attempts left: {attempts}")
        
#     if attempts == 0:
#         print("Account Locked")
#         break
    
    
    
# #2)შექმენი ცვლადი total = 0.ციკლში სთხოვე მომხმარებელს რიცხვის შეყვანა.ყოველი შეყვანილი რიცხვი დაემატოს total - სთუ მომხმარებელი ჩაწერს სიტყვას "stop" - ს, ციკლი შეწყდეს და დაიბეჭდოს ჯამი f"Total sum: {total}".

# total = 0

# print("enter numbers as much as you want")
# print("when you want to stop, type (Stop)")

# while True:
#     number = input("enter a number:")
    
#     if number == "Stop":
#         break
    
#     number = int(number)
        
#     total += number
#     print(f"Total sum: {total}")
# else:
#     print("error")
    
    
    
    
    
# #3)პროგრამაში წინასწარ განსაზღვრულია საიდუმლო რიცხვი(secret_number = 7)მომხმარებელმა უნდა გამოიცნოს რიცხვი:თუ შეყვანილი რცხვი მეტია საიდუმლოზე - f"Too high, try again"თუ ნაკლებია - f"Too low, try again"
# #თუ დაემთხვა - "Congratulations, you guessed it!" და ციკლი წყდება.



# secret_number = 7

# while True:
#     user_Guess = int(input("enter your guess:"))
#     if user_Guess > secret_number:
#         print(f"Too high, try again")
#     elif user_Guess < secret_number:
#         print(f"Too low, try again")
#     elif user_Guess == secret_number:
#         print("Congratulations, you guessed it!")
#         break
#     else:
#         print("Error!")
        
        
        
        
        
        
#4)მომხმარებელს შემოაყვნინე რაიმე სიტყვა, ამის შემდეგ for loop ით გაიგე რამდენი ხმოვანია მასში.

word = input("enter a word: ")
ct = 0
vowels = "aeiou"

for i in word:
    if i in vowels:
        ct += 1
print(ct)