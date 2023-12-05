import pandas as pd
import os 
import glob

current_dir = os.getcwd()

os.chdir(current_dir)
i = 0
for file in glob.glob("*.csv"):
    print(file)
    df = pd.read_csv(file)
    #df.drop_duplicates(keep=False)
    df = df.drop(df[df['Schedule name'] == 'Schedule name'].index)
    name = 'testframe'
    name = name + str(i) + '.csv'
    df.to_csv(name, encoding='utf-8', index=False)


