words = ['one', 'two', 'three', 'four']
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word]  = 1
    else:
        word_count[word] += 1

for word in sorted(word_count):
    print(word, word_count)

keys_list   = list(word_count.keys())
values_list = list(word_count.values())

del(word_count['one'])

d1 = word_count.copy()
