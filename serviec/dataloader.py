from fastapi import FastAPI, HTTPException
import uvicorn 

from pydantic import BaseModel
from database import *

app = FastAPI()
connection = create_connection()

class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/students/")
def api_create_student(student: Student):
    create_student(connection, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/students/")
def api_get_students():
    students = get_students(connection)
    print("hhh")
    return students

@app.get("/students/{student_id}")
def api_get_student(student_id: int):
    student = get_student_by_id(connection, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def api_update_student(student_id: int, student: Student):
    update_student(connection, student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def api_delete_student(student_id: int):
    delete_student(connection, student_id)
    return {"message": "Student deleted successfully"}