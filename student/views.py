from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from student.models import Student
from student.schema import StudentIn, StudentOut

router = Router(tags=["student"])


# Create
@router.post("/student/create", response={201: StudentOut})
def create_student(request, payload: StudentIn):
    student = Student.objects.create(**payload.dict())
    return 201, student


# Read all
@router.get("/student/list", response=List[StudentOut])
def list_students(request):
    students = Student.objects.all()
    return 200, list(students)


# Read one
@router.get("/student/{student_id}", response=StudentOut)
def get_student(request, student_id: int):
    student = get_object_or_404(Student, id=student_id)
    return 200, student


# Update
@router.put("/student/update/{student_id}", response=StudentOut)
def update_student(request, student_id: int, payload: StudentIn):
    student = get_object_or_404(Student, id=student_id)
    for attr, value in payload.dict().items():
        setattr(student, attr, value)
    student.save()
    return student


# Delete
@router.delete("/student/delete/{student_id}", response={200: str})
def delete_student(request, student_id: int):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return 200, "Deleted successfully"
