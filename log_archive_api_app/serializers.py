from django.contrib.auth.models import User, Group
from log_archive_api_app.models import LogEntry
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry