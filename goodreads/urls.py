from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import landing

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing, name='landing'),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
