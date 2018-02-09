from django.urls import path

from ..apis import (
    SectionListView,
    SectionDetailView,
    SectionNoteListView,
    SectionNoteDetailView,
)

urlpatterns = [
    path(
        'section/',
        SectionListView.as_view(),
        name='section-list',
    ),
    path(
        'section/<int:section_pk>/',
        SectionDetailView.as_view(),
        name='section-detail',
    ),
    path(
        'section/<int:section_pk>/note/',
        SectionNoteListView.as_view(),
        name='section-note-list'
    ),
    path(
        'section/<int:section_pk>/note/<int:note_pk>/',
        SectionNoteDetailView.as_view(),
        name='section-note-detail'
    ),
]
