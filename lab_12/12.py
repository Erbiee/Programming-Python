# # 1
# n = int(input())
# a = []
# for i in range(n):
#     s = input().split()
#     a.append(s)
#
# for i in range(len(a)):
#     if a[i][1] == "captain":
#         a[i][1] = 3
#     elif a[i][1] == "man":
#         a[i][1] = 2
#     elif a[i][1] == "woman":
#         a[i][1] = 1
#     elif a[i][1] == "child":
#         a[i][1] = 1
#
# a = sorted(a, key=lambda x: x[1])
# for i in a:
#     print(i[0])


# # 2
# s = input()
#
# cnt = 0
# for c in s:
#     if c == "Q":
#         cnt += 1
#     elif c == "A":
#         cnt -= 1
#
#     if cnt < 0:
#         break
# if cnt == 0:
#     print("+")
# else:
#     print("-")


# # 3
# from random import randint

# k = 2
# b = randint(0, 4)
# N = int(input())
# x = 1
# print(k, b, N)

# for i in range(N):
#     x = k * x + b
# print(x)
