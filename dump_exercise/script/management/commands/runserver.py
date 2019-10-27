import subprocess

from django.conf import settings
from django.core.management.commands import runserver


class Command(runserver.Command):
    CMD = 'python manage.py dump'

    def handle(self, *args, **options):
        process = subprocess.Popen(
            self.CMD,
            cwd=settings.BASE_DIR,
            shell=True,
            stdout=subprocess.PIPE
        )
        process.communicate()
        super().handle(*args, **options)
        print("runserver terminate")
        process.terminate()