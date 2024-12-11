from django.db import models
from ucaklar.models import Ucak
from takimlar.models import Takim

class Parca(models.Model):
    # Parça türleri
    PARCA_TIPLERI = [
        ('SOLKANAT', 'Sol Kanat'),  #
        ('SAGKANAT', 'Sağ Kanat'),  
        ('GOVDE', 'Gövde'),         
        ('KUYRUK', 'Kuyruk'),       
        ('AVIYONIK', 'Aviyonik'),   
    ]

    KATEGORI_TIPLERI = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'Akıncı'),
        ('KIZILELMA', 'Kızıl Elma'),
    ]

   
    isim = models.CharField(max_length=150, blank=True)  
    

    kategori = models.CharField(max_length=50, choices=KATEGORI_TIPLERI)  
    
    
    tur = models.CharField(max_length=50, choices=PARCA_TIPLERI)
    
   
    takim = models.ForeignKey(Takim, on_delete=models.CASCADE)
    
    
    stok = models.PositiveIntegerField(default=0)
    
    
    kullanildi = models.BooleanField(default=False)
    
    
    ucak = models.ForeignKey(Ucak, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.isim} - {self.kategori} - {self.tur} ({'Kullanıldı' if self.kullanildi else 'Kullanılmadı'})"
    
    @classmethod
    def check_part_availability(cls, part_type, aircraft_type):
        """
        Kontrol eder, belirtilen tipteki parçaların yeterli olup olmadığını.
        Belirtilen uçak tipi için (Örneğin: TB2, AKINCI) envanterde parça olup olmadığı kontrol edilir.
        """
        try:
            part = cls.objects.get(tur=part_type, kategori=aircraft_type)
            return part.stok > 0  
        except cls.DoesNotExist:
            return False  