from collections import defaultdict
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from user.models import User
from django.contrib.auth.hashers import check_password
from user.helpers import get_logged_in_user
from django.http import HttpResponseRedirect
from parcalar.models import Parca
from takimlar.models import Takim

def login_view(request):
    # Eğer kullanıcı zaten giriş yaptıysa, login sayfasına gidemez
    if 'user_id' in request.session:
        return redirect('dashboard')  # Giriş yaptıysa dashboard'a yönlendir

    if request.method == 'POST':
        username = request.POST['username'].strip()  
        password = request.POST['password']

        print(f"Attempting to log in with username: '{username}'")

        # Kullanıcıyı veritabanında arıyor
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            print("No user found with that username")
            return render(request, 'user/login.html', {'error': 'User does not exist'})

        # Parolayı kontrol ediyor
        if check_password(password, user.password):
            print("Password matched successfully!")

            # Kullanıcının giriş yaptığını kaydettim
            request.session['user_id'] = user.id  # Custom User için session'ı manuel olarak sakladım
            return redirect('dashboard')  # Başarıyla giriş yaptıysa dashboard'a yönlendiriyor
        else:
            print("Password does not match")
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})

    return render(request, 'user/login.html')


def dashboard_view(request):
    user = get_logged_in_user(request)
    if isinstance(user, HttpResponseRedirect):
        return user

   # Takım üyelerini ve parcaları çekiyor
    parcalar = Parca.objects.filter(takim=user.takim)
    takim_uyeleri = user.takim.uyeler.all()  #

    #
    all_parcalar = Parca.objects.all()
    kategorize_parcalar = {}

    for parca in all_parcalar:
        takim = parca.takim
        # Diğer takımların parçalarını göstermesi için kendi takımını almıyor
        if takim == user.takim:
            continue
        if takim not in kategorize_parcalar:
            kategorize_parcalar[takim] = []
        kategorize_parcalar[takim].append(parca)

    # Takım URETIM takımıysa parca düzenlemesine izin veriyor, html'de bunu URETIM ile MONTAJ takımlarına ayrı ayrı componentlar göstermek için kullandım 
    can_edit_parts = user.takim.takim_tipi == 'URETIM'

    # Kullanılması için dashboard'a yolluyor
    return render(request, 'user/dashboard.html', {
        'user': user,
        'parcalar': parcalar,
        'kategorize_parcalar': kategorize_parcalar,
        'can_edit_parts': can_edit_parts,   
        'takim_uyeleri': takim_uyeleri
    })


def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')
