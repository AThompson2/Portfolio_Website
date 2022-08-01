from django.db import models



# Create your models here.

# Project1
class Website_content(models.Model):
    headding_content = models.CharField(max_length=50, blank=True)
    image_content = models.ImageField(upload_to= 'images/NCD_Website', null=True, blank=True)
    content_paragraph = models.CharField(max_length=2000, blank=True)


    def __str__(self):
        return self.headding_content



class Website_steps(models.Model):
    headding_step = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=2000, blank=True)
    card_image = models.ImageField(blank=True)
    headding_model = models.CharField(max_length=50, blank=True)
    long_description = models.CharField(max_length=2000, blank=True)
    website_cont = models.ManyToManyField(Website_content, blank=True)


    def __str__(self):
        return self.headding_step

# End Project1

# Start project2

class content2(models.Model):
    headding_content = models.CharField(max_length=50, blank=True)
    image_content = models.ImageField(upload_to= 'images/NCD_Website', null=True, blank=True)
    content_paragraph = models.CharField(max_length=2000, blank=True)


    def __str__(self):
        return self.headding_content


class steps2(models.Model):
    headding_step = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=2000, blank=True)
    card_image = models.ImageField(blank=True)
    headding_model = models.CharField(max_length=50, blank=True)
    long_description = models.CharField(max_length=2000, blank=True)
    website_cont2 = models.ManyToManyField(content2, blank=True)


    def __str__(self):
        return self.headding_step

# End Project1



# Start contact models

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

# End contact models
