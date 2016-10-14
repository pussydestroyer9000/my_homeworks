print("Hello, welcome to my program.\nI'm going to help you with your calculations!\nEnter your numbers to check your numbers to suit the following requirements:\n1) a + b = c\n2) a / b = c\n")
print("(Remember to enter only integer numbers otherwise program will not work)\n\n")

a = int(input("Enter 'a':"))
b = int(input("Enter 'b':"))
c = int(input("Enter 'c':"))

switch_ = 0

sum_ = a + b
if sum_ == c:
    print("\nWow! Look!", a, "+", b, "is actually equal", c, "for real!")
else:
    print("\nI am so sorry, but", a, "+", b, "is not equal", c, "in this world.")
    switch_ = 1

mul_ = b*c
if switch_ == 0:
    if mul_ == a:   
        print("You are a lucky man!", a, "/", b, "is equal", c, "too!")
    else:
        print("But wait,", a, "/", b, "is not equal", c, "unfortunately. Well, live is a cruel thing!")
else:
    if mul_ == a:   
        print("But look! Do you see this?", a, "/", b, "is equal", c, "for real! You are a lucky man!")
    else:
        print("Well, as we can see", a, "/", b, "is not equal", c, "in this world neither. Do not worry, friend!")    

print("\nAnd thank you for using my program! Good luck!")
