from django import forms

class AnimalContactForm(forms.Form):
    nameField = forms.CharField(label="Your Name", max_length=100)
    emailField = forms.EmailField(label="Email")
    textField = forms.CharField(label="Your query", widget=forms.Textarea)
