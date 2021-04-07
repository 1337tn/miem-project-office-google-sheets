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

sheet1 = client.open("Копия Копия Test").worksheet(
    'Защита проекта:23-30 апреля')

j = 2
delete_this = True
for i in range(2, 672):
    print('i = ', i)
    print('j = ', j)
    print(sheet1.acell("C" + str(j)).value)
    if sheet1.acell("C" + str(j)).value == "Прогр-аппарат.":
        delete_this = False
        j += 1
    else:
        if sheet1.acell("C" + str(j)).value is None:
            if delete_this:
                print("deleting", sheet1.acell("C" + str(j)).value)
                sheet1.delete_row(j)
            else:
                j += 1
        else:
            print("deleting", sheet1.acell("C" + str(j)).value)
            sheet1.delete_row(j)
            delete_this = True
    sleep(3)
