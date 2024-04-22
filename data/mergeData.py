import csv
import pandas as pd


#convert text to csv 
with open("histo_cotation_2020.txt","r") as f:
    lines= f.readlines()
    
with open("histo_cotation_2020.csv","w",newline='') as outfile:
    writer = csv.writer(outfile)
    lines.pop(1)

    for line in lines:
        row= line.split(" ")
        row =[x for x in row if x != '' and x != '\n']
        writer.writerow(row[:11])

with open("histo_cotation_2021.txt","r") as f:
    lines= f.readlines()
    
with open("histo_cotation_2021.csv","w",newline='') as outfile:
    writer = csv.writer(outfile)
    lines.pop(1)

    for line in lines:
        row= line.split(" ")
        row =[x for x in row if x != '' and x != '\n']
        writer.writerow(row[:11])

#install openpyxl if not installed
#merge the csv files   
excel_files = ["histo_cotation_2023.xlsx","histo_cotation_2022.xlsx"]
csv_files =["histo_cotation_2021.csv","histo_cotation_2020.csv"]
cols=['SEANCE', 'GROUPE', 'CODE', 'VALEUR',
       'OUVERTURE ', 'CLOTURE', 'PLUS_BAS', 'PLUS_HAUT',
       'QUANTITE_NEGOCIEE', 'NB_TRANSACTION', 'CAPITAUX']
dfs=[]

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    df.columns=cols
    dfs.append(df)
for excel_file in excel_files:
    df = pd.read_excel(excel_file, engine='openpyxl')
    df.columns=cols
    dfs.append(df)

df_merged = pd.concat(dfs, ignore_index=True)
df_merged.to_csv('histo_cotation.csv', index=False)   