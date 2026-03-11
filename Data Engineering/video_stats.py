import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:\\Users\\50916\\Python Files\\.env")

api_key= os.getenv("api_key")
Channel_handle= "@MrBeast"

def get_playlist_id():
#try and accept function to ensure that the function can handle potential issues
                   
    try:

        url= f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_handle}&key={api_key}"


        response= requests.get(url)
        response.raise_for_status()

        data= response.json()

        #json converts a python method into a json string, you must import the module
        #print(json.dumps(data,indent=4))


        channel_items=data["items"][0]

        channel_playlistid=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistid)

        return channel_playlistid

    except requests.exceptions.RequestException as e:
        raise e


if __name__== "__main__":
    get_playlist_id()


