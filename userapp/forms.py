from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from postapp.models import Post


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post sarlavhasi'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post mazmuni', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Post rasmi', 'rows': 5}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Post tagi', 'rows': 5}),
        }

