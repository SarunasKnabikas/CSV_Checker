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
    account_list = load_csv_file("Accounts.csv", True)
    return account_list


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