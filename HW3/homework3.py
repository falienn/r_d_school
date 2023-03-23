# 1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.

print("I love Python " * 42)

# 2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.


MY_YEAR = 1996
current_year = 2023
month = 12
age_in_month = (current_year - MY_YEAR) * month
print(age_in_month)

# 3.  Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
#     Підказка: використовуючи арифметичні оператори та/або приведення типів).


age_in_years = age_in_month / month
print(int(age_in_years))

# 4.  Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”,
#     де на замість пропусків буде підставлятись ваші імʼя та вік.
#     Значення віку слід брати зі змінної age_in_years.


my_name = "Vitalii"
my_age = f"My name is {my_name}. I’m {int(age_in_years)} years old"
print(my_age)

# 5.  Створити змінну зі значенням 1. Використовуючи оператори порівняння,
#     порівняти її із будь-якими іншими значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.


one = 1
two = 2
tree = 3
four = 4
five = 5
six = 6

print(one > two)
print(one < tree)
print(one > four)
print(one < five)
print(one > six)

# 6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”

a, b, c = 2, 5, 6
d = str(a) + str(b) + str(c)
print(d, type(d))
