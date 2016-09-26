from django import forms
from .models import SignUp


class send_mail(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        return email

    def clean_full_name(self):
        username = self.cleaned_data.get('username')
        # write validation code.
        return username
