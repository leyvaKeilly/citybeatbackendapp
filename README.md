# Welcome to our project for City News Beat!

We are a team of four seniors that created an A.I. engine as part of our project for the Software Engineering class at the University of North Carolina - Chapel Hill. Our algorithm reads data of users interactions with City News Beat app and tries to recommend videos based on the user's interests. Our goal is to deliver to each user a Newscast-for-1 based on their preferences.

We created a website to demo how our algorithm to recommend videos works.

To open website demo: https://city-news-beat.herokuapp.com/

To clone the git repo and deploy your own heroku app follow these instructions:

What you need:
- Node.js and npm
- Heroku
- Git
- Visual Studio Code (or any other code editor)


Open Visual Studio Code (or any other source code editor).
- Note: This walkthrough uses Visual Studio Code as source code editor.
  To install VS Code: https://code.visualstudio.com/

Clone the github repo.
In VS Code:
- Click View/Command Palette/
- Type: Git:clone
- Paste the following link: https://github.com/523TeamD/comp523citybeatbackend.git
- Press Enter
- Select the folder where you would like to clone the repo.

Note: If you don't have git, please download it here:
https://git-scm.com/downloads
- Create a github account if you don't have one.
- Make sure in VS Code the git: Enable setting is checked. For this click in Manage (the tool icon on the bottom left corner) / Settings / type git enable on the search bar and make sure that box is checked.
- Restart your computer after installing git.

After you cloned the github repo
- Open the folder that you just cloned (if it's not already opened). For this go to File/Open folder/ and search for the location of the folder on your computer. 
- Go to Termianl/Open new terminal or right click on comp523citybeatbackend folder and select open a new terminal.

Note: you should see on the terminal the path to the cloned folder Ex: C:\Users\UserName\Desktop\comp523citybeatbackend

- If you don't have Node.js: Download and install Node.js OS installer at: https://nodejs.org/en/download/

On the VS Code terminal write: 
- npm install heroku
- After heroku is installed write: heroku login
- You should see something like this: 
  heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
  heroku: Waiting for login...
  Logging in... done
  Logged in as me@example.com

Note: If you don't have a heroku account:
- On your browser go to heroku: https://dashboard.heroku.com
- Sign up to create a new account and enter your information.

Write on the VS Code terminal:
- heroku create nameOfApp --buildpack heroku/python
- git init
- heroku git:remote -a nameOfApp
- git push heroku master

Go to heroku
- Select the app you just created
- Click on Open app on the top right corner

To save changes made to the heroku app in terminal on VS Code:
- git add .
- git commit -m "add a message"
- git push heroku master

To run locally:
- Install python (version >= 3)
- Install Django
- Open project folder on terminal
- Write: python manage.py runserver
- Open on browser: localhost:8000

Note: IMPORTANT

If you haven't cloned the frontend part of this demo, go to https://github.com/523TeamD/CityNewsBeatAIDemoAPP.git and follow the README instructions.

To communicate your new frontend app with the backend app on heroku:

On backend:

- On VS Code open comp523citybeatbackend folder
- Open terminal
- Open the settings.py file and in ALLOWED_HOSTS add the urls of your new frontend and backend apps

On frontend:

- On VS Code open CityNewsBeatAIDemoAPP folder
- Open terminal
- On Scripts, open the workSpace.js file and set the herokuUrl variable to the url of your new frontend app.



- For more help on Heroku: https://devcenter.heroku.com/articles/
