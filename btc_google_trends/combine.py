import pandas as pd
import matplotlib.pyplot as plt
import os

# 2019 csv file has an extra blank line at the beginning
# Class that manages the importing of csv data from the current directory
class Import:
    def __init__(self):
        self.path = os.getcwd()
        self.data = dict()
        self.combined = pd.DataFrame()
        self.df = pd.DataFrame()
        self.files = list()

    def read_csv(self):
        # Get list of files in current directory
        for i in os.listdir(self.path):
            if i[-3:] == "csv":
                self.files.append(i)
        # Read csv files from list of names in files and do not use index
        for i in self.files:
            self.data[i] = pd.read_csv(i, usecols=None,index_col=None)

    def clean_and_combine(self):
        # Iterate over the files in self.files and clean the data
        for i in self.files:
            # Drop the first row of the data frame
            df = self.data[i]
            self.data[i] = df.drop(df.index[0])
            # Concatenate each data frame into self.df 
            self.df = pd.concat([self.df, self.data[i]])

    def import_data(self):
        self.combined = pd.read_csv("combined.csv",usecols=None,index_col=None)
        print(self.combined)

    def save_csv(self):
        self.df.to_csv("combined.csv")

class Analyze:
    def __init__(self) -> None:
        pass

if __name__ == '__main__':
    # data = Import()
    # data.read_csv()
    # data.clean_and_combine()
    # data.save_csv()
    data = Import()
    data.import_data()



# Drop first two lines of a pandas data frame 
# df = pd.read_csv('data.csv')
# df = df.drop(df.index[0])
# df = df.drop(df.index[0])
# df.to_csv('data.csv')


