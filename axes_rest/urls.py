from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'accessattempts', views.AccessAttemptViewSet)
router.register(r'accesslog', views.AccessLogViewSet)

# app_name = 'axes_rest'

urlpatterns = router.urls