import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Objava(models.Model):
    # blank - nije neophodno u django-u
    # null - nije neophodno u bazi
    # id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    sadrzaj = models.TextField(blank=True, null=True)
    slika = models.FileField(upload_to='slike/', blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def serialize(self):
        return {
            "id": self.id,
            "sadrzaj": self.sadrzaj,
            "svidjanja": random.randint(0, 131)
        }