import json
import time
import logging
import re

# 1. До завдання, в якому ви реалізовували телефонну книгу,
# додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX


t = time.localtime()


class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        super().__init__(message)

        timestamp = f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}"
        logger = logging.getLogger("my_logger")
        logger.addHandler(logging.FileHandler("error.log"))
        logger.error(f"[{timestamp}] {message}")


try:
    raise MyCustomException
except MyCustomException as e:
    print(e)


def log_decor(func):
    logging.basicConfig(filename="log.txt", level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}"
        logging.info(f'[{timestamp}] {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


@log_decor
def load_phonebook():
    try:
        with open('phonebook.json') as f:
            phonebook = json.load(f)
    except:
        phonebook = {}
    return phonebook


def save_phonebook(phonebook):
    with open('phonebook.json', 'w') as f:
        json.dump(phonebook, f)


@log_decor
def stats_contact():
    return len(phonebook)


@log_decor
def list_contact():
    lst = []
    for elem in phonebook.keys():
        lst.append(elem)
    return lst


@log_decor
def add_contact(name, phone):
    pattern = r"^(?:\+380|380|0)\d{9}$"
    if re.match(pattern, phone):
        phonebook[name] = phone
        save_phonebook(phonebook)
        print(f"{name} успешно добавлен в телефонную книгу.")
    else:
        print("Некоректний номер телефону. Спробуйте ще раз.")


@log_decor
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print(f"{name} успешно удален из телефонной книги.")
    else:
        print(f"{name} не найден в телефонной книге.")


phonebook = load_phonebook()

while True:
    print("Виберіть дію:")
    print("1. Додати контакт")
    print("2. Видалити контакт")
    print("3. Кількість контактів")
    print("4. Список всіх імен в книзі")
    print("5. Вихід")

    choice = input("Введите номер действия: ")
    if choice == "1":
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Введіть ім'я яке треба видалити")
        delete_contact(name)
    elif choice == "3":
        print(stats_contact())
    elif choice == "4":
        print(list_contact())
    elif choice == "5":
        break
    else:
        print("Не корректні данні.")
