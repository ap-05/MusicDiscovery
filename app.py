from flask import Flask, render_template
import os
import requests
import json
import random
from method import getToken, getArtistInfo, getTracks #, getPath, getLyrics
from test_data import gettestArtistInfo, gettestTracks
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

# declaring app name
app = Flask(__name__)
 
# defining home page   
@app.route('/')
def index():

    #Artist ID from spotify 
    artists=["4YRxDV8wJFPHPTeXepOstw", "1TbRSunWGZ46mqnapcWxrm", "3xU8YsNNkmWSPewlB18NUz","0oOet2f43PA68X5RxKobEy", "5f4QpKfy7ptCHwTqspnSJI"]
    rand_id = random.choice(artists)
    try: 
        artistInfo = getArtistInfo(rand_id)
        tracks = getTracks(rand_id)
    except:
        artistInfo = gettestArtistInfo()
        tracks = gettestTracks()
      
   
    return render_template(
        "index.html",
        artistImg =artistInfo["images"][0]["url"],
        artistName =artistInfo["name"],
        tracks=getTracks(rand_id),
        tracksLen = len(tracks),
        )

# running app 
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
