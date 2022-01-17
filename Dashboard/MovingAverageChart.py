"""
    File name: MovingAverageClass.py
    Author: Michael Hopkins
    Date created: 1/15/2020
    Date last modified: 1/16/2020
    Python Version: 3.10
"""

import pandas as pd


class StockChart:

    def __init__(self, file, time_period):
        """
            StockChart init
            df: dataframe read in by pandas from specified file
            assembled_chart: resulting dataframe after moving average operation and
                changing columns and rows to desired format
        """
        self.df = pd.read_csv(file)
        self.assembled_chart = self.assemble_chart(time_period)

    @staticmethod
    def moving_average(i, list):
        """
            moving_average
            description: calculates the two day moving average
            i: index of the list you are at
            list: the list the average is calculated form
        """
        return (list[i - 1] + list[i]) / 2

    def assemble_chart(self, time_period):
        """
            assemble_chart
            description: initalizes two day average arrays for each stock
                and zips together the unique dates and prices for each day to assemble the new dataframe
            time_period: The amount of days covered by the data in data.csv
        """
        ibm_average = [0]
        aapl_average = [0]
        msft_average = [0]
        dates = []
        # Grab the unique dates for the chart later
        dates = self.df.Date.unique()
        # Query dataframe and change to numpy to allow easier traversal
        ibm = self.df.query("Symbol == 'IBM'").Price.to_numpy()
        aapl = self.df.query("Symbol == 'AAPL'").Price.to_numpy()
        msft = self.df.query("Symbol == 'MSFT'").Price.to_numpy()
        # Skip the first day as we don't have data from the previous day
        for i in range(1, time_period):
            ibm_average.append(self.moving_average(i, ibm))
            aapl_average.append(self.moving_average(i, aapl))
            msft_average.append(self.moving_average(i, msft))
        # zip together to match desired chart format
        list_chart = list(zip(dates, ibm, aapl, msft, ibm_average, aapl_average, msft_average))
        # convert to dataframe with proper headers
        chart = pd.DataFrame(list_chart, columns=['Date', 'IBMClosePx', 'AAPL ClosePx', 'MSFT ClosePx',
                                                  'IBM 2DMovingAvg', 'AAPL 2DMovingAvg', 'MSFT 2DMovingAvg'])
        return chart
