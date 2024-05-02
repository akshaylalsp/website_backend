from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
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
    cgpa = models.FloatField()
    higher_secondary_score = models.CharField(max_length=100)
    sslc_score = models.CharField(max_length=100)
    mooc_course = models.CharField(max_length=100)
    internship_attended = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    groups = models.ManyToManyField('auth.Group', related_name='custom_users_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users_permissions')