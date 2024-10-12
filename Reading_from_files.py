import json
import pandas as pd
import numpy as np

def CSV():
    path_csv = r"D:\Python\Data Reading\Files\CSV.csv"
    df = pd.read_csv(path_csv)
    print(df)

def JSON():
    path_json = r"D:\Python\Data Reading\Files\JSON.json"
    with open(path_json,'r') as json_file:
        df = json.load(json_file)
    print(df)

def Excel():
    path_excel = r"D:\Python\Data Reading\Files\EXCEL.xlsx"
    df = pd.read_excel(path_excel)
    print(df)

def Text():
    path_txt = r"D:\Python\Data Reading\Files\Text.txt"
    with open(path_txt,'r')as text_file:
        df = text_file.read();
    print(df)

def Read(value):
    if value==1:
        CSV()
    elif value==2:
        JSON()
    elif value==3:
        Excel()
    elif value==4:
        Text()
    else:
        print("File not found")

value = int(input('''---Enter 1 to read CSV file---
---Enter 2 to read Json file---
---Enter 3 to read Excel file---
---Enter 4 to read Text file---\n'''))
Read(value)