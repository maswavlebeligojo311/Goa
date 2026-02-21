#while loop კოდის გამეორებას ახდენს უცნობი რაოდენობით, როდესაც for loop_ს ლიმიტს ჩვენ უთითებთ.
#range ფუნქცია გვეხმარება იმისათვის რომ განვსაზღვროთ რიცხვების სია, for loop_ის შემთხვევაში ის ჩვენ გვეხმარება რომ ჩავწეროთ რაოდენობა და შემდეგ გავიმეოროთ საიტერაციო ცვლადის მეშვეობით.
for i in range (0, 100, 2):
         print (i)

for i in range (1, 100, 2):
          print (i)

for i in range (11):
          print ("Nikoloz")

cars = 5
Money = 0
while cars > 0:
        cars = cars - 1
        print ("car is sold!")
        Money = Money + 5000
print("Total amount of money made" + str(Money))