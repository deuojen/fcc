import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    np.set_printoptions(formatter={'all': lambda x: "{:.7f}".format(x)})
    # pd.set_option("display.precision", 9)
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lr_1880_2012 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), lr_1880_2012.slope *
             range(1880, 2051, 1) + lr_1880_2012.intercept)

    # Create second line of best fit
    lr_2000_2012 = linregress(df.query('Year >= 2000')['Year'],
                              df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), lr_2000_2012.slope *
             range(2000, 2051, 1) + lr_2000_2012.intercept)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

    # # Read data from file
    # np.set_printoptions(formatter={'all':lambda x: "{:.7f}".format(x)})
    # # pd.set_option("display.precision", 9)
    # df = pd.read_csv('epa-sea-level.csv')

    # # Create scatter plot
    # plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # # Create first line of best fit
    # lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # xA = np.arange(df['Year'].min(),2050,1)
    # yA = xA*lineA.slope + lineA.intercept
    # print(yA)
    # plt.plot(xA,yA)

    # # Create second line of best fit
    # df_2000 = df[df['Year'] >= 2000]

    # lineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    # xB = np.arange(2000,2050,1)
    # yB = xB*lineB.slope + lineB.intercept

    # plt.plot(xB,yB)

    # # Add labels and title
    # plt.xlabel('Year')
    # plt.ylabel('Sea Level (inches)')
    # plt.title('Rise in Sea Level')

    # # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    # return plt.gca()
