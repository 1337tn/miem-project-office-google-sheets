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


values = [
    [
        "HELLO", "HELLO"
    ],
    [
        "BYE", "BYE", "BYE"
    ]
]
body = {
  'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="A2:D3",
    valueInputOption="RAW", body=body).execute()