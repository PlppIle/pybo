from django import forms
from .models import UserProfile, Guestbook, FileUpload

class UserGuestBookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['content']
        labels = {
            'content': '내용',
        }

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields =['title', 'imgfile', 'content']
        label = {
            'title': '제목',
            'imgfile': '사진',
            'content': '내용',
        }