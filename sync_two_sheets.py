from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import sleep

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service.json'

creds = None

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
client = gspread.authorize(creds)

sheet1 = client.open("Test").worksheet('Защита проекта:23-30 апреля')
sheet2 = client.open("Test").worksheet('projectKPI (копия)')

project_types2 = sheet2.col_values(3)
project_types2.pop(0)
print("Fetched project_types")
project_numbers1 = sheet1.col_values(1)
project_numbers1.pop(0)
project_numbers2 = sheet2.col_values(1)
project_numbers2.pop(0)
print("Fetched project_numbers")

index_of_project_number1 = 'A2'
index_of_project_type1 = 'C2'
j = 0
#sheet1.update(index_of_project_type1, 'AAAAA')
for i in range(len(project_numbers1)):
    print('i = ', i)
    print('j = ', j)
    print('cur type', project_types2[j])
    print('index_of_project_number1', sheet1.acell(
        index_of_project_number1).value)
    print('number from 2nd sheet', project_numbers2[j])
    if sheet1.acell(index_of_project_number1).value is not None:
        while sheet1.acell(index_of_project_number1).value > project_numbers2[j]:
            j += 1
        if sheet1.acell(index_of_project_number1).value == project_numbers2[j]:
            sheet1.update(index_of_project_type1, project_types2[j])
            j += 1
    index_of_project_number1 = 'A' + str(3 + i)
    index_of_project_type1 = 'C' + str(3 + i)
    print("final ", index_of_project_number1)
    sleep(3)
