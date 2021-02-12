import csv


def count_people_by_name(name, filename):
    count_pessoas = 0
    with open(filename, 'r') as f:
        for p in csv.DictReader(f):
            if p['nome'] == name:
                count_pessoas += 1
    return count_pessoas
