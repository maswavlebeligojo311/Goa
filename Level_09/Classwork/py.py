#1)გაიარე ციკლით 1 - დან 15 - ის ჩათვლით.თუ რიცხვი 10 - ზე მეტია - f"{x} is high"სხვა შემთხვევაში - f"{x} is low"


for i in range(1, 15):
    if i > 10:
        print( f"{i} is hight")
    else:
        print(f"{i} is low")


#2)ტემპერატურა იწყება 15 - დან და ადის 25 - მდე.თუ ტემპერატურა 22 - ზე მეტია - f"temperature is {t}: too hot!!"სხვა შემთხვევაში - "temperature is {t}: normal"


for i in range(15, 25):
    if i > 22:
        print(f"temperature is {i}: too hot!!")
    else:
        print(f"temperature is {i}: normal")




#3)საწყისი ელემენტია 0 %, ყოველ იტერაციაზე იზრდება 25 ით.სანამ 100 - ზე ნაკლებია - f"charging... curent level: {battery} %"როცა გახდება 100 - f"battery fully charged!".


for i 