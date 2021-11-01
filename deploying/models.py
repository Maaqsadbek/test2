from django.db import models

# Create your models here.
from django.db import models
class rang(models.Model):
    nomi=models.CharField(max_length = 20)
    def __str__(self):
        return self.nomi
class tur(models.Model):
    nomi=models.CharField(max_length = 20)
    def __str__(self):
        return self.nomi
# indexsdagi maxsulotlar royxat uchun
class Maxsulotlar(models.Model):
    nomi=models.CharField(max_length = 40)
    turi=models.ForeignKey(tur,on_delete = models.CASCADE, null = True)
    old_prise=models.IntegerField()
    new_prise=models.IntegerField()
    rangi=models.ForeignKey(rang, on_delete = models.CASCADE, null = True)
    desc=models.CharField(max_length = 200)
    chegirma=models.CharField(max_length = 4,null = True)
    rasm=models.ImageField(upload_to = 'media/')
## indexsdagi cegirma maxsulotlar uchun
class Chegirmalar(models.Model):
    nomi = models.CharField(max_length = 40)
    turi = models.ForeignKey(tur, on_delete = models.CASCADE, null = True)
    narxi = models.IntegerField()
    rangi = models.ForeignKey(rang, on_delete = models.CASCADE, null = True)
    desc = models.CharField(max_length = 200)
    rasm = models.ImageField(upload_to = 'media/')
class Happy_clents1(models.Model):
    ismi = models.CharField(max_length = 40)
    rasmi=models.ImageField(upload_to = 'media/')
    desc=models.CharField(max_length = 200)
class Happy_clents2(models.Model):
    ismi = models.CharField(max_length = 40)
    rasmi=models.ImageField(upload_to = 'media/')
    desc=models.CharField(max_length = 200)
class Happy_clents3(models.Model):
    ismi = models.CharField(max_length = 40)
    rasmi=models.ImageField(upload_to = 'media/')
    desc=models.CharField(max_length = 200)
# Create your models here.
class Onemail(models.Model):
    nomi=models.EmailField(max_length = 200,null = True)
class Arizalar(models.Model):
    ism=models.CharField(max_length = 50)
    fam=models.CharField(max_length = 50)
    adres=models.CharField(max_length = 200)
    ish_joy=models.CharField(max_length = 200)
    telefon_raqam=models.IntegerField()
    maxsulot_nomi=models.CharField(max_length = 800)
    soni=models.IntegerField()
    def __str__(self):
        return self.soni
class Surat(models.Model):
    surat=models.ImageField(upload_to = 'media/')
