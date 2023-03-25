# Import the necessary libraries
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from flask import Flask, render_template, request

# Authenticate with the Google Sheets API using the Google API service account credentials
creds = Credentials.from_service_account_file('fhabri-admin-e4690b763633.json')
service = build('sheets', 'v4', credentials=creds)

# Define a function to retrieve the data from the Google Sheets spreadsheet
def get_data():
    spreadsheet_id = '1tLRctGGzHwFZnGh-pEP1XU-6BLhEdekPQw08wZSyf9Q'
    range_name = 'Sheet1!A1:AX64'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values

# Create a Flask app
app = Flask(__name__)

# Define a route for the search page
@app.route('/')
def search():
    query = request.args.get('query')
    data = get_data()
    results = []
    if query:
        for row in data:
            if query.lower() in [str(val).lower() for val in row]:
                results.append(row)
    else:
        query = ""
    return render_template('search.html', query=query, results=results)


# Run the Flask app
if __name__ == '__main__':
    app.run(port=5005, debug=True)

