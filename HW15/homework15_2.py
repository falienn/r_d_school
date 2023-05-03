import re

# 2. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.

filename = 'mail.txt'

with open(filename, 'r') as file:
    text = file.read()

    pattern = r'\w.+@\w.+'
    emails = re.findall(pattern, text)


    for email in emails:
        text = text.replace(email, '*@*')

    print(text)
