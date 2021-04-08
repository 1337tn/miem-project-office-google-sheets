from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account

from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service.json'

creds = None

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gPalfAyEgmnwDuZqOImQ8PtUWFMQH0ehkzwHyhGlgpM'
SAMPLE_RANGE_NAME = 'A2:B2'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

all_data = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A2:E671').execute()['values']

range_value_data_list = []

deltaListcolNames = ["название проекта", "тип проекта"]
deltaListcolVals = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='B2:D671').execute()['values']
width = 1
height = 1
for i in range (0,len(deltaListcolNames) ):
        rangeItem = deltaListcolNames[i]
        print(" the value for rangeItem is : ", rangeItem)
        batch_input_value = str(deltaListcolVals[i])
        print(" the value for batch_input_value is : ", batch_input_value)
        # construct the data structure for the value
        grid = [[None] * width for i in range(height)]
        grid[0][0] = batch_input_value

        range_value_item_str = { 'range': rangeItem, 'values': (grid) }
        range_value_data_list.append(range_value_item_str)

print(range_value_data_list)