from django import forms
from .models import Project
from .models import Lesson

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_number', 'project_name', 'client', 'project_location', 'market_sector')

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('projectnumber', 'projectname', 'client', 'projectlocation', 'description', 'division','marketsector','discipline','memo','linkfile')
