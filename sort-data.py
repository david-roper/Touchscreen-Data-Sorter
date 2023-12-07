import pandas as pd
import os 
import glob

current_dir = os.getcwd()

os.chdir(current_dir)

i = 0
if(not os.path.isdir('clean-data')):
    os.mkdir(current_dir + '/clean-data/')

for file in glob.glob("*.csv"):
    print(file)
    df = pd.read_csv(file)
    #df.drop_duplicates(keep=False)
    df = df.drop(df[df['Schedule name'] == 'Schedule name'].index)
    name = file + '-clean' + '.csv'
    path = current_dir + '/clean-data/'
    df.to_csv(path+name, encoding='utf-8', index=False)


