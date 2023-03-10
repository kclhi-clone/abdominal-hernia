# caliber, 2021.

import sys, csv, re

codes = ["T19","T19.1","T19.2","T19.3","T19.8","T19.9","T20","T20.1","T20.2","T20.3","T20.4","T20.8","T20.9","T21","T21.1","T21.2","T21.3","T21.4","T21.8","T21.9","T22","T22.1","T22.2","T22.3","T22.8","T22.9","T23","T23.1","T23.2","T23.3","T23.4","T23.8","T23.9","T24","T24.1","T24.2","T24.3","T24.4","T24.8","T24.9","T25","T25.1","T25.2","T25.3","T25.8","T25.9","T26","T26.1","T26.2","T26.3","T26.4","T26.8","T26.9","T27","T27.1","T27.2","T27.3","T27.4","T27.8","T27.9","T97","T97.1","T97.2","T97.3","T97.8","T97.9","T98","T98.1","T98.2","T98.3","T98.8","T98.9"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["procedure-for-abdominal-hernia---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["procedure-for-abdominal-hernia---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["procedure-for-abdominal-hernia---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
