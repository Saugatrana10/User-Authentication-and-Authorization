from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.


# how the register and login works 

# [ User Registers ]
#    |
#    v
# Data saved in DATABASE
# (username, email, password hash, etc.)
#    |
#    v
# [ User Logs In ]
#    |
#    v
# Credentials checked against DATABASE
#    |
#    v
# If valid → SESSION created
#    |
#    v
# Session ID stored in BROWSER COOKIE
#    |
#    v
# Session data stored on SERVER (links session ID to user)
#    |
#    v
# [ Authenticated Requests ]
# Browser sends session ID → Server looks up session → User recognized as logged in


# from django.db import models

# class Email(models.Model):
#     subject = models.CharField(max_length=200)
#     body = models.TextField()

#     class Meta:
#         permissions = [
#             ("can_view_protected", "Can view protected page"),
#         ]



class ProtectedPage(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('can_view_protected', 'Can view protected page'),
        ]

