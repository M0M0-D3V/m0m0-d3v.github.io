# Generated by Django 3.1.4 on 2021-02-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_project_demo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]