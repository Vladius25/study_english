from django.conf import settings
from rest_framework import permissions


class HasAPIAccess(permissions.BasePermission):
    message = 'Secret неверный или отсутсвует'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_SECRET', '')
        return api_key == settings.API_SECRET
