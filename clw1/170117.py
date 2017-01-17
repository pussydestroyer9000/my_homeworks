#ключами могут быть не любыми типами данных (только неизменяемые: строка, число, число с плавающей точкой), не могут быть одинаковыми
#значения могут быть любыми типами данных, могут быть одинаковыми
#словари устроены так, чтобы они работали быстро
#


dict_= {1: 'a', 2: 'b'} #initialisation of the dictionary

dict_[4] = 'd' #adding new values to the dictionary
dict_['pisos'] = 'pisos hehehe'

value_1 = dict_[2]

if 3 in dict_:
    value_1 = dict_[3] #checking the key

#dict_[3] = []
#dict_[3].append('abc') #not the way you should add values to the dic

dict_[4] = 0
dict_[4] += 1 #math with dic

for k in dict_:
    print(dict_[k]) #printing only the values



a= [1, 2, 3, 4]
for i in a:
    dict_[i] = 0

#do not change the dictionary in cycle

a = [1, 2, 3]
a[0] = 4
#a[12] = 4
