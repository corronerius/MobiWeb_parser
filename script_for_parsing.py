#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os
import datetime

application_window = tk.Tk()

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('csv files', '.csv'), ('xls files', '.xls'),('xlsx files', '.xlsx')]

# Ask the user to select a single file name.
file_path = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)

df = pd.read_csv(file_path,sep=None,skipfooter=1,engine='python')#,error_bad_lines=False)

cols = [0,1,5]

df.drop(df.columns[cols],axis=1,inplace=True)

s = df['MNC'].str.split(' ').apply(pd.Series, 1).stack()

s.index = s.index.droplevel(-1) # to line up with df index

s.name = 'MNC' # needs a name to join

del df['MNC']

df = df.join(s)

df = df.reindex(columns=['MCC','MNC','Price(EUR)'])

filepath_to = file_path.split('.')[0]+'_COOCKED.'+file_path.split('.')[1]

df.to_csv(filepath_to,encoding='utf-8',index=False)

