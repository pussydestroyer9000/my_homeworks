def filework (filename):
    with open(filename, 'r', encoding="utf-8") as file:
        text = file.read()
        length = len(text)
        return (text, length)
    

def back_comparing (a, b, place=1): #функция, которая помогает сделать функцию find_words универсальной (проводится сравнение слов сзади)
    lenb = len(b)
    if len(a) < lenb:
        return 0
    if a[-lenb:] == b[-lenb:]:
        return 1
    else:
        return 0
    


def find_words (word):
    word_counter = 0
    wordstart = 0

    for i in range(len_):
        if text[i] == ' ' or text[i] == ',' or text[i] == '.' or text[i] == '!' or text[i] == '?' or text[i] == ':' or text[i] == ';' or text[i] == '\n':
            if back_comparing(text[wordstart:i], word) == 1:
                word_counter += 1
            wordstart = i+1
    return word_counter

    

text, len_ = filework("paptext.txt")
print("Предположительное количество форм на -ed:", find_words("ed"))
print("Предположительное количество слов на -ed, образованных от глаголов на -y или -е:", find_words("ied"))
