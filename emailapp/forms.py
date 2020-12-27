from django import forms

class Emailform(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email