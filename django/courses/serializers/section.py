from rest_framework import serializers

from ..models import Section

__all__ = (
    'SectionSerializer',
    'SectionDetailSerializer',
)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = (
            'pk',
            'subject',
            'title',
            'description',
        )


class SectionDetailSerializer(SectionSerializer):
    class Meta(SectionSerializer.Meta):
        fields = SectionSerializer.Meta.fields + (

        )
