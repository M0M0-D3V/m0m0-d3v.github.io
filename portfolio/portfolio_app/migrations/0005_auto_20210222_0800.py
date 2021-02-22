# Generated by Django 3.1.4 on 2021-02-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_auto_20210222_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='project',
        ),
        migrations.AddField(
            model_name='teammember',
            name='projects',
            field=models.ManyToManyField(related_name='members', to='portfolio_app.Project'),
        ),
    ]