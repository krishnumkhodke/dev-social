# Generated by Django 3.2.7 on 2021-10-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
