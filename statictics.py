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

sheet = client.open(
    "Копия Программно-аппаратные проекты").worksheet('Защита проекта:23-30 апреля')

values = sheet.col_values(3)
values = [x for x in values if x]
print("Программно-аппаратных проектов: ", len(values))
