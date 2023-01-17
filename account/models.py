from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_customer = models.BooleanField('Customer', default=False)
    is_employee = models.BooleanField('Employee', default=False)