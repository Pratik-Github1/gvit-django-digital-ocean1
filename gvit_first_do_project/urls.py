from django.contrib import admin
from django.urls import path
from gvit_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index , name="index"), 
    path('another_page/', views.another_page , name="another_page")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
