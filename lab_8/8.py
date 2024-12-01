# # 1
# a = [1, "a", 3, 4, "b", 6]
#
# d = []
# c = []
# for i in a:
#     if str(i).isdigit():
#         d.append(i)
#     else:
#         c.append(i)
# print(d)
# print(c)


# # 2
# from random import randint
# a = []
# for i in range(6):
#     a.append(randint(1, 49))
# print(*a)


# # 3
# a = [1, 5, 2, 4, 3]
# for i in range(1, len(a)-1):
#     if a[i-1] < a[i]:
#         print(a[i], end=" ")


# # 4
# a = []
# i = input()
# while i != "":
#     a.append(int(i))
#     i = input()
# print(sum(a)/len(a))
# for i in a:
#     if i < sum(a)/len(a):
#         print(i, end=" ")
# print()
# for i in a:
#     if i > sum(a)/len(a):
#         print(i, end=" ")


# # 5
# a = [215, 207, 196, 176, 168, 166]
# n = int(input())

# for i in range(len(a)):
#     if n > a[i]:
#         print(i+1)
#         break


# # 6
# from random import choice

# n = 0
# s = ""
# while "ООО" not in s and "РРР" not in s:
#     s += choice(["О", "Р"])
#     n += 1
# print(s, "Попыток:", n)


# # 7
# s = "4276440013361511"
# nechet = s[::2]
# chet = s[1::2]
# sum = sum(map(int, list(chet))) + sum(map(int, list(nechet))) * 2
# if sum > 9:
#     sum -= 9
# if len(s) != 16:
#     print("Некорректый номер")
# elif sum % 10 == 0:
#     print("Корректный номер")
# else:
#     print("Некорректый номер")









