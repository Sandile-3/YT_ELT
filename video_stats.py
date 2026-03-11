import requests
api_key="AIzaSyCe23AUyE0sMTO891Q0zvYkXNuecLOxheU"
Channel_handle="@MrBeast"
url= f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDeails&forHandle={Channel_handle}&key={api_key}"


response= requests.get(url)
print(response)