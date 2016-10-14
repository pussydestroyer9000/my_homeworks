right_number = 4
manual_number = 0
print("Try to guess the number :)\n")
manual_number = int(input("Type it:"))
if right_number == manual_number:
    print("WOW! Congrats! You r right!")
else:
    if right_number > manual_number:
        print("It is too small number :)")
    if right_number < manual_number:
        print("It is too big number :)")
    print("try again!\n")
    
manual_number = int(input("Type it:"))
if right_number == manual_number:
    print("WOW! Congrats! You r right!")
else:
    if right_number > manual_number:
        print("It is too small number :)")
    if right_number < manual_number:
        print("It is too big number :)")
    print("Im sorry!\n")
