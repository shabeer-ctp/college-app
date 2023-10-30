# Generated by Django 4.2.3 on 2023-10-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('courses', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('materials', models.CharField(max_length=100)),
            ],
        ),
    ]
