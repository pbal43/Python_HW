# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.

# Создать пустой empty.csv файл.
import csv
filepath = "D:/Programms/Python/pjcts/Python_Homework/"
empty_title = 'empty.csv'
csv_empty = filepath + empty_title
f = open(csv_empty, 'w')
f.close()
# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150

digits_title = 'digits.csv'
csv_digits = filepath + digits_title

with open(csv_digits, 'w', newline="") as digits1_writer:
    writer_dig = csv.writer(digits1_writer)
    for i in range (0, 151):
        writer_dig.writerow([i])

# Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
import names
names_title = 'names.csv'
csv_name = filepath + names_title
with open(csv_name, 'w', newline="") as name_writer:
    writer_names = csv.writer(name_writer)
    for i in range(100):
        x = names.get_full_name()
        writer_names.writerow([x])

# Вариант 1. Создать emails.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
import random
import string
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters.lower()) for _ in range(char_num))
emails_title = 'emails.csv'
csv_emails = filepath + emails_title
with open (csv_emails, 'w', newline="") as emails_writer:
    writer_emails = csv.writer(emails_writer)
    for i in range(100):
        z = random_char(7)+"@gmail.com"
        writer_emails.writerow([z])

# Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.



# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
#
#
# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
#
#
# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
#
#
# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
#
#
# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
#
#
#
#
#
# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.
#
#
#
#
# P.S.
# Задания специально написаны немного запутанно)) Привыкайте.
# Реализация и порядок выполнения каждого задания и внутренних подпунктов заданий любая, особенно в 10 и 11 задании. )) Главное чтобы работало.
