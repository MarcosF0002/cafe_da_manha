import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import json

def get_client():
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    # Pega o dicionário dos secrets
    service_account_info = st.secrets["gcp_service_account"]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        dict(service_account_info),
        scopes=scopes
    )
    return gspread.authorize(creds)
