# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('dokumentor', '0003_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/medias/photos'), null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
