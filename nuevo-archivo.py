# Este es un código de python 

import glob
import os


file_in = open('tabla1.csv', 'r')

isfirstline = True

n = 0

for line in file_in:

    if isfirstline:

        isfirstline = False

        continue

    text = line.split(',')

    filename = text[0] + '-' + text[1] + '-' + text[6] + '.txt'

    f = open(filename, 'a')

    f.write(text[-1])

    f.close()

    n += 1

    if n == 5000:

        break

file_in.close()
