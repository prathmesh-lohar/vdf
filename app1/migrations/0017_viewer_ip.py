# Generated by Django 3.2.9 on 2022-01-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_viewer_ttl'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewer',
            name='ip',
            field=models.CharField(default='', max_length=500, unique=True),
        ),
    ]
