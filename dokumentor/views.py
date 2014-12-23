from django.shortcuts import render, redirect

from dokumentor.models import Project
from dokumentor.forms import NameStepForm

def index(request):
    projects = Project.objects.order_by('created_at')
    context = { 'projects': projects, }
    return render(request, 'dokumentor/index.html', context)


def name_step(request):
    if request.method == 'POST':
        form = NameStepForm(request.POST)
        new_project = form.save()
        return redirect('projects:index')

    else:
        form = NameStepForm()
    return render(request, 'dokumentor/name_step.html', {'form': form})

