# Generated by Django 5.0.2 on 2024-04-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuses',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='statuses',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
    ]
