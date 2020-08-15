import os
import unittest, pytest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Person, Job

class CapstoneCase(unittest.TestCase):
     
    def setUp(self):
            """Define test variables and initialize app."""
            self.app = create_app()
            self.client = self.app.test_client
            self.database_name = "capstone"
            self.database_path = os.environ['DATABASE_URL']
            self.token = os.environ['token']
            # self.manger_token = os.environ['manger_token']
            # @pytest.fixture
            # def token():
            #      return {'Authorization': f'Bearer {TOKEN}'}
            
            self.new = {
            "name":"ssaara",
            "phone":"50987755",
            "email":"Noura@outlook.sa",
            "job_id":4
        }
            self.update = {
            "name":"nnnn",
            "phone":"50987755",
            "email":"nnnn@outlook.sa",
            "job_id":3
        }

    
    def tearDown(self):
        """Executed after reach test"""
        pass
    # def test_job_success_behavior(self):
    #     # res=self.client().get('/job', headers={'Authorization': f'Bearer {TOKEN}'})
    #     # token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB3VkFKTFhfNmF6cGFDSl9rY1ZDUiJ9.eyJpc3MiOiJodHRwczovL2ZzZG5qby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmNjA1OWI3Y2JjODUwMDE5MmExZmE3IiwiYXVkIjoicGVyc29uIiwiaWF0IjoxNTk3MTM1ODExLCJleHAiOjE1OTcxNDMwMTEsImF6cCI6Ik5GcDBMTU5WdVBOajVzWmoyS1FqUHAyNU9SbFplU25PIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6am9iLWxpc3QiLCJnZXQ6cGVyc29ucy1kZXRhaWwiXX0.VXbEjWs2icCUnZR1RJ3C-w0iYkbM8qxhcayYjW5oQ0SECCo9vOhuYlIQKseXhlf4Mk3kIJ3TvvK3NT6odTJ-vHpq1nvGqlPQY6RJ4ooi-dA5WU6d2dAZr3c3UPY3IMTrNW7s5Ucpr5xiUJKl-0cJ2Cv8WxBRHa8gCMpSqRqvFCIN3kpR6KGxUA5iqNzecvOPed9lVynBhYdpWF1g-pcwqPSRs3DqYcqa754BYw4gSE94-ZJs1z7AleQxqJoLkbIcDOu5TXCkTEjJmixpIX10aNm85GQR1JCapTR9g69bDbCmwa5QpjeGY1LyNSIN1AGilCdPsybu7U_B7_Fie9I_Ag'
    #     res = self.client().get(
    #     '/job',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['token']
    #         )
    #      )
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    # def test_job_error_behavior(self):
    #     res = self.client().post(
    #     '/job',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['token']
    #         )
    #      )
    #     # data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 405)
    
    # def test_person_success_behavior(self):
    #     res = self.client().get(
    #     '/persons',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['token']
    #         )
    #      )
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    # #    
    # def test_persons_error_behavior(self):
    #     res = self.client().post(
    #     '/persons',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['token']
    #         )
    #      )
        
    #     self.assertEqual(res.status_code, 405)
        
        

#'''___Success behavior For Post Delete Patch_____'''


    # def test_delete_person_success(self):
    #     res = self.client().delete('/person3/42',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['manger_token']
    #         )
    #      )
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'],True)

    # def test_update_person_success(self):
    #     res = self.client().patch('/person2/13',json=self.update,
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['manger_token']
    #         )
    #      )
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'],True)

    def test_add_person_success(self):
        res = self.client().post('/person1',json=self.new,
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)


#'''___Error behavior For Post Delete Patch_____'''

    # def test_add_person_error_behavior(self):
    #     res = self.client().delete('/person1',json=self.new,
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['manger_token']
    #         )
    #      )
    #     self.assertEqual(res.status_code, 405)

    # def test_update_person_error_behavior(self):
    #     res = self.client().delete('/person2',json=self.update,
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['manger_token']
    #         )
    #      )
    #     self.assertEqual(res.status_code, 404)
    #     def test_delete_person_error_behavior(self):
    #         res = self.client().delete('/person3/40',
    #     headers=dict(
    #         Authorization='Bearer ' + os.environ['manger_token']
    #         )
    #      )
    #     self.assertEqual(res.status_code, 404)

if __name__ == "__main__":
    unittest.main()
