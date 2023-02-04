# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В
# случае с английским алфавитом очки распределяются так:
# A, D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.     А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:   ноутбук
# Вывод:  12
your_world = input('type world: ')
print(your_world.lower())
letters_eng = \
    {
        '2': {'A', 'D', 'G'},
        '3': {'B', 'C', 'M', 'P'},
        '4': {'F', 'H', 'V', 'W', 'Y'},
        '5': 'K',
        '8': {'J', 'X'},
        '10': {'Q', 'Z'}
    }
count = 0
for letter in your_world:
    if letter == letters_eng.values():
        count = count + letters_eng.values()
