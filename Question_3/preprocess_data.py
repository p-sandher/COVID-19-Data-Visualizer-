'''
main.py
  Author(s): Puneet Sandher, Lester Chavez, Matthieu Laroche, Ethan Katz
  Project: COVID-19 SK Data Visualizer 
  Date of Last Update: Mar 28, 2022

  Functional Summary
      preprocess.py takes two csv files the raw vaccine or cases for each region in SK and a blank csv file to print processed data. The processed data will only have the date, region and number of cases or vaccines respectively. 
     Commandline Parameters: 3
        
        sys.argv[1] = name of SK raw data file (e.g. raw_vaccine_by_region_data.csv)
        sys.argv[2] = name of blank csv file to print processed data with only date, region and # of cases or vaccines

python preprocess_data.py raw_vaccine_by_region_data.csv temp.csv

'''

import sys
import csv
from datetime import date

#python preprocess_data.py raw_vaccine_by_region_data.csv


def main(argv):

    #Check to ensure user enters correct amount of arguments
    if len(argv) != 3:
        print("Usage: preprocessData.py <raw file name><processed file name")
        sys.exit(1)

    data_filename = sys.argv[1]

    #open data file and create a csv reader
    try:
        data_fh = open(data_filename, encoding="utf-8-sig")

    except IOError as err:
        #in case of error, message is printed and program ends
        print("Unable to open names file '{}' : {}".format(data_filename, err),
              file=sys.stderr)
        sys.exit(1)
    data_reader = csv.reader(data_fh)

    #open blank csv file in write move and create csv writer
    csv_file = open(sys.argv[2], 'w')
    csv_writer = csv.writer(csv_file)
    header = ['Date', 'Population', 'Region']
    csv_writer.writerow(header)
    previous_zone = ''

    #skip the header in raw data files
    next(data_reader)

    for row_data_fields in data_reader:
        given_zone = row_data_fields[1]
        given_zone = given_zone.lower()
        #repetition of zones in raw data, this checks to ensure the last zone checked is not the same as the first
        if (previous_zone != given_zone):
            record_date = row_data_fields[0]

            #the dates in raw data file is "2022/12/12"

            #which is split by '/', converted to int and into isoformat
            temp_record_date = record_date.split('/')

            record_date = date(int(temp_record_date[0]),
                               int(temp_record_date[1]),
                               int(temp_record_date[2])).isoformat()
            given_zone = row_data_fields[1]
            given_zone = given_zone.lower()
            cases = row_data_fields[2]
            previous_zone = given_zone

            #in the raw data 0 cases or vaccines are placed as "", which is changed to 0
            if (cases == ""):
                cases = 0
            csv_writer.writerow([record_date, cases, given_zone])

    csv_file.close()


main(sys.argv)
