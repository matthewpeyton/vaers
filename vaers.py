#!/usr/bin/python3
import pandas as pd

class vaers():
    def __init__(self):
        self = ''

    def read_year(self, year, dtype): # load in the data from a year provided
        data = pd.read_csv('data/'+str(year)+'VAERS'+dtype+'.csv', encoding = 'utf-8')

        df = pd.DataFrame(data, columns= ['VAERS_ID','RECVDATE','STATE','AGE_YRS','CAGE_YR','CAGE_MO','SEX','RPT_DATE','SYMPTOM_TEXT','DIED','DATEDIED','L_THREAT','ER_VISIT','HOSPITAL','HOSPDAYS','X_STAY','DISABLE','RECOVD','VAX_DATE','ONSET_DATE','NUMDAYS','LAB_DATA','V_ADMINBY','V_FUNDBY','OTHER_MEDS','CUR_ILL','HISTORY','PRIOR_VAX','SPLTTYPE','FORM_VERS','TODAYS_DATE','BIRTH_DEFECT','OFC_VISIT','ER_ED_VISIT','ALLERGIES'])
        return df

    def visualize(self, df): # visualizes the data in some interesting way, i guess?
        plt = df.plt
        return plt

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Read data for a year and type provided.')
    parser.add_argument('-t', '--type', type=str, help='the type of data to request. Options are DATA,VAX, and SYMPTOMS')
    parser.add_argument('-y', '--year', type=int, help='the year of data to request. Starts at 1990')

    args = parser.parse_args()

    vaers = vaers()

    df = vaers.read_year(args.year, args.type)

    print(df.loc[df['DIED'] == 'Y', ['SEX','SYMPTOM_TEXT','DIED','DATEDIED']])