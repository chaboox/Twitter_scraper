# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:03:36 2019

@author: deboosere_am
"""

import csv
with open('male_all.csv', 'r') as inp, open('new data/male_all_10.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if len(row[0].split()) >10:
            writer.writerow(row)