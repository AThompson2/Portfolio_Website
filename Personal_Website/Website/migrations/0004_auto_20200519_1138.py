# Generated by Django 3.0.5 on 2020-05-19 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20200517_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_content',
            name='image_content',
            field=models.ImageField(upload_to=''),
        ),
    ]
