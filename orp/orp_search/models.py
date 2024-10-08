import json

from datetime import timedelta

from orp_search.public_gateway import SearchDocumentConfig

from django.db import models
from django.utils import timezone


class PublicGatewayCache(models.Model):
    search_terms = models.CharField(max_length=255)
    document_types = models.JSONField()
    response = models.TextField()
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
            cache_entry = cls.objects.get(
                search_terms=key[0], document_types=key[1]
            )
            if cls.is_expired(cache_entry):
                # If expired, delete it and return None
                cache_entry.delete()
                return None
            return cache_entry.response
        except cls.DoesNotExist:
            return None

    @classmethod
    def cache_response(cls, config, response):
        # Store the response in the cache
        key = cls._config_to_key(config)
        cache_entry, created = cls.objects.update_or_create(
            search_terms=key[0],
            document_types=key[1],
            defaults={"response": response, "created_at": timezone.now()},
        )
        return cache_entry

    @classmethod
    def is_expired(cls, cache_entry):
        # Check if the cache entry has expired
        return timezone.now() > cache_entry.created_at + cls.TTL

    @classmethod
    def clean_up_expired_entries(cls):
        # Delete expired cache entries
        cls.objects.filter(created_at__lt=timezone.now() - cls.TTL).delete()
