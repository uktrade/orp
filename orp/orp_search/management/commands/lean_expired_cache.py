from django.core.management.base import BaseCommand

from ...models import PublicGatewayCache


class Command(BaseCommand):
    help = "clean up expired cache entries"

    def handle(self, *args, **kwargs):
        PublicGatewayCache.clean_up_expired_entries()
        self.stdout.write(
            self.style.SUCCESS("successfully cleaned up expired cache entries")
        )
