# 1.    Створити функцію, яка призводить аргумент до степені і повертає його,
#       степінь теж повинна бути аргументом.

def power(a, b):
    return a ** b


print(power(2, 4))


# 2. Створити функцію, яка сумує будь-яку кількість аргументів і повертає результат.

def sum__1(*args):
    sum_args = 0
    for i in args:
        sum_args += i
    return sum_args


def sum__2(*args):
    sum_args = sum(args)
    return sum_args


print(sum__1(12, 13, 12, 11))
print(sum__2(12, 13, 12, 11))

# 3. (необов'язкове виконання) Знайти найбільший елемент масиву

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# — використати built-in функцію
print(max(list_))


# — створити свою функцію
def max_elem_2(lists):
    max_ = lists[0]
    for i in lists:
        if i > max_:
            max_ = i
    return max_


print(max_elem_2(list_))

# — використати лямбда функцію
max_elem_3 = lambda lists: max(lists)

print(max_elem_3(list_))
