import math
x1=float(input('Введите первое значение x1:'))
x2=float(input('Введите второе значение х2:'))
h=float(input('Введите шаг смещения по оси x:'))
m=int((max(x1,x2)-min(x1,x2))//h)
print(m)
x=min(x1,x2)
if (x1<0 and x2<0) or (x1>0 and x2>0) or abs(x1)==abs(x2):
    m+=1
elif (x1<=0 and x2>=0) or (x2<=0 and x1>=0):
    m+=2
print(m)
for i in range (0,m):
    print(math.log(math.sqrt((1+x*x)/(1-x*x))),', при х =',x)
    x+=h
##############################################################
n=int(input('Введите от и до какого значения будем производить сумму 3n+1:\nот:'))
m=int(input('и до:'))
s=0
for i in range(n,m+1):
    s+=(3*i+1)/12
print('S =',s)
##################################################################
n=int(input('Введите размерность матрицы nxn:'))
w=input('Параметр 1:')
q=input('Параметр 2:')
k=w+' '
for i in range(1,n//2+1):
    k*=i
    for j in range(1,n-i*2+1):
        k+=q+' '
    print(k+(w+' ')*i)
    k=w+' '
if n%2==1:
   print((w+' ')*n)
for i in range(n//2,0,-1):
    k*=i
    for j in range(n-i*2+1,1,-1):
        k+=q+' '
    print(k+(w+' ')*i)
    k=w+' '
print('Сумма',n,'- го столбца =',n*int(w))
print('Сумма',n-1,'- го столбца =',(n-2)*int(w)+2*int(q))
print('Сумма',n-2,'- го столбца =',(n-4)*int(w)+4*int(q))