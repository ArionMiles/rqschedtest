import logging

from django.core.management.base import BaseCommand, CommandError
import django_rq
from django_rq.management.commands import rqscheduler

from multisched.tasks import say_hello

scheduler = django_rq.get_scheduler()
log = logging.getLogger(__name__)


def clear_scheduled_jobs():
    # Delete any existing jobs in the scheduler when the app starts up
    for job in scheduler.get_jobs():
        log.debug("Deleting scheduled job %s", job)
        job.delete()


def register_scheduled_jobs():
    # do your scheduling here
    scheduler.cron(
        "* * * * *",    # Run every minute
        func=say_hello, # Function to be queued
        repeat=None     # Repeat this number of times (None means repeat forever)
    )


class Command(BaseCommand):
    """Simple test scheduling job"""
    def handle(self, *args, **kwargs):
        # This is necessary to prevent dupes
        clear_scheduled_jobs()
        register_scheduled_jobs()
        self.stdout.write(self.style.SUCCESS("Added a job"))
        # super(Command, self).handle(*args, **kwargs)
