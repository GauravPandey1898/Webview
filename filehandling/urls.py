from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='filehandling'

urlpatterns=[
    path('',views.homeView,name="home"),
    path('home_auth/',views.home_authView,name="home_auth"),
    path('login/',views.loginView,name="login"),
    path('login/register',views.registerView,name="register"),
    path('logout/',views.logoutView,name="logout"),
    path('imageupload/',views.image_uploadView,name="image_upload"),
    path('viewimage/',views.imageView,name="see-image"),
    path('classification/',views.classificationView,name="classification"),
    #path('emotion-analysis/',views.emotionView,name="emotion-analysis"),
    #path('gender-analysis/',views.genderView,name="gender-analysis"),
    #path('age-analysis/',views.ageView,name="age-analysis"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
