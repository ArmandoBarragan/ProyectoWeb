# Generated by Django 3.1.2 on 2020-11-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20201028_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(null=True, upload_to='static/media'),
        ),
    ]
