import time

#   1.  Написати власний декоратор, задачею якого має бути друк назви функції і часу,
#       коли вона була викликана. Декоратор має працювати для різних функцій однаково.


t = time.localtime()


def my_decorator(func):
    def wraper(*args, **kwargs):
        print(f"{func.__name__} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}")
        func(*args, **kwargs)

    return wraper


@my_decorator
def my_func():
    print("Hello World")


my_func()


@my_decorator
def add(a, b):
    print(a + b)


add(2, 4)


#   2.  (необов'язкове виконання) Написати власний менеджер контексту,
#       задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням коду та
#       після виконання коду, таким чином виділяючи блок коду символами дорівнює.
#       У випадку виникнення будь-якої помилки вона має бути надрукована текстом,
#       проте програма не має завершити своєї роботи.

class MyManager():
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=" * 10)
        return True


# with MyManager():
#     print("Hello World")
#
# with MyManager():
#     my_func()
#
# with MyManager():
#     add(3, 4)


with MyManager():
    raise ZeroDivisionError


#   3.  (необов'язкове виконання) Переписати декоратор із першого завдання,
#       щоб він приймав цілочисельний аргумент `times`.
#       Стільки разів виконувавати друк назви функції і часу, скільки ‘times’ задано.

def my_decorator_1(times):
    def real_decor(func):
        def wraper(*args, **kwargs):
            print((f" {func.__name__} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}") * times)
            return func(*args, **kwargs)

        return wraper

    return real_decor


@my_decorator_1(times=5)
def hello_world():
    print("Hello World")


with MyManager():
    hello_world()
