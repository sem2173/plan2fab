from django.forms import ModelForm

from dokumentor.models import Project

class NameStepForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
