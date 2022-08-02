from Google import Create_Service
import pandas as pd
import gspread
import time

gc = gspread.service_account(filename='certi.json')
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/17nvxi-mgxd_rZy8mDuM3Bangutjw1YS384kfqajalyc/edit?usp=sharing")
worksheet = sh.worksheet("Sheet1")
uid_list = worksheet.col_values(1)
names_list = worksheet.col_values(5)
uid_list.remove(uid_list[0])
names_list.remove(names_list[0])
scope = ["https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# client.json.
CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


folder_id = 'https://drive.google.com/drive/u/1/folders/1UFv8GyQ0y51f48OziR941cYcA-uu2hiK' # Folder id.
query = f"parents = '{folder_id}'"

response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.min_rows', 500)
pd.set_option('display.max_colwidth', 150)
pd.set_option('display.width', 200)
pd.set_option('expand_frame_repr', True)
df = pd.DataFrame(files)
str = "https://drive.google.com/uc?export=download&id="
df = df.sort_values(by=['name'])
print(df)

# Sort sheet by UID number before this.
n = len(names_list)
for i in range(0,n):
    uid = uid_list[i]
    fname = uid + '.jpg'
    if(fname == df.iloc[i]["name"]):
        fid = df.iloc[i]["id"]
        flink = str + fid
        worksheet.update_cell(i+2, 9, flink)
    time.sleep(5)