# 1.    Створити телефонну книгу, яка матиме наступні команди:
#           stats: кількість записів
#           add: додати запис
#           delete <name>: видалити запис за іменем (ключем)
#           list: список всіх імен в книзі
#           show <name>: детальна інформація по імені
#       Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.


phone_book_1 = {}


def stats(phone_book):
    return len(phone_book)


def add(phone_book, name, number):
    if name not in phone_book:
        phone_book[name] = number
    else:
        return "Такий запис вже існує"


def delete(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        return f"Запис {name} видалено"


def list_(phone_book):
    lst = []
    for elem in phone_book.keys():
        lst.append(elem)
    return lst


def show(phone_book, name):
    return phone_book[name]


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
    match choice:
        case "1":
            print(operation[choice](phone_book_1))
        case "2":
            name = input("Введіть ім'я абонента ->")
            number = input("Введіть номер абонента ->")
            operation[choice](phone_book_1, name, number)
        case "3":
            name = input("Введіть ім'я абонента ->")
            print(operation[choice](phone_book_1, name))
        case "4":
            print(operation[choice](phone_book_1))
        case "5":
            name = input("Введіть ім'я абонента ->")
            print(operation[choice](phone_book_1, name))
        case "6":
            break
        case _:
            print("Повторіть вибір правильно")
