# Generated by Django 3.0.5 on 2022-06-20 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0026_auto_20211205_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='content2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headding_content', models.CharField(max_length=50)),
                ('image_content', models.ImageField(blank=True, upload_to='images/NCD_Website')),
                ('content_paragraph', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='steps2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headding_step', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=2000)),
                ('card_image', models.ImageField(upload_to='')),
                ('headding_model', models.CharField(max_length=50)),
                ('long_description', models.CharField(max_length=2000)),
                ('website_cont2', models.ManyToManyField(to='Website.content2')),
            ],
        ),
    ]
