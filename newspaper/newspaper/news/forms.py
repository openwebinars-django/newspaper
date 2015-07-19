from bootstrap3_datetime.widgets import DateTimePicker
from django import forms


from newspaper.news.models import News
from newspaper.news.models import Event

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'



#formulario de Eventos
class EventsForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'         
        start_date = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))