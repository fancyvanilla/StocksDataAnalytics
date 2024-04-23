import csv
import pandas as pd



def convert_date(date_str):
    date = date_str.split('/')
    if len(date)==3:
      return f"{date[2]}-{date[1]}-{date[0]}"
    return ""

#convert text to csv 
with open("data/histo_cotation_2020.txt","r") as f:
    lines= f.readlines()
    
with open("data/histo_cotation_2020.csv","w",newline='') as outfile:
    writer = csv.writer(outfile)
    lines.pop(1)

    for line in lines[:-1]:
        row= line.split(" ")
        row =[x for x in row if x != '' and x != '\n']
        writer.writerow(row[:11])

with open("data/histo_cotation_2021.txt","r") as f:
    lines= f.readlines()
    
with open("data/histo_cotation_2021.csv","w",newline='') as outfile:
    writer = csv.writer(outfile)
    lines.pop(1)

    for line in lines[:-1]:
        row= line.split(" ")
        row =[x for x in row if x != '' and x != '\n']
        writer.writerow(row[:11])

#install openpyxl if not installed
#merge the csv files   
excel_files = ["histo_cotation_2022.xlsx","histo_cotation_2023.xlsx"]
csv_files =["histo_cotation_2020.csv","histo_cotation_2021.csv"]
cols=['SEANCE', 'GROUPE', 'CODE', 'VALEUR',
       'OUVERTURE ', 'CLOTURE', 'PLUS_BAS', 'PLUS_HAUT',
       'QUANTITE_NEGOCIEE', 'NB_TRANSACTION', 'CAPITAUX']
dfs=[]

for csv_file in csv_files:
    df = pd.read_csv("data/"+csv_file)
    df.columns=cols
    df['SEANCE'] = df['SEANCE'].apply(lambda x:convert_date(x))
    dfs.append(df)

for excel_file in excel_files:
    df = pd.read_excel("data/"+excel_file, engine='openpyxl')
    df.columns=cols
    df['SEANCE'] = df['SEANCE'].dt.date
    dfs.append(df)

df_merged = pd.concat(dfs, ignore_index=True)
df_merged.to_csv('histo_cotation.csv', index=False)   