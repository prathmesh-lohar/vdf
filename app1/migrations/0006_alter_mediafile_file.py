# Generated by Django 3.2.9 on 2021-12-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20211216_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(default='', upload_to='app1/mediafiles/imgs'),
        ),
    ]
