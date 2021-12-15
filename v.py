p1, p2 = input(), input()
if p1 == p2: print("Пароль принят")
else: print("Пароль не принят")


a=input()
print(int(a)+int(a+a)+int(a+a+a))





a,b,c,d= int(input()), int(input()), int(input()), int(input())
print(a**b + c**d)


a, b = int(input()), int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2+b**2)




a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

a=int(input())
a3=a%10
a2=a//10%10
a1=a//10**2%10


print("Сумма цифр =", a1+a2+a3)
print("Произведение цифр =", a1*a2*a3)




a=int(input())
a3=str(a%10)
a2=str(a//10%10)
a1=str(a//10**2%10)
print(a1+a2+a3,
      a1+a3+a2,
      a2+a1+a3,
      a2+a3+a1,
      a3+a1+a2,
      a3+a2+a1, sep='\n')




a=int(input())
a3=str(a%10)
a2=str(a//10%10)
a1=str(a//10**2%10)
a0=str(a//10**3%10)
print('Цифра в позиции тысяч равна', a0)
print('Цифра в позиции сотен равна', a1)
print('Цифра в позиции десятков равна', a2)
print('Цифра в позиции единиц равна', a3)
