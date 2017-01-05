from django import forms

class AnimalContactForm(forms.Form):
    nameField = forms.CharField(label="Your Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    emailField = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    textField = forms.CharField(label="Your query", widget=forms.Textarea(attrs={'placeholder': 'Your query'}))
