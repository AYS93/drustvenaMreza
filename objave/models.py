import random
from django.db import models

# Create your models here.
class Objava(models.Model):
    # blank - nije neophodno u django-u
    # null - nije neophodno u bazi
    # id = models.AutoField(primary_key=True)
    sadrzaj = models.TextField(blank=True, null=True)
    slika = models.FileField(upload_to='slike/', blank=True, null=True)

    def serialize(self):
        return {
            "id": self.id,
            "sadrzaj": self.sadrzaj,
            "svidjanja": random.randint(0, 131)
        }