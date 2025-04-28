import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_client():
    filename = "cafedamanha-71e815f25d5f.json"
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        filename=filename,
        scopes=scopes
    )
    return gspread.authorize(creds)
