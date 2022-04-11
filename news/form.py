from django import forms

from .models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            'title',
            'image_image',
            'detail',
            'add_time',
            'post_viewcount',
            'category'
        )
        widgets = {
            'title': forms.TextInput,
            'detail': forms.TextInput,
        }