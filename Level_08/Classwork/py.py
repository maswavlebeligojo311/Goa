#1)დაბეჭდე 1-დან 100-მდე ყველა ლუწი რიცხვი და ბოლოს გამოითვალე მათი ჯამი.

idk1 = 0
while idk1 <= 100:
    print(idk1)
    idk1 += 2
print(idk1 + idk1)



#2(1-დან 100-მდე იპოვე რამდენი რიცხვი იყოფა ერთდროულად 3-ზეც და 5-ზეც.)

number2 = 0
while number2 <= 100:
    if number2 % 3 == 0 and number2 % 5 == 0:
        print(number2)
        number2 += 1