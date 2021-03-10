import pandas as pd
import csv
from octotest.models import UploadCleanData
from django.http import HttpResponse
from datetime import datetime

def handle_uploaded_file(f):
    with open('octotest/media/Files/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def clean_file(f):
    df = pd.read_csv('octotest/media/Files/'+f.name,sep="|", skipfooter=1, header=None, usecols=range(0,8), engine='python').fillna(0)
    df = df.iloc[1:]
    df1 = df.to_csv('octotest/media/Cleaned_Files/'+f.name, encoding='utf-8', header=None, index=False)

def upload_data(f):
    file_data = f.read().decode("utf-8")
    lines = file_data.splitlines()
    df = pd.DataFrame(columns=["MPAN_Core",
    "BSC_Validation_Status",
    "Meter_ID",
    "Reading_Type",
    "Meter_Register_ID",
    "Reading_Date_Time",
    "Register_Reading",
    "Meter_Reading_Flag",
    "Reading_Method",
    "file"])
    for line in lines:
        fields = line.split(",")
        
        if fields[0] == "026":
            datetime_obj = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            df = df.append({'MPAN_Core' : fields[1],
            'BSC_Validation_Status' : fields[2],
            'Meter_ID': "",
            'Reading_Type':"",
            'Meter_Register_ID': "",
            'Reading_Date_Time': datetime_obj,
            'Register_Reading': "",
            'Meter_Reading_Flag': "",
            'Reading_Method': "",
            'file': f.name}, ignore_index=True)
            
        elif fields[0] == "028":
            datetime_obj = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            df = df.append({'MPAN_Core' : "",
            'BSC_Validation_Status' : "",
            'Meter_ID': fields[1],
            'Reading_Type': fields[2],
            'Meter_Register_ID': "",
            'Reading_Date_Time': datetime_obj,
            'Register_Reading': "",
            'Meter_Reading_Flag': "",
            'Reading_Method': "",
            'file': f.name}, ignore_index=True)

        else:
            datetime_obj = datetime.strptime(fields[2], '%Y%m%d%H%M%S')
            df = df.append({'MPAN_Core' : "",
            'BSC_Validation_Status' : "",
            'Meter_ID': "",
            'Reading_Type': "",
            'Meter_Register_ID': fields[1],
            'Reading_Date_Time': datetime_obj,
            'Register_Reading': fields[3],
            'Meter_Reading_Flag': fields[6],
            'Reading_Method': fields[7],
            'file': f.name}, ignore_index=True)
         

    for i in range(df.shape[0]):
        model = UploadCleanData()
        model.MPAN_Core = df.iloc[i,0]
        model.BSC_Validation_Status = df.iloc[i,1]
        model.Meter_ID = df.iloc[i,2]
        model.Reading_Type = df.iloc[i,3]
        model.Meter_Register_ID = df.iloc[i,4]
        model.Reading_Date_Time = df.iloc[i,5]
        model.Register_Reading = df.iloc[i,6]
        model.Meter_Reading_Flag = df.iloc[i,7]
        model.Reading_Method = df.iloc[i,8]
        model.file = df.iloc[i,9]
        model.save()