# Generated by Django 5.0.6 on 2024-06-15 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headteacher', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='headteacher.class'),
        ),
    ]
