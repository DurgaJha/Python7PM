# # x = 10
# # print(type(x))
# # print(dir(x))
# # name = "Ram"
# # print(dir(name))
# # y = 3.45455
# # print("%.2f" % y)
# # print(round(y,2))
# # x = "python"
# # print(x.upper())
# # print(f"{x} {y}")
# # y = input("Enter any number: ")
# # x = input("Enter any number: ")
# # print(int(x)+int(y))
# a = ["ram", 1234, 34.56]
# # # print(a[0:2])
# # student = [["ram", 1234, 34.56],
# #            ["Hari", 1234, 34.56],
# #            ["sophia", 1234, 34.56]]
# # print(student[2][0])
# a[0] = "Hari"
# print(a)
# a.append(99)
# print(a)
# x=100
# y=20
# z=30
# if x>y and x>z:
#     print("X is large")
# elif y>x and y>z:
#     print("Y is large")
# else:
#     print("Z is large")

# age = int(input("How old are you? :"))
# if age < 20:
#     print("Sorry, Not allowed")
# elif age > 40:
#     print("Sorry, Not allowed")
# else:
#    print("You are welcome")
#
# math = int(52)
# science = int(55)
# pop = int(47)
# eng = int(56)
# nepali = int(65)
# if math > 100:
#     print("Mark can not be greater than 100")
# if science > 100:
#     print("Mark can not be greater than 100")
# if eng > 100:
#     print("Mark can not be greater than 100")
# if nepali > 100:
#     print("Mark can not be greater than 100")
# else:
# #     print(math+science+pop+eng+nepali)
# input("username") = "admin"
# password = "admin002"
# if username == "admin" and password == "admin002":
#     print("welcome")
# else:
# #     print("Username and password is invalid")
# data = ['ram','sita', 'hari']
# for user in data:
#     print(user, end=',')
#
# x = 10
# # while x <= 20:
# #     print(x)
# #     x += 1
#
# users = ['rama', 'sita', 'gita']
# x = 0
# while x < 2:
#     print(users[x], end=' ')
#     x += 1
#
# x=0
# y=0
# for x in range(1,11):
#     for y in range(1,11):
#         print(x*y, end='\t')
#     print('\t')

# num = int(input('Enter any number: '))
# x=0
# y=0
# for x in range(1, 11):
#     for y in range(1, num + 1):
#         print(f"{x * y}", end="")
#     print('\t')

# def add(x,y):
#     print(x+y)
# add()20,40

import calculator
print(calculator.add(20,40))


