# Generated by Django 3.2.25 on 2025-05-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=50)),
                ('e_email', models.EmailField(max_length=25)),
            ],
        ),
    ]
