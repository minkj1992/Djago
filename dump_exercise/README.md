# 기본적인 CRUD 웹사이트에 자동 backup 기능 추가

> [참고자료](https://lhy.kr/django-auto-backup-db)


- `./script`: 자동 backup script
- `./blog`: crud 게시판 app
- `./dump_exercise`: base root project


1. `python manage.py startapp script`를 통하여 script app 생성

2. `script`app이 항상 실행되도록 등록해준다.

- `./dump_exercise/settings.py`
```python
INSTALLED_APPS = [
    'script',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

3. `dump.py` 생성
 
`dump.py`를 통하여 `python manage.py dump`를 실행할때 `dump`기능을 수행할 코드를 만들어준다.

- `./script/management/commands/dump.py`
```python
import subprocess
from django.conf import settings
from django.core.management import BaseCommand

class Command(BaseCommand):
    CMD = 'python manage.py dumpdata ' \
          # dump 대상이 되는 app 이름
          'blog ' \
          '--indent=4 > ' \
          # dump file을 저장시킬 dir (base_dir에 dump라는 폴더를 생성하였다.)
          './dump/db.json'

    def handle(self, *args, **options):
        process = subprocess.Popen(
            self.CMD,
            cwd=settings.BASE_DIR,
            shell=True,
            stdout=subprocess.PIPE
        )
        process.communicate()
```

4. `runserver.py` 생성

- `python manage.py runserver`를 실행시킬 때마다, 실행될 script
- 실행시 `python manage.py dump`라는 cmd를 자동으로 실행되도록 만들었다.


- `./script/management/commands/runserver.py`
```python
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
        process.terminate()
```

기본적으로 script는 `subprocess`를 통해서 실행이되며, 새로운 process를 생성하고 pipe를 통해서 communicate 시킨다.

**궁금한점은 process terminate이 어떻게 진행되는지 궁금하다. 찍어보면 runserver terminate가 2번 print되는데, dump terminate이 아닌 runserver가 2번 찍히는게 의문이긴 하다.**

runserver가 종료되는 시점에 subprocess들이 종료가 된다.