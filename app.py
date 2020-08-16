import os
from flask import (Flask,request,jsonify,abort)
from flask_cors import CORS
from models import setup_db, Person, Job 
from auth import AuthError, requires_auth


def create_app(test_config=None):
    
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        
        return "greeting"

    @app.route('/start')
    def be_cool():
        return "Welcome to capstone project"

    @app.route('/job')   
    @requires_auth('get:job-list')
    def show_job(jwt):

        jobs=[r.format() for r in Job.query.all()]
        
        return jsonify ({
            "success":True,
            "ALL_jobs":jobs,
            "TotalJobs": len(Job.query.all()),
            })
            
    @app.route('/persons', methods=['GET'])
    @requires_auth('get:persons-detail')
    def show_person(jwt):
        try:
            person1=[l.format() for l in Person.query.all()]
            if person1 is None:
                abort(405)  
        except Exception:
            abort(422)
        return jsonify ({
            "success":True,
            "All_Persons":person1,
            "TotalPerson": len(Person.query.all())
        })

    @app.route('/person1', methods=['POST'])
    @requires_auth('post:person')
    def add_person(jwt):
        from_body = request.get_json()
        # print (from_body)
        
        new_name = from_body.get('name')
        new_phone = from_body.get('phone')
        new_email = from_body.get('email')
        job_id = from_body.get('job_id')
        
        add_person = Person(name=new_name, phone=new_phone, email=new_email, job_id=job_id)
        
        add_person.insert()
        

        return jsonify({
            'success':True,
            'Job':[add_person.format()],
            'Total_job': len(Person.query.all())
        })
    @app.route('/person3/<int:id>', methods=['DELETE'])
    @requires_auth('delete:person')
    def delete_person(jwt, id):
        
        rm_person = Person.query.filter(Person.id==id).one_or_none()
        rm_person.delete()
        

        return jsonify({
        "success":True,
        "DeletePerson":id,
        "TotalPerson": len(Person.query.all())
            })
    @app.route('/person2/<int:id>', methods=['PATCH'])
    @requires_auth('update:person')
    def updateperson(jwt, id):
        from_body = request.get_json()
        try:
            person = Person.query.filter(Person.id==id).one_or_none()
            name = from_body.get('name')
            phone = from_body.get('phone')
            email = from_body.get('email')
            job_id = from_body.get('job_id')

            person.name = name
            person.phone=phone
            person.email=email
            person.job_id=job_id
            person.update()
            if person is None:
                abort(405)
        except Exception:
            abort(422)
        return jsonify({
            "success":True,
            "Person":[person.format()],
            "TotalPerson": len(Person.query.all())
        })
    # Error Handling

    @app.errorhandler(400)
    def bad_request (error):
        return jsonify({
    'message': "Bad_Request ",
    'success': False
    }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        "message": "unprocessable",
        "success": False
        }), 422

    @app.errorhandler(AuthError)
    def get_authError(get):
        return jsonify({
            'success': False,
            'error': get.status_code,
            'message': get.error
        }),401
        
    @app.errorhandler(405)
    def methode_not_allwod(error):
        return jsonify({
        "message": "method not allowed",
        "success": False
        }), 405

    @app.errorhandler(401)
    def unauthorized (error):
        return jsonify({
        "message": "unauthorized ",
        "success": False
        }), 401

    return app

app = create_app()

if __name__ == '__main__':
    app.run()