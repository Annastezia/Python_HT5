with open('Text4.txt', 'r') as data:
    txt = data.read()


def compress(txt):
    count = 1
    res = ' '
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def extract(txt):
    number = ' '
    res = ' '
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ' '
    return res


s = input("Введите текст для сжатия: ")
print(f"Текст после сжатия: {compress(s)}")
print(f"Текст после распаковки: {extract(compress(s))}")