# COVID-19-Data-Visualizer-

COVID-19-Data-Visualizer is a Python program that displays and compares COVID-19 vaccination rates and
cases of two regions in Saskatchewan, Canada from a start and end date.

## Usage

preprocess data
run preprocess_data.py
    sys.argv[0] = name of SK raw data file (e.g. raw_vaccine_by_region_data.csv)
    sys.argv[1] = name of blank csv file to print processed data with only date, region and # of cases or vaccines
  example: python preprocess_data.py raw_vaccine_by_region_data.csv temp.csv


collect parameters (regions and time)
run plot_data.py
    sys.argv[1] = name of SK cases data file
    sys.argv[2] = name of SK vaccine data file

plot data
run plot_data.py 
  Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of graphics file to create

*This COVID-19 Data is no longer collected*

