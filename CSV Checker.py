import csv

def csv_Checker():
    with open('Check/test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        observed_output = []
        expected_output = []
        i = 1
        for row in reader:
            print(row)

def expected_csv_headers():
    with open('Parameters/Headers.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = reader.next()
        return i
