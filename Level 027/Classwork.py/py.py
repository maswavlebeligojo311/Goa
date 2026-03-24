#როდესაც list არის mutable ნიშნავს რომ ცვლადის დაწერის შემდეგაც მისი შეცვლა
#შეიზლება, ხოლო lists შვენ ვერ შევცვლით რომელსაც immutable ეწოდება.

name1 = "vato"
name2 = "alex"
name3 = "dato"
name4 = "gio"
name5 = "niko"
name6 = "soso"
name7 = "lasha"
List = [name1, name2,  name3,  name4,  name5,  name6,  name7]
print (List)

Your_name = input("enter you name:")
Your_number = int(input("enter your number:"))
print (Your_name[Your_number])