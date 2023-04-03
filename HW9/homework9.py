# 1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.


def recursion(n):
    print(f"{n}", end=" ")
    if n == 0:
        return
    return recursion(n - 1)

n = int(input(">>>"))
print(recursion(n))


# 2.    (необов'язкове виконання) Створити програму, яка буде приймати число і
#       друкувати відповідне число в послідовності Фібоначчі, використовуючи рекурсію.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n1 = int(input(">>>"))
print(fibonacci(n1))


# 3.    (необов'язкове виконання) Написати програму,
#       яка буде повертати факторіал введеного числа, використовуючи рекурсію.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n2 = int(input(">>>"))
print(factorial(n2))
