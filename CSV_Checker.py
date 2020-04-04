import csv
from os import listdir
import re
import time


def csv_checker():
    files_list = get_all_check_filenames()
    account_list = get_account_name_list()
    header_list = get_headers_parameter()

    for file in files_list:
        row_count = 0
        correct_row_count = 0
        incorrect_row_count = 0
        total_units = 0
        total_value = 0.00
        total_store = 0
        total_dc = 0
        total_base_value = 0
        total_base_units = 0

        file_content = load_csv_file(file)
        incorrect_rows = []
        print("<-------------------------------------------------------------------------------->")
        print(" File name: " + file)

        for row in file_content:

            if row_count != 0:

                ch_b_date = check_date_format(row[0])  # Begin date
                ch_e_date = check_date_format(row[1])  # End date
                ch_ean = check_whole_number_format(row[2])  # EAN
                ch_upc = check_whole_number_format(row[3])  # UPC
                ch_u = check_whole_number_format(row[8])  # Total Sales Volume
                ch_v = check_decimal_number_format(row[9])  # Total Sales Amount
                ch_s = check_whole_number_format(row[10])  # Store On Hand Volume Units
                ch_dc = check_whole_number_format(row[11])  # DC on Hand Volume Units
                ch_b_u = check_whole_number_format(row[12])  # Baseline Sales Amount
                ch_b_v = check_whole_number_format(row[13])  # Baseline Sales Volume Units

                if ch_b_date & ch_e_date & ch_ean & ch_upc & ch_u & ch_v & ch_s & ch_dc & ch_b_u & ch_b_v:
                    correct_row_count = correct_row_count + 1
                    total_units = total_units + int(row[8])
                    total_value = total_value + float(row[9])
                    total_store = total_store + int(row[10])
                    total_dc = total_dc + int(row[11])
                    total_base_value = total_base_value + int(row[12])
                    total_base_units = total_base_units + int(row[13])
                else:
                    incorrect_row_count = incorrect_row_count + 1
                    incorrect_rows.append(row)

            row_count = row_count + 1

        print(" Units: " + str(total_units) + "\tValue: " + str(total_value) + "\tStore stock: " + str(total_store) +
              "\tDC stock: " + str(total_dc))

        print(" Base Value: " + str(total_base_value) + "\tBase Units: " + str(total_base_units))

        print("<-------------------------------------------------------------------------------->\n")

    """
        if incorrect_row_count > 0:
            print("Incorrect rows:\n")
            headers_row = ""

            for column in header_list:
                headers_row = headers_row + column + '\t'
            print(headers_row)

            for row in incorrect_rows:
                row_data = ""
                for column in row:
                    row_data = row_data + column + '\t'
                print(row_data)

    return True
    """


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


def check_date_format(date):
    match_date_format = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', date)
    if match_date_format is not None:
        return True
    else:
        return False


def check_whole_number_format(number):
    match_number_format = re.match('[0-9]', number)
    if match_number_format is not None:
        return True
    else:
        return False


def check_decimal_number_format(number):
    try:
        val = float(number)
        return True
    except ValueError:
        return False


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


startTime = time.time()
csv_checker()
print('The script took {0} second!'.format(round(time.time() - startTime, 2)))
