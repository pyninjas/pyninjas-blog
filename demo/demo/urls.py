from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from filebrowser.sites import site


site.directory = "uploads/"


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('blog/', include('pyninjas.blog.urls', namespace='blog')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
