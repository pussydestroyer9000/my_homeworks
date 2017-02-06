def filework (filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines

def findingline (lines, phrase):
    switch = 0
    for line in lines:
        if line.find(phrase) > -1 or switch > 0:
            if switch == 2:
                return line
            if switch == 1:
                switch = 2
            if switch == 0:
                switch = 1

    if switch == 0:
        print("ПОДСТРОКА НЕ НАЙДЕНА")
        return 0

def findinganswer(filename, phrase):
    lines = filework(filename)
    line = findingline(lines, phrase)
    line = line.split("title")
    line = line[1].split('"')
    return line[1]

print("Данный ученый известен в данной научной сфере:", findinganswer("Альварес, Луис — Википедия.html", "Научная сфера"))
