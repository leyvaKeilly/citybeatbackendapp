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
- Paste the following link: https://github.com/leyvaKeilly/citybeatbackendapp.git
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

Note: you should see on the terminal the path to the cloned folder Ex: C:\Users\UserName\Desktop\citybeatbackendapp

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
- Click on "Open app" on the top right corner

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

If you haven't cloned the frontend part of this demo, go to https://github.com/leyvaKeilly/citybeatfrontendapp.git and follow the README instructions.

To communicate your new frontend app with the backend app on heroku:

On backend:

- On VS Code open citybeatbackendapp folder
- Open terminal
- Open the settings.py file and in ALLOWED_HOSTS add the names of your new frontend and backend apps

On frontend:

- To keep using our demo backend and database on citybeatfrontendapp, scripts folder, open the workSpace.js file and set the herokuUrl variable to https://citybeatapp.herokuapp.com/

- To set your own backend and database on citybeatfrontendapp, scripts folder, open the workSpace.js file and set the herokuUrl variable to the url of your new backend app.

Note: If you want to run your own backend, you need to set up the database on Heroku.

Overview to set up database:

- Go to Heroku, open your backend app.
- Go to Resources, and click on Heroku Postgres.
- On the menu, next to Durability, click on Settings, then click on View Credentials. We will use these credentials to create and manage a Postgres database using pgAdmin4.
- Open pgAdmin4. (Download here: https://www.pgadmin.org/download/)
- Create a new server with the Heroku postgres database credentials. Now, the Heroku postgres database can be manage from pgAdmin.
- On pgAdmin4 create the tables (follow the instructions on Documentation for the column names and datatypes: https://teamd.web.unc.edu/files/2020/04/TeamD_Documentation-3.pdf)
- Import a csv file with the data collected, or use a backup file to populate the tables.
- If you want to modify our ai_engine: Go to the backend app, open train folder, and open ai_engine.py. To understand how ai_engine.py is working, please refer to the Documentation: https://teamd.web.unc.edu/files/2020/04/TeamD_Documentation-3.pdf  


- For more help on Heroku: https://devcenter.heroku.com/articles/
