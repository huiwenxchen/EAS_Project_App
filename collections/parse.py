import csv
import os

def update_file(filename):

    basename = os.path.splitext(filename)[0]
    new_file = 'updated' + basename + '.csv'

    with open(filename, 'r') as csv_file, open(new_file, 'w', newline='') as updated_csv_file:

        # create a DictReader object and a DictWriter object
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames + ['Museum']
        csv_writer = csv.DictWriter(updated_csv_file, fieldnames)

        museum = {"cleveland": "Cleveland Art Museum", "met": "The Metropolitan Museum of Art", "smithsonian": "The Freer Gallery of Art"}
        # write the updated header row to the new CSV file
        csv_writer.writeheader()
        # loop through each row in the CSV file
        for row in csv_reader:
            # add a new column with the same value to each row
            row['Museum'] = museum[basename]

            # write the updated row to the new CSV file
            csv_writer.writerow(row)



update_file('cleveland.csv')
update_file('met.csv')
update_file('smithsonian.csv')