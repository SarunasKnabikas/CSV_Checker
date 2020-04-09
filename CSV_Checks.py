import re


def check_date_format(date):
    match_date_format = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', date)
    if match_date_format is not None:
        return True
    else:
        return False


def check_column_count(row, expected_column_number):
    column_number = 0
    for column in row:
        column_number = column_number + 1

    if column_number == expected_column_number:
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


def check_if_exist_in_list(value, value_list):
    if value in value_list:
        return True
    else:
        return False


def check_for_duplicates(list_of_elements):
    ''' Check if given list contains any duplicates '''
    if len(list_of_elements) == len(set(list_of_elements)):
        return False
    else:
        return True


def check_text(value_to_check, text):
    if value_to_check == text:
        return True
    else:
        return False


def check_if_lists_equal(listToCheck, mainList):
    if listToCheck == mainList:
        return True
    else:
        return False
