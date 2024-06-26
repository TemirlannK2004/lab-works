from django import forms
from .models import Item,Profile,User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
\


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
     
        fields = ['age', 'city', 'bio', 'profile_picture']


class SignupForm(forms.Form):
    uname = forms.CharField(required=True)
    fname = forms.CharField(required=True)
    lname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    pass1 = forms.CharField(required=True, widget=forms.PasswordInput())
    pass2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')
        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match")
        
        if (len(pass1) and len(pass2)) < 8:
            raise forms.ValidationError("Password should be at least 8 characters long")
        
        if not any(char.isupper() for char in pass1):
            raise forms.ValidationError(("Password should contain at least one uppercase letter"))

        if not any(char.islower() for char in pass1):
            raise forms.ValidationError(("Password should contain at least one lowercase letter"))
          
        uname = cleaned_data.get('uname')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Username is already taken")
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already taken")
        return cleaned_data 
    

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('pass')
        
        if not (username and password):
            raise forms.ValidationError("Username and password are required.")
        
        user = authenticate(username=username, password=password)
        
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        
        return cleaned_data


class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(SigninForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("pass")

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid login credentials")
        return cleaned_data



class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'





class CreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'categorylist':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileField( widget=forms.FileInput( attrs={'class':'form-control'})),
            'recipe':forms.FileField( widget=forms.FileInput( attrs={'class':'form-control'})),
            
        }


        


class CreateUserForm(forms.ModelForm):
   
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    pass1 = forms.CharField(required=True, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'pass1']



