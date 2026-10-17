# #1)მომხმარებელს სთხოვე პასუხი (yes ან no) თუ შეიყვანს "yes" - "Access Granted" და გააჩერე ციკლი თუ შეიყვანს "no"  -  "Access Denied" და გააჩერე ციკლინებისმიერ სხვა პასუხზე -  "Invalid Input, try again" და ციკლი გაგრძელდეს.
# choice = input("yes or no?: ")
# if choice is "yes":
#     if choice == "yes":
#         print("Access Granted")
#     elif choice == "no":
#         print("Access Denied")
#     else:
#         print("Invalid Input, try again")


# #2)
# count = 5

# while True:
#     if count > 0:
#         print(f"Time remaining: {count}")
#         count -= 1
#     else:
#         print("Liftoff!")
#         break



# #3)
# battery = 0

# while True:
#     if battery < 100:
#         print(f"charging... current level: {battery} %")
#         battery += 25
#     else:
#         print("battery fully charged!")
#         break


# #1)

# while True:
#     answer = input("Enter yes or no: ")

#     if answer == "yes":
#         print("Access Granted")
#         break
#     elif answer == "no":
#         print("Access Denied")
#         break
#     else:
#         print("Invalid Input, try again")



# #2)

# count = 5

# while count > 0:
#     print(f"Time remaining: {count}")
#     count -= 1

# print("Liftoff!")


# #3)

# battery = 0

# while battery < 100:
#     print(f"charging... current level: {battery} %")
#     battery += 25

# print("battery fully charged!")



#List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.



#2)მთვლელი იწყება 5-დან და მცირდება 1-ით სანამ 0-ზე მეტია  - "Time remaining: {count}"როცა გახდება 0   -  "Liftoff!" და გაჩერდეს ციკლი.



for count in range(5, -1, -1):

    if count > 0:
        print(f"Time remaining: {count}")
    else:
        print("Liftoff!")