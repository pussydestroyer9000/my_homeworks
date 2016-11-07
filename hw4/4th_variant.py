number_of_cycles = int(input("Enter N: "))
stop_word = "программирование"

for i in range(number_of_cycles):
    word = str(input("Enter your word: "))

    if word == stop_word:
        break
    
    print(word, "\n\n")

print("Thank you! Goodbye!")
