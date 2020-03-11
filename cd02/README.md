# ch02) 장고
**01-파이썬 설치(윈도우)**

파이썬 설치

아나콘다 설치

conda create --name askcompany python=3.7

conda activate askcompany

django~=3.0.0 설치



**02-Visual Studio Code 설치**

vscode 설치

python extensions 설치



**03-장고 프로젝트 생성**

아래 명령어로 django 프로젝트 생성

django-admin startproject 프로젝트이름



프로젝트이름으로 폴더명이 만들어진다.

**내부 파일 안내**

manage.py: 명령행을 통해 각종 장고 명령 수행

askcompany 폴도: 프로젝트명으로 생성된 디렉토리, 최상위 폴더와는 다르게 이 이름을 참조하고 있는 코드가 있기 때문에 함부로 수정하면 안된다.

_ _ init _ _.py

settings.py

urls.py: 최상위 urls.py

wsgi.py: 실서비스에서의 웹서비스 진입점



이후 실행한 명령어

python manage.py migrate

python manage.py createcuperuser

python manage.py runserver



**04-장고 주요 구성요소**





**05-장고앱과 블로그 코딩쇼**



