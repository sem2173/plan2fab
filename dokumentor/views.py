from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from dokumentor.models import Project
from dokumentor.forms import (
    NameStepForm,
    BuildStepForm,
    BetterDescriptionForm,
    PhotoStepForm,
)

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

def build_step(request, id):
    try:
        project = Project.objects.get(id=id)
    except ObjectDoesNotExist:
         return redirect('projects:index')

    if request.method == 'POST':
        BuildStepForm(request.POST, instance=project).save()
        return redirect('projects:index')
    else:
        form = BuildStepForm(instance=project)
        return render(request, 'dokumentor/build_step.html', {'form': form})

def photo_step(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = PhotoStepForm(request.POST, request.FILES, instance=project)
        new_photo = form.save()
        return redirect('projects:index')
    else:
        form = PhotoStepForm(instance=project)
    return render(request, 'dokumentor/photo_step.html', {'form': form})

def view_project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'dokumentor/project.html', {'project': project})

def better_description(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = BetterDescriptionForm(request.POST, instance=project)
        new_tags = form.save()
        return redirect('projects:index')
    else:
        form = BetterDescriptionForm(instance=project)
    return render(request, 'dokumentor/better_description.html', {'form': form})
