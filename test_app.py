import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Person, Job

class CapstoneCase(unittest.TestCase):
     
    def setUp(self):
            """Define test variables and initialize app."""
            self.app = create_app()
            self.client = self.app.test_client
            self.database_name = "job"
            self.database_path = os.environ['DATABASE_URL']
            self.token = os.environ['token']
            self.manger_token = os.environ['manger_token']
           
            
            self.new = {
            "name":"Salah",
            "phone":"50987755",
            "email":"Salah@outlook.sa",
            "job_id":4
        }
            self.update = {
            "name":"Rame",
            "phone":"50987755",
            "email":"Rame@outlook.sa",
            "job_id":3
        }

    
    def tearDown(self):
        """Executed after reach test"""
        pass
#'''___Success and error behavior For GET _____'''

    def test_job_success_behavior(self):
        res = self.client().get(
        '/job',
        headers=dict(
            Authorization='Bearer ' + os.environ['token']
            )
         )
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_job_error_behavior(self):
        res = self.client().post(
        '/job',
        headers=dict(
            Authorization='Bearer ' + os.environ['token']
            )
         )
        self.assertEqual(res.status_code, 405)
    
    def test_person_success_behavior(self):
        res = self.client().get(
        '/persons',
        headers=dict(
            Authorization='Bearer ' + os.environ['token']
            )
         )
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    #    
    def test_persons_error_behavior(self):
        res = self.client().post(
        '/persons',
        headers=dict(
            Authorization='Bearer ' + os.environ['token']
            )
         )
        
        self.assertEqual(res.status_code, 405)
        
        

#'''___Success behavior For Post Delete Patch_____'''


    def test_delete_person_success(self):
        res = self.client().delete('/person3/2',
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

    def test_update_person_success(self):
        res = self.client().patch('/person2/3',json=self.update,
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

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

    def test_add_person_error_behavior(self):
        res = self.client().delete('/person1',json=self.new,
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        self.assertEqual(res.status_code, 405)

    def test_update_person_error_behavior(self):
        res = self.client().delete('/person2',json=self.update,
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        self.assertEqual(res.status_code, 404)
        def test_delete_person_error_behavior(self):
            res = self.client().delete('/person3/4',
        headers=dict(
            Authorization='Bearer ' + os.environ['manger_token']
            )
         )
        self.assertEqual(res.status_code, 404)

if __name__ == "__main__":
    unittest.main()
