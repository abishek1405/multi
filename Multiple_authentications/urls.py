
from django.contrib import admin
from django.urls import path, include
from authentication import views


from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('work/',views.create_view),
    path('dddd/',views.fen),
    path('',views.come),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

] 
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
