import os
from flask import Flask, render_template,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'lessons.sqlite?check_same_thread=False')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

association_table = db.Table('association', db.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'))
)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Vardas", db.String(50), nullable=False)
    l_name = db.Column("Pavardė", db.String(50), nullable=False)
    full_name = db.Column("Vardas ir Pavardė", db.String)
    lessons = db.relationship("Lesson", secondary=association_table, back_populates="students")
    
class Lesson(db.Model):
    __tablename__ = "lesson"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Pavadinimas", db.String(50), nullable=False)
    students = db.relationship('Student', secondary=association_table, back_populates="lessons")
    lecturer = db.relationship('Lecturer')
    lecturer_id = db.Column(db.Integer, db.ForeignKey("lecturer.id"))
    
class Lecturer(db.Model):
    __tablename__ = "lecturer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Vardas", db.String(50), nullable=False)
    l_name = db.Column("Pavardė", db.String(50), nullable=False)
    full_name = db.Column("Vardas ir Pavardė", db.String)
    lessons = db.relationship("Lesson")
    
@app.route("/add_lecturer", methods=["GET", "POST"])
def add_lecturer():
    db.create_all()
    form = forms.LecturerForm()
    if form.validate_on_submit():
        add_lecturer = Lecturer(name=form.name.data, l_name=form.l_name.data, full_name=f"{form.name.data} {form.l_name.data}")
        for lesson in form.lessons.data:
            assigned_lesson = Lesson.query.get(lesson.id)
            add_lecturer.lessons.append(assigned_lesson)
        db.session.add(add_lecturer)
        db.session.commit()
        return render_template("add_lecturer.html", form=False)
    return render_template("add_lecturer.html", form=form)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    db.create_all()
    form = forms.StudentForm()
    if form.validate_on_submit():
        add_student = Student(name=form.name.data, l_name=form.l_name.data, full_name=f"{form.name.data} {form.l_name.data}")
        for lesson in form.lessons.data:
            assigned_lesson = Lesson.query.get(lesson.id)
            add_student.lessons.append(assigned_lesson)
        db.session.add(add_student)
        db.session.commit()
        return render_template("add_student.html", form=False)
    return render_template("add_student.html", form=form)

@app.route("/add_lesson", methods=["GET", "POST"])
def add_lesson():
    db.create_all()
    form = forms.LessonForm()
    if form.validate_on_submit():
        add_lesson = Lesson(name=form.name.data, lecturer_id=form.lecturer.data.id)
        for student in form.students.data:
            attending_student = Student.query.get(student.id)
            add_lesson.students.append(attending_student)
        db.session.add(add_lesson)
        db.session.commit()
        return render_template("add_lesson.html", form=False)
    return render_template("add_lesson.html", form=form)


    
@app.route("/lecturer_delete/<int:id>")
def lecturer_delete(id):
    uzklausa = Lecturer.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('lecturers'))

@app.route("/student_delete/<int:id>")
def student_delete(id):
    uzklausa = Student.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('students'))

@app.route("/lesson_delete/<int:id>")
def lesson_delete(id):
    uzklausa = Lesson.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('lessons'))
    
@app.route("/lecturers")
def lecturers():
    try:
        lecturers = Lecturer.query.all()
    except:
        lecturers = []
    return render_template("lecturers.html", lecturers=lecturers)

@app.route("/students")
def students():
    try:
        all_students = Student.query.all()
    except:
        all_students = []
    return render_template("students.html", all_students = all_students)

@app.route("/lessons")
def lessons():
    try:
        all_lessons = Lesson.query.all()
    except:
        all_lessons = []
    return render_template("lessons.html", all_lessons = all_lessons)

@app.route("/")
def about():
    return render_template('base.html')

if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)