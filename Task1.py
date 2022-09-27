# txt = 'Напишите абв пабврограмму программу, удаляющую из этого незабвенного текста все абвслова слова, содерабващие содержащие последовательность букв а, б и в "абв"'
txt = open('Task1Text.txt')

def remove(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return ' '.join(txt)

txt = remove(txt)
print(txt)

