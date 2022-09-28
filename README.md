# COVID-19 Data Visualizer


## Description

COVID-19-Data-Visualizer is a Python program that displays and compares COVID-19 vaccination rates and cases of two regions in Saskatchewan, Canada from a start and end date. This project is used to compare, contrast and find patterns of the attitudes of Saskatchewanians towards vaccines because of the number of COVID-19 Cases.

Note: This COVID-19 Data is no longer collected by the Government of Saskatchewan

## Getting Started

### Dependencies

Python Libraries Used: datetime, pandas, seaborn and matplotlib.


### Executing program

* How to run the program

1. Preprocess data of COVID-19 Cases and Vaccination Rates in SK(not required, files are already availble in repo)
run preprocess_data.py <dataFileName.csv>
2. Collect parameters for visualization (regions and start and end date) run plot_data.py sys.argv[1] = name of SK cases data file sys.argv[2] = name of SK vaccine data file
3. plot data run plot_data.py Commandline Parameters: 2 sys.argv[0] = name of file to read sys.argv[1] = name of graphics file to create


## Authors

Puneet Sandher 


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [PUNEET SANDHER] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
