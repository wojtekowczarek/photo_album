from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField(label="login", max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password', max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    email = forms.CharField(label='email', max_length=100, widget=forms.EmailInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get


class UserAuthenticateForm(forms.Form):
    username = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)
