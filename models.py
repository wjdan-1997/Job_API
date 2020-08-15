import os 
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy 
import json 


database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



class Person(db.Model):
    __tablename__='Person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    email= Column(String(120), nullable=False)
    job_id=db.Column(db.Integer, db.ForeignKey(
        'Job.id'), nullable=False)

    def __init__(self, name, phone, email, job_id):
        self.name = name
        self.phone = phone 
        self.email = email
        self.job_id = job_id
    def format(self):
        return{
            'id':self.id,
            'name':self.name,
            'phone':self.phone,
            'email':self.email,
            'job_id':self.job_id
        } 
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
class Job(db.Model):
    __tablename__ = 'Job'
    id = Column(Integer, primary_key=True)
    job_title = Column(String, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()

    def __init__(self, job_title ):
        self.job_title = job_title
        
    def format(self):
        return{
            'id':self.id,
            'job_title':self.job_title
        }
