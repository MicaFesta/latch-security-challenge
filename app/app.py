import re
from utils.files import open_file
from utils.logger import *


def get_name_info(name, file_name='./dataset/nombres-permitidos.csv'):
    file = open_file(file_name, ';')
    for row in file:
        if row[0].lower() == name.lower():
            fila_dict = {
                "Name": row[0],
                "Gender": row[1],
                "Origin": row[2],
                "Meaning": row[3]
            }
            return fila_dict


def find_name_by_condition(letter=None, pattern=None, file_name='./dataset/nombres-permitidos.csv'):
    if pattern is None and letter is None:
        log.info('A letter or pattern was not provided to perform the search.')
        return 'We need a pattern or letter to be able to search.'
    regex_letter = ''
    regex_pattern = ''
    if letter is not None:
        regex_letter = str(rf'^{re.escape(letter)}')
    if pattern is not None:
        regex_pattern = str(rf'.*{re.escape(pattern)}.*')

    condition_for_letter_and_pattern = re.compile(regex_letter + regex_pattern)

    filtered_names = []
    file = open_file(file_name, ';')

    for row in file:
        if condition_for_letter_and_pattern.search(row[0].lower()):
            filtered_names.append(row)
    return filtered_names


def calculate_count_names_per_gender(file_name='./dataset/nombres-permitidos.csv'):
    names_per_gender = {}

    file = iter(open_file(file_name, ';'))
    next(file)

    for row in file:
        gender = row[1]
        if gender in names_per_gender:
            names_per_gender[gender] += 1
        else: names_per_gender[gender] = 1
    return names_per_gender


def get_more_used_names(file_name = './dataset/dataset_Nombres.csv'):
    names_and_quantity = {}

    file = iter(open_file(file_name, ','))
    next(file)

    for row in file:
        name = row[1]
        quantity = int(row[3])
        if name in names_and_quantity and name != 'COMPLETAR':
            names_and_quantity[name] += quantity
        else: names_and_quantity[name] = quantity

    all_names = sorted(names_and_quantity.items(), key=lambda x: x[1], reverse=True)

    return all_names[:10]


def is_approved_name(name, file_name='./dataset/nombres-permitidos.csv'):
    full_name = name.split(' ')
    values = {}
    for name in full_name:
        if get_name_info(name, file_name) is not None:
            values[name] = True
        else: values[name] = False
    return values
