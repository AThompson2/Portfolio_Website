# Generated by Django 3.0.5 on 2020-05-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0010_auto_20200519_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_content',
            name='image_content',
            field=models.ImageField(upload_to='static/images/NCD_Website'),
        ),
    ]
