from django.test import TestCase
from django.core.urlresolvers import reverse

from dokumentor.models import Project

class ProjectTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        Project.objects.create(name="SomeThing", duration=0)
        project = Project.objects.get(name="SomeThing")
        self.assertEqual(project.name, "SomeThing")

    def test_form_to_create_project(self):
        response = self.client.post(reverse('projects:name_step'), {'name': "A Project name", 'description': 'a beautiful project I started...'})

        projects = Project.objects.order_by('name')
        project = Project.objects.get(name="A Project name")
        self.assertEqual("A Project name", project.name)
        self.assertContains(response, '', status_code=302)

