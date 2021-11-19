#Программы по  курсу Stepik
"""print(input(), '- чемпион!')""" #s1,s2,s3 = input(), input(), input()
#sep  sep=' '   # пробел                      оно начинает с новой строки без end
"""print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**')"""
#end  end='\n'  # перевод строки                оно продолжает строку только если в end не помещен "\n"
"""print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')"""

"""print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')"""

#format
"""name = input()
print("Привет, {0}!".format(name))"""

#** 	Возведение в степень
#% 	Остаток от деления
#// 	Целочисленное деление    Отрицательные числа округляются в меньшую сторону.

"""a,b,c = input()
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')"""


#if
"""num = int(input())
s1=num // 1000
s2=(num%1000)//100
s3=(num%100)//10
s4=num%10
if s1+s4==s2-s3:
    print("ДА")
else:
    print("НЕТ")"""


"""a,b,c = int(input()),int(input()),int(input())
raz = b-a 
if c==b+raz:
    print("YES")
else:
    print("NO")"""

"""a,b,c,d = int(input()),int(input()),int(input()),int(input())
minAB = 0
minCD = 0
if a<b:
    minAB = a
else:
    minAB = b
if c<d:
    minCD = c
else:
    minCD = d
if minAB<minCD:
    print(minAB)
else:
    print(minCD)"""

#2 способ решения
"""a,b,c,d = int(input()),int(input()),int(input()),int(input())
print(min(a,b,c,d))"""

#логические операторы and — логическое умножение;   or — логическое сложение;   not — логическое отрицание.
"""age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')"""

#Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
"""num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')"""

#вложенные циклы
"""for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)"""

"""for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)""" #<<1 0 2 0 2 1

"""for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)"""#<<0 1 0 2 1 0 1 2 2 0 2 1

#28n+30k+31m=365.
"""total = 0
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1,12):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print('n =', n, 'k =', k,"m =", m)"""

"""n = int(input())
plus = 0
count = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    print(i,'+'*count, sep='')
    count = 0"""

"""#28n+30k+31m=365.
total = 0
for n in range(1, 11):  #бык
    for k in range(1, 21):  #корова
        for m in range(1,201):  #теленок
            if 10 * n + 5 * k + 0.5 * m == 100 and n+k+m==100:
                print('n =', n, 'k =', k,"m =", m)"""









#cтроки и индексироване .find,.rfind,.count,.startswith,.endswith,.replace("o","@"),strip()
"""n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)
"""

"""s = input()
f = s.count('f')
if f>1:
    print(s.find('f'),s.rfind('f'))
elif f==1:
    print(s.find("f"))
else:
    print("NO")"""
#isalpha,isdigit,islower,isupper,isspace,isalnum
#Форматирование строк
"""age = 27
txt = 'My name is Timur, I am {}'.format(age)
print(txt)"""

"""first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')"""

#ASCII & Unicode(аски)
#ord,chr
"""for i in range(26):
    print(chr(ord('A') + i))""" # выводит алфавит англ

"""s = input()
for i in s:
     print(ord(i), end = " ")"""

"""num1 = int(input())
num2 = int(input())
for i in range(num1 , num2+1):
    print(chr(i), end=" ")"""


"""n = int(input())
s = input()
k =''
for c in s:
    if ord(c) -n < 97:
        k += chr(ord(c) - n - 6)
    else:
        k += chr(ord(c) - n )
print(k.lower())"""

#списки  list()             numbers = list(range(5))
"""numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']"""

#len(),sum(),min(),max()
#print(len(['apple', 'banana', 'cherry']))   # выводим длину списка, состоящего из 3 элементов

"""numbers = [2, 4, 6, 8, 10]

if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')"""

"""fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] = ['банан', 'вишня', 'киви']"""

"""print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)"""

"""numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))
print('Сумма всех элементов списка =', sum(numbers))"""

#append(),extend(),del
"""numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список
numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка"""

"""numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]
numbers.extend(odds)
print(numbers)""" #<<[0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # удаляем элемент имеющий индекс 5
print(numbers)"""

"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]
print(numbers)"""


"""n = int(input())
ls = []
ls2 = []
if n>2:
    for i in range(n):
        a = int(input())
        ls.append(a)
        if i>=1:
            ls2.append(ls[i-1]+ls[i])
    print(ls2)
elif n==2:
    x = int(input())
    y = int(input())
    ls.append(x+y)
    print(ls)"""

#del удаление нечетных символов
"""n = int(input())
lis = []
for i in range (n):
    a = int(input())
    lis.append(a)
del lis[1:n:2]
print(lis)
"""

#k-ая буква слова 🌶️🌶️
"""n = int(input())
str = ''
ls1 = []
ls2 = []
ls3 = []
for _ in range(n):
    x = input()
    ls1.append(x)
k = int(input())
for i in range(n):
    ls2.extend(ls1[i])
    if len(ls2)< k:
        del ls2[::]
        continue
    elif len(ls2) >= k:
        ls3.append(ls2[k-1])
    del ls2[::]
lns = len(ls3)
for i in range(lns):
    str += ls3[i]
print(str)"""

# Вывод элементов списка
"""numbers = [0, 4, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
"""
"""numbers = [0, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    print(numbers[i])"""

"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers)"""

"""numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers, sep='\n')"""

"""numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
for i in range(len(numbers)):
    numbers[i] = numbers[i]**2
print(sum(numbers))
"""

"""n = int(input())
ls = []
fx = 0
for i in range(n):
    x = int(input())
    print(x)
    fx = x**2 + 2*x + 1
    ls.append(fx)
print()
print(*ls, sep="\n")"""

"""#1
n = int(input())
ls = []
for i in range(n):
    x = int(input())
    ls.append(x)
ls.remove(max(ls))
ls.remove(min(ls))
print(*ls, sep="\n")
#2
n = int(input())
ls = []
for i in range(n):
    x = int(input())
    ls.append(x)
del ls[ls.index(max(ls))]
del ls[ls.index(min(ls))]
print(*ls, sep="\n")"""


"""n = int(input())
j = []
for i in range(n):
    k = input()
    if k not in j:
        j.append(k)
print(*j, sep="\n")"""

"""n = int(input())
j = []
for i in range(n):
    k = input()
    j.append(k)
psk = input()
for i in range(len(j)):
    if psk.lower() in j[i].lower():
        print(j[i])"""

#split(), join() строковые методы
"""s = 'Python is the most powerful language'
words = s.split()
print(words)"""

"""ip = '192.168.1.24'
numbers = ip.split('.')    # указываем явно разделитель
print(numbers)"""

"""words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
print(s)"""

"""st = input().split()
for i in range(len(st)):
    print(st[i][0], end=".")"""

"""st = input().split()
for i in range(len(st)):
    st[i] = int(st[i])
    print('+' * st[i])"""

"""numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])"""

"""st = input().split(".")
flag = 0
for i in range(len(st)):
    st[i] = int(st[i])
    if 0<=st[i]<=255:
        flag+=1
    else:
        print("НЕТ")
        break
if flag==4:
    print("ДА")"""


"""
st = input()
raz = input()
print(raz.join(st))"""

"""st = input().split()
count = 0
for i in range(len(st)):
    st[i] = int(st[i])
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        if st[i] == st[j]:
            count += 1
print(count)"""

#методы списка insert(),index(),remove(),pop(),reverse(),count(),clear(),copy(),sort()
"""names = ['Gvido', 'Roman' , 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)""" #['Gvido', 'Roman' , 'Timur']   ['Anders', 'Gvido', 'Roman' , 'Timur']  ['Anders', 'Gvido', 'Roman' , 'Josef', 'Timur']

"""names = ['Gvido', 'Roman' , 'Timur']
position = names.index('Timur')
print(position)""" #2

"""names = ['Gvido', 'Roman' , 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')"""

"""food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)"""# ['Курица', 'Рыба', 'Брокколи', 'Рис']

"""item = names.pop(1)
print(item)
print(names)""" # Roman      ['Gvido', 'Timur']

"""names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')
print(cnt1)
print(cnt2)
print(cnt3)""" # 3   1   0

"""names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)""" # ['Timur', 'Roman', 'Gvido']

"""
names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)"""# []

"""names = ['Gvido', 'Roman' , 'Timur']
names_copy = names.copy()              
print(names)
print(names_copy)"""# создаем поверхностную копию списка names

"""numbers = [8, 9, 10, 11]
numbers[1]=17
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.remove(8)
numbers += numbers
numbers.insert(3, 25)
print(numbers)"""

"""st = input().split()
for i in range(len(st)):
    st[i] = int(st[i])
index1 = st.index(min(st))
index2 = st.index(max(st))
st[index1],st[index2] = st[index2],st[index1]
print(*st)"""

"""st = input().lower().split()
c1 = st.count('a')
c2 = st.count('an')
c3 = st.count('the')
print("Общее количество артиклей:",c1+c2+c3)"""

"""n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())"""

# sort()
"""a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort(reverse = True)   # сортируем по убыванию
print('Отсортированный список:', a)"""

"""a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort()
print('Отсортированный список:', a)""" # отсортированый спсиок по возрастанию

"""st = input().split()
for i in range(len(st)):
    st[i] = int(st[i])
st.sort()
print(*st)
st.sort(reverse=True)
print(*st)"""

"""numbers = []
for i in range(10):
    numbers.append(i)"""
"""zeros = [0 for i in range(10)] #Создать список, заполненный 10 нулями можно и при помощи списочного выражения:
squares = [i ** 2 for i in range(10)] #2. Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
cubes = [i ** 3 for i in range(10, 21)]#3. Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
chars = [c for c in 'abcdefg']
print(chars)#4. Создать список, заполненный символами строки:"""

"""lines = [input() for _ in range(int(input()))]
print(lines)"""

"""evens = [i for i in range(21) if i % 2 == 0]
print(evens)"""

# 1
"""numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)"""
# 2
"""for i in range(1, 5):
    for j in range(2):
        numbers.append(i * j)
print(numbers)"""

"""keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords =[m for m in keywords if len(m)>=5]
print(new_keywords)"""

"""palindromes = [i for i in range(100,1001) if str(i)==str(i)[::-1]]
print(palindromes)"""

# 1
"""n = int(input())
numbers = [i**2 for i in range(1,n+1)]
print(*numbers, sep='\n')"""
# 2
"""print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')"""

# 1
"""
st = input().split()
for i in range(len(st)):
    st[i] = int(st[i])
new_st = [st[i]**3 for i in range(len(st))]
print(*new_st)
"""
# 2
"""print(*[int(i) ** 3 for i in input().split()])"""

"""print(*[st for st in input().split()],sep = '\n')"""

"""s = input()
print(*[i for i in s if i.isdigit()], sep="")"""


"""print(*[int(i)**2 for i in input().split() if int(i)**2%10!=4 and int(i)%2==0 ], sep=" ")"""

# Sort   Bubble sort     Selection sort      Insertion sort      Медленные сортировки
# Быстрые сортировки     Shell sort      Quick sort      Merge sort      Heap sort
#  Bubble sort
"""a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами

print('Отсортированный список:', a)"""
# Selection sort
"""a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
n = len(a)
i = 0
while i < n-1:
    m = i
    j = i + 1
    while j < n:
        if a[j] < a[m]:
            m = j
        j += 1
    a[i], a[m] = a[m], a[i]
    i += 1
print(a)"""

# Insert sort
"""a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
print('Начинаем цикл перебора всех элементов списка, начиная со второго (неотсортированный список)')
for i in range(1, n):
    print(a, i, 'итерация: a[i] =', a[i])
    elem = a[i]  # первый элемент из неотсортированной части списка
    print('Запоминаем проверяемый элемент списка в доп память - elem = a[i] =', a[i])
    j = i
    if a[j - 1] <= elem:
        print(f'В while не заходим, тк проверяемое число ({a[i]}) больше предыдущего ({a[i - 1]})')
    while j >= 1 and a[j - 1] > elem:
        print(f'while: сравниваем индекс = {j}: на место a[j] = {a[j]} записываем число {a[j - 1]}, и получаем', end=' ')
        a[j] = a[j - 1]
        print(a)
        j -= 1
    print(f'Извлекаем из доп памяти elem = {elem} в индекс {j}')
    a[j] = elem

print(a)"""

"""num = input().split("-")
ls = []
flag = False
for i in range(len(num)):
    if num[i].isdigit()==True:
        flag = True
    else:
        print("NO")
        flag = False
        break
if flag == True:
    if len(num)==4 or len(num)==3:
        for i in range(len(num)):
            ls.append(len(num[i]))
        if (ls == [1,3,3,4] and num[0]=='7') or ls == [3,3,4]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")"""

# Пользовательские функции   def
"""def draw_box():
    for _ in range(5):
        print('*' * 7)"""       # именовать функцию лучше названия_что_она_делает()

"""def do_nothing():
    pass
"""

"""def draw_box():
    print('*'*10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*'*10)

draw_box()"""

# функции с параметрами
"""def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)"""

"""def print_text(txt, n):
    print(txt * n)

print_text('Hello', 5)
print_text('A', 10)"""

"""def print_digit_sum(num):
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    print(summ)

n = input()
print_digit_sum(n)"""

"""def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

n = int(input())
print_digit_sum(n)"""

# локальные переменные, параметричиские переменные
"""def print_texas():
    birds = 5000 #это локальная переменная и больше нигде,как в этой функции она не достпуна.
    print('В Техасе обитает', birds, 'птиц.')"""

"""def draw_box(height, width):    #Параметрические переменные тут height, width. Внутри функции объявляется одна локальная переменная i. Параметрическая переменная тоже локальная.
    for i in range(height):
        print('*' * width)"""

# функция ничего не возвращает по этому 4-3, а не 3-4
"""def swap(a, b):
    a, b = b, a

a = 4
b = 3
swap(a, b)
print(a - b)"""

"""number = 101
def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if num != 1 and flag == True:
        print('Число', num, 'простое.')
    else:
        print('Число', num, 'составное.')
x = 17
y = int(input())
is_prime(x)
is_prime(y)
is_prime(number)"""# локальные переменные здесь - Flag,num,i

# Глобальные переменные
"""birds = 5000    # глобальная переменная

def print_texas():
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')"""
"""def print_texas():
    global birds
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

print_texas()
print_california()"""# В Техасе обитает 5000 птиц. В Калифорнии обитает 5000 птиц.


# Return

"""def convert_to_celsius(temp):
     return (5 / 9) * (temp - 32)

# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия"""

"""def convert_grade(grade):
    result = -1
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70:
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1
    return result

grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))"""

"""def get_days(month):
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return mon[month-1]

num = int(input())
print(get_days(num))"""

"""def get_factors(num):
    ls = []
    for i in range(1,num+1):
        if num%i==0:
            ls.append(i)
        else: continue
    return ls

n = int(input())
print(get_factors(n))"""

"""def find_all(target, symbol):
    ls = []
    for i in range(len(target)):
        if target[i] == symbol:
            ls.append(i)
    return ls

string = input()
char = input()
print(find_all(string, char))"""

"""def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)"""


"""def merge_list(n):
    ls = []
    for i in range(n):
        string = input().split()
        string.sort()
        for i in range(len(string)):
            string[i] = int(string[i])
        ls.extend(string)
    ls.sort()
    return ls

n = int(input())
merge = merge_list(n)
merge.sort()
print(*merge)"""

#Функции с возвратом значения Булевые функции
"""def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
number = int(input())
if is_even(number):
    print("YES")
else:
    print("NO")"""

"""def get_next_prime(num):
    prime = 0
    while prime == 0:
        num += 1
        count = 0
        for i in range(1,num+1):
            if num%i == 0:
                count+=1
        if count > 2:
            continue
        elif count == 1:
            continue
        elif count == 2:
            prime = num
            break
    return prime

n = int(input())
print(get_next_prime(n))"""

"""def is_password_good(password):
    u = sum(1 for i in password if i.isupper())
    l = sum(1 for i in password if i.islower())
    q = sum(1 for i in password if i.isdigit())
    if len(password) >= 8:
        if u >= 1 and l >= 1 and q >= 1:
            return True
        else:
            return False
    else:
        return False

txt = input()
print(is_password_good(txt))"""

"""def is_one_away(word1, word2):
    count = 0
    if word1 == word2:
        return False
    else:
        if len(word1) == len(word2):
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    count += 1
                else:
                    continue
            if count == len(word1) or count == len(word1) - 1:
                return True
            else:
                return False


        else:
            return False

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))"""


#можно удалять символы с помощью replace
"""def is_palindrome(text):
    symbols = [' ',',','.','?','!','-']
    for c in symbols:
        text = text.replace(c,"")
    text = text.lower()
    return text == text[::-1]


txt = input()
print(is_palindrome(txt))"""

"""def is_valid_password(password):
    password = password.split(':')
    count = 0
    if len(password) == 3:
        password[0] = password[0].lower()
        if password[0] == password[0][::-1]:
            password[1] = int(password[1])
            for i in range(1,password[1]+1):
                if password[1]%i == 0:
                    count += 1
            if count == 2:
                password[2] = int(password[2])
                if password[2]%2 == 0:
                    return True
                else:
                    return False
            elif count > 2:
                return False
            elif count == 1:
                return False
        else:
            return False
    else:
        return False

psw = input()
print(is_valid_password(psw))"""

#1
"""def convert_to_python_case(text):
    snake = ''
    snake += text[0].lower()
    for i in range(1, len(text)):
        if text[i] == text[i].upper():
            snake += '_'
            snake += text[i].lower()
        elif text[i] in '0123456789':
            snake += text[i]
        else:
            snake += text[i]
    return snake
txt = input()
print(convert_to_python_case(txt))"""
#2
"""def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]
txt = input()
print(convert_to_python_case(txt))"""

#return может выводить несколько значений (не только одно)
"""def solve(a, b, c, d, e, f):
    x = (d * e - b * f)/(a * d - b * c)
    y = (a * f - c * e)/(a * d - b * c)
    return x, y

xsol, ysol = solve(2, 3, 4, 1, 2, 5)
print('Решением системы являются числа', 'x =', xsol, 'y =', ysol)"""

#модуль random  randrange()  randint()  random()    uniform()   seed()
#ПСЕВДО СЛУЧАЙНЫЕ ЧИСЛА      from random import *
"""import random
num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)
print(num1)
print(num2)"""

"""import random
num = random.randrange(0, 101, 10)"""

"""import random

num = random.random()
print(num)"""

"""import random

num = random.uniform(1.5, 17.3)
print(num)"""

"""import random
random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
for _ in range(10):
    print(random.randint(1, 100))"""

"""import random
again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')"""

"""import random
for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')"""

#shuffle()  choice()    sample()
"""import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)"""

"""import random
print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))"""

"""import random

numbers = [2, 5, 8, 9, 12]
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))"""

"""import math
n = int(input())
print(math.ceil(math.log(n , 2)))"""

"""def is_valid(n):
    if n.isdigit() :
        n = int(n)
        if n > 100 or n < 1:
            return ('Ты че, дебил? АБОБА')
        elif 1 <= n <= 100:
            if n > num:
                return ('Ваше число больше загаданного, попробуйте еще разок')
            elif n < num:
                return ('Ваше число меньше загаданного, попробуйте еще разок')
            elif n == num:
                return ('Вы угадали, поздравляем!')
    elif n.isalpha():
        return ('А может быть все-таки введем целое число от 1 до 100?')

import random
num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
n = input()
while num != n:
    print(is_valid(n))
    n = input()"""

"""import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, Я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как тебя зовут?')
print('Привет',  name)

again = 'д'
while again.lower() == 'д':
    question = input('Задай мне свой вопрос: ')
    print(random.choice(answers))
    again = input('Задать еще один вопрос? (д = да, н = нет): ')

    if not again.lower() == 'д':
        print('Возвращайся если возникнут вопросы!')"""

"""def generate_password(length , chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

import random
digits =  '0123456789'
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "!#$%&*+-=?@^_"
chars = ''
n = int(input('Какое количество паролей нужно для генерации?'))
length = int(input('Длину одного пароля'))
flag1 = input('Включать ли цифры 0123456789?')
flag2 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
flag3 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
flag4 = input('Включать ли символы !#$%&*+-=?@^_?')
flag5 = input('Исключать ли неоднозначные символы il1Lo0O?').strip()
if flag1.lower() == 'д':
    chars += digits
if flag2.lower() == 'д':
    chars += uppercase_letters
if flag3.lower() == 'д':
    chars += lowercase_letters
if flag4.lower() == 'д':
    chars +=  punctuation
if flag5.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c , '')

while n!=0:
    print("Пароль  : " , end = ' ')
    print(generate_password(length,chars))
    n -= 1"""

#ШИФР ЦЕЗАРЯ
# Задаем четыре вопроса пользователю: шифр-дешифр, язык, шаг, текст.
# За каждым вопросом стоит while-проверка, что введенный ответ является корректным значением.
"""
whats_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()

whats_language = input('Какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input('Что-то не то ты ввёл. Напиши "русский" либо "английский". \n').lower()

whats_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Что-то не то ты ввёл. Напиши число. \n')

whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Что-то не то ты ввёл. Введи текст. \n')


# Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
def caesar(direction, language, step, text):
    # Четыре словаря под русские и английские символы, большие и маленькие.
    # В теории можно обойтись без них и обращаться к таблице Unicode.
    # Но мне было удобнее создать свои словари.

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Объявляем цикл for. Количество итераций равно длине строки text.
    for i in range(len(text)):

        # Задаем локальные переменные: длину алфавита и значения словарей.
        if language == 'русский':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == 'английский':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        # Если text[i] является буквой:
        if text[i].isalpha():

            # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            # Если нужно дешифровать, то:
            if direction == 'дешифровать':
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс - Шаг % Длина алфавита
                index = (place - int(step)) % alphas


            # Если нужно зашифровать, то:
            elif direction == 'шифровать':
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс + Шаг % Длина алфавита
                index = (place + int(step)) % alphas

            # Выводим измененный символ.
            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')

                # Если text[i] не является буквой:
        else:
            # Делаем print этого символа без изменений.
            print(text[i], end='')


# Вызываем функцию, передавая в аргументы четыре input`а из начала кода.
caesar(whats_direction, whats_language, whats_step, whats_text)"""

"""from random import choice

word_list = [
    'год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место',
    'вопрос', 'лицо', 'глаз', 'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова',
    'система', 'вид', 'конец', 'отношение', 'город', 'часть', 'женщина', 'проблема', 'земля',
    'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец', 'история', 'нога', 'вода',
    'война', 'возможность', 'компания', 'результат', 'дверь', 'народ', 'область', 'число',
    'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд', 'деньга',
    'уровень', 'начало', 'государство', 'стол', 'средство', 'связь', 'имя', 'президент', 'форма',
    'путь', 'организация', 'качество', 'действие', 'статья', 'общество', 'ситуация', 'деятельность',
    'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель',
    'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок', 'предприятие',
    'партия', 'роль', 'смысл', 'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр',
    'внимание', 'производство', 'квартира', 'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната',
    'семья', 'сын', 'смерть', 'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор',
    'окно', 'ответ', 'совет', 'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план',
    'проект', 'глава', 'материал', 'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль', 'наука',
    'документ', 'неделя', 'вещь', 'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'ход',
    'стена', 'директор', 'плечо', 'опыт', 'встреча', 'принцип', 'событие', 'структура', 'количество', 'товарищ',
    'создание', 'значение', 'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример',
    'лес', 'исследование', 'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат',
    'представитель', 'борьба', 'использование', 'шаг', 'игра', 'участие', 'территория', 'край', 'размер', 'номер',
    'район', 'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь',
    'направление', 'позиция', 'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик', 'фильм',
    'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт', 'церковь', 'завод', 'фирма',
    'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух', 'музыка',
    'способ', 'хозяин', 'поле', 'доллар', 'память', 'природа', 'дерево', 'оценка', 'объем', 'картина',
    'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант', 'берег',
    'модель', 'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол', 'зрение',
    'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство', 'солнце', 'автомобиль', 'родитель',
    'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'море', 'удар', 'знание',
    'солдат', 'миллион', 'строительство', 'технология', 'председатель', 'сон', 'сознание', 'бумага', 'реформа',
    'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок', 'услуга', 'поэт',
    'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет', 'представление',
    'площадь', 'генерал', 'господин', 'дочь', 'понятие', 'кабинет', 'безопасность', 'фонд', 'сфера', 'папа',
    'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика', 'сумма', 'контроль',
    'парень', 'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь', 'нос', 'волос', 'ухо',
    'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето', 'камень', 'здание',
    'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня', 'депутат', 'проведение',
    'рот', 'масса', 'комиссия', 'цвет', 'рассказ', 'функция', 'определение', 'мужик', 'обеспечение',
    'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение', 'победа', 'товар',
    'воля', 'зона', 'предел', 'целое', 'личность', 'офицер', 'влияние', 'поддержка', 'ответственность',
]


def get_word():
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [
        '''
        \|||/ 
        (o o)
----ooO--(_)---------
|                     |
|                     |
|      К О Н Е Ц      |
|                     |
|                     |
'---------------ooO---'
       |  |  | 
       |  |  | 
       |__|__| 
       /_'Y'_\  
      (__/ \__)  
        ''',
        '''
        \|||/ 
        (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 1 попытка |
|                     |
|                     |
'---------------ooO---'
       |  |  | 
       |  |  | 
       |__|__| 
       /_'Y'_\  
      (__/ \__)  
        ''',
        '''
        \|||/ 
  """ """     (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 2 попытки |
|                     |
|                     |
'---------------ooO---'
       |  |  |
       |  |  |
       |__|__|
       /_'Y'_\
      (__/ \__)
        ''',

        '''
        \|||/
        (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 3 попытки |
|                     |
|                     |
'---------------ooO---'
       |  |  |
       |  |  |
       |__|__|
       /_'Y'_\
      (__/ \__)
        ''',
        '''
        \|||/
        (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 4 попытки |
|                     |
|                     |
'---------------ooO---'
       |  |  |
       |  |  |
       |__|__|
       /_'Y'_\
      (__/ \__)
        ''',
        '''
        \|||/
        (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 5 попыток |
|                     |
|                     |
'---------------ooO---'
       |  |  |
       |  |  |
       |__|__|
       /_'Y'_\
      (__/ \__)
        ''',
        '''
        \|||/
        (o o)
----ooO--(_)---------
|                     |
|                     |
|  Осталось 6 попыток |
|                     |
|                     |
'---------------ooO---'
       |  |  |
       |  |  |
       |__|__|
       /_'Y'_\
      (__/ \__)
      '''
    ]
    return stages[tries]


def letter_finder(ltr, original_word, hidden_word):
    lst_index = []
    for i, letter in enumerate(original_word):
        if letter == ltr:
            lst_index.append(i)
    for i in lst_index:
        hidden_word[i] = ltr
    return hidden_word


def play(word):
    end = '- ' * 30
    pc_word = list(word)
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('\nДавайте играть в угадайку слов!')
    print('Загаданное слово состоит из', len(pc_word), 'букв')
    # print(pc_word)  # Выводит загаданное слово
    while True:
        easy_or_not = input('Чтобы было проще, хотите открыть первую и последнюю буквы? (да/нет) ')
        if easy_or_not.isalpha():
            if easy_or_not.lower() == 'да':
                word_completion[0] = pc_word[0]
                word_completion[-1] = pc_word[-1]
                break
            elif easy_or_not.lower() == 'нет':
                print('Ваш выбор, играем! =)')
                break
            else:
                print('Не понял, повторите...')
        else:
            print('Не понял, повторите...')

    while tries:
        if word_completion == pc_word:  # Проверка на случай угадывания слова по одной букве
            print('Ура! Вы выиграли!')
            break
        print(display_hangman(tries))
        print(end)
        print(*word_completion)
        user_letter = input('\nВведите букву или слово полностью: ').upper()
        if len(user_letter) == len(pc_word):  # Проверка на слово полностью
            if user_letter in guessed_words:
                print('Такое слово вы уже пробовали, это не оно!')
                continue
            guessed_words.append(user_letter.upper())
            if user_letter.upper() == ''.join(pc_word):  # Проверка на ввод слова полностью
                print('Ура! Вы выиграли!')
                break
        if not user_letter.isalpha():
            print('Вы что-то неправильно ввели!')
            continue
        elif user_letter in guessed_letters:
            print('Вы уже называли такую букву!')
            continue
        guessed_letters.append(user_letter)  # Добавляем букву в список уже названных букв
        if user_letter in pc_word:  # Если буква была угадана
            letter_finder(user_letter, pc_word, word_completion)
            tries -= 1
        else:
            print('Вы не угадали букву/слово!')
            tries -= 1
    print('Игра закончена!')
    print(display_hangman(0))
    print('Загаданное слово было:', *pc_word)
    return end


print(play(get_word()))

while True:
    repeat = input('Хотите сыграть ещё раз? (да/нет) ')
    if repeat.isalpha():
        if repeat.lower() == 'да':
            play(get_word())
        elif repeat.lower() == 'нет':
            print('Спасибо за игру! До встречи! =)', '* ' * 30, sep='\n')
            break
        else:
            print('Не понял, повторите')
    else:
      print('Не понял, повторите')"""