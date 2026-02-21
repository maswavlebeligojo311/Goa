temperature = int(input("enter temperature:"))
if temperature > 30 and temperature < 35:
    print ("გარეთ ზალიან ცხელა")
elif temperature > 20 and temperature < 30:
    print ("ნორმალური ტემპერატურაა")
elif temperature > 15 and temperature < 20:
    print ("აცივდა")
else:
    print ("ყინავს")