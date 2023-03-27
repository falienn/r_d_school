# 1.  Створити програму, яка буде очікувати від користувача введення тексту
#     і виведе інформацію по кожному надрукованому символу:
#
#     це “число” + яке воно (парне, непарне),
#     це “буква” + яка вона (велика чи маленька),
#     це “символ”


# ORD_A = 65
# ORD_Z = 90
# ORD_a = 97
# ORD_z = 122
# ORD_0 = 48
# ORD_9 = 57
#
# user_input = "23-q9W5!0"
#
# for i in user_input:
#     if ORD_a < ord(i) < ORD_z:
#         print(f"{i} <- буква маленька")
#     elif ORD_A < ord(i) < ORD_Z:
#         print(f"{i} <- буква велика")
#     elif ORD_0 <= ord(i) <= ORD_9:
#         if int(i) == 0:
#             print(f"{i} <- число не парне (нуль)")
#         elif int(i) % 2 == 0:
#             print(f"{i} <- число парне")
#         else:
#             print(f"{i} <- число не парне")
#     else:
#         print(f"{i} <- символ")

user_input1 = "23-q9W5!0"

for i in user_input1:
    if i.isdigit():
        print(f"{i} <- Число парне" if int(i) % 2 == 0 else f"{i} <- Число не парне")
    elif i.isalpha():
        print(f"{i} <- Буква велика" if i.isupper() else f"{i} <- Буква маленька")
    else:
        print(f"{i} <- Символ")

# 4. (необов'язкове виконання) Надрукувати наступний патерн, використовуючи цикл в циклі
#     1
#     2 2
#     3 3 3
#     4 4 4 4
#     5 5 5 5 5

# str_ = "12345"

# for i, item in enumerate(str_):
#     print(item * (i + 1))

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

# 2.  Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди,
#     поки її виконання не буде перервано вручну.


import time

second = 4.2

while True:
    print("I love Python")
    time.sleep(second)
