from django_celery_beat.models import CrontabSchedule, PeriodicTask

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Setup periodic task for rebuilding cache"

    def handle(self, *args, **kwargs):
        # Create or get the crontab schedule
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute="0", hour="1"
        )
        # Create the periodic task
        task, created = PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name="Rebuild Cache Daily",
            task="fbr.cache.tasks.rebuild_cache",
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS("Periodic task created successfully.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Periodic task already exists.")
            )
