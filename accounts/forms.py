from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

class CustomUserCreationForm(UserCreationForm): 
    email = forms.EmailField(required=True)
    
    class Meta: 
        model = CustomUser 
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta: 
        model = CustomUser
        fields = ('username', 'email')

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True)

class CustomSetPasswordForm(SetPasswordForm):
    class Meta: 
        model = CustomUser
        fields = ('NewPassword1', 'NewPassword2')

class CustomUserChangeForm(UserChangeForm):
    password = None 
    class Meta: 
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
        def __str__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'form-control'})
        def __str__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'class': 'form-control'})
        def __str__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        def __str__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
