# Generated by Django 3.0.5 on 2020-05-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0019_auto_20200519_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_content',
            name='image_content',
            field=models.ImageField(upload_to=''),
        ),
    ]
