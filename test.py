import codecs
print("Добрый день!\nПодождите, идет выполнение первой части программы...")
answerline = ""
with open ("textfortest.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    #1
    for line in lines:
        if line.find("союз") != -1:
            answerline += line
    print(answerline)
    print("================================================================================")

    #2
    print("Подождите, идет выполнение второй части программы...")
    answerline = ""
    ipm = 0
    for line in lines:
        if line.find("сущ") != -1 and line.find("жен") != -1 and line.find("ед") != -1:
            answerline += line.split(" ")[0]
            answerline += ", "
            ipm += float(line.split(" | ")[-1])
    print("Вот список всех существительных женского рода единственного числа:\n", answerline[:-2], "\n\nIPM равняется", ipm)
    print("================================================================================")

    #3
    print("Добро пожаловать в третью часть программы!")
    lever = 0
    while 2+2==4:     
        word2find = input("Введите слово, которое вам хотелось бы найти:")
        if word2find == "":
            break

        for line in lines:
            if word2find == line.split(" | ")[0]:
                print("Вот морфологическая информация о данном слове:", line.split(" | ")[1], "\nIPM слова <", word2find, "> равно", line.split(" | ")[-1], "\n")
                lever = 1
                break
        if lever == 0:
            print("Извините, такого слова в данном словаре найти не удалось, попробуйте найти что-то другое\n")
        lever = 0
