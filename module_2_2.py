first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and first == third and third == second:
    print(int(3))
elif first == second or first == third or third == second:
    print(int(2))
else:
    print(int(0))
