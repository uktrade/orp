import logging

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models

logger = logging.getLogger(__name__)


class DataResponseModel(models.Model):
    title = models.TextField(null=True, blank=True)
    identifier = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    publisher_id = models.TextField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    format = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_issued = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    date_valid = models.TextField(null=True, blank=True)
    sort_date = models.DateField(null=True, blank=True)
    audience = models.TextField(null=True, blank=True)
    coverage = models.TextField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    license = models.TextField(null=True, blank=True)
    regulatory_topics = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    date_uploaded_to_orp = models.DateField(null=True, blank=True)
    has_format = models.TextField(null=True, blank=True)
    is_format_of = models.TextField(null=True, blank=True)
    has_version = models.TextField(null=True, blank=True)
    is_version_of = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    is_referenced_by = models.TextField(null=True, blank=True)
    has_part = models.TextField(null=True, blank=True)
    is_part_of = models.TextField(null=True, blank=True)
    is_replaced_by = models.TextField(null=True, blank=True)
    replaces = models.TextField(null=True, blank=True)
    related_legislation = models.TextField(null=True, blank=True)
    id = models.TextField(primary_key=True)
    score = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    def clean(self):
        """
        Validate the id field to check if it's a URL or not.
        """
        url_validator = URLValidator()
        try:
            url_validator(self.id)
        except ValidationError:
            # It's not a URL, which is acceptable as it's a
            # CharField that supports both
            pass
