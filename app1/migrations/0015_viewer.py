# Generated by Django 3.2.9 on 2022-01-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_mou'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl', models.IntegerField()),
            ],
        ),
    ]
