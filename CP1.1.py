x1=float(input('Введите координаты основной диагонали прямоугольника\nдля задания прямоугольника на координатной плоскости\nx1 = '))
y1=float(input('y1 = '))
x2=float(input('Координаты второй точки:\nx2 = '))
y2=float(input('y2 = '))
print("Координаты прямоугольника:A[",x1,';',y1,'], B[',x1,';',y2,'], C[',x2,';',y2,'], D[',x2,';',y1,']')
x=float(input('Введите координаты искомой точки:\nx='))
y=float(input('y='))
if min(x1,x2)<x<max(x1,x2) and min(y1,y2)<y<max(y1,y2):
    print('Точка принадлежит прямоугольнику\nS =','%.1f'%abs((x2-x1)*(y2-y1)))
    print('P =',2*(abs(x2-x1)+abs(y2-y1)))
elif (min(x1,x2)>x or x>max(x1,x2)) or (min(y1,y2)>y or y>max(y1,y2)):
    a=input('Точка не принадлежит прямоугольнику\nВведите две строки:\nпервая:')
    b=input('вторая')
    if abs((x2-x1)*(y2-y1))>max(len(a) ,len(b)):
       print('S >',max(a,b))
    else:
       print('S <=',max(a,b))
else:
     if (x == x1 or x == x2) and min(y1, y2) < y < max(y1, y2):
         x = (x2 + x1) / 2
     elif (y == y1 or y == y2) and min(x1, x2) < x < max(x1, x2):
         y = (y2 + y1) / 2
     else:
         x = (x2 + x1) / 2
         y = (y2 + y1) / 2
     print('Точка на границе\nX = ', x)
     print('Y = ', y)