**1. Description of the software**

The software we are creating is a HaaS application for credential and resource management. The tools we will be using include Python for the backend framework connected to a mongoDB database. Furthermore, React.js will be used for the frontend to facilitate user interaction. Additionally, Github will be used to store our codes, and a Jira board will be used for the planning, bug tracking, and managing of our project. Lastly, our project will be hosted on either Google Cloud or Heroku (whichever one works better). Our approach to our project will follow the Agile software development lifecycle. On our website, a user will be able to create a user account, which will require them to create a username and password. This account will store all of their current project and user information. Furthermore, sensitive information (such as their password) will be encrypted. The users will be able to create different projects and be able to checkout and checkin hardware sets on the website. Additionally, the users will be able to download the datasets of Physionet, a third party dataset website. 


**2. To run the backend on your Flask (backend)**

$> source venv/bin/activate (for Mac user)

$> ./venv/Scripts/activate  (for Windows user)

(download python packages)
  
$> pip install -r requirements.txt (from the root directory)

(To run the flask server locally)
  1. change the FLASK_ENV=production -> FLASK_ENV=development (from .env file)
  2. flask run
  3. should be run on your local

<img width="588" alt="Flask server run" src="https://user-images.githubusercontent.com/22105481/140564422-84704943-5c38-421a-ada9-8befd63e1426.png">
