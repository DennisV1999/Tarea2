import csv

class CsvReader:

    def __init__(self,path):
        self.path = path

    def fileReader(self):
        with open(self.path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for rw in reader:
                if line == 0:
                    print(f'\t{", ".join(rw)}')
                else:
                    print(f'\t{rw[0]}, \t{rw[1]}, \t{rw[2]}')