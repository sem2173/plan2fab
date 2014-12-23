from django.shortcuts import render

from dokumentor.models import Project

def index(request):
    projects = Project.objects.order_by('created_at')
    context = { 'projects': projects, }
    return render(request, 'dokumentor/index.html', context)


def name_step(request):
    return HttpResponse("dokumentor name step")

