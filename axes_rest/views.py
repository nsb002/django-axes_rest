from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.apps import apps

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, AccessAttemptSerializer, AccessLogSerializer

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth import logout

# Found there : https://stackoverflow.com/a/46451704/2309273
class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

# @TODO: Require specific user privileges (or group) to access the API.

class UserViewSet(LoginRequiredMixin, LogoutIfNotStaffMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_required = 'is_staff'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(LoginRequiredMixin, LogoutIfNotStaffMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_required = 'is_staff'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AccessAttemptViewSet(LoginRequiredMixin, LogoutIfNotStaffMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows AccessAttempt to be viewed or edited.
    """
    permission_required = 'is_staff'
    model = apps.get_model('axes', 'AccessAttempt')
    queryset = model.objects.all()
    serializer_class = AccessAttemptSerializer

class AccessLogViewSet(LoginRequiredMixin, LogoutIfNotStaffMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows AccessLog to be viewed or edited.
    """
    permission_required = 'is_staff'
    model = apps.get_model('axes', 'AccessLog')
    queryset = model.objects.all()
    serializer_class = AccessLogSerializer