# Generated by Django 5.0.6 on 2024-06-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_student_student_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_avatar',
            field=models.ImageField(default='avatar.jpg', null=True, upload_to=''),
        ),
    ]
