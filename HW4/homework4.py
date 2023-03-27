# 1.  Створити програму, яка буде очікувати введення тексту від користувача
#     і повідомляти — чим є введений текст “числом” чи “словом”.

text_user = input(">>> ")

if text_user.isdigit():
    print("число")
    # 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
    if int(text_user) % 2 == 0:
        print("парне")
    else:
        print("не парне")
elif text_user.isalpha():
    print("слово")
    # 3. Якщо це “слово”, програма має вказати його довжину.
    print(f"довжина слова > {len(text_user)}")
else:
    print("нічого")

# 4.  (необов'язкове виконання) Створити програму, яка буде очікувати введення тексту від користувача
#     і повідомляти якого типу введені дані. Використати match, case і вбудовані функції Python

user_input = "qwe"
# user_input = 123
# user_input = [1,2,3]

match user_input:
    case int():
        print(int)
    case str():
        print(str)
    case list():
        print(list)
    case _:
        print(type(user_input))
