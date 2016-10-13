word = input("Enter a word from the second group: ")

if  word.endswith('о') or word.endswith('ь') or word.endswith('л') or word.endswith('т') or word.endswith('с'):
    print("IMENITELNIY PADESZH, EDINSTVENNOE CHISLO")

if word.endswith('а') or word.endswith('я') :
    print("RODITELNIY PADESZH, EDINSTVENNOE CHISLO")

if word.endswith('у') or word.endswith('ю') :
    print("DATELNYI PADESZH, EDINSTVENNOE CHISLO")

if word.endswith('я') or word.endswith('о') :
    print("VINITELNIY PADESZH, EDINSTVENNOE SHISLO")

if word.endswith('м'):
    if word.endswith('ем') or word.endswith('ом'):
        print("TVORITELNIY PADESZH, EDINSTVENNOE CHISLO")
    else:
        print("IMENITELNIY PADESZH, EDINSTVENNOE CHISLO")

if word.endswith('е'):
    print("PREDLOSZHNYI PADESZH, EDINSTVENNOE CHISLO")
