
input_seq = input("Enter file name: ")
DNA_seq = open(input_seq).read()

DNA_seq = DNA_seq.replace("\n","")
letterA = DNA_seq.find("A")
letterG = DNA_seq.find("G")
letterC = DNA_seq.find("C")
letterT = DNA_seq.find("T")

comp_ls = [letterA, letterG, letterC, letterT]                                  # Creats a list of the position of each letters found for the first time

for num in comp_ls:                                                             # Removes any number smaller than 40 from the list
    if 0 in comp_ls:
        break
    elif num < 40:
        comp_ls.remove(num)
comp_ls.sort()
in_num = comp_ls[0] 

numberA = DNA_seq.count("A")
numberG = DNA_seq.count("G")
numberC = DNA_seq.count("C")
numberT = DNA_seq.count("T")
A = (numberA * 100)/len(DNA_seq[in_num:])
G = (numberG * 100)/len(DNA_seq[in_num:])
C = (numberC * 100)/len(DNA_seq[in_num:])
T = (numberT * 100)/len(DNA_seq[in_num:])

t = A+G+C+T

AllNul_dict = {"Base Percent": ["A%", "G%", "C%", "T%", "TOTAL"], "Value": [A, G, C, T, t]}

import pandas as pd

df = pd.DataFrame(AllNul_dict)
print(df)