Grade = int(input("enter your grade (1_100):"))
if Grade >= 90:
    print ("A")
elif Grade >= 80 and Grade < 90:
    print ("B")
elif Grade >= 70 and Grade < 80:
    print ("C")
elif Grade >= 60 and Grade < 70:
    print ("D")
else:
    print ("F")




number = int(input("აირჩიე რიცხვი:"))

if number > 0:
    print("რიცხვი დადებითია")
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი არის ნული")


Num1 = int(input("enter first number:"))
Num2 = int(input("enter second number:"))
if Num1 > Num2:
    print("First Number is Greater than second one")
else:
    print("Second Number is Greater than first one")



temperature = int(input("ცელსიუსი:"))

if temperature < 0:
    print("Cold")
elif 0 >= temperature and temperature <= 30:
    print("Normal")
else:
    print("Hot")