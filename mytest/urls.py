from django.urls import  path 
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    path('',views.home,name='home'),
    path('show/<int:id_show>',views.show,name='show'),
    path('asd/',views.asd,name='asd'),
    path('try/',views.side,name='side'),#try=====================================
    path('forms_html/<int:f_h>/',views.forms_html,name='forms_html'),
    path('delet/<int:dl_d>/',views.de_let,name='de_let'),




    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_views.LogoutView.as_view()),
    path('password_change/',auth_views.PasswordChangeView.as_view()),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view()),
   
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


       
