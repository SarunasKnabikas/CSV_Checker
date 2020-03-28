import csv
from os import listdir


def csv_checker():
    with open('Check/test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        observed_output = []
        expected_output = []
        i = 1
        for row in reader:
            print(row)
            print()


def get_headers_parameter():
    param_file = load_csv_file("Headers.csv", True)
    headers_list = next(param_file)
    return headers_list


def get_column_number_parameter():
    param_file = load_csv_file("Headers.csv", True)
    headers_list = next(param_file)
    header_count = 0
    for column_count in headers_list:
        header_count = header_count + 1
    return header_count


def load_csv_file(filename, param=False):
    if param == True:
        folder = "Parameters/"
    else:
        folder = "Check/"

    with open(folder + filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        return reader


def get_all_check_filenames():
    filenames = listdir('Check/')
    suffix = ".csv"
    return [filename for filename in filenames if filename.endswith(suffix)]


filenames = get_all_check_filenames()
for name in filenames:
    print(name)
