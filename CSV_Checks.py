import re


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


def check_if_exist_in_list(value, value_list):
    if list.count(value_list) == 1:
        return True
    else:
        return False


def check_if_duplicates_1(list_of_elems):
    ''' Check if given list contains any duplicates '''
    if len(list_of_elems) == len(set(list_of_elems)):
        return False
    else:
        return True
