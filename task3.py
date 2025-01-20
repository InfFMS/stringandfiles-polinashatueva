# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
g = "ugfghe fjq ugqu dqjkqw fjkqfq d".count("f")
print(g)
with open("task3.txt","r",encoding="utf-8") as f:
    r = f.read()
    r = r.replace(".","")
    r = r.replace(",", "")
    r = r.replace("!", "")
    r = r.replace("\n", "")
    print(r)
    b = r.split()
    print(b)
    d = r.lower()
    print(d)
a1 = "солнце"
a2="светит"
a3="ярко"
a4="ветер"
a5="колышет"
a6="траву"
a7="садится"
a8='за'
a9="горизонт"
a10="а"
a11="стихает"
b1 = d.count("солнце")
print(b1,a1)
b2 = d.count("светит")
print(b2,a2)
b3 = d.count("ярко")
print(b3,a3)
b4 = d.count("ветер")
print(b4,a4)
b5 = d.count("колышет")
print(b5,a5)
b6 = d.count("траву")
print(b6,a6)
b7 = d.count("садится")
print(b7,a7)
b8 = d.count('за')
print(b8,a8)
b9 = d.count("горизонт")
print(b9,a9)
b10 = d.count("а")
print(b10,a10)
b11 = d.count("стихает")
print(b11,a11)


