'''
main.py
  Author(s): Puneet Sandher, Lester Chavez, Matthieu Laroche, Ethan Katz
  Project: COVID-19 SK Data Visualizer 
  Date of Last Update: Mar 28, 2022

  Functional Summary
      create_name_plot.py takes two processed csv files with vaccine and cases numbers of Saskatchewan by region. Two new csv files are produced with the respective vaccine and cases count for two specific regions in Saskatchewan from a range of time.

     Commandline Parameters: 3
        
        sys.argv[1] = name of SK cases data file
        sys.argv[2] = name of SK vaccine data file
        
'''
import sys
import csv
from datetime import date


def main(argv):
    if len(argv) != 3:
        print("Usage: main.py <processed case_data><processed vaccine data>")
        sys.exit(1)

    cases_file = sys.argv[1]
    vaccine_file = sys.argv[2]

    #open both files, create readers and if an error occurs exit
    try:
        cases_fh = open(cases_file, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(cases_file, err),
              file=sys.stderr)
        sys.exit(1)

    cases_reader = csv.reader(cases_fh)

    try:
        vaccine_fh = open(vaccine_file, encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open names file '{}' : {}".format(vaccine_file, err),
              file=sys.stderr)
        sys.exit(1)
    vaccine_reader = csv.reader(vaccine_fh)

    #the files are no longer updated, but this is the min start and end date in iso format
    min_start_date = date(2020, 8, 4).isoformat()
    max_end_date = date(2022, 2, 6).isoformat()

    start_date = date(1, 1, 1).isoformat()

    print("Enter a start date between the range", min_start_date, "and",
          max_end_date, ". Format YYYY-MM-DD")

    #a while loop is used until user inputs an appropriate start and end date in isoformat 

    while (not (min_start_date <= start_date <= max_end_date)):
        try:
            start_date = input("Enter start date: ")
            temp_start_date = start_date.split('-')
            start_date = date(int(temp_start_date[0]), int(temp_start_date[1]),
                              int(temp_start_date[2])).isoformat()

        except ValueError as err:
            print(f"Incorrect format. Format in YYYY-MM-DD: {err}",
                  file=sys.stderr)

        end_date = date(1, 1, 1).isoformat()

    while (not (start_date <= end_date <= max_end_date)):
        try:
            end_date = input("Enter end date: ")
            temp_end_date = end_date.split('-')
            end_date = date(int(temp_end_date[0]), int(temp_end_date[1]),
                            int(temp_end_date[2])).isoformat()
        except ValueError as err:
            print(f"Incorrect format. Format in YYYY-MM-DD: {err}",
                  file=sys.stderr)

    #an array of all the regions in the data file

    regions = [
        "far north west", "far north central", "far north east", "north west",
        "north central", "north east", "central west", "central east",
        "regina", "saskatoon", "south central", "south east", "south west"
    ]

    #print all the regions for the user to pick
    print("Pick two regions from the following list")
    for region in regions:
        print(region, end=",")
    print("\n")

    region_one = ""
    region_two = ""

    #user will be prompted for region until they pick on that is in the data file
    while (not (region_one in regions)):
        region_one = input("Enter first region: ").lower()

    while (not (region_two in regions) or (region_two == region_one)):
        region_two = input("Enter second region: ").lower()

    #Create two csv files
    #1. case data between the two dates and regions
    #2. vaccine data between the two dates and regions

    #skip the header given in the csv file
    next(cases_reader)

    #open file in write mode
    #write header into file
    #Loop through each row in cases data file and if it is one of the specified regions and between the start and end date then it is written into the new file
    with open('regions_case_data.csv', mode='w') as region_case_file:
        region_cases_writer = csv.writer(region_case_file, delimiter=',')
        header = ['Date', 'Population', 'Region']
        region_cases_writer.writerow(header)
        for row_data_fields in cases_reader:
            record_date = row_data_fields[0]
            region = row_data_fields[2]
            if ((record_date >= start_date)) and (record_date <= end_date):
                if ((region == region_one) or (region == region_two)):
                    cases = row_data_fields[1]
                    region_cases_writer.writerow([record_date, cases, region])

    region_case_file.close()

    next(vaccine_reader)

    with open('regions_vaccines_data.csv', mode='w') as region_vaccine_file:
        region_vaccine_writer = csv.writer(region_vaccine_file, delimiter=',')
        region_vaccine_writer.writerow(header)
        for row_data_fields in vaccine_reader:
            record_date = row_data_fields[0]
            region = row_data_fields[2]
            if ((record_date >= start_date)) and (record_date <= end_date):
                if ((region == region_one) or (region == region_two)):
                    vaccine_count = row_data_fields[1]
                    region_vaccine_writer.writerow(
                        [record_date, vaccine_count, region])
    region_vaccine_file.close()


main(sys.argv)
