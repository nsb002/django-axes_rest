from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

from axes.models import AccessAttempt, AccessLog

class AccessAttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessAttempt
        fields = ('url', 'user_agent', 'ip_address', 'username', 'http_accept',
                  'path_info', 'attempt_time', 'get_data', 'post_data',
                  'failures_since_start')

class AccessLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessLog
        fields = ('url', 'user_agent', 'ip_address', 'username', 'http_accept',
                  'path_info', 'attempt_time', 'trusted', 'logout_time')