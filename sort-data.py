import pandas as pd
import os 
import glob

current_dir = os.getcwd()

os.chdir(current_dir)


if(not os.path.isdir('cleanData')):
    os.mkdir(current_dir + '/cleanData/')

for file in glob.glob("*.csv"):
    df = pd.read_csv(file)
    #this code drops all title rows that arent the first one
    df = df.drop(df[df[df.columns[0]] == df.columns[0]].index)

    name = file[:-4] + '-clean' + '.csv'
    path = current_dir + '/cleanData/'
    df.to_csv(path+name, encoding='utf-8', index=False)
    print(file + ' is now cleaned')

for file in glob.glob("*.txt"):
    df = pd.read_csv(file, sep= "\t")
    #this code drops all title rows that arent the first one
    df = df.drop(df[df[df.columns[0]] == df.columns[0]].index)

    name = file[:-4] + '-clean' + '.csv'
    path = current_dir + '/cleanData/'
    df.to_csv(path+name, encoding='utf-8', index=False)
    print(file + ' is now cleaned')
print('\ncleaned data files can be found in the /clean-data folder, thanks!')


