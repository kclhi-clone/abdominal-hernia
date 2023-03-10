# caliber, 2021.

import sys, csv, re

codes = ["7H16000","7H16100","7H16111","7H16200","7H16.00","7H16y00","7H16z00","7H17000","7H17100","7H17200","7H17300","7H17.00","7H17.11","7H17y00","7H17z00","J330100","J331100","J332100","J333100","J33..12","J33z100"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-hernia-incision---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-hernia-incision---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-hernia-incision---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
