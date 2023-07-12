import email
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                   "placeholder":"form_full_name"
                   }
            )
        )
    email=forms.EmailField(
        widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder":"Your Email"
               }
    )
                          )
    content=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control'
            ,"placeholder":"Your message"
            }
        )
                            )
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    
    
class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    password=forms.CharField(label='confirm Password',widget=forms.PasswordInput)
    
    
    def  clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('This username has been used')
        return username
    
    def  clean_email(self):
        username=self.cleaned_data.get('email')
        qs=User.objects.filter(email= email)
        if qs.exists():
            raise forms.ValidationError('This email has been used')
        return username
        
        
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password2 !=password:
            raise forms.ValidationError("Password must be the same")
        return data
    
        
  
       