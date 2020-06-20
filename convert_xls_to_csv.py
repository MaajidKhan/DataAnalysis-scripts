import pandas as pd
import glob
# Mention the folder name where all the .xls files are present which are to be combined
excel_files = glob.glob('C://Users//maajdkhan//Desktop//sudhaaorg//gaana//apr18-mar-19//*.xls')

import os
#Change the dump location where you want all the files to be dumped
os.chdir("C://Users//maajdkhan//Desktop//sudhaaorg//gaana//apr18-mar-2019_csv")
print("Directory changed")
print("Current Working Directory " , os.getcwd())

#Dump all those .xls files as an csv in the location you want.
for excel in excel_files:
    out = excel.split('.')[0]+'.csv'
    out_name = out.split('\\')[-1]
    print(out_name)
    df = pd.read_excel(excel) # if only the first sheet is needed.
    df.to_csv(out_name)
    #r'C://Users//maajdkhan//Desktop//sudhaaorg//gaana//apr18-mar-2019_csv'
    