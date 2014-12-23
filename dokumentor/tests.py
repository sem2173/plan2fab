from django.test import TestCase
from django.core.urlresolvers import reverse

from dokumentor.models import Project

class ProjectTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        project = Project(name="SomeThing")
        self.assertEqual(project.name, "SomeThing")

    def test_form_to_create_project(self):
        response = self.client.get(reverse('projects:create'))
        self.assertContains(response, '', status_code=200)

