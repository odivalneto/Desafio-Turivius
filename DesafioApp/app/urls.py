from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'app'

router = routers.DefaultRouter(use_regex_path=False)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls), name='api'),
]