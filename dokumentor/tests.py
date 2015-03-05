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

    def test_can_access_name_step(self):
        response = self.client.get(reverse('projects:name_step'))
        self.assertContains(response,'', status_code=200)

    def test_access_name_step_existant_project(self):
        project = Project.objects.create(name="SomeThing")
        response = self.client.get(reverse('projects:name_step', args=[project.id]))
        self.assertContains(response, project.name, status_code=200)

    def test_can_modify_name(self):
        project = Project.objects.create(name='something', description='blabla')
        response = self.client.post(reverse('projects:name_step', args=[project.id]),
            {'name': 'another thing', 'description': project.description})
        self.assertRedirects(response, reverse('projects:index'), status_code=302, target_status_code=200)
        project = Project.objects.get(id=project.id)
        self.assertEqual("another thing", project.name)
