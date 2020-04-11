import csv
import time
import shutil
import CSV_Checks
import CSV_Params
import datetime
from datetime import datetime


def row_check(row, account_list, exp_column_number, row_number, ean_list, file_name):
    begin_date = datetime.strptime(row[0], '%Y-%m-%d').date()
    end_date = datetime.strptime(row[1], '%Y-%m-%d').date()
    results = [True, ""]
    if row_number == 0:
        if not CSV_Checks.check_column_count(row, exp_column_number):
            results[0] = False
            results[1] = "Comma error."
            return results
    else:
        if not CSV_Checks.check_column_count(row, exp_column_number):
            results[0] = False
            results[1] = 'Comma error.'
            return results
        if not CSV_Checks.check_date_format(row[0]):  # Begin date
            results[0] = False
            results[1] = 'Begin date format incorrect.'
            return results
        if not datetime.strptime(row[0], '%Y-%m-%d').date().weekday() == 6:  # Begin date weekday check

            results[0] = False
            results[1] = 'Begin date in not Sunday.'
            return results
        if not CSV_Checks.check_date_format(row[1]):  # End date
            results[0] = False
            results[1] = 'End date format incorrect.'
            return results
        if not datetime.strptime(row[1], '%Y-%m-%d').date().weekday() == 5:  # End date
            results[0] = False
            results[1] = 'End date is not Saturday.'
            return results
        if not CSV_Checks.check_whole_number_format(row[2]):  # EAN
            results[0] = False
            results[1] = 'EAN format is incorrect.'
            return results
        if not CSV_Checks.check_if_exist_in_list(row[2], ean_list):  # Does EAN exist
            results[0] = False
            results[1] = 'EAN is not in DB.'
            return results
        if not CSV_Checks.check_count_in_list(row[2],
                                              CSV_Params.get_check_csv_ean_list(
                                                  str(file_name))):  # Checks EAN for duplicates
            results[0] = False
            results[1] = 'EAN is duplicated.'
            return results
        if row[3] == '':  # UPC
            results[0] = False
            results[1] = 'UPC is empty.'
            return results
        if not CSV_Checks.check_text(row[4], 'ABC'):  # Prod Desc Retailer
            results[0] = False
            results[1] = 'Product description is not ABC.'
            return results
        if not CSV_Checks.check_text(row[5], 'GBP'):  # Currency
            results[0] = False
            results[1] = 'Currency not GBP.'
            return results
        if not CSV_Checks.check_text(row[6], 'UN'):  # UOM
            results[0] = False
            results[1] = 'UOM is not UN.'
            return results
        if not CSV_Checks.check_if_exist_in_list(str(row[7]), account_list):  # Retailer
            results[0] = False
            results[1] = 'Retailer is not in account list.'
            return results
        if not CSV_Checks.check_whole_number_format(row[8]):  # Total Sales Volume
            results[0] = False
            results[1] = 'Units figure format incorrect.'
            return results
        if not CSV_Checks.check_decimal_number_format(row[9]):  # Total Sales Amount
            results[0] = False
            results[1] = 'Value figure format incorrect.'
            return results
        if not CSV_Checks.check_whole_number_format(row[10]):  # Store On Hand Volume Units
            results[0] = False
            results[1] = 'Store stock figure format incorrect.'
            return results
        if not CSV_Checks.check_whole_number_format(row[11]):  # DC on Hand Volume Units
            results[0] = False
            results[1] = 'DC stock figure format incorrect.'
            return results
        if not CSV_Checks.check_whole_number_format(row[12]):  # Baseline Sales Amount
            results[0] = False
            results[1] = 'Base Value figure format incorrect.'
            return results
        if not CSV_Checks.check_whole_number_format(row[13]):  # Baseline Sales Volume Units
            results[0] = False
            results[1] = 'Base Units figure format incorrect.'
            return results
        else:
            results[0] = True
            return results


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
                    row_check_results = row_check(row, account_list, expected_column_number, row_count, ean_list, file)
                    if row_check_results[0]:

                        correct_row_count = correct_row_count + 1
                        total_units = total_units + float(row[8])
                        total_value = total_value + float(row[9])
                        total_store = total_store + float(row[10])
                        total_dc = total_dc + float(row[11])
                        total_base_value = total_base_value + float(row[12])
                        total_base_units = total_base_units + float(row[13])
                    else:
                        row.append(row_check_results[1])
                        incorrect_row_count = incorrect_row_count + 1
                        incorrect_rows.append(row)
                else:
                    row.append('Incorrect headers!')
                    incorrect_row_count = incorrect_row_count + 1
                    incorrect_rows.append(row)

            row_count = row_count + 1

        if incorrect_row_count == 0:
            print(
                " File name: " + file + "\t\t\tRow count: " + str(
                    row_count) + "\t\t\t ===> OK <===" + "\t\t\tUnits: " + str(
                    round(total_units, 0)) + "\tValue: " + str(
                    round(total_value, 2)) + "\tStore stock: " + str(round(total_store, 0)) +
                "\tDC stock: " + str(round(total_dc, 0)) + " Base Value: " + str(
                    round(total_base_value, 2)) + "\tBase Units: " + str(
                    round(total_base_units, 0)))

            shutil.move('Check/' + file, 'Correct/' + file)
        else:
            with open('Error/' + file, 'w', newline='') as errorFile:
                writer = csv.writer(errorFile)
                writer.writerows(incorrect_rows)
                print(" File name: " + file + "\t\t\tRow count: " + str(row_count) + ' \t\t\tErrors in rows: ' + str(
                    incorrect_row_count) + "\t\t\t===> Error file saved. <===")

    return True


startTime = time.time()
csv_checker()
print('The script took {0} seconds!'.format(round(time.time() - startTime, 3)))
