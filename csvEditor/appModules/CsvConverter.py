import csv


class CsvConverter:
    @staticmethod
    def edit_file(file_url: str, delimiter: str = ',', quoting: int = 1,
                  encodings: tuple = ('utf-8', 'utf-8'), dict=None):
        with open(file_url, newline='', mode='r', encoding=encodings[0]) as csvfile:
            csvfile.seek(0)
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
            csv.register_dialect('dialect_name', delimiter=delimiter, quoting=quoting, skipinitialspace=True,
                                 lineterminator='\n')
            if dict:
                with open(dict + '/' + file_url.split('/')[-1], mode='w', encoding=encodings[1]) as file:
                    writer = csv.writer(file, dialect='dialect_name')
                    for row in reader:
                        writer.writerow(row)
            else:
                with open(file_url[:-4] + '_new.csv', mode='w', encoding=encodings[1]) as file:
                    writer = csv.writer(file, dialect='dialect_name')
                    for row in reader:
                        writer.writerow(row)
                        print(row)
