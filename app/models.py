from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to="app/images/")
    github = models.CharField(max_length=250, blank=True)
    website = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


