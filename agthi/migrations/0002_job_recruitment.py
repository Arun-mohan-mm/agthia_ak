# Generated by Django 5.0.6 on 2024-07-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agthi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('salary_range', models.CharField(max_length=200, null=True)),
                ('age_limit', models.CharField(max_length=200, null=True)),
                ('employment_type', models.CharField(max_length=200, null=True)),
                ('place', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
