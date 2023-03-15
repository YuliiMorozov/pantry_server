from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re


def validate_username(username):
    
    if not re.match(r'^[a-zA-Z]{5,10}$', username):
        raise ValidationError('Username should be between 5 and 10 characters long and contain only Latin letters.')
    
    if User.objects.filter(username=username).exists():
        raise ValidationError('A user with that username already exists.')
    

def validate_email(email):
    
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError('Invalid email format')
    
    if User.objects.filter(email=email).exists():
        raise ValidationError('Email already exists')
    

def validate_password(password):

    if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$', password):
        raise ValidationError(
            'Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*()_+)'
        )