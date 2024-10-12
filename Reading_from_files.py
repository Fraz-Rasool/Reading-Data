import json
import pandas as pd
import numpy as np

def CSV(path):
    df = pd.read_csv(path)
    print(df)
    # path_csv = r"D:\Python\Data Reading\Files\CSV.csv"

def JSON(path):
    with open(path,'r') as json_file:
        df = json.load(json_file)
    print(df)
    # path_json = r"D:\Python\Data Reading\Files\JSON.json"

def Excel(path):
    df = pd.read_excel(path)
    print(df)
    # path_excel = r"D:\Python\Data Reading\Files\EXCEL.xlsx"

def Text(path):
    with open(path,'r')as text_file:
        df = text_file.read();
    print(df)
    # path_txt = r"D:\Python\Data Reading\Files\Text.txt"

def Read(value):
    path =input(r'Enter the path without "quotes":')
    if value==1:
        CSV(path)
    elif value==2:
        JSON(path)
    elif value==3:
        Excel(path)
    elif value==4:
        Text(path)
    else:
        print("File not found")

value = int(input('''---Enter 1 to read CSV file---
---Enter 2 to read Json file---
---Enter 3 to read Excel file---
---Enter 4 to read Text file---\n'''))

Read(value)