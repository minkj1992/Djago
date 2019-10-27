import subprocess
from django.conf import settings
from django.core.management import BaseCommand

class Command(BaseCommand):
    CMD = 'python manage.py dumpdata ' \
          'blog ' \
          '--indent=4 > ' \
          './dump/db.json'

    def handle(self, *args, **options):
        process = subprocess.Popen(
            self.CMD,
            cwd=settings.BASE_DIR,
            shell=True,
            stdout=subprocess.PIPE
        )
        process.communicate()
        print("dump terminate !!!!!!!!!!!!")
        process.terminate()