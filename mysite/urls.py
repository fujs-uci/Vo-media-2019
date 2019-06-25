from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.mysite_home, name='home'),
    path('gallery/', views.mysite_gallery, name='gallery'),
    path('gallery/<str:image_slug>/', views.mysite_view_image, name='view_image'),
    path('contact-me/', views.mysite_contact_me, name='contact_me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
