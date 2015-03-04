from django.test import TestCase
from django.core.urlresolvers import reverse

from dokumentor.models import Project

class ProjectTests(TestCase):

    def test_project_as_name(self):
        Project.objects.create(name="SomeThing", duration=0)
        project = Project.objects.get(name="SomeThing")
        self.assertEqual(project.name, "SomeThing")

    def test_form_to_create_project(self):
        response = self.client.post(reverse('projects:name_step'),
            {'name': "A Project name", 'description': 'a beautiful project I started...'})

        projects = Project.objects.order_by('name')
        project = Project.objects.get(name="A Project name")
        self.assertEqual("A Project name", project.name)
        self.assertContains(response, '', status_code=302)

    def test_no_build_form_when_project_doesnt_exist(self):
        response = self.client.get(reverse('projects:build_step', args=[42]))

        self.assertRedirects(response, reverse('projects:index'), status_code=302, target_status_code=200)
