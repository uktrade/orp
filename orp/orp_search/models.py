import json
import logging
import uuid

from datetime import timedelta

from orp_search.config import SearchDocumentConfig

from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class PublicGatewayCache(models.Model):
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    description = models.TextField()
    date_issued = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_valid = models.DateTimeField()
    audience = models.CharField(max_length=255)
    coverage = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    regulatory_topics = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date_uploaded_to_orp = models.CharField(max_length=255)
    has_format = models.CharField(max_length=255)
    is_format_of = models.CharField(max_length=255)
    has_version = models.CharField(max_length=255)
    is_version_of = models.CharField(max_length=255)
    references = models.CharField(max_length=255)
    is_referenced_by = models.CharField(max_length=255)
    has_part = models.CharField(max_length=255)
    is_part_of = models.CharField(max_length=255)
    is_replaced_by = models.CharField(max_length=255)
    replaces = models.CharField(max_length=255)
    related_legislation = models.CharField(max_length=255)

    search_terms = models.CharField(max_length=255)
    document_types = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for TTL
    TTL = timedelta(days=1)  # Time-To-Live duration for cache entries

    @staticmethod
    def _config_to_key(config: SearchDocumentConfig):
        # Convert config to a tuple that can be used as a key
        return config.search_terms, json.dumps(
            config.document_types, sort_keys=True
        )

    @classmethod
    def get_cached_response(cls, config):
        # Look up the cached response for the given config
        key = cls._config_to_key(config)
        try:
            cache_entries = cls.objects.filter(
                search_terms=key[0], document_types=key[1]
            )
            if not cache_entries:
                return None
            if any(cls.is_expired(entry) for entry in cache_entries):
                # If any entry is expired, delete all related entries and
                # return None
                cache_entries.delete()
                return None
            return [
                {
                    "title": entry.title,
                    "identifier": entry.identifier,
                    "publisher": entry.publisher,
                    "language": entry.language,
                    "format": entry.format,
                    "description": entry.description,
                    "date_issued": entry.date_issued,
                    "date_modified": entry.date_modified,
                    "date_valid": entry.date_valid,
                    "audience": entry.audience,
                    "coverage": entry.coverage,
                    "subject": entry.subject,
                    "type": entry.type,
                    "license": entry.license,
                    "regulatory_topics": entry.regulatory_topics,
                    "status": entry.status,
                    "date_uploaded_to_orp": entry.date_uploaded_to_orp,
                    "has_format": entry.has_format,
                    "is_format_of": entry.is_format_of,
                    "has_version": entry.has_version,
                    "is_version_of": entry.is_version_of,
                    "references": entry.references,
                    "is_referenced_by": entry.is_referenced_by,
                    "has_part": entry.has_part,
                    "is_part_of": entry.is_part_of,
                    "is_replaced_by": entry.is_replaced_by,
                    "replaces": entry.replaces,
                    "related_legislation": entry.related_legislation,
                    "created_at": entry.created_at,
                }
                for entry in cache_entries
            ]
        except cls.DoesNotExist:
            return None

    @classmethod
    def cache_response(cls, config, response):
        logger.info(f"caching service received response: {response}")

        # Cache the response for the given config
        if isinstance(response, list) and response:
            records = response[0].get("rows", [])
        else:
            records = []

        if not records:
            logger.info("no records to cache")
            return

        logger.info("attempting to cache records: %s", records)

        # Store each record in the response in the cache
        key = cls._config_to_key(config)
        for record in records:
            logger.info("caching record: %s", record)
            record_id = record.get(
                "id", str(uuid.uuid4())
            )  # Use a unique identifier for each record
            cls.objects.update_or_create(
                search_terms=key[0],
                document_types=key[1],
                record_id=record_id,
                defaults={
                    "title": record.get("title"),
                    "identifier": record.get("identifier"),
                    "publisher": record.get("publisher"),
                    "language": record.get("language"),
                    "format": record.get("format"),
                    "description": record.get("description"),
                    "date_issued": record.get("date_issued"),
                    "date_modified": record.get("date_modified"),
                    "date_valid": record.get("date_valid"),
                    "audience": record.get("audience"),
                    "coverage": record.get("coverage"),
                    "subject": record.get("subject"),
                    "type": record.get("type"),
                    "license": record.get("license"),
                    "regulatory_topics": record.get("regulatory_topics"),
                    "status": record.get("status"),
                    "date_uploaded_to_orp": record.get("date_uploaded_to_orp"),
                    "has_format": record.get("has_format"),
                    "is_format_of": record.get("is_format_of"),
                    "has_version": record.get("has_version"),
                    "is_version_of": record.get("is_version_of"),
                    "references": record.get("references"),
                    "is_referenced_by": record.get("is_referenced_by"),
                    "has_part": record.get("has_part"),
                    "is_part_of": record.get("is_part_of"),
                    "is_replaced_by": record.get("is_replaced_by"),
                    "replaces": record.get("replaces"),
                    "related_legislation": record.get("related_legislation"),
                },
            )

    @classmethod
    def is_expired(cls, cache_entry):
        # Check if the cache entry has expired
        return timezone.now() > cache_entry.created_at + cls.TTL

    @classmethod
    def clean_up_expired_entries(cls):
        # Delete expired cache entries
        cls.objects.filter(created_at__lt=timezone.now() - cls.TTL).delete()
