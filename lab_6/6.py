# # 1
# arr = []
# while 1:
#     a = int(input())
#     if a == 0:
#         break
#     arr.append(a)
#
# if len(arr) > 0:
#     print(f"Самый высокий: {max(arr)}")
#     print(f"Самый низкий: {min(arr)}")
# else:
#     print("Некого сравнивать")


# # 2
# res = 0
# for i in range(2, 101, 2):
#     res += i
# print(res)


# # 3
# n = int(input())
# res = 0
# for i in range(1, n+1):
#     res += i**2
# print(res)


# # 4
# n = int(input())
# for i in range(0, n):
#     print(" " * (n - i - 1) + "#" * (1 + 2 * i))
# print(" " * (n - 1) + "#")


# # 5
# n = int(input())
# if n < 0:
#     print("Ошибка")
# elif n <= 2:
#     print("Введенный вами год эквивалентен 10.5 человеческим")
# else:
#     print(f"Введенный вами год эквивалентен {21 + 4 * (n - 2)} человечески")


# # 6
# import random
#
# secret = random.randint(1, 10)
#
# print("Хорошо, я загадал число. Попробуй его отгадать")
# otv = "да"
#
# while otv == "да":
#     cnt = 1
#     while 1:
#         num = int(input(f"Попытка {cnt} > "))
#
#         if num == secret:
#             print("Поздравляю! Вы угадали!")
#             break
#         else:
#             if num > secret:
#                 print("Нее, ты не угадал. Попробуй меньше")
#             elif num < secret:
#                 print("Нее, ты не угадал. Попробуй больше")
#             cnt += 1
#     otv = input("Сыграть снова?: ")


# # 7
# n = input()
# if len(n) != 6:
#     print("Некорректный билет")
# else:
#     if sum(map(int, list(n[:3]))) == sum(map(int, list(n[-3:]))):
#         print("Поздравляю! Ваш билет - счастливый")
#     else:
#         print("Обычный билет")


# 8
n = input()
d = 0
e = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] == "1":
        d += 2 ** e
    e += 1
print(d)
