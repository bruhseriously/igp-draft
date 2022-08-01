import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
coh_csv = Path.cwd()/'csv_reports'/'Cash on Hand.csv'

def cashonhand_function(forex):
    if coh_csv.exists():
        with coh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            day = []
            cash = []
            next(reader)
            for row in reader:
                day.append(float(row[0]))
                cash.append(float(row[1]) * forex)
    