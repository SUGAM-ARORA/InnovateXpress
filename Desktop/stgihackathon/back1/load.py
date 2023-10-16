import csv 
import os
from models import Records

def run():
    file = open('/Users/akshitsharma/Desktop/djangostgi/storef/InnovateXpress/filtered_data.csv') #Change '\' to '/*
    read_file=csv.reader (file)
#optional
    Records.objects.all().delete()
    count=1 #To avoid header values
    for record in read_file:
        if count==1:
            pass 
        else:
            print(record) #optional
            Records.objects.create(CASE_NUMBER=record[0], DECISION_DATE=record [1], EMPLOYER_NAME=record[2], VISA_CLASS=record[3],NAIC_CODE=record[4],WAGE_UNIT_OF_PAY=record[5],PREVAILING_WAGE=record[6]) 
        count+=1
run()