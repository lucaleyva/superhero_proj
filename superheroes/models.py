from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)
    # image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name