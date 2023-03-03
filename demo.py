from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = 'fhabri-admin-e4690b763633.json'
creds = Credentials.from_service_account_file(filename=SERVICE_ACCOUNT_FILE)

out = build('sheets', 'v4', credentials=creds)
print(out)

GOOGLE_SHEETS_ID = '1tLRctGGzHwFZnGh-pEP1XU-6BLhEdekPQw08wZSyf9Q'

worksheet_name = 'Sheet1!'
cell_range_insert = 'A5:D5'
values = (
    ('3/3/2023', 'Ahmad Hassan', 'A', '100'),
)
value_range_body = {
    'majorDimension' : 'ROWS',
    'values' : values
}

out.spreadsheets().values().update(
    spreadsheetId=GOOGLE_SHEETS_ID,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()