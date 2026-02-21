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