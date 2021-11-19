# 2 Курс по Stepik
# 1 решение
"""n = len(input()) * 60
n = str(n)
if len(n) <= 2:
    print(0,'р.',n[-2:],'коп.')
elif n[-2] == n[-1]:
    print(n[:-2], 'р.', n[-1], 'коп.')
else:
    print(n[:-2],'р.',n[-2:],'коп.')"""

"""n = len(input()) * 60
print(f'{n // 100} р. {n % 100} коп.')"""
# 1 решение
"""year_of = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
god = int(input())
print(year_of[god%12])"""

# 2 решение
"""year_of = [ "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц" , "Дракон", "Змея", "Лошадь", "Овца"]
god = int(input())
print(year_of[god%12 + 4])"""

# 1 решение
"""str = input()
if len(str) == 6:
    str1 = str[0]
    str1 += str[::-1]
    print(str1[:-1])
elif len(str) == 5:
    str = str[::-1]
    str = int(str)
    print(str)"""

# 2 решение
"""num = input()
if len(num) == 5:
    print(int(num[-1::-1]))
else:
    print(int(num[0] + num[-1:-6:-1]))"""

# разделяет число запятыми с помощью .format

"""amount = int(input())
print("{:,}".format(amount))"""

# второе решение, делает тоже самое что и .format

"""number = input()
for i in range(len(number)-3, 0, -3):
    number = number[:i] + ',' + number[i:]
print(number)"""

# 1
"""def funk(n,k):
    if n==1:
        return n
    if n > 1:
        return (funk(n-1,k) + k - 1)% n + 1

n = int(input())
k= int(input())
print(funk(n,k))"""

# 2
"""n = int(input())
k = int(input())

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)"""

"""n = int(input())
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(n):
    x, y = map(int, input().split()) # с помощью функции map() все используется к каждому элементу. То есть вводя строку (0 , 1) оно разделит на значения x и y.
    if x > 0 and y > 0:
        c1 += 1
    elif x < 0 and y > 0:
        c2 += 1
    elif x < 0 and y < 0:
        c3 += 1
    elif x > 0 and y < 0:
        c4 += 1
print("Первая четверть:",c1)
print("Вторая четверть:",c2)
print("Третья четверть:",c3)
print("Четвертая четверть:",c4)
"""

"""string = input().split()
new = []
new.append(string[-1])
for i in range(len(string)-1):
    new.append(string[i])
print(*new)"""

# 1 1 1 2 2 2 2 3 3 3
"""string = input().split()
summ = 0
for i in range(len(string)):
    string[i] = int(string[i])
for i in range(1,len(string)):
    if string[i] == string[i-1]:
        continue
    else:
        summ += 1
print(summ+1)"""

"""
n = int(input())
list = []
flag = False
for i in range(n):
    num = int(input())
    list.append(num)
multiplie = int(input())
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] * list[j] == multiplie:
            flag = True
            break

if flag == False:
    print('НЕТ')
elif flag == True:
    print('ДА')"""

"""timur = input()
ruslan = input()
m = {'к-к': 'ничья', 'к-н': 'Тимур', 'к-б': 'Руслан', 'н-н': 'ничья','н-б': 'Тимур', 'н-к': 'Руслан', "б-б": 'ничья','б-к': 'Тимур','б-н': 'Руслан'}
m1 = timur[0] + "-" + ruslan[0]
print(m[m1])"""

"""m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}
timur = input()
ruslan = input()
m1 = timur + "-" + ruslan
print(m[m1])"""

"""a, b = input()[0], input()[0]
print('ничья' if a == b else 'Тимур' if a + b in ('кн', 'бк', 'нб', 'кя', 'яС', 'Сн', 'ня', 'яб', 'бС', 'Ск') else 'Руслан')"""

"""string = input().split("О")
max_P = 0
for i in range(len(string)):
    if len(string[i]) > max_P:
        max_P = len(string[i])
print(max_P)"""
#0000a0000n00t00000o000000n
"""for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break    
"""
"""n = int(input())
list = []
for i in range(1,n+1):
    x = input()
    fl = x.find('a')
    sl = x.find('n',fl+1)
    tl = x.find('t',sl+1)
    fol = x.find('o',tl+1)
    fil = x.find('n',fol+1)
    if -1 < fl < sl < tl < fol < fil :
        list.append(i)
print(*list)
"""

"""word = input() + ' запретил букву '
b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(len(b)):
    print(word + b[i])
    word = word.replace(b[i],'')
    word = word.lstrip()
    if len(word) == 0:
        break"""

"""word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()"""

#Bool   and     or     not
"""print(17 > 7) << True
print(17 == 7) << False
print(17 < 7) << False"""

"""print(True + True + True - False) << 3
print(True + (False / True)) << 1"""

"""numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
res = 0
for num in numbers:
    res += (num % 2 == 0)
print(res)"""

#if flag == True:   =   if flag:       if flag == False:    =   if not flag
#Предикат
"""def is_even(num):
    return num % 2 == 0"""
#isinstance() проверка на тип данных обьекта
"""print(isinstance(3, int))
print(isinstance(3.5, float))
print(isinstance('Beegeek', str))
print(isinstance([1, 2, 3], list))
print(isinstance(True, bool))"""
#type() говорит тип данных
"""print(type(3))
print(type(3.5))
print(type('Beegeek'))
print(type([1, 2, 3]))
print(type(True))"""

#NoneType
"""var = None"""
"""var = None
if var is None:   # используем оператор is
  print('None')
else:
  print('Not None')"""

"""var = None
if var == None:  # используем оператор ==
    print('None')
else:
    print('Not None')"""

#.join()
"""words = ['Hello', 'Python']
print('-'.join(words)) << Hello-Python"""

#Вложеннные списки
"""my_list = [[0], [1, 2], [3, 4, 5]]
print(my_list[0]) << [0]
print(my_list[1]) << [1, 2]
print(my_list[2]) << [3, 4, 5]"""

"""my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]
print(my_list[0][2])       # индексирование строки 'Python'
print(my_list[1][1])       # индексирование списка [10, 20, 30]
print(my_list[2][-1])      # индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1][-1])  # индексирование строки 'Stepik!'"""

"""total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
for li in my_list:
    total += len(li)
print(total)"""

"""list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for li in list1:
    if max(li) > maximum:
        maximum = max(li)
print(maximum)"""

"""list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
list1[0].reverse()
list1[1].reverse()
list1[2].reverse()
list1[3].reverse()
list1[4].reverse()
print(list1)"""

"""list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for elem in list1:
    elem.reverse()
print(list1)"""

"""list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for elem in list1:
    counter += len(elem)
    total += sum(elem)
print(total / counter)"""

"""n, m = int(input()), int(input())    # считываем значения n и m
my_list = []
for _ in range(n):
    my_list.append([0] * m)
print(my_list)"""

"""n, m = int(input()), int(input())
my_list = [[0] * m ] * n
my_list[0][0] = 17
print(my_list)"""

"""n = 4                                          # количество строк (элементов)
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)"""

"""my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()   """

"""my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
    print()"""

"""my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
maximum = my_list[0][0]
minimum = my_list[0][0]
for row in my_list:
    maximum = max(row)
    minimum = min(row)
print(maximum + minimum)"""

"""n = int(input())
for i in range(1,n+1):
    ls = []
    for j in range(1,i+1):
        ls.append(j)
    print(ls)"""

"""n = int(input())
p  = []
for i in range(n):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = p[i-1][j-1] + p[i-1][j]

    p.append(row)

for r in p:
    print(r)"""

"""char_list = []
a = []
for char in input().split():
    if len(a) == 0:
        a.append(char)
    elif len(a) != 0:
        if a[-1] == char:
            a.append(char)
        elif a[-1] != char:
            char_list.append(a)
            a = []
            a.append(char)
if a:
    char_list.append(a)
print(char_list)"""

"""char_list = []
a = []
str = input().split()
n = int(input())
for i in range(0,len(str),n):
    for j in range(n):
        if str[i] != str[-1]:
            a.append(str[i+j])
        elif str[i] == str[-1]:
            a.append(str[i])
            break
    char_list.append(a)
    a = []
print(char_list)"""

"""def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())
print(chunked(symbols, n))"""

"""input_data = input().split()
output_data = [[]]
for i in range(len(input_data)):
    for j in range(len(input_data) - i):
        output_data.append(input_data[j:j + i + 1]) #str[i: i] добавит в список [['a']]
print(output_data)"""

#Matrix  ljust() rjust()
"""matrix  = [[2, -5, -11, 0],
           [-9, 4, 6, 13],
           [4, 7, 12, -2]]
print(matrix[1][2])"""

"""rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()"""

"""rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()"""

"""print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))"""

"""print('a'.ljust(3))
print('ab'.ljust(3))
print('abc'.ljust(3))"""

"""print('a'.rjust(3))
print('ab'.rjust(3))
print('abc'.rjust(3))"""

"""print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))"""

"""rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]
for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()"""

"""n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
for i in range(n):                     # заполняем главную диагональ 1-цами, а побочную 2-ками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2
for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()"""

"""def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
print_matrix(matrix, n)"""

"""n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)"""

"""rows = int(input())
colon = int(input())
matrix = []
for i in range(rows):
    row = []
    for j in range(colon):
        row.append(input())
    matrix.append(row)

for i in range(rows):
    for j in range(colon):
        print(matrix[i][j], end=' ')
    print()
print()
for i in range(colon):
    for j in range(rows):
        print(matrix[j][i], end=' ')
    print()"""

"""n, m = int(input()), int(input())
arr = [[input() for _ in range(m)] for _ in range(n)]
for row in arr:
    print(*row)
print()
for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')
    print()
"""
"""n = int(input())
matrix = []
total = 0
for _ in range(n):
    digits = input().split()
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    matrix.append(digits)
for i in range(n):
    total += matrix[i][i]
print(total)"""

"""n = int(input())
matrix, total = [], 0
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
for i in range(n):
    total += matrix[i][i]
print(total)"""

"""n = int(input())
sred = 0
for _ in range(n):
    count = 0
    row = [int(i) for i in input().split()]
    sred = sum(row)/len(row)
    for i in row:
        if sred < i:
            count += 1
    print(count)
"""

"""n = int(input())
fmax = -1000000
for i in range(1,n+1):
    row = [int(i) for i in input().split()]
    smax = max(row[0:i])
    if smax > fmax:
        fmax = smax
print(fmax)
"""

# создание матрицы
"""n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)"""

"""n = int(input())
fmax = -1000000
for i in range(1,n+1):
    row = [int(i) for i in input().split()]
    smax = max(row[0:i] + row[-i:])
    if smax > fmax:
        fmax = smax
print(fmax)"""

"""n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]

print(largest)"""
#1
"""n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

total1 = 0
total2 = 0
total3 = 0
total4 = 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            total1 += matrix[i][j]
        if i < j and i > n - 1 - j:
            total2 += matrix[i][j]
        if i > j and i < n - 1 - j:
            total3 += matrix[i][j]
        if i > j and i > n - 1 - j:
            total4 += matrix[i][j]
print('Верхняя четверть:',total1)
print('Правая четверть:',total2)
print('Нижняя четверть:',total4)
print('Левая четверть:',total3)"""
#2
"""n = int(input())
mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
print('Верхняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)]))
print('Правая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)]))
print('Нижняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)]))
print('Левая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)]))"""

"""n, m = int(input()), int(input())
arr = [[i*j for i in range(m)] for j in range(n)]
for i in arr:
    string = str(i)
    print(string.ljust(3))"""

"""n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        string = str(i*j)
        print(string.ljust(3), end = " ")
    print()"""

"""n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()"""
"""n, m = int(input()), int(input())
matrix = []
for i in range(n): #matrix = [[int(i) for i in input().split()] for _ in range(n)]  можно создать матрицу так.
    row = [int(i) for i in input().split()]
    matrix.append(row)
largest = matrix[0][0]
index_largest = "0 0"
for i in range(n):
    for j in range(m):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            index_largest = str(i) + " " + str(j)
print(index_largest)"""

"""n, m = int(input()), int(input())
matrix = [[i for i in input().split()]for _ in range(n)]
i,j = [int(i) for i in input().split()]

for ch in range(n):
    matrix[ch][i],matrix[ch][j] = matrix[ch][j],matrix[ch][i]
for i in matrix:
    print(*i)"""

"""n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
flag = 1
for i in range(n):
    for j in range(n):
        if matrix[i][j] == matrix[j][i]:
            continue
        else:
            flag = 0
            break
if flag == 1:
    print("YES")
elif flag == 0:
    print("NO")"""

"""n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    matrix[i][n-1-i],matrix[n-1-i][-i-1] = matrix[n-1-i][-i-1],matrix[i][n-1-i]

for i in matrix:
    print(*i)"""

"""n = int(input())
arr = []
for i in range(n):
    row = [int(i) for i in input().split()]
    arr.append(row)

for i in range(1,n+1):
    print(*arr[n-i])"""


"""def list_rot90(data, times=1):
    rot_data = []
    for t in range(times):
        m = len(data)
        n = len(data[0])
        rev_data = data[:: -1]
        rot_data = [[rev_data[j][i] for j in range(m)]
                    for i in range(n)];
        data = rot_data
    return rot_data


n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
rot_matrix = list_rot90(matrix)
for s in rot_matrix:
    print(*s)"""
"""n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)"""


"""matrix, n = [['.' for _ in range(8)]for _ in range(8)], 8
dot = input()
dot_x,dot_y = 8-int(dot[1]),ord(dot[0])-97
matrix[dot_x][dot_y] = "N"
for i in range(n):
    for j in range(n):
        if (i - dot_x) ** 2 + (j - dot_y) ** 2 == 5:
            matrix[i][j] = '*'
for i in matrix:
    print(*i,sep=' ')
"""

"""n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
flag = True
old = 0
for i in range(n):
    new = 0
    for j in range(n):
        if matrix[i][j] > n**2 or matrix[i][j] < 1:
            flag = False
            break
        elif matrix[i][j] <= n**2 and matrix[i][j] >= 1:
            new += matrix[i][j]


    if i != 0:
        if old != new:
            flag = False
        elif flag == False:
            break
    old = new
if flag == True:
    print("YES")
elif flag == False:
    print("NO")"""

"""def magic_mtrx(n, matrix):
    control = sum(matrix[0])                        # сумма чисел в линии
    for i in range(1, n):                           # проверка сумм по рядам
        if sum(matrix[i]) != control:
            return 'NO'
    lst = [i for i in range(1, n ** 2 + 1)]         # список всех чисел матрицы
    mtx = [[0] * n for _ in range(n)]               # поворачиваем матрицу по чс на 90 грд для удобства
    for r in range(n):
        for c in range(n):
            if matrix[r][c] in lst:                 # если элемент матрицы в списке
                del lst[lst.index(matrix[r][c])]    # удаляем его из списка
            else:
                return 'NO'
            mtx[c][n - r - 1] = matrix[r][c]
    for i in range(n):                              # аналогичная проверка повернутой матрицы
        if sum(mtx[i]) != control:
            return 'NO'
    return 'YES'

size = int(input())
mtrx = [list(map(int, input().split())) for i in range(size)]
print(magic_mtrx(size, mtrx))"""

"""ni,nj = [int(i) for i in input().split()]
matrix = []
for i in range(ni):
    row = []
    for j in range(nj):
        if (i+j) % 2 != 0:
            row.append('*')
        else:
            row.append('.')
    matrix.append(row)
for i in matrix:
    print(*i)"""

"""n = int(input())
matrix = [[int(0) * n for i in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ( i <= j and i > n - 1 - j) or (i > j and i >= n - 1 - j):
            matrix[i][j] = 2
for i in range(n):
    matrix[i][n - i - 1] = 1
for i in matrix:
    print(*i)"""

"""n,m = [int(i) for i in input().split()]
matrix = []
inch = 1
for i in range(n):
    for j in range(m):
        print(str(inch).ljust(3),end=" ")
        inch += 1
    print()"""

"""n, m = [int(i) for i in input().split()]
matrix = [[0]*m for i in range(n)]
inch = 1
for j in range(m):
    for i in range(n):  
        matrix[i][j] = inch
        inch += 1
for i in matrix:
    print(*i)"""

"""n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
            matrix[i][j] = 1
for i in matrix:
    print(*i)"""

"""n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
for j in range(m):
    for i in range(n):
        matrix[i][j] = (i + j) % m + 1

for i in matrix:
    print(*i)"""

"""n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
inch = 1
for j in range(n):
    for i in range(m):
        matrix[j][i] = inch
        inch += 1
i = 0
for j in matrix:
    if i % 2 == 1:
        print(*j[::-1])
    else:
        print(*j)
    i += 1"""

"""nm = input()
n = int(nm[0])
m = int(nm[2])
c = 1
l = 0
a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m+n-1):
    for j in range(n):
        if ((i-j) > -1) and ((i-j) < m):
            a[j][i-j]+=c
            l+=1
            c+=1
    l = 0
for i in a:
    print(*i)"""


"""n, m = [int(i) for i in input().split()]
matr1x = [[int(i) for i in input().split()] for i in range(n)]
p = input()
matr2x = [[int(i) for i in input().split()] for i in range(n)]

for i in range(n):
    for j in range(m):
        new = matr1x[i][j] + matr2x[i][j]
        matr1x[i][j] = new
for i in matr1x:
    print(*i)"""

"""n1, m1 = [int(i) for i in input().split()]
mat = [[int(i) for i in input().split()] for _ in range(n1)]
p = input()
n2, m2 = [int(i) for i in input().split()]
mat2 = [[int(i) for i in input().split()] for _ in range(n2)]
k = m1 = n2
matrix = [[0] * n1 for i in range(m2)]
row = []
a = 0
for i in range(n1):
    for j in range(m2):
        for x in range(k):
            a += (mat[i][x] * mat2[x][j])
        matrix[i][j] = a
        a = 0

for i in matrix:
    print(*i)"""

"""import numpy as np
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
step = int(input())
a = np.array(matrix)
result = np.linalg.matrix_power(a, step)
for i in result:
    print(*i)"""

"""a = input().split()
n = int(input())
list = []
for i in range(n):
    b = a[i::n]
    list.append(b)
print(list)"""


#экз(разобрать)
"""a = input().split()
n = int(input())
list = []
for i in range(n):
    b = a[i::n]
    list.append(b)


print(list)"""

"""def list_rot90(data, times=1):
    rot_data = []
    for t in range(times):
        m = len(data)
        n = len(data[0])
        rev_data = data[::]
        rot_data = [[rev_data[j][i] for j in range(m)]
                    for i in range(n)];
        data = rot_data
    return rot_data


n = int(input())
matrix = []
for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
rot_matrix = list_rot90(matrix)
for s in rot_matrix:
    print(*s)"""

"""n = int(input())
a = [["."] * n for i in range(n)]
for i in range(n):
    a[i][i] = "*"
    a[n - 1 - i][i] = "*"
    a[i][n//2] = "*"
    a[n//2][i] = "*"
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))"""

"""n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            flag = False
            break
print('YES' if flag else 'NO')
"""

"""n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break

print(result)"""

"""n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))"""

#Кортежи -  неизменяемые аналоги списков   tuple
"""empty_tuple = ()    """                                  # пустой кортеж
"""point = (1.5, 6.0)     """                               # кортеж из двух чисел
"""names = ('Timur', 'Ruslan', 'Roman') """                 # кортеж из трех строк
"""info = ('Timur', 'Guev', 28, 170, 60, False) """         # кортеж из 6 элементов разных типов
"""nested_tuple = (('one', 'two'), ['three', 'four'])"""    # кортеж из кортежа и списка

"""my_tuple = (1,)"""   #Для создания кортежа с единственным элементом после значения элемента ставят замыкающую запятую

"""def get_powers(num):
    return num**2, num**3, num**4
result = get_powers(5)
print(result)""" # (25, 125, 625)

"""my_tuple = (1, 'python', [1, 2, 3])
print(my_tuple)
my_tuple[2][0] = 100
my_tuple[2].append(17)
print(my_tuple)""" # Меняется список, а не кортеж.

# tuple()
"""number_tuple = (1, 2, 3, 4, 5)
number_list = list(number_tuple)
print(number_list)"""

"""str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)"""

"""text = 'hello python'
str_tuple = tuple(text)
print(str_tuple)"""

"""s = 'симпотичный'
print(s)
a = list(s)
a[4] = 'а'
s = ''.join(a)
print(s)"""

"""writer = ('Лев Толстой', 1827)
print(writer)
a = list(writer)
a[1] = 1828
writer = tuple(a)
print(writer)"""

"""numbers = (2, 4, 6, 8, 10)
if 2 in numbers:
    print('Кортеж numbers содержит число 2')
else:
    print('Кортеж numbers не содержит число 2')"""

"""tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
list_ = []
for i in range(len(tuples)):
    if len(tuples[i]) == 0 :
        continue
    else:
         list_.append(tuples[i])
non_empty_tuples = list_
print(non_empty_tuples)
"""

"""tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i]
print(non_empty_tuples)"""

"""tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
for i in range(len(tuples)):
    list_ = list(tuples[i])
    list_[-1] = 100
    list_ = tuple(list_)
    new_tuples.append(list_)
print(new_tuples)"""

"""numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in range(len(numbers)):
    print(numbers[i])"""

"""numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
languages = ('Python', 'C++', 'Java')
print(*numbers)
print(*languages, sep='\n')"""

#Сравнение кортежей
"""print((1, 8) == (1, 8))
print((1, 8) != (1, 10))
print((1, 9) < (1, 2))
print((2, 5) < (6,))
print(('a', 'bc') > ('a', 'de'))"""

# sotred()
"""not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)
sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)"""

"""poets = [
    ('Есенин', 13),
    ('Тургенев', 14),
    ('Маяковский', 28),
    ('Лермонтов', 20),
    ('Фет', 15)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])"""


"""import math
n = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
print(math.prod(n))"""

"""numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
total = 1
for i in numbers:
    total *= i
print(total)"""

"""numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
numbers = list(numbers)
for i in range(len(numbers)):
     numbers[i] = sum(numbers[i]) / len(numbers[i])
print(numbers)"""

"""n = int(input())
cort = []
all_list = []
for i in range(n):
    str = input()
    all_list.append(str)
    if int(str[-1]) >= 4:
        cort.append(str)
for i in all_list:
    print(i)
print()
for i in cort:
    print(i)"""

#Упаковка кортежей
"""tuple1 = (1, 2, 3)
tuple2 = ('b',)
tuple3 = ('red', 'green', 'blue', 'cyan')

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))"""

"""colors = ('red', 'green', 'blue', 'cyan')

(a, b, c, d) = colors
print(a)
print(b)
print(c)
print(d)"""

"""colors = ('red', 'green', 'blue')
a, b, _ = colors
print(a)
print(b)"""

"""#Последовательность Трабонначи
limit = int(input())
a = [1,1,1]
if limit <= 3:
    print('1 ' * limit)
    flag = False
else:
    flag = True
    for _ in range (limit-3):
        a.append(sum(a[-3:]))
if flag == True:
    print(*a)"""

"""print(dir(tuple))"""

#множества
"""n,m,k,x,y,z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
nx = n - x
mxy = m - x - y
ky = k - y
print(nx + mxy + ky + x + y + z)"""

"""n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
x1 = n + m - x - t
x2 = m + k - y - t
x3 = n + k - z - t
n1 = n - x1 - x3 - t
m1 = m - x2 - x3 - t
k1 = k - x1 - x2 - t
print(n1 + m1 + k1)
print(x1 + x2 + x3)
print(a - t - (n1 + m1 + k1) - (x1 + x2 + x3))"""

# Множества set()
"""myset = set()   """ # пустое множество

"""myset = set([1, 2, 2, 3, 4, 4, 4])
print(len(myset))"""

"""numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))
"""

"""numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
sorted_numbers = sorted(numbers)
print(*sorted_numbers, sep='\n')"""

"""numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
sortnumbers = sorted(numbers, reverse=True)
print(*sortnumbers, sep='\n')"""

"""
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
new_fruits = sorted(fruits, reverse = True)
print(*new_fruits, sep = '\n')
"""

"""print(len(set(input())))"""

"""old = input()
new = set(old)
if len(old) == len(new):
    print("YES")
else:
    print("NO")"""

"""n = input()
print('YES' if len(n) == len(set(n)) else 'NO')
"""

"""s1 = set(input())
s2 = set(input())
new = s1.union(s1,s2)
print('YES' if len(new) == 10 else "NO")"""

"""s1 = set(input())
s2 = set(input())
s1 = sorted(s1)
s2 = sorted(s2)
print("YES" if s1 == s2 else "NO")"""

"""print(['NO', 'YES'][set(input()) == set(input())])"""

"""s = input().split()
for i in range(len(s)):
    s[i] = sorted(s[i])
print("YES" if s[0] == s[1] == s[2] else "NO")"""

# add() remove() discard() pop() clear()
"""myset = set('python')

item = myset.pop()
print(item, len(myset))"""

"""n = int(input())
new = set()
for i in range(n):
    s = input().lower()
    for j in s:
        new.add(j)
print(len(new))"""
#Milk is white and so is glue, Ghosts are white and they say BOO!
"""import re

words = re.sub(r'[.,;:-?-!]', '', input().lower())
words = words.split()
for i in words:
    if words.count(i) > 1:
        print(i)
        count = words.count(i)
        for j in range(count-1):
            de = words.index(i)
            words.remove(words[de])
print(len(set(words)))"""

"""words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(len(set(words)))"""

"""values = [int(i) for i in input().split()]
sit = set()
for i in values:
    if i not in sit:
        sit.add(i)
        print("NO")
    elif i in sit:
        print("YES")"""

#methods of set
# 1
"""myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.union(myset2)
print(myset3)"""
# 2
"""myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 | myset2
print(myset3)"""

"""myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.intersection(myset2)
print(myset3)"""

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 & myset2
print(myset3)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.difference(myset2)
print(myset3)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 - myset2
print(myset3)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.symmetric_difference(myset2)
print(myset3)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 ^ myset2
print(myset3)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1.update(myset2)      # изменяем множество myset1
print(myset1)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 |= myset2
print(myset1)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1.intersection_update(myset2)      # изменяем множество myset1
print(myset1)'''

'''myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 &= myset2
print(myset1)'''

"""s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
print(len(s1 & s2))"""

"""s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s3 = sorted( s1 & s2 )
print(*s3)"""

"""s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
print(*(sorted(s1 - s2)))"""

"""ls = [list(input()) for _ in range(int(input()))]
print(*sorted(set(ls.pop()).intersection(*ls)))"""

# issubset()
#1
"""set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1.issubset(set2))"""
#2
"""set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1 <= set2)"""

"""set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'c', 'e'}
print(set1.issuperset(set2))"""
# set = { }
"""set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7}
set3 = {7, 8, 9}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
print(set2.isdisjoint(set3))"""

"""n1 = set(input())
n2 = set(input())
print(*["NO" if n1.isdisjoint(n2) else "YES"])"""

"""n1 = set(input())
s2 = set(input())
print(*["YES" if n1 & s2 == s2 else "NO"])"""

"""s1 = set(*[int(i) for i in input().split()])
s2 = set(*[int(i) for i in input().split()])
s3 = set(*[int(i) for i in input().split()])
print(*["YES" if s1 & s2 ])"""

"""s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
s3 = [int(i) for i in input().split()]

s12 = set(s1) & set(s2)
s123 = s12.difference(s3)
s123 = sorted(list(s123), reverse = True)
print(s123)
print(*s123)
"""

"""s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
s3 = [int(i) for i in input().split()]
_list = []
for i in range(len(s1)):
    if s1[i] in s2 and s1[i] not in s3:
        _list.append(s1[i])
    if s2[i] in s3 and s2[i] not in s1:
        _list.append(s2[i])
    if s3[i] in s1 and s3[i] not in s2:
        _list.append(s3[i])
    if s1[i] not in s2:
        _list.append(s1[i])
    if s2[i] not in s3:
        _list.append(s2[i])
    if s3[i] not in s1:
        _list.append(s3[i])
_list = set(_list)
print(*_list)"""

"""set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())
print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))"""

"""s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
s3 = [int(i) for i in input().split()]
print(*sorted((set(s3) - (set(s1)) - set(s2)), reverse = True))"""

"""values = {0,1,2,3,4,5,6,7,8,9,10}
s1 = set(int(i) for i in input().split())
s2 = set(int(i) for i in input().split())
s3 = set(int(i) for i in input().split())
values = values - s1 - s2 -s3
print(*sorted(list(values)))"""

"""items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
new_items = {int(i) for i in items}
print(*sorted(new_items))"""

"""words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
new = [i[0].lower() for i in words]
print(*sorted(set(new)))"""

"""import re
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
words = re.sub(r'[.,;:-?-!()]', '', sentence)
words = [word for word in words.split() if len(word) <= 4]
print(*sorted(set(word.lower() for word in words)))"""

"""files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
word = [i for i in files if i[-3:].lower() == 'png' ]
word = set([i.lower() for i in word])
print(*sorted(word))"""

#frozenset()
"""sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'
words = sentence.lower().replace('.', '').replace(',', '').split()
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
print(*consonants, sep='\n')"""

"""myset = {'Yellow', 'Orange', 'Black'}
myset.update(['Blue', 'Green', 'Red', 'Orange'])
print(myset)"""

"""n = int(input())
list_ = []
for i in range(n):
    list_.append(input())
list_ = set(list_)
new = [input()]
new = set(new)
if len(new & list_) >= 1:
    print("REPEAT")
else:
    print("OK")"""

"""set_set = {input() for _ in range(int(input()))}
print('REPEAT' if input() in set_set else 'OK')"""

"""m = int(input())
n = int(input())
s1 = {input() for _ in range(m)}
for i in range(n):
    x = input()
    if x in s1:
        print('YES')
    else:
        print('NO')"""

"""s1 = {int(i) for i in input().split()}
s2 = {int(i) for i in input().split()}
if s1 & s2:
    print(*sorted(s1 & s2, reverse = True))
else:
    print("BAD DAY")"""

"""m = int(input())
n = int(input())
s1 = {input() for _ in range(m)}
s2 = {input() for _ in range(n)}
x = len(s1 - s2) + len(s2 - s1)
if x >= 1 :
    print(x)
else:
    print("NO")"""

"""m = int(input())
n = int(input())
count = 0
s1 = {input() for _ in range(m)}
s2 = {input() for _ in range(n)}
s3 = len(s1 & s2) * 2
if m + n - s3 >= 1:
    print(m + n - s3)
else:
    print("NO")"""

# dict()
"""languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг', 
             'C++': 'Бьёрн Страуструп'}

print('Создателем языка C# является', languages['C#'])      =      print('Создателем языка C# является', languages['C' + '#']) """

"""dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')"""

"""info = {'name': 'Timur',
        'age': 28,
        'job': 'Teacher',
        'city': 'Moscow',
        'email': 'timyr-guev@yandex.ru'}

print(info['name'])
print(info['email'])"""

"""keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info = dict(zip(keys, values))
print(info)"""

"""my_dict = dict([('first', 1), ('second', 2), ('third', 3)])
print(my_dict)"""

"""my_dict = {198: 'beegeek', 'name': 'Bob', True: 'a', (2, 2): 25}
print(my_dict)"""

"""my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(max(my_dict) + min(my_dict))"""

"""capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key in capitals:
    print('Столица', key, '- это', capitals[key])"""

# Методы keys(), values(), items()
"""capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
    print(key)"""

"""capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
    print(value)"""

"""capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for item in capitals.items():
    print(item)"""

"""capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key, value in capitals.items():
    print(key, '-', value)"""

"""capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
for key in sorted(capitals):
    print(key)"""

"""users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

result = [user['name'] for user in users if user['phone'].endswith('8')]
print(*sorted(result))"""

"""users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

result = [user['name'] for user in users if 'email' not in user or user['email'] == '']
print(*sorted(result))"""

"""d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

n = input()
for i in n:
    print(d[int(i)], end = " ")"""

"""d = {
    "CS101": "CS101: 3004, Хайнс, 8:00",
    "CS102": "CS102: 4501, Альварадо, 9:00",
    "CS103": "CS103: 6755, Рич, 10:00",
    "NT110": "NT110: 1244, Берк, 11:00",
    "CM241": "CM241: 1411, Ли, 13:00"
}
key = input()
print(d[key])"""


"""d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0'
}
result = ""
str = input().upper()
for i in str:
    if i in d:
        result += d[i]
    else:
        continue
print(result)"""

"""letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
info = dict(zip(letters, morse))
str = input().upper()
for i in str:
    if i in info:
        print(info[i], end = " ")
    else:
        continue"""

#1
"""numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1"""
#2
"""numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
"""
# get()
"""info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

item1 = info.get('salary')
item2 = info.get('salary', 'Информации о зарплате нет')"""

# update()
"""info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}

info1.update(info2)"""

# setdefault()
"""info = {'name': 'Bob',
        'age': 25}

name1 = info.setdefault('name')           # параметр default не задан           
name2 = info.setdefault('name', 'Max')    # параметр default задан
print(name1)    #Bob
print(name2)    #Bob"""


"""info = {'name': 'Bob',
        'age': 25}

job = info.setdefault('job', 'Dev')
print(info)
print(job)"""

#del()  pop()   popitem()   clear()
"""info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

del info['email']    # удаляем элемент имеющий ключ email
del info['job']      # удаляем элемент имеющий ключ job"""


"""info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
print(email)
print(job)
print(info)"""

"""info = {'name': 'Bob',          #popitem удаляет последний добавленный элемент
     'age': 25,
     'job': 'Dev'}

info['surname'] = 'Sinclar'
item = info.popitem()
print(item)
print(info)"""

"""info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info.clear()
print(info)"""

"""info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info_copy = info.copy()
print(info_copy)"""

"""info = {'name': 'Bob',          # Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной.
        'age': 25,
        'job': 'Dev'}

new_info = info
new_info['name'] = 'Tim'
print(info)"""

"""num = int(input())

if num == 1:
    description = 'One'
elif num == 2:
    description = 'Two'
elif num == 3:
    description = 'Three'
else:
    description = 'Unknown'
print(description)"""

"""num = int(input())

description = {1: 'One', 2: 'Two', 3: 'Three'}
print(description.get(num, 'Unknown'))"""

"""result = {i : int(i**2) for i in range(1, 16)}
print(result)"""
#{i for i in dict1 if i in (dict1 and dict2)}
#1
"""dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
result.update(dict1)
result.update(dict2)
for i in result:
     if i in dict2 and i in dict1:
          result[i] = dict1[i] + dict2[i]
     else:
          continue
print(result)"""
#2
"""dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value"""

#1
"""text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
s_text = sorted(set(text))
result = {}
for i in s_text:
     count = text.count(i)
     result[i] = count
print(result)"""
#2
"""text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for c in text:
    result[c] = result.get(c, 0) + 1"""

"""pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0])"""

"""s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
result = {}
for i in s:
     result[i] = result.get(i, 0) + 1
max_digit = max(result.values())   #values   keys
spis = []
for i, j in result.items():
     if j == max_digit:
          spis.append(i)
spis = sorted(spis)
print(spis[0])"""


#удаление ненужных символов
"""import re
str = re.sub(r'[.,;:-?-!]', '', input()).lower().split()
dic = {}
for i in str:
     dic[i] = dic.get(i, 0) + 1
min_ = min(dic.values())
l = []
for i,j in dic.items():
     if j == min_ :
          l.append(i)
l = sorted(l)
print(l[0])"""

"""lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1"""

"""n = int(input())
dic = {}
for _ in range(n):
    str = input().split(':')
    dic[str[0].lower()] = str[1]
n = int(input())
for i in range(n):
    s = input().lower()
    if s in dic.keys():
        print(dic[s].lstrip())
    else:
        print("Не найдено".lstrip())"""
# 1
"""s1 = input()
s = {}
s2 = input()
s_ = {}
for i in s1:
    s[i] = s.get(i, 0) + 1
for i in s2:
    s_[i] = s_.get(i, 0) + 1
if s == s_:
    print("YES")
else:
    print("NO")"""
# 2
"""print('YES' if sorted(input()) == sorted(input()) else 'NO')"""

# 1
"""import re
str1 =  re.sub(r'[.,;:-?-!]', '', input()).lower().split()
d1 = {}
for i in str1:
    for j in i:
        d1[j] = d1.get(j, 0) + 1
str2 =  re.sub(r'[.,;:-?-!]', '', input()).lower().split()
d2 = {}
for i in str2:
    for j in i:
        d2[j] = d2.get(j, 0) + 1
if d1 == d2:
    print("YES")
else:
    print("NO")
"""
# 2
"""def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res


print(("NO", "YES")[s(input()) == s(input())])"""

"""d = {}
d1 = {}
for i in range(int(input())):
    s = input().split()
    d[s[0]] = s[1]
    d1[s[1]] = s[0]
poisk = input()
if poisk in d:
    print(d[poisk])
elif poisk in d1:
    print(d1[poisk])"""

# 1
"""d = {}
for i in range(int(input())):
    s = input().split()
    d[s[0]] = s[1:]
for i in range(int(input())):
    s = input()
    for k,v in d.items():
        if s in v:
            print(k)"""
# 2
"""d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    for c in cities:
        d[c] = country
for _ in range(int(input())):
    print(d[input()])"""

# 1
"""d = {}
for i in range(int(input())):
    num, name = input().lower().split()
    if name not in d:
        d[name] = [num]
    elif name in d:
        d[name] += [num]

for i in range(int(input())):
    s = input().lower()
    if s not in d:
        print("абонент не найден")
    elif s in d:
        print(*d[s])"""

# 2
"""dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))"""

# 1
"""dict_alpha = {}
shifr = input()
for i in range(int(input())):
    v, k = input().split(': ')
    dict_alpha[int(k)] = v
for i in shifr:
    print(dict_alpha[shifr.count(i)], end='')"""
# 2
"""s = input()
for i in range(int(input())):
    sym, count = input().split(": ")
    for i in s:
        if s.count(i) == int(count):
            s = s.replace(i, sym)
            break
print(s)"""

# Вложенные словари, генераторы словарей
"""info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
    print()"""

"""squares = {}
for i in range(6):
    squares[i] = i**2"""

"""squares = {i: i**2 for i in range(6)}"""

"""dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]

dict2 = {k: dict1[k] for k in selected_keys}
print(dict2)"""

"""squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(squares)"""

"""squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}

for value in squares.values():
    print(value)"""

"""numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i] ** 2 for i in range(len(numbers))}"""

"""favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
result = {i : favorite_numbers[i] for i in favorite_numbers if len(str(favorite_numbers[i])) == 2}"""

# 1
"""s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
s = s.split()
result = {}
for i in s:
    i = i.split(":")
    result[int(i[0])] = i[1]
print(result)"""

# 2
"""s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(k):v for k, v in [l.split(':') for l in s.split()]}"""

# ASCII
"""words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {i : [ord(j) for j in i] for i in words}"""

# 1
"""result = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
for i in remove_keys:
    del result[i]"""

# 2
"""letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {key: letters[key] for key in (set(letters) - set(remove_keys))}"""

"""students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

result = {i : students[i]  for i in students if students[i][0] > 167 and students[i][1] < 75}   #result = {name: inf for name, inf in students.items() if inf[0] > 167 and inf[1] < 75}"""


"""tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

result = {i[0] : i[1:] for i in tuples}"""

"""student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
result = [{student_ids[i] : {student_names[i] : student_grades[i]}} for i in range(len(student_grades))]
print(result)"""
#result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]
"""my = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = { key : [i for i in value if i <= 20] for key, value in my.items()}"""

"""emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
list  = [[j+"@"+i for j in k] for i,k in emails.items()]
new_list = []
for i in list:
    for j in i:
        new_list.append(j)
new_list = sorted(new_list)
for i in new_list:
    print(i)"""

"""rnk = {"G" : "C",
       "C" : "G",
       "T" : "A",
       "A" : "U"}
str = input()
new = ""
for i in str:
    new += rnk[i]
print(new)"""

# 1
"""str = input().split()
d = {}
for i in str:
    if i in d:
        print(d[i], end = " ")
    else:
        print(1, end = " ")
    d[i] = d.get(i, 0) + 1"""

# 2
"""s = input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
    print(d[i], end = ' ')"""

# 1
"""d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
res = 0
str = input()
for i in str:
    for k,v in d.items():
        if i in v:
            res += k

print(res)"""

# 2
"""d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

print(sum([k for i in input() for k, v in d.items() if i in v]))"""

"""database = {}
for _ in range(int(input())):
    name, good, amount = input().split()
    database[name][good] = database.setdefault(name, {}).get(good, 0) + int(amount)
for k, v in database.items():
    print(k + ":")
    for i, j in v.items():
        print(str(i) , str(j))"""

"""def build_query_string(params):
    count = 0
    stri = ""
    for k, v in sorted(params.items()):
        count += 1
        stri += str(k) + "="
        if count == len(params):
            stri += str(v)
        else:
            stri += str(v) + "&"
    return stri"""

"""def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res"""

"""transform = {'execute': 'X', 'write': 'W', 'read': 'R'}
mydict = {}

for _ in range(int(input())):
    name, *operations = input().split()
    mydict[name] = operations

for _ in range(int(input())):
    operation, name = input().split()
    if transform[operation] in mydict[name]:
        print('OK')
    else:
        print('Access denied')"""

#random
"""import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
for _ in range(10):
    print(random.randint(1, 100))"""

# 1
"""import random

n = int(input())
for _ in range(n):
    if random.randint(0, 1):
        print("Орел")
    else:
        print("Решка")"""

# 2
"""from random import randint

COIN = ['Орел', 'Решка']

for _ in range(int(input())):
    print(COIN[randint(0, 1)])"""


"""import random

s = set()
while len(s) < 7:
    s.add(random.randint(1, 49))
print(*sorted(s))"""

#shuffle()  choice()    sample()    module string

"""import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)"""

# 1
"""import random
def generate_ip():
    string = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    return string"""
# 2
"""from random import randrange as r

def generate_ip():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'
"""

"""from random import randrange as r
def generate_index():
    vars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return f'{vars[r(len(vars) - 1)]}{vars[r(len(vars) - 1)]}{r(100)}_{r(100)}{vars[r(len(vars) - 1)]}{vars[r(len(vars) - 1)]}'"""



"""from random import choice, randint
from string import ascii_uppercase as letter

def generate_index():
    return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'"""


"""from random import shuffle
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for i in matrix:
    shuffle(i)"""

# 1
"""from random import randint as r
s = set()
while len(s) != 100:
    s.add(r(1000000, 9999999))

print(*s, sep = "\n")"""
# 2
"""import random
print(*random.sample(range(1000000, 10000000), 100), sep='\n')"""

"""import random
string = list(input())
print(*random.sample(string, len(string)), sep = "")"""

# ljust()
# 1
"""import random
chars = list(range(1,75))

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            x = str(0)
            print(x.ljust(3), end = "")
        else:
            x = str(random.choice(chars))
            chars.remove(int(x))
            print(x.ljust(3), end="")

    print()"""

# 2
"""from random import sample
numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()
"""


"""from random import choice as r

p = [input() for _ in range(int(input()))]
f = set(p)
for s in p:
    c = r(list(f - {s}))
    print(s + ' - ' + c)
    f -= {c}"""

# 1
"""import random
digits = '23456789'
lowercase_letters = 'abcdefghijkmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
al = digits + lowercase_letters + uppercase_letters
con = int(input())
length = int(input())

for _ in range(con):
    result = ""
    for i in range(length):
        result += str(random.choice(al))
    print(result)"""

# 2
"""from string import *
from random import sample

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    return ''.join(sample(LETTER, length))

def generate_passwords(count, length):    
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')"""

# 1
"""from string import *
import random

letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
ups = ''.join(set(ascii_uppercase) - set('IO'))
los = ''.join(set(ascii_lowercase) - set('lo'))
dig = '23456789'

def generate_password(length):
    result = ""
    if dig not in result:
        result += str(random.choice(dig))
    if ups not in result:
        result += str(random.choice(ups))
    if los not in result:
        result += str(random.choice(los))
    while len(result) != length:
        result += str(random.choice(letter))
    print(result)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n , m =int(input()), int(input())
generate_passwords(n, m)"""

# 2
"""import string, random


def generate_password(length):
    symbols = ([x for x in string.ascii_uppercase if x not in 'OI'],
               [x for x in string.ascii_lowercase if x not in 'ol'],
               [x for x in string.digits[2:]])

    password = [random.choice(symbols[i]) for i in range(3)]
    password += random.sample(''.join([''.join(symbols[i]) for i in range(3)]), length - 3)
    random.shuffle(password)

    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')"""

#Метод Монте-Карло

"""import random

n = 10**6       # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1
print((k/n)*s0)"""

# болотная сортировка
"""import random
def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)"""

# module decimal    as_tuple()      get.context().prec      quantize()
"""from decimal import *

d1 = Decimal(1)
d2 = Decimal(567)
d3 = Decimal(-93)
d4 = Decimal('12345')
d5 = Decimal('52.198')
print(d1, d2, d3, d4, d5, sep='\n')"""

#Не рекомендуется создавать Decimal числа из float чисел. В Decimal попадет уже неправильно округленное число. Создавать Decimal числа нужно из целых чисел, либо из строк!
"""from decimal import *

num1 = Decimal('-1.4568769017')
num2 = Decimal('0.523')

print(num1.as_tuple())
print(num2.as_tuple())"""

"""from decimal import *
num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num_tuple.sign)
print(num_tuple.digits)
print(num_tuple.exponent)"""

"""from decimal import *

getcontext().prec = 3      # устанавливаем точность в 3 знака

num = Decimal('3.1415')
print(num)
print(num * 1)
print(num * 2)
print(num / 2)"""

"""from decimal import *

getcontext().prec = 4                    # устанавливаем точность числа

num = Decimal('3.1415926535')

print(num.quantize(Decimal('1.000')))    #  округление до 3 цифр в дробной части  
print(num.quantize(Decimal('1.00')))     #  округление до 2 цифр в дробной части
print(num.quantize(Decimal('1.0')))      #  округление до 1 цифр в дробной части"""

# quantize()
# ROUND_CEILING – округление в направлении бесконечности (Infinity);
# ROUND_FLOOR – округляет в направлении минус бесконечности (- Infinity)
# ROUND_DOWN – округление в направлении нуля;
# ROUND_HALF_EVEN – округление до ближайшего четного числа, число 6.9 округлится не до 7, а до 6;
# ROUND_HALF_DOWN – округление до ближайшего нуля;
# ROUND_UP – округление от нуля;
# ROUND_05UP – округление от нуля (если последняя цифра после округления до нуля была бы 0 или 5, в противном случае к нулю).

"""from decimal import *

s = '1.34 3.45 1.00 0.03 9.25'

numbers = [Decimal(i) for i in s.split()]

maximum = max(numbers)
minimum = min(numbers)
numbers.sort()
print(maximum)
print(minimum)
print(numbers)"""

"""from decimal import *
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
ls = [Decimal(i) for i in s.split()]
print(max(ls) + min(ls))"""

"""from decimal import *
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
ls = [Decimal(i) for i in s.split()]
print(sum(ls))
for _ in range(5):
    print(max(ls), end = " ")
    ls.remove(max(ls))"""

# 1
"""from decimal import *
x = input()
z = Decimal(x)
z_tuple = z.as_tuple()
if '0' in x:
    print(max(z_tuple.digits) + Decimal(0))
else:
    print(max(z_tuple.digits) + min(z_tuple.digits))"""
# 2
"""from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()
print(min(num_tuple.digits) + max(num_tuple.digits))"""

#методы Decimal()
"""from decimal import *
x = Decimal(input())
print(x.sqrt() + x.log10() + x.ln() + x.exp())"""

#module fraction()
"""from fractions import Fraction

num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')

print(num1, num2, num3, sep='\n')"""
# Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число. Создавать Fraction числа нужно из целых чисел, либо из строк!

# numerator denominator
"""from fractions import Fraction

num = Fraction('5/16')

print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)"""

# as_integer_ratio()
"""from fractions import Fraction

num = Fraction('-5/16')

print(num.as_integer_ratio())"""

"""from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for i in numbers:
    print(i,"=",Fraction(i))"""
    #print(f'{num} = {Fraction(num)}')

"""from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
w = [Fraction(i) for i in s.split()]
print(max(w) + min(w))"""

"""from fractions import Fraction as F
print(F(int(input()), int(input())))"""

"""from fractions import Fraction as F
x = input()
y = input()
s1 = F(x)
s2 = F(y)
print(x,"+",y,"=",s1+s2)
print(x,"-",y,"=",s1-s2)
print(x,"*",y,"=",s1*s2)
print(x,"/",y,"=",s1/s2)"""

"""from fractions import Fraction as F
n = int(input())
sum = 0

for i in range(1,n+1):
    sum += F(1, i**2)
print(sum)"""

"""from fractions import Fraction as F
from math import factorial as f
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += F(1, f(i))
print(sum)"""

"""from fractions import Fraction as F

n = int(input())
i = n // 2
while F(i, n - i).numerator != i:
    i -= 1
print(f'{i}/{n - i}')"""

# model complex()
"""z = 1 + 1j
print(z**3 + z**2 + z + 1)"""

"""z1 = -3 + 2j              # создание на основе литерала
z2 = complex(6, -8)       # z2 = 6 - 8j
z3 = complex(0, 2.5)      # z3 = 2.5j
z4 = complex(5, 0)        # z4 = 5 + 0j
z5 = complex('3+4j')      # создание на основе строки

print(z1, z2, z3, z4, z5, sep='\n')"""

# real  imag

"""z = 3+4j

print('Действительная часть =', z.real)
print('Мнимая часть =', z.imag)"""
# conjugate()

"""z = 3+4j
print('Сопряженное число =', z.conjugate())"""

# abs()
"""z = 3+4j
print('Модуль числа =', abs(z))"""

# cmath
"""import cmath
z = 2+3j
print(cmath.phase(z)) # полярный угол
print(cmath.polar(z)) # полярные координаты"""

# 1
"""z = complex(input())
z2 = complex(input())
print(f'{z} + {z2} = {z + z2}')
print(f'{z} - {z2} = {z - z2}')
print(f'{z} * {z2} = {z * z2}')"""

# 2
#eval()
"""a = input()
b = input()
for i in "+-*":
    print(f"({a}) {i} ({b}) =",  eval(f"({a}){i}({b})"))"""

# 1
"""numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
max = -1000
max_mod = -1000
for i in numbers:
    if abs(i) > max_mod:
        max_mod = abs(i)
        max = i
print(max)
print(max_mod)"""

# 2
"""numbers = [3+4j, 3+1j, -7+3j, 4+8j, -8+10j, -3+2j, 3-2j, -9+9j, -1-1j, -1-10j, -20+15j, -21+1j, 1j, -3+8j, 4-6j, 8+2j, 2+3j]

print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))"""

# 3
"""numbers = [3+4j, 3+1j, -7+3j, 4+8j, -8+10j, -3+2j, 3-2j, -9+9j, -1-1j, -1-10j, -20+15j, -21+1j, 1j, -3+8j, 4-6j, 8+2j, 2+3j]

largest = max((abs(i), i) for i in numbers)
print(largest[1], largest[0], sep='\n')"""

"""
n = int(input())
z1 , z2 = complex(input()), complex(input())
print((z1 ** n) + (z2 ** n) + (z1.conjugate() ** (n)) + (z2.conjugate() ** (n + 1)))
"""

#modul turtle
"""import turtle
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)"""

"""import turtle

turtle.shape('square')
turtle.forward(100)
turtle.setheading(90)

turtle.shape('arrow')
turtle.forward(100)
turtle.setheading(180)

turtle.shape('turtle')
turtle.forward(100)
turtle.setheading(270)

turtle.shape('circle')
turtle.forward(100)"""

"""import turtle
def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

for _ in range(8):
    turtle.left(45)
    square(120)"""

"""import turtle as t
from random import choice


def rhomb(side):
    colors = ['green', 'red', 'blue', 'orange', 'black', 'cyan', 'purple', 'magenta', 'yellow', 'brown']
    t.color(choice(colors))
    for i in [60, 120] * 2:
        t.backward(side)
        t.left(i)

def snowflake(side, count = 10):
    for _ in range(count):
        rhomb(side)
        t.right(360 / count)

t.pensize(2)
# rhomb(150)
snowflake(50) # вторым параметром можно передать количество
t.done()"""

"""import turtle as t
t.left(90)

def sq(n):
  for _ in range(4):
    t.forward(n)
    t.left(90)

c = 20
for i in range(15):
  sq(c)
  c +=5"""

"""import turtle as t
import math
def spiral(segment, count, a=90):
    for i in range(1, count):
        angle = a * i
        length = segment * math.ceil(i / 2)
        t.setheading(angle)
        t.forward(length)
t.speed(100)
t.pensize(2)
segment =3
turns = 150
angle = 75
print("segment=",segment, "turns=", turns, "angle=", angle )
spiral(segment, turns, angle)
t.done()"""

"""import turtle as t
import random

t.Screen().setup(640, 480)
t.shape('triangle')
t.Screen().bgcolor('black')
t.speed(1000)
t.pensize(3)
t.penup()
s = 40
for _ in range(600):
    t.pencolor(('blue', 'DarkOrchid', 'DeepSkyBlue', 'goldenrod', 'PaleGreen')[random.randint(0, 4)])
    t.stamp()
    t.right(152)
    t.forward(s)
    s += 0.5"""

"""import turtle
turtle.Screen().bgcolor('blue')
moon = turtle.Turtle()
moon.hideturtle()
moon.pencolor('orange')
moon.dot(200)
shadow = {0: turtle.Turtle(), 5: turtle.Turtle()}
for i in [0, 5]:
  shadow[i].hideturtle()
  shadow[i].pencolor('blue')
  shadow[i].penup()
while 1:
  for i in range(200, -201, -5):
    shadow[i % 10].goto(i, 0)
    shadow[i % 10].dot(200)
    shadow[(i + 5) % 10].clear()"""


"""
from turtle import *
from random import randint

ZOOM = 0.6
PITCH = 18
planets = (('Солнце', 1390, 'yellow'),
           ('Меркурий', 4.8794, '#8A8784'),
           ('Венера', 12.1036, '#D08824'),
           ('Земля', 12.742, '#6082CA'),
           ('Марс', 6.78, '#BF9A76'),
           ('Юпитер', 139.822, '#BAB9C3'),
           ('Сатурн', 116.464, '#D9AB47'),
           ('Уран', 50.724, '#60BDEE'),
           ('Нептун', 49.244, '#4C6DED'),
           ('Плутон', 2.3766, '#5B5D5A'))

def ellipse(rad):
    for i in range(2):
        circle(rad - 90, 90)
        circle(rad // 2 - 90, 90)

Screen().setup(1000, 400)
Screen().colormode(255)
Screen().bgcolor('black')
speed(0)
ht()
x = -2050
pencolor('white')
penup()
goto(77, -70)
pendown()
ellipse(220)
for _ in range(50):
    penup()
    goto(randint(0, 999) - 500, randint(0, 399) - 200)
    pendown()
    circle(0.5)
for p in planets:
    penup()
    x += p[1] * ZOOM + PITCH
    goto(x, -p[1] * ZOOM)
    pendown()
    fillcolor(p[2])
    pencolor(p[2])
    begin_fill()
    circle(p[1] * ZOOM)
    end_fill()
    penup()
    goto(x, -p[1] * ZOOM - PITCH)
    pendown()
    pencolor('white')
    write(p[0], move=False, align='center', font=('Arial', 8, 'normal'))
    x += p[1] * ZOOM + PITCH
done()"""

"""from turtle import *
from random import *
speed(0)
def stars(size, count, colo, x,y):
  for i in range(count):
    h = tuple(randint(0, 255) for _ in '123')
    size = randint(3,33)
    fillcolor(h)
    color(h)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
      forward(size)
      left(144)
    end_fill()
size = randint(10,20)
count = randint(50,80)
h = tuple(randint(0, 255) for _ in '123')

def left_mouse_click(x, y):
    stars(1,1,h,x, y)
hideturtle()
Screen().bgcolor('black')
Screen().onclick(left_mouse_click)
Screen().listen()"""

# поз. аргументы    именованые аргументы    необязательные аргументы
"""def diff(x, y):
    return x - y
res = diff(10, 3)    # используем позиционные аргументы
print(res)"""

"""def diff(x, y):
    return x - y
res = diff(x=10, y=3)   # используем именованные аргументы
print(res)"""

#Мы можем вызывать функции, используя именованные и позиционные аргументы одновременно. Но позиционные значения должны быть указаны до любых именованных!
#атрибут __defaults__
"""def append(element, seq=[]):
    seq.append(element)
    return seq

print('Значение по умолчанию', append.__defaults__)
print(append(10))
print('Значение по умолчанию', append.__defaults__)
print(append(5))
print('Значение по умолчанию', append.__defaults__)
print(append(1))
print('Значение по умолчанию', append.__defaults__)"""

# 1
"""def matrix(n = 1, m = None, value = 0):
    if m is None:
        m = n
        x = [[value for i in range(m)] for j in range (n)]
    else:
        x = [[value for i in range(m)] for j in range(n)]
    return x"""
# 2
"""def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]"""

# *args     **kwargs
"""def my_func(*args):
    print(type(args))
    print(args)

my_func()
my_func(1, 2, 3)
my_func('a', 'b')"""

"""def my_sum(*args):
    return sum(args)    # args - это кортеж

print(my_sum(*[1, 2, 3, 4, 5]))   #  распаковка списка
print(my_sum(*(1, 2, 3)))  """       #  распаковка кортежа

"""def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    
my_func()
my_func(a=1, b=2)
my_func(name='Timur', job='Teacher')"""

"""def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)

my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, 3, 4, job='Teacher', language='Python')"""

"""def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    
info = {'name':'Timur', 'age':'28', 'job':'teacher'}
my_func(**info)"""

"""def print_info(name, surname, age, city, *children, **additional_info):
    print('Имя:', name)
    print('Фамилия:', surname)
    print('Возраст:', age)
    print('Город проживания:', city)
    if len(children) > 0:
        print('Дети:', ', '.join(children))
    if len(additional_info) > 0:
        print(additional_info)
    
children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
additional_info = {'height':163, 'job':'actress'}

print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)"""

"""def make_circle(x, y, radius, *, line_width=1, fill=True):
    print(x,y,radius,line_width,fill)
#Здесь * выступает разделителем: отделяет обычные аргументы (их можно указывать по имени и позиционно) от строго именованных.
make_circle(10, 20, 5)                                     # x=10, y=20, radius=5,  line_width=1, fill=True
make_circle(x=10, y=20, radius=7)                          # x=10, y=20, radius=7,  line_width=1, fill=True
make_circle(10, 20, radius=10, line_width=2, fill=False)   # x=10, y=20, radius=10, line_width=2, fill=False
make_circle(x=10, y=20, radius=17, line_width=3)           # x=10, y=20, radius=17, line_width=3, fill=True"""

# Мы также можем объявить функцию, у которой будут только строго именованные аргументы, для этого нужно поставить * в самом начале перечня аргументов.
"""def make_circle(*, x, y, radius, line_width=1, fill=True):"""

"""def sq_sum(*args):
    return sum([i**2 for i in args])"""

# type()
"""def mean(*args):
    s = [i for i in args if type(i) in (int, float)]
    if len(s) > 0:
        return sum(s)/len(s)
    else:
        return 0.0
"""

# 1
"""def greet(name ,*args):
    if len(args) > 0:
        s = f'Hello, {name} and {" and ".join(args)} !'
        return s
    else:
        s = f'Hello, {name}!'
        return s"""
# 2
"""def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'"""

# 1
"""def print_products(*args):
    s = [i for i in args if type(i) is str and len(i) >= 1]
    if len(s) > 0:
        for i in range(1, len(s) + 1):
            print(f'{i}) {s[i-1]}')
    else:
        print("Нет продуктов")"""

# 2
"""def print_products(*args):
    cnt = 0
    for e in args:
        if type(e) == str and e:
            cnt += 1
            print(f'{cnt}) {e}')
    if cnt == 0:
        print('Нет продуктов')"""

# keys values in kwargs
"""def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')"""

# Парадигмы программирования
# Функции как обьекты
"""def hello():
    print('Hello from function')
func = hello     #  присваиваем переменной func функцию hello
func()           #  вызываем функцию"""


"""def start():
    # тело функции start

def stop():
    # тело функции stop

def pause():
    # тело функции pause

commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
command = input()        # считываем название команды
commands[command]()      # вызываем нужную функцию через словарь по ключу"""

#Функции, способные в качестве аргумента принимать или/и возвращать другие функции, называются функциями высшего порядка.

#key()
"""numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers, key=abs))        #  указываем функцию abs в качестве компаратора
print(min(numbers, key=abs))        #  указываем функцию abs в качестве компаратора
print(sorted(numbers, key=abs))     #  указываем функцию abs в качестве компаратора"""


"""def compare_by_second(point):
    return point[1]

def compare_by_sum(point):
    return point[0] + point[1]

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа"""


"""def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom

f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))"""


"""def comparator(item):
    return item[0]

data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
data.sort(key=comparator)   # сортируем по первому полю

print(data)"""

"""def f1(x):
    return 2*x+1
def f2(x):
    return x**2
def f3(x):
    return -x**2+1
def f4(x):
    return x-3
funcs = [f1, f2, f3, f4]
i = int(input())
print(funcs[i](2))
"""

# 1
"""def maxx(number):
    return sum(number[:])/len(number[:])

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
numbers.sort(key = maxx)
print(numbers[0])
print(numbers[-1])"""
# 2
"""def mean(number):
    return sum(number)/len(number)

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
print(min(numbers, key=mean), max(numbers, key=mean), sep='\n')"""

"""def p(point):
    return (point[0]**2 + point[1]**2)**0.5

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key = p)
print(points)"""

"""def sort(number):
    return min(number) + max(number)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
numbers.sort(key = sort)
print(numbers)"""

# 1
"""atl = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = int(input())

def sort(at):
    return at[n-1]
atl.sort(key = sort)
for i in atl:
    print(*i)"""
# 2
"""athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def sort_name(athlete):
    return athlete[0]

def sort_age(athlete):
    return athlete[1]

def sort_height(athlete):
    return athlete[2]

def sort_weight(athlete):
    return athlete[3]

sort_by = {1: sort_name, 2: sort_age, 3: sort_height, 4: sort_weight}
for i in sorted(athletes, key=sort_by[int(input())]):
    print(*i)"""

"""import math
def operation(x, oper):
    operat = {'квадрат': x ** 2, 'куб': x ** 3, 'корень': x ** 0.5, 'модуль': abs(x), 'синус': math.sin(x)}
    return operat[oper]

x = int(input())
oper = input()
print(operation(x, oper))"""

"""import math
x = int(input())
oper = input()
operation = {'квадрат' : x**2, 'куб' : x**3, 'корень' : x**0.5, 'модуль' : abs(x), 'синус' : math.sin(x)}
print(operation[oper])

"""

"""def s(strg):
    return sum(int(i) for i in str(strg))

string = [int(i) for i in input().split()]
#string = sorted(string)
string.sort(key = s)
print(*string)"""

# Функции высшего порядка
"""def high_order_function(func):     # функция высшего порядка, так как принимает функцию
    return func(3)

def double(x):                     # обычная функция = функция первого порядка
    return 2*x

def add_one(x):                    # обычная функция = функция первого порядка
    return x + 1
print(high_order_function(double))
print(high_order_function(add_one))"""

# map()
"""strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']

numbers1 = [int(str) for str in strings]   # используем списочное выражение для преобразования
numbers2 = map(int, strings)               # используем функцию map() для преобразования
print(numbers1)
print(numbers2)"""

"""numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
new_numbers = map(abs, map(int, numbers))
print(new_numbers)"""

# filter()
"""def is_greater10(num):   # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10

numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
large_numbers = filter(is_greater10, numbers)   #  список large_numbers содержит элементы, большие 10
print(large_numbers)"""

# reduce()
"""def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
        print(acc)
    return acc

def add(x, y):
    return x+y

def mult(x, y):
    return x*y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total)
print(product)"""

"""numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
var1 = max(numbers, key=abs)
var2 = min(map(abs, numbers))
print(var1 + var2)"""

# округление round()
"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def ron(x):
    return round(x, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(ron, numbers), sep = '\n')"""

"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def f(x):
    return len(str(x)) < 4 and x % 5 == 2

def d(x):
    return x ** 3

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
nums = filter(f,numbers)

print(*map(d, nums), sep = '\n')"""

# 1 map()
"""numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
def square(x):
    return x ** 2

nums = sum(map(square, numbers))
print(nums)"""

# 2 reduce()
"""def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

def x_on_x(element):
    return element**2

def add(one, two):
    return one + two**2
numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
print(reduce(add, numbers, 0))"""

"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def f(x):
    return ((len(str(x)) == 2 and str(x)[0] in '0123456789') or (len(str(x)) == 3 and str(x)[0] == '-')) and x % 7 == 0
    #return 9 < abs(item) < 100 and not item % 7

def square(x):
    return x ** 2


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
nums = filter(f, numbers)
print(sum(map(square, nums)))"""

"""def func_apply(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result"""

# map()
"""def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(map(increase, numbers))     #  используем встроенную функцию map()
print(new_numbers)"""

"""def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]
new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
print(new_numbers)"""

# map с округлением
"""circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]

result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой

print(circle_areas) #[3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
print(result1) #[3.6, 5.6, 4.3, 6.2, 91.0, 32.0]
print(result2) #[3.6, 5.58, 4.319, 6.2024, 91.01344, 32.01213]"""

# filter()
"""def func(elem):
    return elem >= 0

numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список

print(positive_numbers)"""

"""true_values = list(filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()]))
for value in true_values:
    print(value)"""

# reduce()
"""from functools import reduce
def func(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(func, numbers, 0)   # в качестве начального значения 0
print(total)"""

# operator()
"""Addition 	a + b 	add(a, b)
Containment Test 	obj in seq 	contains(seq, obj)
Division 	a / b 	truediv(a, b)
Division 	a // b 	floordiv(a, b)
Exponentiation 	a ** b 	pow(a, b)
Modulo 	a % b 	mod(a, b)
Multiplication 	a * b 	mul(a, b)
Negation (Arithmetic) 	-a 	neg(a)
Subtraction 	a - b 	sub(a, b)
Ordering 	a < b 	lt(a, b)
Ordering 	a <= b 	le(a, b)
Equality 	a == b 	eq(a, b)
Difference 	a != b 	ne(a, b)
Ordering 	a >= b 	ge(a, b)
Ordering 	a > b 	gt(a, b)"""


"""from operator import *     #  импортируем все функции

print(add(10, 20))         #  сумма
print(floordiv(20, 3))     #  целочисленное деление
print(neg(9))              #  смена знака
print(lt(2, 3))            #  проверка на неравенство <
print(lt(10, 8))           #  проверка на неравенство <
print(eq(5, 5))            #  проверка на равенство ==
print(eq(5, 9))            #  проверка на равенство =="""

# использование operator()
"""from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs'] 
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
concat_words = reduce(operator.add, words)             #  конкатенация элементов списка
print(opposite_numbers)
print(concat_words)"""

# str.methods
"""pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']
 
uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))

print(uppered_pets)
print(capitalized_pets)
print(only_letters)"""

# Анонимные функции
# lambda

"""f1 = lambda: 10 + 20               # функция без параметров
f2 = lambda х, у: х + у            # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами

print(f1())
print(f2(5, 10))
print(f3(5, 10, 30))"""


"""points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа"""

"""strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]
new_strings = list(map(lambda x, y: x*y, strings, numbers))

print(new_strings)"""

"""numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

print(list(filter(lambda x: x > 0, numbers))) #  положительные числа
print(list(filter(lambda x: x > 50, numbers))) #  числа, большие 50
print(list(filter(lambda x: x % 2 == 0, numbers))) #  четные числа"""

"""from functools import reduce
words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)
print(product)
print(sentence)"""

"""numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
print(result)"""

# Передача аргументов в анонимную функцию
"""f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z

print(f1(1, 2, 3))
print(f2(1, 2))
print(f2(1, y=2))
print(f3(1, 2, 3, 4, 5))
print(f4(one=1, two=2, three=3))
print(f5(1))
print(f5(1, y=2, z=3))"""

"""print((lambda х, у: х + у)(5, 10))     # 5 + 10
print(1 + (lambda x: x*5)(10) + 2)     # 1 + 50 + 2"""

"""funcs = [lambda x: x ** 0.5, lambda x: x ** 2, lambda x: x ** 3]
print(funcs[1](9))"""

# 1
"""from functools import reduce
floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)"""

# 1
"""
from functools import reduce
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

data_result = sorted(list(filter(lambda da: da[1] > 10000000 and da[-1] == 'primary', data)))
str = f'Cities: {", ".join(i[0] for i in data_result)}'
print(str)"""

# 2
"""
cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
cities = map(lambda city: city[0], cities)
cities = sorted(cities)
cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)
print(cities)"""

"""func = lambda x: x % 19 == 0 or x % 13 == 0"""

# 1
"""func = lambda string: string[0].lower() == 'a' and string[-1].lower() == 'a'"""
# 2
"""func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')"""

"""is_non_negative_num = lambda x: x[0] != '-' and x.replace('.','', 1).isdigit()"""

"""is_num = lambda x: x.replace('.','', 1).replace('-','', 1).isdigit() and '-' not in x[1:]"""

"""words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
print(*sorted(filter(lambda x: len(x) == 6, words)))"""

# 1
"""numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
cht = list(filter(lambda x: (x%2 == 0) > 47 or x <= 47 or x%2 == 0, numbers))
ch = list(map(lambda x: x // 2 if (x%2 == 0) else x, cht))
print(*ch)"""
# 2
"""print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))"""

"""data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
new = sorted(data, key = lambda s: s[1][-1], reverse = True)
for i in new:
        print(f'{i[-1]}: {i[0]}')"""

# Лексикографический порядок и потом сортировка через key
"""data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
data = sorted(data)
print(*sorted(data, key = lambda x: len(x)))"""

# 1
"""mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
mix_end = list(filter(lambda x: int(x) if str(x).isdigit() else 0, mixed_list))
print(max(mix_end))"""
# 2
"""print(max(mixed_list, key=lambda x: (isinstance(x, int), x)))"""

# 1
"""mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
v = sorted(list(filter(lambda x: isinstance(x, int), mixed_list)))
s = sorted(list(filter(lambda x: isinstance(x, str), mixed_list)))
print(*(v + s))"""
# 2
"""mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
print(*sorted(mixed_list, key = lambda x: (isinstance(x,str), x)))"""

"""s = [int(i) for i in input().split()]
print(*list(map(lambda x: abs(x - 255), s)))"""

"""s = [int(i) for i in input().split()]
max_ch = len(s) - 1
x = int(input())
result = 0
for i in s:
        result += i*(x**max_ch)
        max_ch -= 1
print(result)"""

# all()
"""print(all([1, 2, 3]))   
print(all([1, 2, 3, 0, 5]))
print(all([True, 0, 1]))
print(all(('', 'red', 'green')))
print(all({0j, 3+4j}))"""

"""print(all([]))          #  передаем пустой список
print(all(()))          #  передаем пустой кортеж
print(all(''))          #  передаем пустую строку
print(all([[], []]))    #  передаем список, содержащий пустые списки"""

# any()
"""print(any([0, 0, 0]))
print(any([0, 1, 0]))
print(any([False, 0, 1]))
print(any(['', [], 'green']))
print(any({0j, 3+4j, 0.0}))"""

"""print(any([]))          #  передаем пустой список
print(any(()))          #  передаем пустой кортеж
print(any(''))          #  передаем пустую строку
print(any([[], []]))    #  передаем список, содержащий пустые списки"""

"""
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
result = all(map(lambda x: True if x > 10 else False, numbers))

if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')"""

"""numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]
result = any(map(lambda x: x % 2 == 0, numbers))

if result:
    print('Хотя бы одно число четное')
else:
    print('Все числа нечетные')"""

# enumerate()
"""colors = ['red', 'green', 'blue']

for pair in enumerate(colors):
    print(pair)"""

"""colors = ['red', 'green', 'blue']

for pair in enumerate(colors, 100):
    print(pair)"""

"""colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
    print(index, item)"""

# zip()
"""numbers = [1, 2, 3]
words = ['one', 'two', 'three']

result = zip(numbers, words)

print(result)
print(list(result))"""

# Мы можем передавать функции zip() сколько угодно итерируемых объектов.

"""keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)"""

"""def ignore_command(command):
        ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
        return any(map(lambda x: x in command, ignore))"""

"""countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for coun, cap, pop in zip(countries,capitals,population):
    print(f'{cap} is the capital of {coun}, population equal {pop} people.')"""

# 1
"""abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
for a,o,ao in zip(abscissas,ordinates,applicates):
    if a**2 + o**2 + ao**2 <= 4:
        s = 1
    else:
        print(False)
        s = 0
        break

if s:
    print(True)"""
# 2
"""abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas,ordinates,applicates))))"""

# 1
"""f = 1
x = [i for i in input().split('.')]
for i in x:
    for j in i:
        if j in 'abcdefghijklmnopqrstuvwxyz':
            f = 0
            break
        else:
            continue
if f:
    print(all(map(lambda i: isinstance(i, int) or 0 <= int(i) <= 255, x)))
else:
    print(False)"""
# 2
"""print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split('.'))))"""

"""    print(all(map(lambda x: True if int(x) != 0 and int(i) % x == 0 else False, list(str(i)))), end = " ")"""

"""ls = list(range(int(input()),int(input())))
for i in ls:
    if all(x != '0' and not i % int(x) for x in str(i)):
        print(i)"""

# 1
"""psw = input()
if all((any(i.isupper() for i in psw), any(i.islower() for i in psw), any(i.isdigit() for i in psw), len(psw) >= 7)):
    print("YES")
else:
    print("NO")"""
# 2
"""psw = input()
print('YES' if all((any(i.isupper() for i in psw), any(i.islower() for i in psw), any(i.isdigit() for i in psw), len(psw) >= 7)) else 'NO')"""

"""n = int(input())
d = []
for _ in range(n):
    d.append([int(input()[-1]) for i in range(int(input()))])
print('YES' if all(map(lambda x: 5 in x, d)) else "NO")"""

# 1
"""def concat(*args, sep = ' '):
    return f'{sep}'.join(str(i) for i in args)
"""
# 2
"""def concat(*args, sep=' '):
    return sep.join(map(str, args))"""

"""words = 'the world is mine take a look what you have started'.split()
print(*map(lambda x: f'"{x}"',words))"""

"""numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x)!= str(x)[::-1], numbers))"""

"""numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers, key = lambda x: sum(x)/len(x), reverse = True)
print(sorted_numbers)"""

# 1
"""def compose(f, g):
    return lambda x: f(g(x))
"""
# 2
"""def compose(f, g):
    def rofler(x):
        return f(g(x))
    return rofler"""

# 1
"""def arithmetic_operation(z):
    if z == '+':
        return lambda a, b : a + b
    if z == '-':
        return lambda a, b : a - b
    if z == '*':
        return lambda a, b : a * b
    if z == '/':
        return lambda a, b : a / b"""

# 2
"""from operator import *
def arithmetic_operation(operation):
    oper = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return oper[operation]"""

"""print(*sorted(input().split(), key = lambda x: x.lower()), sep = " ")"""

# 1
"""l = [input() for _ in range(int(input()))]
def f(word):
    result = 0
    for i in word.upper():
        result += ord(i) - ord('A')
    return result
l.sort()
print(*sorted(l, key = f), sep = '\n')"""
# 2
"""l = [input() for _ in range(int(input()))]
l.sort()
print(*sorted(l, key = lambda x: sum(map(lambda y: ord(y.upper()) - ord('A'), x))), sep = '\n')"""

# 1
"""l = [[int(i) for i in input().split('.')] for i in range(int(input()))]
new_l = sorted(l, key = lambda x: x[0] * 256 ** 3 + x[1] * 256 ** 2 + x[2] * 256 ** 1 + x[3] * 256 ** 0)
for i in new_l:
    print(f'{i[0]}.{i[1]}.{i[2]}.{i[3]}')"""
# 2
"""print(*sorted([input() for _ in range(int(input()))], key=lambda x: [*map(int, x.split('.'))]), sep='\n')"""

"""def pretty_print(data, side = '-', delimiter = '|'):
    s2 = f'{delimiter} ' + f' {delimiter} '.join(str(i) for i in data) + f' {delimiter}'
    s1 = f' {side * (len(s2) - 2)} '
    s3 = s1
    print(f'{s1}\n{s2}\n{s3}')
pretty_print([1, 2, 10, 23, 123, 3000])"""

# Файловый ввод и вывод
# open()
"""student_file = open('students.txt', 'r')"""
# r - read
# w - write
# a - append
# r+ - read and write
# x - create

# создает файл и таким именем
"""sales_file = open('sales.txt', 'w')"""

# находит файл по абсолютному пути
"""test_file = open('C:\\Users\\temp\\test.txt', 'w')"""

# сырые строки
"""path = r'C:\new\text.txt'"""

# При работе с текстом на русском языке нужно указать кодировку, для этого служит параметр encoding:
"""file = open('info.txt', 'r', encoding='utf-8')"""

"""file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w', encoding='utf-8')

print(file1.encoding)
print(file2.encoding)

file1.close()
file2.close()"""

# close()
# closed()

"""file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w')

file1.close()

print(file1.closed)
print(file2.closed)

file2.close()    """

# read()    readline()      readlines()

"""file1 = open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding='utf-8')
content = file1.readlines()
print(content)
file1.close()"""

# Прочитать содержимое всего файла построчно можно двумя способами.
# 1
"""file = open('languages.txt', 'r', encoding='utf-8')

line = file.readline()         # считываем первую строку

while line != '':              # пока не конец файла
    print(line.strip())        # обрабатываем считанную строку
    line = file.readline()     # читаем новую строку

file.close()"""
# 2
"""file = open('languages.txt', 'r', encoding='utf-8')
for line in file:
    print(line.strip())

file.close()"""

# Чтобы удалить символ '\n' можно использовать списочное выражение:
"""languages = [line.strip() for line in file.readlines()] """
"""languages = list(map(str.strip, file.readlines()))"""

# 'r' - read 'b' - binary

"""file = open(input(), 'r')
print(file.read())
file.close()"""

# 1
"""file1 = open(input(), 'r')
content = list(file1)
print(content[-2])
file1.close()"""
# 2
"""print(open(input()).readlines()[-2])"""

# 1
"""import random
print(open('lines.txt').readlines()[random.randint(0, len(list('lines.txt')))])"""
# 2
"""from random import * 
print(choice(list(open("lines.txt"))))"""

# 1
"""x = int(open('numbers.txt').readlines()[0])
y = int(open('numbers.txt').readlines()[1])
print(x + y)"""
# 2
"""with open('numbers.txt') as f:
    print(sum(list(map(int, f.readlines()))))"""
# 3
"""file = open('numbers.txt')
print(sum(map(int, file)))"""

# 1
"""file = open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding= 'utf-8')
content = []
result = 0
for i in list(file):
    content.append(i.split('\t'))
    count = int(content[0][1])
    mult = int(content[0][2].rstrip())
    result += count * mult
    del content[:]
print(result)
file.close()"""
# 2
"""file = open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding= 'utf-8')
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()"""

# seek()
"""file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
file.seek(0)               # переводим курсор в самое начало
line2 = file.readline()

print(line1, line2)

file.close()"""

# tell()
"""file = open('languages.txt', 'r', encoding='utf-8')
print(file.tell())
line1 = file.readline()
print(file.tell())

file.close()"""

# with - block
"""with open('languages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
                          # автоматическое закрытие файла
print('Файл закрыт')"""

# with
"""with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # обработка файлов"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines()[::-1]:
        print(line.strip())"""
# 2
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep = '')"""

"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding = 'utf-8') as file:
    result = [i.strip() for i in list(file)]
    m = len(max(result, key = len))
    print(*filter(lambda x: len(x) == m, result), sep = '\n')"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding = 'utf-8') as file:
    for line in file.readlines():
        s = [int(i.strip()) for i in line.split()]
        print(sum(s))"""
# 2
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        print(sum(map(int, line.split())))"""

"""with open('numbers.txt', encoding='utf-8') as file:
    row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(sum(map(int, row.split())))
"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as file:
    line = 0
    for l in file.readlines():
        line += 1

    words = 0
    letters = 0
    file.seek(0)
    for l in file.readlines():
        words += len(l.split())
        for i in l:
            if i.isalpha():
                letters += 1
    print(line)
    print(words)
    print(letters)"""
# 2
"""with open('lines.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')"""

"""from random import choice as ch
with open('first_names.txt') as fn, open('last_names.txt') as ln:
    i = fn.read()
    f = ln.read()
    print(ch(i.split()),ch(f.split()))
    print(ch(i.split()), ch(f.split()))
    print(ch(i.split()), ch(f.split()))"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r') as file:
    for line in file:
        x = line.strip().split()
        if x[0][0] == 'G' and int(x[-1]) >= 500000:
            print(x[0])"""
# 2
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r') as file:
    for line in file:
        x,y = line.split('\t')
        if x.startswith('G') and int(y) >= 500000:
            print(x)"""

# write()
# Сначала все стирается, а потом уже добавляется.
# Это из-за режима 'w', если бы режим был 'a' - то оно добавилось в конец.
"""with open('myfile.txt', 'w', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik <3')"""

"""with open('myfile.txt', 'a', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik <3')"""

"""philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']

with open('philosophers.txt', 'w', encoding='utf-8') as file:
    file.writelines(philosophers)"""

# print()
"""with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', file=output)
    print('Дэвид Хьюм', file=output)
    print('Эдмyнд Берк', file=output)"""

"""with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)"""

"""import random
with open('random.txt', 'w') as file:
    for i in range(25):
        print(random.randint(111, 777), file=file)"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as input, open('C:\\Users\\Admin\\Desktop\\file2.txt', 'r+') as output:
    i = 0
    for line in input.readlines():
        i += 1
        output.writelines(f'{i}) {line}')"""
# 2
"""with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)"""

"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as input, open('C:\\Users\\Admin\\Desktop\\file2.txt', 'r+') as output:
    for line in input.readlines():
        x, y = line.split()
        y = int(y)
        if y < 95:
            y += 5
        elif y >= 95:
            y += (100 - y)
        print(f'{x} {y}', file = output)"""

"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as fin, open('C:\\Users\\Admin\\Desktop\\file2.txt', 'r+') as fout:
    colors, total = {}, 0
    for line in fin:
        if line not in ('COLOURS\n', 'GOATS\n'):
            colors[line] = colors.get(line, -1) + 1
            total += 1
    [fout.write(k) for k in colors if colors[k] >= total * 0.7]"""

# 1
"""with open('output.txt', 'w') as output:
    for i in range(int(input())):
        name_file = input()
        with open(name_file, 'r') as file:
            cont = file.read()
            output.write(cont)"""
# 2
"""with open('output.txt', 'w') as output:
    for i in range(int(input())):
        with open(input()) as file:
            output.write(file.read())"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', encoding='utf-8') as file, open('C:\\Users\\Admin\\Desktop\\file2.txt', 'w') as output:
    for line in file.readlines():
        l = line.split()
        x1,x2 = l[2].split(':')
        x2 = x2.replace(',','')
        y1,y2 = l[-1].split(':')
        y2 = y2.replace(',','')
        sx = int(x1) * 60 + int(x2)
        sy = int(y1) * 60 + int(y2)
        if sy - sx >= 60:
            l_n = l[1]
            l_n = l_n.replace(',','')
            print(f'{l[0]} {l_n}', file = output)"""
# 2
"""def time(time1,time2):
    t1 = list(map(int, time1.split(':')))
    t2 = list(map(int, time2.split(':')))
    return (t2[0] * 60 + t2[1]) - (t1[0] * 60 + t1[1])

with open('C:\\Users\\Admin\\Desktop\\file.txt', encoding='utf-8') as file, open('C:\\Users\\Admin\\Desktop\\file2.txt', 'w') as output:
    for line in file:
        name,time1,time2 = line.strip().split(', ')
        if time(time1,time2) >= 60:
            print(name, file = output)"""
# 3
"""from datetime import datetime

with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
    for log in logfile.read().split('\n'):
        name, first_time, second_time = log.split(', ')
        delta = datetime.strptime(second_time, "%H:%M") - datetime.strptime(first_time, "%H:%M")
        if delta.seconds >= 3600:
            print(name, file=output)"""

"""with open(input()) as file:
    print(len(file.readlines()))"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', encoding='utf-8') as file:
    summ = 0
    for line in file:
        summ += int(line[1:])
    print(summ)"""
# 2
"""with open('ledger.txt') as ledger:
    result = sum(map(lambda x: int(x.strip('$')), ledger.readlines()))
    print('$', result, sep='')"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as file:
    count = 0
    for line in file:
        if all(map(lambda x: int(x) >= 65, line.split()[1:])):
            count += 1
    print(count)"""
# 2
"""with open('grades.txt') as f:
    print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))"""

"""with open('C:\\Users\\Admin\\Desktop\\file.txt', 'r', encoding = 'utf-8') as file:
    s = file.read().split()
    m = max(map(len, s))
    for word in s:
        if len(word) == m:
            print(word)"""

"""with open('C:\\Users\\Admin\\Desktop\\file.txt') as file:
    print(*file.readlines()[-10:] , sep = "")"""

# 1
"""with open('C:\\Users\\Admin\\Desktop\\file.txt', encoding='utf-8') as file_pattern, open('C:\\Users\\Admin\\Desktop\\file2.txt') as file_in:
    pattern, text = file_pattern.read().split(), file_in.read()

text_lower = text.lower()
for word in pattern:
    text_lower = text_lower.replace(word, '*' * len(word))

result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
print(result)"""
# 2
"""import re
with open(input()) as inp, open('forbidden_words.txt') as fw:
    text, bad = inp.read(), fw.read().split()

for i in bad:
    text = re.sub(i, '*' * len(i), text, flags=re.IGNORECASE)
print(text)"""

# Перевод текста(рус) с txt в англ. кирилицу
"""d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

# Добавляем заглавные буквы
d.update({k.upper(): (v[0].upper() + v[1:]) for k, v in d.items()})

# Вуаля!
with open('cyrillic.txt', 'r', encoding='utf-8') as inp, open('transliteration.txt', 'w', encoding='utf-8') as out:
    text= inp.read()
    print(''.join(map(lambda ch: d.get(ch, ch), text)), file=out)"""

"""s = ''

with open(input()) as fin:
    t = fin.readlines()
    for i, row in enumerate(t):
        if row[:4] == 'def ' and (i == 0 or t[i - 1][0] != '#'):
            c = row.find('(')
            s = s + row[4:c] + '\n'
    print(s[:-1] if s else 'Best Programming Team')"""


