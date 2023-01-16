from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS, cross_origin
from datetime import datetime, date, time, timezone

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libery.DB.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

# model
######################## ---BOOKS CLASS---  #############################################

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    student_name = db.Column(db.String)
    student_city = db.Column(db.String)
    student_age = db.Column(db.Integer)
    student_grade = db.Column(db.Integer)  # 1/2/3

    def __init__(self, student_name, student_city, student_age, student_grade):
        self.student_name = student_name
        self.student_city = student_city
        self.student_age = student_age
        self.student_grade = student_grade

######################## ---BOOKS CRUDE---  #############################################

@app.route('/', methods=["POST", "GET"])
@app.route('/student', methods=["POST", "GET"])
@app.route('/student/<sid>', methods=["DELETE", "PUT"])
@cross_origin()
def crude_book(sid=0):
    if request.method == 'POST':
        request_data = request.get_json()
        student_name = request_data['student_name']
        student_city = request_data["student_city"]
        student_age = request_data["student_age"]
        student_grade = request_data["student_grade"]
        newStudent = Students(student_name, student_city, student_age, student_grade)
        db.session.add(newStudent)
        db.session.commit()
        return {"student": "created"}
    if request.method == 'GET':
        res = []
        for student in Students.query.all():
            res.append({"student_name": student.student_name, "id": student.id,
                        "student_city": student.student_city,
                       "student_age": student.student_age, "student_grade": student.student_grade})
        return (json.dumps(res))
    if request.method == 'DELETE':  # not implemented yet
        del_student = Students.query.filter_by(id=sid).first()
        db.session.delete(del_student)
        db.session.commit()
        return {"student": "deleted"}
    if request.method == 'PUT':
        request_data = request.get_json()
        upd_stuent = Students.query.filter_by(id=bid).first()
        upd_stuent.student_name = request_data['student_name']
        upd_stuent.student_city = request_data["student_city"]
        upd_stuent.student_age = request_data["student_age"]
        upd_stuent.student_grade = request_data["student_grade"]
        db.session.commit()
        return {"student": "updated"}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
