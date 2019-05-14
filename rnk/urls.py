from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login', auth_views.LoginView.as_view(template_name='acc/loginpg.html'), name="login"),
    path('', views.home, name='home'),
    #path('authen/', views.authen, name='authen'),
    # path('logout/', views.lout, name='lout'),
    path('printw/', views.printw, name='printw'),
    path('dload/', views.dload, name='dload'),
    path('getplotdata/', views.plot, name='getplotdata'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
