from rest_framework import serializers

from ..models import SectionNote

__all__ = (
    'SectionNoteSerializer',
    'SectionNoteDetailSerializer',
)


class SectionNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionNote
        fields = (
            'section',
            'title',
        )


class SectionNoteDetailSerializer(SectionNoteSerializer):
    class Meta(SectionNoteSerializer.Meta):
        fields = SectionNoteSerializer.Meta.fields + (
            'content',
        )
