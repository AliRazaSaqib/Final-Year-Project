# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from check import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process', views.process, name='process'),
    path('help', views.help, name='help'),
    path('ImagePreview', views.ImagePreview, name="ImagePreview"),
    path('final', views.final, name='final'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    # path('search', views.search),
    path('accuracy', views.accuracy, name='accuracy'),
    path('developers', views.developers, name='developers')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
