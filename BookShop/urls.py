
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings # new

from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name = 'home'),
    path('book/',include('book.urls')),
    path('user/',include('registration.urls')),

]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
