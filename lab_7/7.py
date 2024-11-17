# # 1
# s = """Довольно распространённая ошибка
# ошибка это лишний повтор повтор
# слова слова Смешно не не правда ли
# Не нужно портить хор хоровод""".split()
#
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         s[i] = ""
# s = " ".join(s).replace("  ", " ")
# print(s)


# # 2
# s = input().split()
#
# if len(s) >= 2:
#     print(" ".join(s[::-1]))
# else:
#     print("Ошибка")


# # 3
# s = list(input())
# print(".".join(s))


# # 4
# s = input()
# s = s.replace("не плохой", 'хороший')
# s = s.replace("не плоха", "хороша")
# print(s)


# # 5
# s = input()
# sym = "АЕИОУЫЭЮЯаеиоуыэюя"
# for i in sym:
#     s = s.replace(i, "*")
# s.split(" / ")
#
# if len(s) != 3:
#     print("Не хайку. Должно быть 3 строки.")
# elif s[0].count("*") == 5 and s[1].count("*") == 7 and s[2].count("*") == 5:
#     print("Хайку!")
# else:
#     print("Не хайку")
#


# # 6
# s = input()
#
# if s[-1] == "#":
#     s = s[:-1]
#     print(s[::2] + s[::-2])
# else:
#     print("Ошибка! Отсутствует символ #")


# # 7
# from random import choice
#
# n = int(input("желаемую длину пароля (целое число); "))
# res = ""
# pas = ""
#
# a2 = input("нужны ли заглавные буквы (да/нет); ")
# if a2 == "да":
#     res += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# a3 = input("нужны ли строчные буквы (да/нет); ")
# if a3 == "да":
#     res += 'abcdefghijklmnopqrstuvwxyz'
#
# a4 = input("нужнужны ли цифры (да/нет); ")
# if a4 == "да":
#     res += '0123456789'
#
# a5 = input("нужны ли специальные символы (да/нет); ")
# if a5 == "да":
#     res += r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
#
# for i in range(n):
#     pas += choice(res)
# print(pas)


# # 8
# s = input()
# a = s[:-4].split("-")
# b = s[-3:].split(":")
#
# if int(b[0]) == int(b[1]):
#     print("Ничья")
# elif int(b[0]) > int(b[1]):
#     print(a[0])
# elif int(b[0]) < int(b[1]):
#     print(a[1])
# else:
#     print("Ошибка")
#
#

