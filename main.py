import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pafy  
url = "https://www.youtube.com/watch?v=z1P94xXsPJ4"
video = pafy.new(url)  
value = video.viewcount 
def changeVideoTitle(id):
    title = "Bu videonun " +str(value) + " " +  "İzlenmesi var"
    desc = "Kanalıma abone olabilirsiniz .!"
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().update(
        part="snippet", #,status
        body={
          "id": id,
          "snippet": {
            "categoryId": 27,
            # "defaultLanguage": "en",
            "description": desc,
             "tags": [
               "deneme"
             ],
            "title": title
          },
        }
    )
    response = request.execute()
    print(response)
changeVideoTitle("z1P94xXsPJ4")