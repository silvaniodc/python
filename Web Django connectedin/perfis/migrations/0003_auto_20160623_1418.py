# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='convite',
            old_name='solitante',
            new_name='solicitante',
        ),
    ]
