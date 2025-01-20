# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open ('task1.txt', encoding="utf-8") as f:
    file_line=f.readlines()
    print(len (file_line))
    a = 0
    c = 0
    for line in file_line:
        b = line.split()
        c = c + len(b)
    print(c)
    for line in file_line:
        d = len(line)
    print(d)


    
