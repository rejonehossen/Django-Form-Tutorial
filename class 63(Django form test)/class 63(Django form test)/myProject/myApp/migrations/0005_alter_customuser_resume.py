# Generated by Django 5.0.6 on 2024-06-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_seekerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='resume',
            field=models.FileField(null=True, upload_to='static/resume'),
        ),
    ]