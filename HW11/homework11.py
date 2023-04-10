# 1. Додати обробку помилок до коду з завдання №7 про телефонну книгу
# (тема: “Колекції та структури даних. Part 1”)
# Повинно бути як мінімум два блоки try except, де їх використовувати — вирішуєте самі.
# 2. (необов'язкове виконання) Написати кастомний Exception клас, MyCustomException,
# який має повідомляти "Custom exception is occurred".

class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        super().__init__(message)


try:
    raise MyCustomException
except MyCustomException as a:
    print(type(a).__name__, a)

print("=" * 50)

phone_book_1 = {}


def stats(phone_book):
    return len(phone_book)


def add(phone_book, name, number):
    if name not in phone_book:
        if len(number) != 9:
            raise MyCustomException("Не коректні данні")
        phone_book[name] = "+380" + number
    else:
        return "Такий запис вже існує"


def delete(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        return f"{name} Видалено"
    else:
        raise KeyError


def list_(phone_book):
    lst = []
    for elem in phone_book.keys():
        lst.append(elem)
    return lst


def show(phone_book, name):
    if name in phone_book:
        return phone_book[name]
    else:
        raise KeyError


operation = {"1": stats,
             "2": add,
             "3": delete,
             "4": list_,
             "5": show}

while True:
    print("""
Оберіть операцію:
1: кількість записів
2: додати запис
3: видалити запис за іменем
4: список всіх імен в книзі
5: детальна інформація по імені
6: Вихід з программи
    """)
    choice = input(">>>")
    if choice == "1":
        print(operation[choice](phone_book_1))
    elif choice == "2":
        name = input("Введіть ім'я абонента ->")
        try:
            number = int(input("Введіть номер абонента без 0 ->"))
            operation[choice](phone_book_1, name, str(number))
        except MyCustomException:
            print("Введіть коректний номер")
    elif choice == "3":
        name = input("Введіть ім'я абонента ->")
        try:
            print(operation[choice](phone_book_1, name))
        except KeyError:
            print("Такого запису не існує")
    elif choice == "4":
        print(operation[choice](phone_book_1))
    elif choice == "5":
        name = input("Введіть ім'я абонента ->")
        try:
            print(operation[choice](phone_book_1, name))
        except KeyError:
            print("Такого запису не існує")

    elif choice == "6":
        break
    else:
        print("Не правільний вибір")

    # match choice:
    #     case "1":
    #         print(operation[choice](phone_book_1))
    #     case "2":
    #         name = input("Введіть ім'я абонента ->")
    #         number = input("Введіть номер абонента ->")
    #         operation[choice](phone_book_1, name, number)
    #     case "3":
    #         name = input("Введіть ім'я абонента ->")
    #         print(operation[choice](phone_book_1, name))
    #     case "4":
    #         print(operation[choice](phone_book_1))
    #     case "5":
    #         name = input("Введіть ім'я абонента ->")
    #         print(operation[choice](phone_book_1, name))
    #     case "6":
    #         break
    #     case _:
    #         print("Не правільний вибір")
