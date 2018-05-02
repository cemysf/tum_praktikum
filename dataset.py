#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


class Dataset:
    df_data: pd.DataFrame = None
    df_labels: pd.DataFrame = None

    def __init__(self, folderpath):
        self.folderpath = folderpath


