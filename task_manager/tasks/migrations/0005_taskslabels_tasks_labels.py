# Generated by Django 5.0.2 on 2024-04-07 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '__first__'),
        ('tasks', '0004_remove_tasks_date_crated_tasks_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.labels', verbose_name='label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks', verbose_name='task')),
            ],
        ),
        migrations.AddField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TasksLabels', to='labels.labels', verbose_name='labels'),
        ),
    ]