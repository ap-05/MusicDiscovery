#ap223
CS490_Project1

##Introduction: 
The Spotify API allows you to fetch a ton of info, including your liked track and albums, song previews. It requires an authentication for the API as developer.

##Getting an authentication token: First, we need to sign up for spotify developer https://developer.spotify.com/dashboard/login .Second, we also need to sign up for genius developer https://genius.com/developers. Then registered your app name and generate your spotify and genius API to obtain an access_token and a sceret_key. Keep both of them safe, as we need them for later use.

##Tools / Frameworks Used
Currently, the following tools and frameworks are being used for development. These may be subject to change as the project progresses.

    Flask 
    Spotify API
    Genuis API
    Basic HTML/CSS for front-end

## SETTING UP PROJECT
1. Clone the repository
  $git clone:https://github.com/NJIT-CS490-SP21/project1-ap223.git

2.Set Up Environment Variables Create a .env file with access keys to be used to access the Spotify API and Genius API.
  Contents of secrets.env:

    # Spotify
    export SPOTIFY_CLIENT_ID=(Spotify Client ID)
    export SPOTIFY_CLIENT_SECRET=(Spotify Client Secret)
    
    #Genius
    export genius_token=(Genius_TOKEN)
  
