from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('saludo/', views.saludo, name='saludo'),
    # path('simple/', views.simple, name='simple'),
    # path('dinamico/<str:name>', views.dinamico, name='dinamico')
    path('comentarios/', include('comentarios.urls')),
    path('post/', include('post.urls')),
]
