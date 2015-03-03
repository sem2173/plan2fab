from django.forms import ModelForm

from dokumentor.models import Project

class NameStepForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class BuildStepForm(ModelForm):
    class Meta:
        model = Project
        fields = ['furnitures', 'duration']

class BetterDescriptionForm(ModelForm):
    class Meta:
        model = Project
        fields = ['history', 'tags']

class PhotoStepForm(ModelForm):
    class Meta:
        model = Project
        fields = ['photo']
