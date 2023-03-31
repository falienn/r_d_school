# 1. Написати функцію, яка повертає тільки однакові елементи двох множин.

def inter(set1, set2):
    return set1.intersection(set2)


print(inter({1, 2, 3, 4}, {3, 4, 5, 6}))


# 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.

def union_(set1, set2):
    return set1.union(set2)


print(union_({1, 2, 3, 4}, {3, 4, 5, 6}))

# 3. (необов'язкове виконання) Перетворити всі елементи списку типу string в верхній регістр, використовуючи map.

lst = ["qwe", "ewq", "www"]
upper_lst = []


def upper_case(word):
    return word.upper()


for i in map(upper_case, lst):
    upper_lst.append(i)
print(upper_lst)

lst_upper = list(map(lambda elem: elem.upper(), lst))
print(lst_upper)

# 4. (необов'язкове виконання) Вивести всі елементу масиву, які є числом, використовуючи filter.

lst1 = ['qwe', '22', '33', '3q3', ]
lst2 = ['qwe', 22, 33, 'q3', 3.14]


def numbers(number):
    return isinstance(number, (int, float))


number_lst = list(filter(numbers, lst2))
print(number_lst)

lst_number = list(filter(lambda elem: elem.isdigit(), lst1))
print(lst_number)
