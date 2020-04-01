import csv
from os import listdir
import re


# from prettyTable import PrettyTable


def csv_checker():
    file_content = load_csv_file('test.csv')
    row_count = 0
    correct_date_count = 0
    incorrect_date_count = 0
    for row in file_content:
        if row_count != 0:
            if check_date_format(row[0]):
                correct_date_count = correct_date_count + 1
            else:
                print(str(row_count) + " " + row + " Incorrect!")
                incorrect_date_count = incorrect_date_count + 1

        row_count = row_count + 1

    print("Correct date count: " + str(correct_date_count))
    print("Incorrect date count: " + str(incorrect_date_count))

    return True


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

        return list(reader)


def get_all_check_filenames():
    filenames = listdir('Check/')
    suffix = ".csv"
    return [filename for filename in filenames if filename.endswith(suffix)]


def check_date_format(date):
    match_date_format = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', date)
    if match_date_format is not None:
        return True
    else:
        return False


csv_checker()
