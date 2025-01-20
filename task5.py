# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
m = 0
with open("task5.txt","r", encoding="utf-8") as f:
    a = f.read()
    print(a)
    b = a.replace("\n", "")
    print(b)
    b = b.replace(".", "")
    print(b)
    b = b.replace("!","")
    print(b)
    c = b.split()
    print(c)
    c.sort(key = len)
    print(c)
    i = max(c, key=len)
    i1=len(i)
    print("Max word:", max(c, key=len))
    print(len(i))
    with open("task5_2", "w", encoding="utf-8") as f2:
        f2.write(i + "-Max word")
        f2.write(f' Its lenth: {len(i)}')
