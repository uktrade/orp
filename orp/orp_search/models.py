import logging

from django.db import models

logger = logging.getLogger(__name__)
_default_char_size = 2048


class DataResponseModel(models.Model):
    title = models.CharField(max_length=_default_char_size)
    identifier = models.URLField(unique=True)
    publisher = models.CharField(
        max_length=_default_char_size, default="Legislation"
    )
    language = models.CharField(max_length=3, default="eng")
    format = models.CharField(max_length=50, default="HTML")
    description = models.TextField()
    date_issued = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    date_valid = models.DateField(null=True, blank=True)
    audience = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    coverage = models.CharField(max_length=2, default="gb")
    subject = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    type = models.CharField(max_length=50)
    license = models.CharField(max_length=255, null=True, blank=True)
    regulatory_topics = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    status = models.CharField(max_length=50, default="Active")
    date_uploaded_to_orp = models.DateField(null=True, blank=True)
    has_format = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    is_format_of = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    has_version = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    is_version_of = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    references = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    is_referenced_by = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    has_part = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    is_part_of = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    is_replaced_by = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    replaces = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    related_legislation = models.CharField(
        max_length=_default_char_size, null=True, blank=True
    )
    id = models.URLField(primary_key=True)
    score = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
