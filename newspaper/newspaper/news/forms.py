from django import forms

from newspaper.news.models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'