# Full Stack Capstone API using the Auth 0 for authentication 


# Motivation 
This is my capstone project submission for Udacity Full-Stack Developer Nanodegree program.

# The Goal For project
This api well help to add job an person
- Design data models with relations use SQLAchemy,m n
- Design HTTP API 

# Getting Started 
- Installing Dependencies
- Once you have your virtual environment setup, running:
```bash
pip install -r requirements.txt

```
This will install all of the required packages we selected within the requirements.txt file.
- Start the app locally:
```bash
source setup.sh
python app.py
```
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
## Testing
To run the tests, run
```bash
source setup.sh
python test_app.py
```
