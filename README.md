# Full Stack Capstone API using the Auth 0 for authentication 


# Motivation 
This is my capstone project submission for Udacity Full-Stack Developer Nanodegree program. I am excisted to have a vaild life api that can be used for any frontend. 

# The Goal For project
This api well add new person to the database. 
- Design data models with relations use SQLAchemy
- Design endpoint
- Create to tables with many to one relationship  

# Getting Started 
# Installing Dependencies

- Python 3.8.4
- Follow instructions to install the correct version of Python for your platform
in the python docs.
# Virtual Environment (venv)
- Once you have your virtual environment setup,  
- To create virtual environment: 
```bash
   py -m venv env 
- to activate:
  source env/Scripts/activate
```
# PIP Dependecies
- Once you have your venv setup and running, install dependencies by navigating
to the root directory and running:
```bash
   pip3 install -r requirements.txt
```
- This will install all of the required packages included in the requirements.txt file.
 

# Start the app locally:
- Once you create the database, open your terminal, navigate to the root folder, and run:

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

- After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.

```bash
source setup.sh
```
# Local Testing
- To test your local installation, run the following command from the root folder:

python test_app.py
- If all tests pass, your local installation is set up correctly.
# Running the server
- From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:

export FLASK_APP=app
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run


# DATA MODELING:
- MODELS.PY
The schema for the database and helper methods to simplify API behavior are in models.py:

There are three tables created: Person, Job
The Person table is used by the role 'Manager' to add  new Person also delete and update person and their informations .
The Person table has a foreign key on the Job table for job_id.
The Job table is used by the role 'Supervisor' to get all of jobs 


# Endpoints
GET '/job'
GET /persons'
POST /person1'
DELETE /person3/<int:id>'
PATCH '/person2/<int:id>'

'''

GET '/job' 
- Fetches a dictionary all of jobs 
- Returns:list of jobs filter by jobs ID
{
  "ALL_jobs": [
    {
      "id": 1,
      "job_title": "Manager"
    },
    {
      "id": 2,
      "job_title": "Supervisor"
    },
  ]}
'''
GET /persons'
- Add a new person in body including new (name, phone , email , job_id).
- Return a list of persons the new person, success ,TotalPerson
{
  "All_Persons": [
    {
      "email": "wjdanjojo2@outlook.sa",
      "id": 45,
      "job_id": 4,
      "name": "ssaara",
      "phone": 50987755
    },
  ]}
'''
DELETE /person3/<int:id>'
- Delete the person by id
- Return the remaining of persone.
{
  "DeletePerson": 45,
  "TotalPerson": 36,
  "success": true
}
PATCH '/person2/<int:id>'
- Update the information  for person by id
- Return new information for person
{
  "Person": [
    {
      "email": "Fatmah@outlook.sa",
      "id": 46,
      "job_id": 4,
      "name": "ssssss",
      "phone": 50987755
    }
  ],
  "TotalPerson": 36,
  "success": true
}

### Setup Auth0

-  Create a new Auth0 Account
-  Select a unique tenant domain
-  Create a new, single page web application
-  Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
- Create new roles for: Manager
 the permissions:
    "delete:person",
    "post:person",
    "update:person"
- Create new roles for: Supervisor
the permissions:
    "get:job-list",
    "get:persons-detail"



```

Heroku:
Please use the below API address to make any request to the database
API address : https://capstoneappjo.herokuapp.com/

- To set up heroku:
- Create Heroku app
heroku create name_of_your_app
- Add git remote for Heroku to local repository
git remote add heroku heroku_git_url
- Add postgresql add on for our database
heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
- Push it up
git push heroku master
- Once your app is deployed, run migrations by running:
 heroku run python manage.py db upgrade --app name_of_your_application

