from django.contrib import admin
from django.urls import path, include

urlpatterns = [ # Her bir app ve admin için ayrı urller ekledim
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  
    path('takimlar/', include('takimlar.urls')),  
    path('parcalar/', include('parcalar.urls')),
    path('ucaklar/', include('ucaklar.urls')),
    path('montaj/', include('montaj.urls')),


]
