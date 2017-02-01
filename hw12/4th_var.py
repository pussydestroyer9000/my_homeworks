import re


def filework (filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        length = len(text)
        return text

def a_print (array):
    l = len(array)
    print('=============================')
    for i in range(l):
        print(array[i])
    print('=============================')

def words_choose (array1):
    array2 = ['empty_space']
    n = len(array2)
    switch = 0
    for i in range(result_l):
        #print('<', array1[i], '>')
        for j in range(n-1):
            #print(j, i, n)
            if array2[j] == array1[i]:
                switch = 1
                break
            else:
                switch = 0
                #print(array2[j], '!=', array1[i])
        if switch == 0:
            array2[n-1] = array1[i]
            array2 += ['empty_space']
            n+=1
        else:
            switch = 0
        #a_print(array2)
        #input()
    return array2[:-1]



text = filework('EMR-3F.txt') 

pattern = re.compile('(вып(?:(?:и(?:ть|л(?:а|о|и?)|вш(?:и(?:ми|[йехм])|е(?:го|му|[еймю])|ую|ая)|т(?:ы(?:ми|[йехм])?|о(?:го|му|[еймю])?|ую|ая?)))|ей(?:те)?|ь(?:е(?:\w\w)|ют?)))')
result = pattern.findall(text)
#a_print(result)

result_l = len(result)
answer = words_choose(result)

a_print(answer)
