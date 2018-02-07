from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Section
from .serializers import SectionSerializer


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('subject',)
    serializer_class = SectionSerializer
