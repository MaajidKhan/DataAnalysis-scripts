import os
import glob
import pandas as pd
os.chdir("C://Users//maajdkhan//Desktop//sudhaaorg//gaana//apr18-mar-2019_csv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig') #Dumps a csv with all the rows combined

#Read the combined csv and choose specific columns you want to have
df = pd.read_csv("combined_csv.csv", usecols = ['Track','Album', 'Artist', 'Total'])
print(df)
df.to_csv( "combined_csv_final.csv", index=False, encoding='utf-8-sig')

