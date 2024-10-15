from django.forms import ModelForm
from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import Profile

class UserInfoForm(forms.ModelForm):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.update({
            'name':'phone',
            'id':'phone',
            'placeholder':'Enter Your Phone Number',
            'class':'form-row',
            'type':'text'
        })
        self.fields["address"].widget.attrs.update({
            'name':'address',
            'id':'address',
            'placeholder':'Enter Your Current Address',
            'class':'form-row',
            'type':'text'
        })
        self.fields["city"].widget.attrs.update({
            'name':'city',
            'id':'city',
            'placeholder':'Enter Your Current City',
            'class':'form-row',
            'type':'text'
        })
        self.fields["country"].widget.attrs.update({
            'name':'country',
            'id':'country',
            'placeholder':'Enter Your Current Country',
            'class':'form-row',
            'type':'text'
        })
        
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'country']
class ChangePasswordForm(SetPasswordForm):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'placeholder':'Enter Your Password',
            'class':'form-row',
            'type':'text'
        })
        self.fields["new_password2"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'placeholder':'Confirm Your Password',
            'class':'form-row',
            'type':'text'
        })
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
class UpdateUserForm(UserChangeForm):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        password=None
        
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'placeholder':'Enter Your Username',
            'class':'form-row',
            'type':'text'
        })
        self.fields["first_name"].widget.attrs.update({
            'name':'firstname',
            'id':'firstname',
            'placeholder':'Enter Your First Name',
            'class':'form-row',
            'type':'text'
        })
        self.fields["last_name"].widget.attrs.update({
            'name':'lastname',
            'id':'lastname',
            'placeholder':'Enter Your Last Name',
            'class':'form-row',
            'type':'text'
        })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'placeholder':'Enter Your Email',
            'class':'form-row',
            'type':'email'
        })
        
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class SignUpForm(UserCreationForm):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'placeholder':'Enter Your Password',
            'class':'form-row',
            'type':'text'
        })
        self.fields["password2"].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'placeholder':'Confirm Your Password',
            'class':'form-row',
            'type':'text'
        })
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'placeholder':'Enter Username',
            'class':'form-row',
            'type':'text'
        })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'placeholder':'Enter Your Email',
            'class':'form-row',
            'type':'email'
        })
        self.fields["first_name"].widget.attrs.update({
            'name':'firstname',
            'id':'firstname',
            'placeholder':'Enter Your First Name',
            'class':'form-row',
            'type':'text'
        })
        self.fields["last_name"].widget.attrs.update({
            'name':'lastname',
            'id':'lastname',
            'placeholder':'Enter Your Last Name',
            'class':'form-row',
            'type':'text'
        })
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']