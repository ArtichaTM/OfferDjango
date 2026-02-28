from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('about.urls', 'about'), namespace='about')),

    path('admin/', admin.site.urls),
    path('filer/', include('filer.urls')),
]
