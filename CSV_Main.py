import csv
import time
import shutil
import CSV_Checks
import CSV_Params


def row_check(row, account_list, exp_column_number, row_number, ean_list):
    if row_number == 0:
        if not CSV_Checks.check_column_count(row, exp_column_number):
            return False
    else:
        if not CSV_Checks.check_column_count(row, exp_column_number):
            return False
        if not CSV_Checks.check_date_format(row[0]):  # Begin date
            return False
        if not CSV_Checks.check_date_format(row[1]):  # End date
            return False
        if not CSV_Checks.check_whole_number_format(row[2]):  # EAN
            return False
        if not CSV_Checks.check_if_exist_in_list(row[2], ean_list):  # Does EAN exist
            return False
        if row[3] == '':  # UPC
            return False
        if not CSV_Checks.check_text(row[4], 'ABC'):  # Prod Desc Retailer
            return False
        if not CSV_Checks.check_text(row[5], 'GBP'):  # Currency
            return False
        if not CSV_Checks.check_text(row[6], 'UN'):  # UOM
            return False
        if not CSV_Checks.check_if_exist_in_list(str(row[7]), account_list):  # Retailer
            return False
        if not CSV_Checks.check_whole_number_format(row[8]):  # Total Sales Volume
            return False
        if not CSV_Checks.check_decimal_number_format(row[9]):  # Total Sales Amount
            return False
        if not CSV_Checks.check_whole_number_format(row[10]):  # Store On Hand Volume Units
            return False
        if not CSV_Checks.check_whole_number_format(row[11]):  # DC on Hand Volume Units
            return False
        if not CSV_Checks.check_whole_number_format(row[12]):  # Baseline Sales Amount
            return False
        if CSV_Checks.check_whole_number_format(row[13]):  # Baseline Sales Volume Units
            return True
        else:
            return False


def csv_checker():
    files_list = CSV_Params.get_all_check_filenames()
    account_list = CSV_Params.get_account_name_list()
    header_list = CSV_Params.get_headers_parameter()
    expected_column_number = CSV_Params.get_column_number_parameter()
    ean_list = CSV_Params.get_ean_list()

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

        file_content = CSV_Params.load_csv_file(file)
        incorrect_rows = []

        headers_check = 1

        for row in file_content:
            if row_count == 0:
                if not CSV_Checks.check_if_lists_equal(row, header_list):
                    headers_check = 2
            else:
                if headers_check == 1:

                    if row_check(row, account_list, expected_column_number, row_count, ean_list):

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
                else:
                    incorrect_row_count = incorrect_row_count + 1
                    incorrect_rows.append(row)

            row_count = row_count + 1

        if incorrect_row_count == 0:
            print(
                " File name: " + file + "\t\t\t ===> OK <===" + "\t\t\tUnits: " + str(total_units) + "\tValue: " + str(
                    total_value) + "\tStore stock: " + str(total_store) +
                "\tDC stock: " + str(total_dc) + " Base Value: " + str(
                    round(total_base_value, 2)) + "\tBase Units: " + str(
                    total_base_units))

            shutil.move('Check/' + file, 'Correct/' + file)
        else:
            with open('Error/' + file, 'w', newline='') as errorFile:
                writer = csv.writer(errorFile)
                writer.writerows(incorrect_rows)
                print(" File name: " + file + ' \t\t\tErrors in rows: ' + str(
                    incorrect_row_count) + "\t\t\t===> Error file saved. <===")

    return True


startTime = time.time()
csv_checker()
print('The script took {0} seconds!'.format(round(time.time() - startTime, 3)))
