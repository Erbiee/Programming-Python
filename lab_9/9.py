# # 1
# def f(x):
#     return x**2

# a = 0
# b = 2
# n = 1000
# h = (b - a) / n

# sum = 0
# i = a + h
# while i < b:
#     sum += ((f(i) + f(i-h))*h)/2
#     i += h
# print(sum)


# # 2
# from random import shuffle

# def f():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
#     while True:
#         shuffle(nums)
#         m = [nums[:3], nums[3:6], nums[6:]]

#         if (sum(m[0]) == sum(m[1]) == sum(m[2]) ==
#             sum(m[i][0] for i in range(3)) == 
#             sum(m[i][1] for i in range(3)) == 
#             sum(m[i][2] for i in range(3)) == 
#             sum(m[i][i] for i in range(3)) == 
#             sum(m[i][2-i] for i in range(3))):
#             return m

# a = f()
# for i in a:
#     print(i)


# # 3
# treasure_map = [
#                 [1, 2],
#                 [3, 5],
#                 [5, 6],
#                 [7, 8]
#                 ]
# print(f"Количество сокровищ:\n{len(treasure_map)}")

# print("Координаты сокровищ:")
# for i in treasure_map:
#     print(i)

# cords = [7, 8]
# print("Координаты Александра:")
# print(cords)

# minl = 1000
# minid = 0

# for i in range(len(treasure_map)):
#     l = ((treasure_map[i][0] - cords[0])**2 + (treasure_map[i][1] - cords[1])**2)**0.5
#     if l < minl:
#         minl = l
#         minid = i
# print(f"Ближайшее сокровище:\n{treasure_map[minid]}")


# # 4
# menu = [
#         ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
#         ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
#         ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
#         ]
# print("""1. Отобразить меню ресторана.
# 2. Найти блюдо по названию и отобразить его ингредиенты и цену.
# 3. Добавить новое блюдо в меню.
# 4. Изменить цену блюда (название цена).""")

# i = int(input())
# if  i == 1:
#     print(menu)
# elif i == 2:
#     a = input()
#     for j in range(len(menu)):
#         if menu[j][0] == a:
#             print(menu[j])
# elif i == 3:
#     a1 = input("Название блюда: ")
#     a2 = list(input("ингредиенты: ").split())
#     a3 = int(input("Цена: "))
#     menu.append([a1, a2, a3])
#     print(menu)
# elif i == 4:
#     a = input("Название - цена: ")
#     a = a.split(" - ")
#     print(int(a[1]))
#     for j in range(len(menu)):
#         if menu[j][0] == a[0]:
#             print("asdasdasd")
#             menu[j][2] = int(a[1])
#             print(menu[j])


# # 5
# m = [[11, 12, 13, 14],
#      [21, 22, 23, 24],
#      [31, 32, 33, 34]
#     ]
# a, b = 3, 4

# new_m = [[], [], [], []]
# for i in range(b):
#     for j in range(a):
#         new_m[i].append(m[j][i])
# for i in new_m:
#     print(i)


# # 6
# n = int(input("Размер матрицы: "))
# m = []

# print("Введите матрицу построчно:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     m.append(row)

# for i in range(n):
#     m[i][i], m[n - i - 1][i] = m[n - i - 1][i], m[i][i]

# print("Новая матрица: ")
# for i in m:
#     print(*i)


# # 7
# n, m = list(map(int, input().split()))
# m = []

# for i in range(n):
#     row = list(input().split())
#     m.append(row)

# k = int(input())

# for i in range(len(m)):
#     if "0"*k in "".join(m[i]):
#         print(i+1)
#         break
# else:
#     print(0)
