from django import forms


class students(forms.Form):
    names = forms.CharField(widget=forms.TextInput
        (attrs={
            "placehoder":"Enter Your Message...",
            "class":"form-control bg-success-subtle"
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
             "placehoder":"Enter Your Email...",
             "class":"form-control bg-warning-subtle"
        }
    ))