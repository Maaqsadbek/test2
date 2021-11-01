from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from deploying.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    menyu = Maxsulotlar.objects.all()
    chegirmalar = Chegirmalar.objects.all()
    mijozlar1 = Happy_clents1.objects.all()
    mijozlar2 = Happy_clents2.objects.all()
    mijozlar3 = Happy_clents3.objects.all()
    max_idlar = Maxsulotlar.objects.all()
    max_id = [1]
    for i in max_idlar:
        max_id.append(i.id)
    new_id = max(max_id)
    new_id = new_id + 1
    chek_idlar = Chegirmalar.objects.all()
    chek_id = [0]
    for i in chek_idlar:
        chek_id.append(i.id)
    new_chek_id = max(chek_id)
    new_id += new_chek_id
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
#### Search bilan iwlash#############
    # if not(request.POST.get('Search') is None):
    #     malumot = request.POST.get('Search')
    #     soz = malumot.strip()
    #     qidirish = Q(nomi__startswith=soz)|Q(turi__startswith=soz)
    #     maks = Maxsulotlar.objects.filter(qidirish)
    #
    #     return render(request, 'index.html',
    #                      {"Maks": maks, "new_id": new_id, 'menyu': menyu, 'chegirmalar': chegirmalar,
    #                       'mijozlar1': mijozlar1,
    #                       'mijozlar2': mijozlar2, 'mijozlar3': mijozlar3})

    return render(request, 'index.html',{ "new_id": new_id, 'menyu': menyu, 'chegirmalar': chegirmalar, 'mijozlar1': mijozlar1,'mijozlar2': mijozlar2, 'mijozlar3': mijozlar3})


def contact(request):
    if "ariza" in request.POST:
        if not (request.POST.get("ariza") is None):
            ism = request.POST.get("ism")
            fam = request.POST.get("fam")
            ish_joy = request.POST.get("ish")
            adres = request.POST.get("adres")
            tel_number = request.POST.get("tell")
            maxsulot_nomi = request.POST.get('message')

            Arizalar(Arizalar.soni + 1, ism, fam, ish_joy, adres, tel_number, maxsulot_nomi).save()
        ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
    return render(request, 'contact.html')


def product(request):
    menyu = Maxsulotlar.objects.all()
    chegirma_menyu = Chegirmalar.objects.all()
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()

    return render(request, 'product.html', {'menyu': menyu, 'chegirma_menyu': chegirma_menyu})


def services(request):
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
    return render(request, 'services.html')


def single(request, id=0):
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
#####single uchun######

    if id!= 0:
        acces=Maxsulotlar.objects.get(id=id)
        ####1 yillik tolovlar uchun ####
        narx=acces.new_prise
        qiymat=narx/100
        qiymat2=int(qiymat*120)
        umumiy_qiymat=int(qiymat2/12)
        #### 6 oylik tolov uchun #####
        narx6=int(narx/6)







    return render(request, 'single.html',{'acces':acces,'umumiy_qiymat':umumiy_qiymat,'qiymat2':qiymat2,
                                          'narx6':narx6,'narx':narx})
