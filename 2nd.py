import json
import hashlib
from datetime import datetime

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__

class Admin:
    def __init__(self, username, password):
        self.username = username
        # Simple hash for simulation
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def verify(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()