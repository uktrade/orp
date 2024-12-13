from django.core.management import BaseCommand

from app.cache.manage_cache import rebuild_cache


class Command(BaseCommand):
    help = "Rebuilds the cache"

    def handle(self, *args, **options):
        rebuild_cache()
