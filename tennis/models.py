from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.ForeignKey(Nation, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name