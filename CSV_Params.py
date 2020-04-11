import csv
from os import listdir


def get_headers_parameter():
    param_file = load_csv_file("Headers.csv", True)
    headers_list = next(iter(param_file))
    return headers_list


def get_column_number_parameter():
    param_file = load_csv_file("Headers.csv", True)
    headers_list = next(iter(param_file))
    header_count = 0
    for column_count in headers_list:
        header_count = header_count + 1
    return header_count


def get_account_name_list():
    account_list = []
    account_file = load_csv_file("Accounts.csv", True)
    for row in account_file:
        account_list.extend(row)

    return account_list


def get_ean_list():
    ean_list = []
    ean_file = load_csv_file("Ean_list.csv", True)
    for row in ean_file:
        ean_list.extend(row)

    return ean_list


def get_check_csv_ean_list(file_name):
    ean_list = []
    check_file = load_csv_file(file_name)
    for row in check_file:
        ean_list.append(str(row[2]))
    return ean_list


def load_csv_file(filename, param=False):
    if param:
        folder = "Parameters/"
    else:
        folder = "Check/"

    with open(folder + filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        return list(reader)


def get_all_check_filenames():
    filenames = listdir('Check/')
    suffix = ".csv"
    return [filename for filename in filenames if filename.endswith(suffix)]
