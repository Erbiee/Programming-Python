# # 1
# a = [" ", ".,?!:", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# #s = list(input())
# s = list("Hello, Wolrd!")
# new_s = ""
#
# for i in range(len(s)):
#     if 97 <= ord(s[i]) <= 122:
#         s[i] = chr(ord(s[i]) - 32)
#
# for c in s:
#     for i in range(len(a)):
#         if c in a[i]:
#             new_s += str(i) * (a[i].index(c) + 1)
#             break
# print(new_s)
# print("4433555555666110966677755531111")


# # 2
# a = {1: "AEILNORSTU", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
# #s = list(input())
# s = list("axq")
# new_s = 0
#
# for i in range(len(s)):
#     if 97 <= ord(s[i]) <= 122:
#         s[i] = chr(ord(s[i]) - 32)
#
# for c in s:
#     for i in [1, 2, 3, 4, 5, 8, 10]:
#         if c in a[i]:
#             new_s += i
# print(new_s)


# # 3
# emails = {"gryffindor.com": ["andrei_serov", "alexander_pushkin", "elena_belova", "k_stepanov"],
# "hufflepuff.com": ["alena.semyonova", "ivan.polekhin", "marina_abrabova"],
# "hogwarts.com": ["sergei.zharkov", "julia_lyubimova", "vitaliy.smirnoff"],
# "slytherin.com": ["ekaterina_ivanova", "glebova_nastya"],
# "ravenclaw.com": ["john.doe", "mark.zuckerberg", "helen_hunt"]}

# for d in emails.keys():
#     for i in emails[d]:
#         print(i + "@" + d)
