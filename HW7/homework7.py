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
        print("Такий запис вже існує")


def delete(phone_book, name):
    if name in phone_book:
        del phone_book[name]


def list_(phone_book):
    lst = []
    for elem in phone_book.keys():
        lst.append(elem)
    return lst


def show(phone_book, name):
    return phone_book[name]


add(phone_book_1, "Vitalii", 123123123)
add(phone_book_1, "Vitalii", 123123123)
add(phone_book_1, "Vitya", 123123123)
print(phone_book_1)
print(list_(phone_book_1))
delete(phone_book_1, "Vitya")
print(list_(phone_book_1))
print(show(phone_book_1, "Vitalii"))
