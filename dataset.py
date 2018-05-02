#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


class Dataset:
    df_data: pd.DataFrame = None
    df_labels: pd.DataFrame = None

    def __init__(self, folderpath):
        self.folderpath = folderpath


class DatasetKDD99(Dataset):

    def __init__(self, folderpath):
        Dataset.__init__(self, folderpath)
        self.loadDataset()
        self.enumerateStringColumns()

    def loadDataset(self):
        print("Preparing dataset:", self.folderpath)

        ### load data and labels (normal and different attack types)
        self.df_data = pd.read_csv(self.folderpath + "kddcup.data_10_percent.gz", header=None)
        self.df_labels = pd.DataFrame(self.df_data.iloc[:, -1])  ### last column has labels
        self.df_data = self.df_data.iloc[:, :-1]  ### columns until last column

        ### read column names and types
        col_names = []
        col_datatypes = []

        with open(self.folderpath + "kddcup.names") as file:
            next(file)  ### skip first line
            for line in file:
                name, datatype = line.split(": ")
                col_names.append(name)
                col_datatypes.append(datatype.replace(".\n", ""))

        self.df_data.columns = col_names
        self.df_labels.columns = ["labels"]

    ### TODO
