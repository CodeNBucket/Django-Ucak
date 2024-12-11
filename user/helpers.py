from django.shortcuts import redirect
from user.models import User

def get_logged_in_user(request): # @-kendi basit authentication sistemimi kurup çalıştırmak user modelini değiştirmekten daha mantıklı geldi
    if 'user_id' not in request.session: # user_id'nin sessionda olup olmadığına bakıyor, eğer varsa user'ı returnluyor, eğer yoksa login sayfasına yönlendiriyor 
        return redirect('login')  
    
    user_id = request.session['user_id']
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return redirect('login')  # Redirect if user does not exist
