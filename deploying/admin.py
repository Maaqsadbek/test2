from django.contrib import admin

# Register your models here.
from django.contrib import admin
from deploying.models import *
# indexdagi maxsulotlar royxati uchun.
class AdminMaxsulotlar(admin.ModelAdmin):
    list_display = ['id','turi', 'nomi','old_prise', 'new_prise', 'rangi','desc','chegirma','rasm']
admin.site.register(Maxsulotlar, AdminMaxsulotlar)
# rang tanlanishi uchun
class AdminRang(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(rang, AdminRang)
#turlari uchun
class AdminTur(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(tur, AdminTur)
class AdminChegirmalar(admin.ModelAdmin):
    list_display = ['id','nomi','turi','narxi','rangi','desc']
admin.site.register(Chegirmalar, AdminChegirmalar)

class AdminHappy_clents1(admin.ModelAdmin):
    list_display = ['id','ismi','rasmi','desc']
admin.site.register(Happy_clents1, AdminHappy_clents1)
class AdminHappy_clents2(admin.ModelAdmin):
    list_display = ['id','ismi','rasmi','desc']
admin.site.register(Happy_clents2, AdminHappy_clents2)
class AdminHappy_clents3(admin.ModelAdmin):
    list_display = ['id','ismi','rasmi','desc']
admin.site.register(Happy_clents3, AdminHappy_clents3)
class AdminOnemail(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Onemail, AdminOnemail)

class AdminArizalar(admin.ModelAdmin):
    list_display = ['id','ism','fam','adres','ish_joy','telefon_raqam','maxsulot_nomi','soni']
admin.site.register(Arizalar, AdminArizalar)

class AdminSurat(admin.ModelAdmin):
    list_display = ['id','surat']
admin.site.register(Surat, AdminSurat)
