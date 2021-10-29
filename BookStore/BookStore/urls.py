from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book/', include("Book.urls")),
    path('customer/',include("customer.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# python manage.py createsuperuser
