# caliber, 2021.

import sys, csv, re

codes = ["14C3.00","25P2.00","25P..12","25P3.00","25P4.00","25P6.00","7H10.00","7H10y00","7H10z00","7H11000","7H11100","7H11111","7H11200","7H11211","7H11212","7H11213","7H11214","7H11500","7H11600","7H11.00","7H11y00","7H11y11","7H11z00","7H12000","7H12100","7H12200","7H12.00","7H12y00","7H12z00","7H13000","7H13100","7H13200","7H13211","7H13212","7H13213","7H13214","7H13215","7H13.00","7H13.11","7H13y00","7H13z00","7H14100","7H14200","7H14.00","7H14y00","7H14z00","7H15000","7H15100","7H15200","7H15.00","7H15y00","7H15z00","7H18000","7H18100","7H18200","7H18400","7H18.00","7H18.11","7H18y00","7H18z00","7H1C000","7H1C100","7H1C200","7H1C.00","7H1Cy00","7H1Cz00","7H1D100","7H1D200","7H1D.00","7H1Dy00","7H1Dz00","7H1E000","7H1E100","7H1E200","7H1E.00","7H1Ey00","7H1Ez00","J300000","J300300","J300.00","J300z00","J301000","J301100","J301200","J301.00","J301z00","J302000","J302100","J302200","J302300","J302.00","J302z00","J303000","J303011","J303012","J303100","J303200","J303300","J303.00","J303z00","J30..00","J30..14","J30y000","J30y100","J30y200","J30y300","J30y.00","J30yz00","J30z.00","J310000","J310.00","J310z00","J311000","J311.00","J311z00","J312000","J312100","J312.00","J312z00","J313000","J313100","J313200","J313.00","J313z00","J31..00","J31y000","J31y100","J31y200","J31y.00","J31yz00","J31z.00","J320100","J320z00","J321100","J321.00","J321z00","J322100","J322.00","J322z00","J323100","J323.00","J323z00","J32..00","J32..12","J32y100","J32y.00","J32yz00","J32z.00","J330200","J330.00","J330z00","J331200","J331.00","J331z00","J332000","J332200","J332.00","J332z00","J333000","J333200","J333211","J333.00","J333z00","J33..00","J33..11","J33z000","J33z200","J33z.00","J35..00","J36..00","J373.00","J37..00","J37y.00","J37z.00","J381.00","J383.00","J38..00","J38z.00","J3A..00","J3C0.00","J3C1.00","J3C2.00","J3C3.00","J3C..00","J3Cy.00","J3Cz.00","J3D..00","J3...00","J3y0.00","J3y1.00","J3y2.00","J3y3.00","J3y..00","J3yy.00","J3yz.00","J3yz.11","J3z0.00","J3z1.00","J3z2.00","J3z3.00","J3z..00","J3zz.00","Jyu3000","Jyu3200","Jyu3.00","PG8..00"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-hernial-hernia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-hernial-hernia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-hernial-hernia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
