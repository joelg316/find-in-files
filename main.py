import os
import csv

def get_files_in_folder(path, type):
    files = []
    for name in os.listdir(path):
        if name.endswith(type):
            print(name)
            files.append(name)
    return files

def find_text_in_csv(pathname, value1, value2):

    total_line_count = 0
    total_num_hits = 0

    for filename in get_files_in_folder(pathname, ".csv"):
        os.chdir(pathname)
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            num_hits = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    if value1 in row[1] and value2 in row[1]:
                        num_hits += 1
                        print(f'Line {line_count}: {row[1]}')
                    line_count += 1
            print(f'Processed {line_count} lines in {filename}. Found {num_hits} search results containing "{value1}" and "{value2}"')
            total_line_count += line_count
            total_num_hits += num_hits
    print(f'{total_line_count} total lines processed, {total_num_hits} total search results for "{value1}" and "{value2}"')
    return

path = r'C:\Users\joelg\Documents\Cases\Alameda County\04964241 - relay access denied'
searchTerm1 = '166.107.208.247'
searchTerm2 = 'reject'

print(find_text_in_csv(path, searchTerm1, searchTerm2))