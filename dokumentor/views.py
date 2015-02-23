from django.shortcuts import render, redirect

from dokumentor.models import Project
from dokumentor.forms import NameStepForm, BuildStepForm, BetterDescriptionForm

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

def build_step(request):
    form = BuildStepForm()
    return render(request, 'dokumentor/build_step.html', {'form': form})

def view_project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'dokumentor/project.html', {'project': project})

def better_description(request):
    form = BetterDescriptionForm()
    return render(request, 'dokumentor/better_description.html', {'form': form})
