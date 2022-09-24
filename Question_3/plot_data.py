''''
plot_data.py
  Author(s): Puneet Sandher, Lester Chavez, Matthieu Laroche
  Project: COVID-19 SK Data Visualizer 
  Date of Last Update: Mar 29, 2022

  Functional Summary
      create_name_plot.py reads a CSV file and saves
      a plot based on the data to a PDF file.

     Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of graphics file to create
'''

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as ticktools


def main(argv):

    if len(argv) != 3:
        print("Usage:", "plot_data.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    plot_filename = argv[2]

    #open csv file, if an erorr occurs program exits
    try:
        csv_df = pd.read_csv(csv_filename)
    except IOError as err:
        print("Unable to open csv file",
              csv_filename,
              ": {}".format(err),
              file=sys.stderr)
        sys.exit(-1)

    fig = plt.figure()
    ax = sns.lineplot(x="Date", y="Population", hue="Region", data=csv_df)

    # a max of 5 ticks on the x-axis
    ax.xaxis.set_major_locator(ticktools.MaxNLocator(7))

    #rotate ticks 45 degrees to the right
    plt.xticks(rotation=45, ha='right')
    fig.savefig(plot_filename, bbox_inches="tight")
    #plt.show()


main(sys.argv)
