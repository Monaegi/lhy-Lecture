from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import Section
from ..serializers import SectionSerializer, SectionDetailSerializer


class SectionListView(ListAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        return Section.objects.all()


class SectionDetailView(RetrieveAPIView):
    serializer_class = SectionDetailSerializer
    lookup_url_kwarg = 'section_pk'

    def get_queryset(self):
        return Section.objects.all()
