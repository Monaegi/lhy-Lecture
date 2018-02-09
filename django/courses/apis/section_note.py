from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import SectionNote
from ..serializers import (
    SectionNoteSerializer,
    SectionNoteDetailSerializer)


class SectionNoteListView(ListAPIView):
    serializer_class = SectionNoteSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )

    def get_queryset(self):
        section_pk = self.kwargs.get('section_pk')
        return SectionNote.objects.filter(section_id=section_pk)


class SectionNoteDetailView(RetrieveAPIView):
    serializer_class = SectionNoteDetailSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    lookup_url_kwarg = 'note_pk'

    def get_queryset(self):
        section_pk = self.kwargs.get('section_pk')
        return SectionNote.objects.filter(section_id=section_pk)
