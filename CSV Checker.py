import csv


def csv_Checker():
    with open('Check/test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        observed_output = []
        expected_output = []
        i = 1
        for row in reader:
            print(row)
            print()


def expected_csv_headers_check(row):
    with open('Parameters/Headers.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = next(reader)

        return i


def expected_csv_column_number_check():
    with open('Parameters/Headers.csv', 'r') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        headers = next(r)
        i = 0
        for column_count in headers:
            i = i + 1
        return i
