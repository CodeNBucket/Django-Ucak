from django.db import models

class Ucak(models.Model):
    MODEL_TIPLERI = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'Akıncı'),
        ('KIZILELMA', 'Kızıl Elma'),
    ]

    isim = models.CharField(max_length=150, unique=True)
    model = models.CharField(max_length=50, choices=MODEL_TIPLERI) 
    def __str__(self):
        return self.isim
