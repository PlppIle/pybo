from django import forms
from .models import UserProfile, Guestbook

class UserGuestBookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['content']
        labels = {
            'content': '내용',
        }