def openf(filename): 
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        return text


def counting():
    word = ''
    word_count = {}

    for letter in text:
        if letter == ' ' or letter == '.' or letter == ',':
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word]  = 1
            word = ''
        else:
            word += letter
    return word_count

def printing():
    for word in sorted(word_count):
        if word_count[word] >= 10:
            print(word, word_count[word])
        
text = openf('file.txt')
word_count = counting()
printing()
