from typing import List

from ninja import ModelSchema, Schema
from pydantic import validator

from student.models import Student


class StudentIn(Schema):
    name: str
    gender: str
    email: str


class StudentOut(Schema):
    id: int
    name: str
    gender: str
    email: str
