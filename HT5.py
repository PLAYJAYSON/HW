#########################################################
N = int(input('Введите количество слов:'))
w = ""
for i in range(N):
    print(i+1,'-е слово:',sep='')
    i = input()
    w += i[0]
print(w.upper())


###########################################################
w = input('Введите анализируемое слово')
print("Общее кол-во символов в строке:", len(w))
print("Первый символ строки:", w[0])
print("Последний символ строки:", w[-1:])
print("Строку в обратном порядке:", w[::-1])
print("Все символы с четными индексами:", w[::2])
print("Все символы с нечетными индексами:", w[1::2])


#######################################################
import string
w = input()
n = 0
if w.isdigit():
    for i in w:
        print(int(i) * 10,sep=', ')
elif w.isalpha():
    for i in w:
        if i == 'q' or i == 'Q':
            n += 1
    print(n)
else:
    r = 0
    for i in w:
        if i in string.punctuation:
            r += 1
    print(r)


########################################################
while True:
    w = input("Задайте строку: >>>")
    if w.upper() == "STOP":
        break
    elif w.isalpha():
        print("Буквенная строка")
    elif w.isdigit():
        print("Цифровая строка")
    elif w.isascii():
        print("Знаковая строка")
    else:
        print('Смешаная строка')
