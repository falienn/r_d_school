import json
import time
import logging

# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string
# (при записі в файл) і JSON string в dict (при читанні із файлу).
# Файл слід оновлювати після кожної успішної операції add або delete.
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
#
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

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
    phonebook[name] = phone
    save_phonebook(phonebook)
    print(f"{name} успешно добавлен в телефонную книгу.")


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
