from django.db import models


class SortableMixin(models.Model):
    _order = models.PositiveIntegerField('순서', default=0, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['_order']


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
