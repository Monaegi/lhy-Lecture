from django.db import models


class SortableMixin(models.Model):
    _order = models.PositiveIntegerField('순서', default=0, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['_order']
