from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from log_archive_api_app.models import LogEntry
from rest_framework import viewsets
from log_archive_api_app.serializers import UserSerializer, GroupSerializer, LogEntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LogEntryViewSet(viewsets.ModelViewSet):

    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer