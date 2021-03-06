# Generated by Django 2.0.1 on 2018-07-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeDirectory', '0002_auto_20180731_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='full_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
