from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Host(User):
    def __init__(self, username, password, email, nationality, first_language, location):
        super().__init__(username, password, email)
        self.nationality = nationality
        self.first_language = first_language
        self.location = location
        self.email = email
        self.username = username
        self.password = password


class Worker(User):
    def __init__(self, username, password, email, nationality, first_language, desired_language, work_experience_category, work_experience):
        super().__init__(username, password, email)
        self.username = username
        self.password = password
        self.email = email
        self.nationality = nationality
        self.first_language = first_language
        self.desired_language = desired_language
        self.work_experience_category = work_experience_category
        self.work_experience = work_experience



        
        




