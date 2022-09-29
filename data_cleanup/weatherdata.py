#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:35:06 2022

@author: elmaneva
"""

import pandas as pd
import numpy as np
import os

files = os.listdir('/home/elmaneva/koulu/intro_ds/miniprojekti/LeffatLoskatJaLantit/data/saa/')

for i in range(len(files)):
    df = pd.read_csv('/home/elmaneva/koulu/intro_ds/miniprojekti/LeffatLoskatJaLantit/data/saa/' + files[i])
    
    df['year'] = df.Vuosi
    df['month'] = df.Kk
    df['day'] = df.Pv
    
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    
    df['degC'] = df['Ilman lämpötila (degC)'].replace('-', np.NAN)    
    df['degC'] = pd.to_numeric(df['degC'])
    df = df[df['degC'].notna()]
    
    df.plot.scatter('date', 'degC', figsize=((25, 7)), title = files[i])
