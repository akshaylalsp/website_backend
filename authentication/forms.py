from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import UserRegistration

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserRegistration
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'department',
            'registration_number',
            'admission_number',
            'cgpa',
            'higher_secondary_score',
            'sslc_score',
            'mooc_course',
            'internship_attended',
            'phone_number',
        ]

    # Custom validation for password
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")


        validate_password(password2)
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)