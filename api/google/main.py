from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2.credentials import Credentials

SERVICE_NAME = 'calendar'
VERSION = 'v3'

service = build(SERVICE_NAME, VERSION, credentials=creds)

creds = Credentials.from_authorized_user_file('credentials.json', SCOPES)
