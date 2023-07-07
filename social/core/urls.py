from django.contrib import admin
from django.urls import path, include
from django.conf import settings # importamos ajustes
from django.conf.urls.static import static # importamos archivos estaticos

from .views import HomeView # importar todo de path
from .views import notification_redirect, notifications_delete # importar todo de path

#PARA PDOER CAMBIAR LA IMAGEN DEL ADMIN DE DJANGO
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "HOLA! AQUI PUEDES MODERAR COALSOCIAL"
admin.site.site_title = "MODERAR COALSOCIAL"
admin.site.index_title = "BIENVENIDO AL ADMINISTRADOR DEL COALSOCIAL!"

urlpatterns = [
    path("admin/", admin.site.urls),

    #autenticar usuarios
    path('accounts/', include('allauth.urls')),

    path('users/', include('users.urls')),
    path('social/', include('social.urls')),

    path('', HomeView.as_view(), name='home'),
    #rediurect
    path('post/<str:dato>/<int:notification_id>/', notification_redirect.as_view(), name='notification-redirect'),
    #eliminar notificaiciones
    path('post/<str:user>/', notifications_delete.as_view(), name='notifications-delete'),
]

#PARA QUE PUEDAN FUNCIONAR LOS ARCHIVOS ESTATICOS EN EL MODO DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
