from django.urls import path,include
from . import views


urlpatterns = [

    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('signup/',views.user_signup,name = 'signup'),
    path('profile/',views.user_profile,name = 'profile'),


]
