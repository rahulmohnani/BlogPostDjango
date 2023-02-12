from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile
from django.utils.translation import gettext_lazy as _ 


class SignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    
    def __init__(self, *args, **kwargs) :
        super(SignUpFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
            
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control",'readonly':'true'}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }

    
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ( 'old_password', 'new_password1', 'new_password2')
        
    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm new Password"
        

class EditProfilePageForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('bio','profile_pic')
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        }