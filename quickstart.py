from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service.json'

creds = None

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Lv8PN4lZj0DPmVlCqSqhgFmqCNQK1ps0JtGr0qNwgs8'
SAMPLE_RANGE_NAME = 'A2:B2'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
#values = result.get('values', [])

all_data = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A2:E671').execute()['values']
#print(all_data)

"""for i in all_data:
    print(i)"""

clean_data = [x for x in all_data if x != []]

#for i in clean_data:
    #print(i)

"""sheet = client.open('Test')
projectKPI = sheet.worksheet_by_title('projectKPI (копия)')
projectKPI_data = projectKPI.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='C2:C411').execute()['values']
print(projectKPI_data)"""
#client = pygsheets.authorize(service_account_file='service.json')
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Test").worksheet('projectKPI (копия)')
project_types = sheet.col_values(3)
print(project_types)