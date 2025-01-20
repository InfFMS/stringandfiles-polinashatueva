# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open ('task2.txt', encoding="utf-8") as f:
    a = f.read()
    print(a)
for line in a:

    b = a.replace ("Python", "Питон")
    with open("a","w",encoding="utf-8") as k:
        k.write(b)
print(a.count("Python"))
print(b)

