from django.db import models

from .mixins import (
    TimeStampedMixin,
    SortableMixin,
)


class BaseModel(models.Model):
    class Meta:
        abstract = True


class SortModel(SortableMixin, BaseModel):
    class Meta(SortableMixin.Meta, BaseModel.Meta):
        abstract = True


class TimeModel(TimeStampedMixin, BaseModel):
    class Meta(TimeStampedMixin.Meta, BaseModel.Meta):
        abstract = True


class SortTimeModel(SortModel, TimeModel):
    class Meta(SortModel.Meta, TimeModel.Meta):
        abstract = True
