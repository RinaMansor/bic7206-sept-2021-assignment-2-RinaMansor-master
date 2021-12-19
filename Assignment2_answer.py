import pandas as pd
import csv
import re
header_list = ['Go Id','contig']
read_file=pd.read_csv(r'C:\Users\Rina Mansor\Documents\Masters\PU\Computer Programming\bic7206-sept-2021-assignment-2-RinaMansor-master\File_A.txt')
read_file.to_csv (r'C:\Users\Rina Mansor\Documents\Masters\PU\Computer Programming\bic7206-sept-2021-assignment-2-RinaMansor-master\File_A.csv', index=None)

f=open("File_C.csv", "w+")

FileC= []
with open('File_A.csv') as file:
    file_A = file.readlines()
    for line in range(0, len(file_A)):
        FileC.append(re.split('\t',file_A[line], maxsplit=1))