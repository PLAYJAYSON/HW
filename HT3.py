a=int(input('Введите число: '))
for i in range(1,11):
    print(a,'x',i,'=', a*i)
#########################################
s=0
a=int(input('Задайте количество чисел: '))
for i in range(1,a+1):
    b=float(input('Введите число: '))
    s+=b
print('Сумма чисел: ',s)
##########################################
a=input('Введите ваш id: ')
while(a!='PRINT'):
    print('id'+a)
    a=input('Введите ваш id: ')
#########################################
a=float(input('Введите два числа:\n'))
b=float(input())
while(b!=0):
    print(a+b,a-b,a*b,a/b,sep='\n')
    a = float(input('Введите два числа:\n'))
    b = float(input())
print('На ноль делить нельзя!')
