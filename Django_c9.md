# c9에 django 2.0이상 버전과 mysql 데이터 베이스 설정해주기
- 1. `Make a new workspace using the “Blank” template`
- 2. `sudo apt-get update`
- 3. `sudo apt-get install python3.6`

# 가상환경 만들기
- 3. `sudo pip3 install virtualenv`
- 4. `virtualenv --python=python3.6 venv`

# mysql setting하기
- 5. `sudo apt-get install python3.6-dev libmysqlclient-dev` (venv 키지 않은 상태여야 한다.)
- 6. `source venv/bin/activate`
- 7. `sudo pip3 install mysqlclient`

# `/settings.py`
- 8. `settings.py`에서 `DATABASES`를 주석처리 해주고 아래 구문으로 대체한다.
```
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'c9',
    'USER': 'root',
    'PASSWORD': '',
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  }
}
```

- 9. `settings.py`의 `ALLOWED_HOSTS`를 `ALLOWED_HOSTS = ['프로젝트이름-메인유저ID.c9users.io']`로 대체해준다.
(ex `ALLOWED_HOSTS = ['ajouactivity-minkj1992.c9users.io']`)

- 10. 서버 켜주기 : `mysql-ctl start`



# 에러처리( migrations 문제 )
> django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table ((1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(6) NOT NULL)' at line 1"))

mysql 버전과 django 버전 호환성 문제로 뜨는 에러인데 

`settings.py` 맨위에 
```
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5
```
를 넣어주면 해결

- 11. 이후 `python manage.py makemigrations`
- 12. `python manage.py migrate`

- 13. 마지막으로 터미널에 `python manage.py runserver $IP:$PORT`켜주면 된다.(c9 RUN 버튼으로 서버 키면 안된다.)
