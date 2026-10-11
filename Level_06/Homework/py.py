#1)
age = int(input("enter you age: "))
job = bool(input("do you have a job? True or False: "))

if age < 18:
    print("You can't")
elif age > 18 and job == True:
    print("you can")
elif age > 18 and job == False:
    print("you can't")



#2)
pin = "a1a1"
ping = input("enter pin: ")
balance = 1220

if ping == pin:
    print("You are in!")
    print("balance 1220")
elif ping != pin:
    print("wrong pin")

total = float(input("withdraw money"))

if total > balance:
    print("withdrawing too much")
else:
    print("withdrawed secsessfully")