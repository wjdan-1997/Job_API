import os
from flask import Flask, request, abort, jsonify
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
    def ShowJob(jwt):
        try:
            jobs=[r.format() for r in Job.query.all()]
        except Exception:
            abort(422)
        return jsonify ({
            "success":True,
            "ALL_jobs":jobs,
            "TotalJobs": len(Job.query.all()),
            
        })
    @app.route('/persons', methods=['GET'])
    @requires_auth('get:persons-detail')
    def ShowPerson(jwt):
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
    def Add_Person(jwt):
        from_body = request.get_json()
        # print (from_body)
        try:
            new_name = from_body.get('name',None)
            new_phone = from_body.get('phone',None)
            new_email = from_body.get('email',None)
            job_id = from_body.get('job_id',None)
            if new_name is None and new_phone is None and new_email is None and job_id is None:
                abort(404)
            add_person = Person(name=new_name, phone=new_phone, email=new_email, job_id=job_id)
            add_person.insert()
            
        except Exception:
            abort(405)
        return jsonify({
            'success':True,
            'Job':[add_person.format()],
            'Total_job': len(Person.query.all())
        })
    @app.route('/person3/<int:id>', methods=['DELETE'])
    @requires_auth('delete:person')
    def DeletePerson(jwt, id):
        try:
            rm_person = Person.query.filter(Person.id==id).one_or_none()
            rm_person.delete()
            if rm_person is None:
                abort(405)
        except Exception:
            abort(422)
        return jsonify({
            "success":True,
            "DeletePerson":id,
            "TotalPerson": len(Person.query.all())
        })
    @app.route('/person2/<int:id>', methods=['PATCH'])
    @requires_auth('update:person')
    def UpdatePerson(jwt, id):
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

        @app.errorhandler(422)
        def unprocessable(error):
            return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
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
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
            }), 405

    return app

app = create_app()

if __name__ == '__main__':
    app.run()