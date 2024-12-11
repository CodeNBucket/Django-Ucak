from django.shortcuts import render, redirect, get_object_or_404
from .models import Parca
from ucaklar.models import Ucak
from user.helpers import get_logged_in_user  
from django.http import HttpResponseRedirect  

def parca_listesi(request):
    """Takıma ait parçaları listele."""
    user = get_logged_in_user(request) 
    if isinstance(user, HttpResponseRedirect):  
        return user

    # Kullanıcının takımına ait parçalar
    parcalar = Parca.objects.filter(takim=user.takim)   
    return render(request, 'parcalar/parca_listesi.html', {'parcalar': parcalar})

def parca_ekle(request):
    """Yeni parça ekle."""
    user = get_logged_in_user(request)
    if isinstance(user, HttpResponseRedirect):
        return user

    if request.method == 'POST':
        stok = request.POST['stok']
        kategori = request.POST['kategori']  
        isim = request.POST['isim']

       
        takim_tipi = user.takim.takim_tipi
        if takim_tipi == 'URETIM':
            tur = request.POST['tur']
        else:
            tur = user.takim.takim_tipi  # Montaj takımıysa değiştirme, üretim yapamıyor

        # Parçayı ekle
        Parca.objects.create(kategori=kategori, tur=tur, takim=user.takim, stok=stok,isim=isim)
        return redirect('dashboard')

    return render(request, 'parcalar/parca_formu.html', {
        'user': user, 
        'ucaklar': Ucak.objects.all() 
    })

def parca_guncelle(request, id):
    """Var olan parçayı güncelle."""
    user = get_logged_in_user(request)
    if isinstance(user, HttpResponseRedirect):
        return user

    parca = get_object_or_404(Parca, id=id)

    # Takım yetkisini kontrol ediyoruz
    if parca.takim != user.takim:
        return render(request, 'error.html', {'error': 'Bu parçayı güncelleme yetkiniz yok.'})

    
    if request.method == 'POST':
        stok = request.POST['stok']
        isim=request.POST['isim']
        kategori = request.POST['kategori'] 
        
        parca.kategori = kategori
        parca.stok = stok
        parca.isim= isim
        parca.save()
        return redirect('dashboard')

    return render(request, 'parcalar/parca_formu.html', {'parca': parca, 'user': user, 'is_ekle': False})

def parca_sil(request, id):
    """Parça sil."""
    user = get_logged_in_user(request)
    if isinstance(user, HttpResponseRedirect):
        return user

    parca = get_object_or_404(Parca, id=id)

   
    if parca.takim != user.takim:
        return render(request, 'error.html', {'error': 'Bu parçayı silme yetkiniz yok.'})

    if request.method == 'POST':
        parca.delete()
        return redirect('dashboard')
    return render(request, 'parcalar/parca_sil_onay.html', {'parca': parca})
