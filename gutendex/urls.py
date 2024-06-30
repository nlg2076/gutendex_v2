from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from books import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='home.html')),
    re_path(r'^', include(router.urls)),
    path('admin/', admin.site.urls),  # Add this line
]