from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve media files correctly in development
#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
