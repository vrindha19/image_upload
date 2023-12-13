from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Website_image_view
from .views import success
from .views import website_display


urlpatterns = [
    path('website_image/', Website_image_view, name='website_image_view'),
	path('success', success, name='success'),
	path('website_display', website_display, name = 'website_display'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)