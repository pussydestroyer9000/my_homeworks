input_word = input("Enter your word: ")
word_len = len(input_word)

temp_input_word = "iamempty"
print("You was asking for this!\n")

for i in range(word_len):
    print(input_word)
    temp_input_word = input_word[-1] + input_word[:-1]
    input_word = temp_input_word
    
    
