from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'cred.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SAMPLE_RANGE_NAME = 'Hoja 1!A1:C3'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1vgZuRiNaVaGtRLYRqTDRowS4yYQoOSAzvva-aeu-qPA'

service = build('sheets', "v4", credentials=creds)

# Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                            range=SAMPLE_RANGE_NAME).execute()

# values = result.get('values', [])

print(service)
