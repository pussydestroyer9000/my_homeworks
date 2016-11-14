string = ""
stop_word = ""
list_of_words = ""

print("Welcome!\nThis program will try to recognize infinitive forms from words that you will type.")
print("If you do not want to type more words just enter the empty request.")

while True:
    string = input("Enter the word: ")

    if string == stop_word:
        break

    if string[-2:] == "re" :
        list_of_words += string
        
    if string[-2:] == "ri" :
        list_of_words += string
        
    if string[-3:] == "sse":
        list_of_words += string 

    list_of_words += "\n"

print("\nInfinitive forms (probably):", list_of_words)    
