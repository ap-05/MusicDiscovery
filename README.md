##ap223

CS490_Project1

##INTRIDUCTION: 

        The Spotify API allows you to fetch a ton of info, including your liked track and albums, song previews. It requires an authentication for the API as developer.

##GETTING AN AUTHENTICATION TOKEN:
        
        First, we need to sign up for spotify developer https://developer.spotify.com/dashboard/login .Second, we also need to sign up for genius developer         https://genius.com/developers. Then registered your app name and generate your spotify and genius API to obtain an access_token and a sceret_key. Keep both of them safe, as we need them for later use.

##TOOLS/FRAMEWORKS USED:

     Currently, the following tools and frameworks are being used for development. These may be subject to change as the project progresses.

    Flask 
    Spotify API
    Genuis API
    Basic HTML/CSS for front-end

## SETTING UP PROJECT

1.Clone the repository

    $git clone:https://github.com/NJIT-CS490-SP21/project1-ap223.git

2.Set Up Environment Variables Create a .env file with access keys to be used to access the Spotify API and Genius API. It is a hidden file.
  Contents of secrets.env:

    # Spotify
    export SPOTIFY_CLIENT_ID=(Spotify Client ID)
    export SPOTIFY_CLIENT_SECRET=(Spotify Client Secret)
    
    #Genius
    export genius_token=(Genius_TOKEN)
  
 3. Create a .gitignore file to ignore your secret acces file names were not committed to the github. And it is hidden file also. 
    Contents of serecet .gitignore:
    
        .env
 4. Install required Python packages
 
        pip install flask
        pip install requests
        pip install python-dotenv
        pip install random
        
 ##DEPLOY TO HEROKU
 
 1. Install Heroku CLI:
        
        npm install -g heroku
    
 2.Create a free account on Heroku https://signup.heroku.com/login
 
 3.Create a requirements.txt file
        
        Flask
        requests
        python-dotenv

4.Create a Procfile, which has the command that Heroku will use to run your app:

        web: python app.py
     
5.Add and commit all changed files with git

6.Log in to Heroku: 
    
        heroku login -i
        
7.Create a Heroku app:

        heroku create
8. Push your code to Heroku: 

        git push heroku main
        
        This actually pushes your code to Heroku's remote repository.
9.Open your app with your new URL: 

        heroku open
        
10. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
        
        Add your secret key from .env with the matching variable name and value.
 
11. Run heroku open or refresh the URL if you have it open.
    
 Running the app
 
       Run command in terminal: python app.py
       Preview web page in browser '/'
        
 Check it out here
 
        https://project1-ap223.herokuapp.com/
        
  
