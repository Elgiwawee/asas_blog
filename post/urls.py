from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "post"

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('post_details/<int:pk>/', views.post_details, name='post_details'),
    path('update_post/<int:pk>/', views.update_post, name='update_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('all/', views.all_created_posts, name='all_created_posts'),
    path('', views.index, name='index'),  # The root URL now points to index view

     path('images/', views.image_list, name='image_list'),
    path('images/add/', views.add_image, name='add_image'),
    path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),

    path('documents/', views.document_list, name='document_list'),
    path('documents/add/', views.add_document, name='add_document'),
    path('documents/delete/<int:document_id>/', views.delete_document, name='delete_document'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
