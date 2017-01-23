import random
___NUMBER_OF_HINTS___ = 3


def opentodict (filename):
    n = 0
    dic = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        random.shuffle(lines)
        for line in lines:
            dic[line.split(',')[0]] = line.split(',')[1:-1]
            n+=1
    return dic, n

def playing (dic, dots):
    keys_list = list(dic.keys())
    i = 0
    points = 0
    
    for i in range(nlines):
        print("\n")
        for p in range(___NUMBER_OF_HINTS___):
            l = len(dic[keys_list[i]][p])
            print(dic[keys_list[i]][p], dots[:l])                           #4 вариант. Многоточие должно содержать столько точек, сколько букв в подсказке          
            
            word = input()
            
            if word == keys_list[i]:                                
                print("+", 3-p, "points!\n")                                    
                points += 3-p
                
                break
            else:
                print("wrong!")
    return points
            
         
riddles, nlines = opentodict("riddles1.csv")
print('hello, lets play a game. im going to tell you adjectives and you will try to guess the word. sooner you guess - more points you get!')
points = "............................."
print("TOTAL SCORE:", playing(riddles, points))
