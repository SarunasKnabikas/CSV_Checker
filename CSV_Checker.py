import csv
import time
import shutil
import CSV_Checks
import CSV_Params


def csv_checker():
    files_list = CSV_Params.get_all_check_filenames()
    account_list = CSV_Params.get_account_name_list()
    header_list = CSV_Params.get_headers_parameter()

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

        for row in file_content:

            if row_count != 0:

                ch_b_date = CSV_Checks.check_date_format(row[0])  # Begin date
                ch_e_date = CSV_Checks.check_date_format(row[1])  # End date
                ch_ean = CSV_Checks.check_whole_number_format(row[2])  # EAN
                ch_upc = CSV_Checks.check_whole_number_format(row[3])  # UPC

                ch_prod_desc = row[4]
                ch_curr = row[5]
                ch_uom = row[6]
                ch_retail = row[7]

                ch_u = CSV_Checks.check_whole_number_format(row[8])  # Total Sales Volume
                ch_v = CSV_Checks.check_decimal_number_format(row[9])  # Total Sales Amount
                ch_s = CSV_Checks.check_whole_number_format(row[10])  # Store On Hand Volume Units
                ch_dc = CSV_Checks.check_whole_number_format(row[11])  # DC on Hand Volume Units
                ch_b_u = CSV_Checks.check_whole_number_format(row[12])  # Baseline Sales Amount
                ch_b_v = CSV_Checks.check_whole_number_format(row[13])  # Baseline Sales Volume Units

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

        if incorrect_row_count == 0:
            print(
                " File name: " + file + "\t\t\t ===> OK <===" + "\t\t\tUnits: " + str(total_units) + "\tValue: " + str(
                    total_value) + "\tStore stock: " + str(total_store) +
                "\tDC stock: " + str(total_dc) + " Base Value: " + str(total_base_value) + "\tBase Units: " + str(
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
print('The script took {0} seconds!'.format(round(time.time() - startTime, 2)))
