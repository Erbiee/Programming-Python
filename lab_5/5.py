# # 1
# d = int(input("дни: "))
# h = int(input("часы: "))
# m = int(input("минуты: "))
# s = int(input("секунд: "))
#
# h += d * 24
# m += h * 60
# s += m * 60
# print(s)


# # 2
# N = int(input())
# K = int(input())
# print(N % 10**K)


# # 3
# res = 0
# N = input()
# for i in N:
#     res += int(i)
# print(res)


# # 4
# from random import randint
# f = randint(1, 2)
# print("""Вы находитесь в землях, заселенных драконами. Перед собой вы видите две пещеры. В одной
# из них — дружелюбный дракон, который готов поделиться с вами своими сокровищами. Во второй
# — жадный и голодный дракон, который мигом вас съест. В какую пещеру вы войдете? (нажмите
# клавишу 1 или 2)""")
#
# inp = int(input("1 | 2: "))
#
# print("""Вы приближаетесь к пещере...
# Ее темнота заставляет вас дрожать от страха...
# Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...""")
#
# if inp == f:
#     print("""...делится с вами своими сокровищами!""")
# else:
#     print("""...моментально вас съедает!""")


# # 5
# a = set(input().split())
# if len(a) == 1:
#     print("равносторонний")
# elif len(a) == 2:
#     print("равнобедренный")
# else:
#     print("разносторонний")


# 6
a = {"январь": 31, "февраль": "28, 29", "март": 31, "апрель": 30, "май": 31, "июнь": 30, "июль": 31, "август": 31, "сентябрь": 30, "октябрь": 31, "ноябрь": 30, "декабрь": 31}
print(a[input("название месяца: ")])
