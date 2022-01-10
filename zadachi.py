a=int(input())
if a%2==0: print("Четное")
else: print("Нечетное")

a=int(input())
a1=a//1000%10
a2=a//100%10
a3=a//10%10
a4=a%10
if a1+a4==a2-a3: print("ДА")
else: print("НЕТ")


a=int(input())
if a>=18: print("Доступ разрешен")
else: print("Доступ запрещен")

a,b,c=int(input()),int(input()),int(input())
if b-a==c-b: print("YES")
else: print("NO")

a,b=int(input()),int(input())
if a>b: print(b)
else: ptint(a)


a,b,c,d=int(input()),int(input()),int(input()),int(input())
if a<b and a<c and a<d: print(a)
elif b<c and b<d: print(b)
elif c<d: print(c)
else: print (d)



a=int(input())
if a<=13: print('детство')
elif 14<=a<=24: print('молодость')
elif 25<=a<=59: print('зрелость')
else: print('старость')


a,b,c=int(input()),int(input()),int(input())
r=0
if a>0:
    r=r+a
else: 
    a=0
    r=r+a
if b>0:
    r=r+b
else: 
    b=0
    r=r+b
if c>0:
    r=r+c
else: 
    c=0
    r=r+c
print(a+b+c)

a=int(input())
if -1<a<17: print('Принадлежит')
else: print('Не принадлежит')

a=int(input())
if a<=-3 or a>=7:
    print('Принадлежит')
else: print('Не принадлежит')


a=int(input())
if a in range(-29,-1) or a in range(8,26):
    print('Принадлежит')
else: print('Не принадлежит')

a=int(input())
if 999<a<10000 and (a%7==0 or a%17==0):
    print("YES")
else: print("NO")

a,b,c=int(input()),int(input()),int(input())
if a+b>c and a+c>b and b+c>a:
    print("YES")
else: print("NO")

a=int(input())
if (a%4==0 or a%400==0) and a%100!=0:
    print("YES")
else: print("NO")

a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print("YES")
else: print("NO")


a,b,c,d=int(input()),int(input()),int(input()),int(input())
if a==c or b==d:
    print("YES")
else: print("NO")

a,b,c,d=int(input()),int(input()),int(input()),int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print("YES")
else: print("NO")


n , k =int(input()),int(input())
if k>n:
    print("YES")
elif k<n: 
    print("NO")
else:
    print("Don't know")


    a,b,c=int(input()),int(input()),int(input())
if a==b==c:
    print('Равносторонний')
elif a==b or a==c or b==c:
    print('Равнобедренный')
else:
    print('Разносторонний')


#Калькулятор
a,b = int(input()), int(input())
c=input()
acb=" "
if b==0 and c=='/':
    print('На ноль делить нельзя!')
elif c=='*':
    acb=a*b
elif c=='/':
    acb=a/b   
elif c=='+':
    acb=a+b  
elif c=='-':
    acb=a-b
elif c!='*' or c!='/' or c!='+' or c!='-': print('Неверная операция')
else: print (acb)
print (acb)

#цветовой микшер
a, c = input(), input()
r="красный"
y="желтый"
b="синий"
f="фиолетовый"
o="оранжевый"
g="зеленый"
if a==c and(a==r or c==r or a==y or c==y or a==b or c==b): print(a)
elif (a==r and c==b) or(c==r and a==b): print(f)
elif (a==r and c==y) or(c==r and a==y): print(o)
elif (a==y and c==b) or(c==y and a==b): print(g)
else: print("ошибка цвета")



a=int(input())
if 0<=a<=36:
    if a==0: print('зеленый')
    elif 0<a<11 or 18<a<29:
        if a%2==0: print('черный')
        else: print('красный')
    elif 10<a<19 or 28<a<37:
        if a%2==0: print('красный')
        else: print('черный')
else: print('ошибка ввода')


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if min(b1, b2) < max(a1, a2): 
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))


y=int(input())
if y%100==0:print('YES')
else:print('NO')


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if (a1+b1)%2==(a2+b2)%2 :print('YES')
else: print('NO')



a, b = int(input()), input()
if 9<a<16 and b=="f": print('YES')
else: print('NO')    


a=int(input())
b="I"
if a==1: b=b
elif a==2: b="II"
elif a==3: b="III"
elif a==4: b="IV"
elif a==5: b="V"
elif a==6: b="VI"
elif a==7: b="VII"
elif a==8: b="VIII"
elif a==9: b="IX"
elif a==10: b="X"
else: b="ошибка"
print(b)


a=int(input())
if a%2!=0: 
    print('YES')
else:
    if 2<=a<=5: print('NO')
    elif 6<=a<=20: print('YES')
    elif a>20: print('NO')


a,b,c,d=int(input()),int(input()),int(input()),int(input())
if ((max(c,a))-(min(c,a))) == ((max(d,b))-(min(d,b))):
    print("YES")
else:
    print("NO")

a,b,c,d=int(input()),int(input()),int(input()),int(input())
if (c==(a+1) and d==(b+2)) or (c==(a+2) and d==(b+1)) or (c==(a-1) and d==(b-2)) or (c==(a-2) and d==(b-1)) or (c==(a+1) and d==(b-2)) or (c==(a+2) and d==(b-1)) or (c==(a-1) and d==(b+2)) or (c==(a-2) and d==(b+1)):
    print('YES')
else: print ("NO")

a,b,c,d=int(input()),int(input()),int(input()),int(input())
if abs(a-c)==abs(b-d) or abs(a-c)==abs(b-d) or  (a!=c and b==d) or (a==c and b!=d):
    print('YES')
else: print ("NO")


a, b = float(input()), float(input())
s=0.5*a*b
print(s)


s, b, c = float(input()), float(input()), float(input())
print(s/(b+c))

a = float(input())
if a==0: print('Обратного числа не существует')
else: print(1/a)

f = float(input())
print(5/9*(f-32))


a=int(input())
if a<=2: print(10.5*a)
else: print(10.5*2+4*(a-2))

f = float(input())
print(int((f*10)%10))

a = float(input())
b = int(a)
print(a-b)

a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
print('Наименьшее число =', min(a,b,c,d,e))
print('Наибольшее число =', max(a,b,c,d,e))

a,b,c=int(input()),int(input()),int(input())
print(max(a,b,c))
if a==b or a==c: print(a)
elif b==c or a==b==c:print(b)
elif a!=max(a,b,c) and a!=min(a,b,c): print(a)
elif b!=max(a,b,c) and b!=min(a,b,c): print(b)
elif c!=max(a,b,c) and c!=min(a,b,c): print(c)  
print(min(a,b,c))

a=int(input())
b=a//100
c=a%10
d=int(((a-c)/10)%10)

if max(b,c,d)-min(b,c,d)==(b+c+d)-max(b,c,d)-min(b,c,d): print('Число интересное')
else: print('Число неинтересное')