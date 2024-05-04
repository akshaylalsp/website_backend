from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        return self.create_user(username, email, password, **extra_fields)



class UserRegistration(AbstractUser):
    CS = 'CS'
    EC = 'EC'
    EEE = 'EEE'
    MECH = 'MECH'

    DEPARTMENT_CHOICES = [
        (CS, 'Computer Science'),
        (EC, 'Electronics and Communication'),
        (EEE, 'Electrical and Electronics'),
        (MECH, 'Mechanical'),
    ]

    department = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=100)
    cgpa = models.FloatField(null=True)
    higher_secondary_score = models.CharField(max_length=100)
    sslc_score = models.CharField(max_length=100)
    mooc_course = models.CharField(max_length=100)
    internship_attended = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15)
    groups = models.ManyToManyField('auth.Group', related_name='custom_users_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users_permissions')
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()