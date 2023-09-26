import csv


def open_file(file_name, delimiter):
    with open(file_name, mode='r', encoding='utf-8') as csv_file:
        return list(csv.reader(csv_file, delimiter=delimiter))
