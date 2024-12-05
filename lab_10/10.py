# # 1
# f = open("file4.txt", "r", encoding="utf8")
#
# a_max = ""
# b_max = 0
# for s in f:
#     a = s.split()[0] + " " + s.split()[1]
#     b = int(s.split()[-1])
#
#     if b > b_max:
#         a_max = a
#         b_max = b
# print(a_max, b_max)


# # 2
# f1 = open("file5.txt", "r", encoding="utf8")
# f2 = open("file6.txt", "r", encoding="utf8")
#
# for s in f1:
#     s = s.split()
#     if "Academy" in s:
#         print("В файле file5.txt")
# for s in f2:
#     s = s.split()
#     if "Academy" in s:
#         print("В файле file6.txt")


# # 3
# f = open("file6.txt", "r", encoding="utf8")
#
# cnt_e, cnt = 0, 0
# for s in f:
#     s = s.split()
#     for w in s:
#         cnt += 1
#         if ("e" in w) or ("E" in w):
#             cnt_e += 1
# print(100 * cnt_e / cnt)


# # 4
# m = open("file8.txt", "r", encoding="utf8")
# w = open("file7.txt", "r", encoding="utf8")
#
# n = int(input())
# x = input()
#
# if x == "м":
#     for i in range(0, n):
#         s = m.readline()
#         print(s.split()[0])
# elif x == "ж":
#     for i in range(0, n):
#         s = w.readline()
#         print(s.split()[0])


# # 5
# f = open("5.txt", encoding="utf8")
# text = f.readlines()
# f.close()
#
# f = open("5.txt", "w+", encoding="utf8")
# inp = input()
#
# for i in range(int(len(text) / 2)):
#     f.write(text[i])
#
# f.write(inp+"\n")
#
# for i in range(int(len(text) / 2), len(text)):
#     f.write(text[i])


# # 6
# f = open("6.txt", encoding="utf8").readlines()[0].split()
# s = ""
# for w in f:
#     s += w[::-1] + " "
# print(s)







