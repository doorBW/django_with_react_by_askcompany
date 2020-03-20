# ch03) 장고 Models
**01- 장고 모델(ORM) 소개**

* 애플리케이션의 다양한 데이터 저장 방법

데이터베이스: RDBMS, NoSQL 등

파일: 로컬, 외부 정적 스토리지

캐시서버: memcached, redis 등



* 데이터베이스와 SQL

데이터베이스의 종류: RDBMS(관계형 데이터베이스 관리 시스템), NoSQL

데이터베이스에 쿼리하기 위한 언어 -> SQL

직접 SQL을 만들어내기도 하지만, ORM(Object-relational mapping)을 통해 SQL을 생성/실행하기도 한다.

하지만, ORM을 쓰더라도 내가 작성된 ORM코드를 통해 어떤 SQL이 실행되고 있는지, 파악을 하고 이를 최적화할 수 있어야 한다. -> 이를 위해 django-debug-toolbar를 적극 활용한다.



장고 ORM인 모델은 RDB만을 지원한다.



* 장고의 강점은 Model과 Form

SQL을 직접 실행할 수도 있지만, 가능하면 ORM을 사용

직접 SQL문자열 조합 말고 인자로 처리 -> SQL Injection 방지



장고 쉘 실행 명령어

python manage.py shell



* Django Model

**데이터베이스 테이블과 파이썬 클래스를 1:1로 매핑**

모델 클래스 명은 단수형으로 지정

클래스이기에 필히 첫 글자가 대문자인 PascalCase 네이밍

매핑되는 모델 클래스는 DB테이블 필드 내역이 일치해야 한다.



DB테이블명: 디폴트 "앱이름_모델명"

커스텀으로 하고자 한다면, Meta 클래스의 db_table속성



**02- 장고 모델 필드**

Primary Key: AutoField, BigAutoField

문자열: CharField, TextField, SlugField

날짜/시간: DateField, TimeField, DateTimeField, DurationField

참/거짓: BooleanField, NullBooleanField

숫자: IntegerField, SmallIntegerField, PositiveIntegerField, PositiveSmallIntegerField, BigIntegerField, DecimalField, FloatField

파일: BinaryField, FileField, ImageField, FilePathField

이메일: EmailField

URL: URLField

UUID: UUIDField

아이피: GenericIPAddressField

Relationship Types: ForeignKey, ManyToManyField, OneToOneField

그리고 다양한 커스텀 필드들,,



* 자주 쓰는 필드 공통 옵션

**blank**: 장고 단에서 validation시에 empty 허용 여부 (디폴트: False)

null (DB옵션): null 허용 여부 (디폴트:Flase)

db_index (DB옵션): 인덱스 필드 여부 (디폴트:Flase)

default: 디폴트 값 지정, 혹은 값을 리턴해줄 함수 지정

unique(DB 옵션): 현재 테이블 내에서 유일성 여부 (디폴트:Flase)

choices: select 박스 소스로 사용

**validators**: validators를 수행할 함수를 다수 지정

verbose_name: 필드 레이블, 미지정시 필드명이 사용

help_text: 필드 입력 도움말



**03- 장고 admin을 통한 데이터 관리**

django.contrib.admin 앱을 통해 django admin 제공

프로젝트(최상단) urls.py를 가면 admin주소가 할당되어있음

django-admin-honeypot 앱을 통해 가짜 admin 노출 가능



모델 클래스 등록을 통해서, 조회/추가/수정/삭제 웹UI를 제공

서비스 초기에 관리도구로서 사용하기에 제격!



java의 toString

django에서는 -> \_\_str\_\_ 이용

![image-20200313210446965](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200313210446965.png)



list_display 속성

![image-20200313210642083](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200313210642083.png)



search_fields 속성 정의 - admin내 검색UI를 통해, DB를 통한 where 쿼리 대상 필드 리스트



list_filter 속성 정의 - 지정 필드값으로 필터링 옵션 제공



**04- 장고가 media 파일을 다루는 방법**

**Static & Media 파일**

* static 파일

개발 리소스로서의 정적인 파일(js, css, image 등)

앱/프로젝트 단위로 저장/서빙

* Media 파일

FileField/ImageField를 통해 저장한 모든 파일

DB필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장

프로젝트 단위로 저장/서빙



\# pillow 라이브러리 설치

pip install pillow



ImageField 내부적으로 pillow를 사용하기 때문에 설치가 필요함



requirements.txt -> 설치한 라이브러리를 적어서 관리할 수 있음

=> pip install -r requirements.txt



* Media 파일 처리 순서

1. HttpRequest.FILES를 통해 파일이 전달

2. 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행한다.
3. FileField/ImageField 필드에 "경로(문자열)"를 저장하고.
4. settings.MEDIA_ROOT 경로에 파일을 저장합니다.



* Media 파일, 관련 settings 예시

각 설정의 디폴트 값

MEDIA_URL = "" => 각 media 파일에 대한 URL Prefix, 필드명.url 속성에 의해서 참조되는 설정

MEDIA_ROOT = "" => 파일필드를 통한 저장 시에, 실제 파일을 저장할 ROOT 경로



* 기본 세팅

![image-20200314211913416](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200314211913416.png)



* FileField와 ImageField

**FileField**

Fiel Storage API를 통해 파일을 저장

장고에서는 File System Storage만 지원. Django-storages를 통해 확장 지원.

해당 필드를 옵션 필드로 두고자 할 경우, blank=True 옵션 적용

**ImageField**(FileField 상속)

Pillow(이미지 처리 라이브러리)를 통해 이미지 width/height 획득

Pillow 미설치 시에, ImageField를 추가한 makemigrations 수행에 실패합니다.

**위 필드를 상속받은 커스텀 필드를 만들 수도 있다.** ex) PDFField, ExcelField 등



media_url -> 파일 접근

media_root -> 파일 저장



* 사용할 만한 필드 옵션

**blank 옵션**

업로드 옵션처리 여부, 디폴트: Flase

**upload_to옵션**

settings.MEDIA_ROOT 하위에서 저장한 파일명/경로명 결정

디폴트: 파일명 그대로 settings.MEDIA_ROOT에 저장

추천) 성능을 위해, 한 디렉토리에 너무 많은 파일들이 저장되지 않도록 조정하기

동일 파일명으로 저장 시에, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지



* 파일 업로드 시에 HTML Form enctype

![image-20200314213433494](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200314213433494.png)

-> 추후 form 쪽에서 다시 설명



* upload_to 인자

파일 저장 시에 upload_to 함수를 호출하여, 저장 경로를 계산

![image-20200314213630719](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200314213630719.png)



**05- 장고 쉘**

* python Interactive Shell

기본 파이썬 쉘

IPython: https://ipython.org

Jupyter Notebook with Python Kernel

BPython: https://bpython-interpreter.org



**06- 모델을 통한 조회 (기초)**

* Model Manage

데이터베이스 질의 인터페이스를 제공

디폴트 Manager로서 modelCls.objects 가 제공

ModelCls.objects.all() \# 생성되는 대강의 SQL 윤곽: SELECT * FROM app_model;

ModelCls.object.all().order_by('-id')[:10] # SELECT * FROM app_model ORDER BY id DESC LIMIT 10;

ModelCls.objects.create(title='New Title') # INSERT INTO app_model (title) VALUES ("New Title")



-> jupyter notebook을 통해 확인(루트폴더에 jupyter_practice라고 저장함)



* QuerySet은 Chaining을 지원

QuerySet은 Lazy한 특성. -> QuerySet을 만드는 동안에는 DB접근을 하지 않고, 실제로 데이터가 필요한 시점에 접근을 한다.

* 데이터가 필요한 시점은?

1. queryset
2. print(queryset)
3. list(queryset)
4. for instance in queryset: print(instance)



* 다양한 조회 요청 방법

**조건을 추가한 Queryset, 획득할 준비**

queryset.filter(...) 

queryset.exclude(...)

**특정 모델 객체 1개 획득을 시도**

queryset[숫자인덱스] -> 모델 객체 혹은 예외 발생(IndexError)

queryset.get(...) -> 모델 객체 혹은 예외발생(DoesNotExist, MultipleObjectsReturned)

queryset.first() -> 모델객체 혹은 None

queryset.last() -> 모델객체 혹은 None



* filter <-> exclude

인자로 "필드명 = 조건값" 지정

1개 이상의 인자 지정 -> 모두 AND 조건으로 묶임

OR조건을 묶으려면, django.db.models.Q 활용

![image-20200314225546785](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200314225546785.png)





**07- Queryset을 통한 간단 검색 구현**

실습) Item 목록/간단검색페이지



**08- Queryset의 정렬 및 범위 조건**

* 정렬 조건 추가

정렬 조건을 추가하지 않으면 일관된 순서 보장받을 수 없음.

정렬 조건을 지정하는 2가지 방법

1. (추천) 모델 클래스의 Meta 속성으로 ordering 설정 : list로 설정
2. 모든 queryset에 order_by(...) 에 지정



1 ->

![image-20200318130923824](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200318130923824.png)

위와 같이 model에 Meta 클래스를 통해 ordering을 지정해주니,

![image-20200318130945512](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200318130945512.png)

이렇게 기본 조회 쿼리에 order by가 적용된 것을 볼 수 있다.

하지만 아래와 같이 order_by를 직접 추가하면

![image-20200318131041044](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200318131041044.png)

디폴트 정렬이 무시된다



* 슬라이싱을 통한 범위조건 추가

str/list/tuple에서의 슬라이싱과 거의 유사하지만, 음수 인덱싱 접근은 지원 안함

객체[start:stop:step]

step이 없을 때 위 코드의 반환값은 queryset이지만,

step이 들어가는 순간 반환값은 list다



**09- django-debug-toolbar를 통한 SQL 디버깅**

* django-debug-toolbar (third party)

현재 req/res에 대한 다양한 디버깅 정보를 보여줌.

SQLPanel을 통해 각 요청 처리시에 발생한 SQL 내역 확인가능

비동기(ajax) 요청에 대한 지원 불가



공식 문서: https://django-debug-toolbar.readthedocs.io/en/latest/

pip install django-debug-toolbar

pip 설치후 settings와 프로젝트 urls 설정



세팅이 정상적으로 끝나면 웹 화면상 우측에 툴바가 생김.

![image-20200318144352984](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200318144352984.png)

해당 패널들 중에 아래와 같이 SQL 쿼리등을 볼 수 있음.

![image-20200318144412497](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200318144412497.png)



* 그외: django-querycount

SQL 실행내역을 개발서버 콘솔에 표준 출력.

ajax내역도 출력 가능



**10- 관계를 표현하는 모델 필드(ForeignKey)**

ORM은 어디까지나 SQL 생성을 도와주는 라이브러리.

* 1:N 관계 => models.ForeignKey
* 1:1 관계 => models.OneToOneField
* M:N 관계 => models.ManyToManyField



**ForeignKey**

ex) Post:Comment, User:Post, User:Comment

ForeignKey(to, on_delete)

to: 대상 모델

-> 클래스를 직접 지정하거나, 클래스명을 문자열로 지정. 자기 참조는 self 지정

on_delete: Record 삭제 시 Rule

-> CASCADE: FK로 참조하는 다른 모델의 Record도 삭제

PROTECT: ProtectedError (IntegrityError 상속)를 발생시키며 삭제 방지

SET_NULL: null로 대체. 필드에 null=True 옵션필수

SET_DEFAULT: 디폴트 값으로 대체. 필드에 디폴트값 지정 필수

SET:대체할 값이나 함수 지정. 함수의 경우 호출하여 리턴값을 사용

DO_NOTHING: 어떠한 액션도 안한다. DB에 따라 오류가 발생할 수도 있다.



* FK에서의 reverse_name

reverse 접근 시의 속성명: 디폴트 -> "모델명소문자_set"

ex)

![image-20200319112100146](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200319112100146.png)



**reverse_name 이름 충돌이 발생하면?**

-> reverse_name은 app이름 고려x, 모델명만 고려하기 때문에 충돌날 수 있음

이름이 충돌이 날 때, makemigrations 명령이 실패

-> 1. 어느 한쪽의 FK에 대해, reverse_name을 포기: related_name='+'

2. 어느 한쪽의 (혹은 모두) FK의 reverse_name을 변경

ex)

FK(User, ..., related_name='blog_post_set')

FK(User, ..., related_name='shop_post_set')



* ForeignKey.limit_choices_to 옵션

Form을 통한 Choice 위젯에서 선택항목 제한 가능

ManyToManyField 에서도 지원



**11- 관계를 표현하는 모델 필드(OneToOneField)**

* OneToOneField(to, on_delete)

1:1 관계에서 어느쪽이라도 가능

ForeignKey(unique=True)와 유사하지만, reverse 차이

User:Profile 을 FK로 지정한다면 -> profile.user_set.first() -> user

User:Profile 을 O2O로 지정한다면 -> profile.user -> user



**12- 관계를 표현하는 모델 필드(ManyToManyField)**

ManyToManyField(to, blank=False)

M:N 관계에서 어느쪽이라도 필드 지정 가능



DB Browser for SQLite 사용



RDBMS지만, DB에 따라 NoSQL기능도 지원



**13- 마이그레이션을 통한 데이터베이스 스키마 관리(1)**

* Migrations

모델의 변경내역을 "데이터베이스 스키마"로 반영시키는 효율적인 방법을 제공

마이그레이션 파일 생성

python manage.py makemigrations <앱이름>

저장 데이터베이스에 마이그레이션 적용

python manage.py migrate <앱이름>

마이그레이션 적용 현황 출력

python manage.py showmigrations <앱이름>

저장 마이그레이션의 SQL 내역 출력

python manage.py sqlmigrate <앱이름> <마이그레이션-이름>



* Migration 파일

데이터베이스에 어떤 변화를 가하는 Operation들을 나열

**주의) 같은 Migration 파일이라 할지라도, DB종류에 따라 다른 SQL이 생성됨.**



![image-20200320200156579](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320200156579.png)



* 언제 makemigrations를 하는가?

모델 필드 관련된 어떠한 변경이라도 발생 시에 마이그레이션 파일 생성을 한다.

실제로 DB Scheme에 가해지는 변화가 없더라도 수행.

-> 마이그레이션 파일은 모델의 변경내역을 누적하는 역할!

적용된 마이그레이션 파일은 절대 삭제하면 안된다.

마이그레이션 파일이 많아지면 squashmigrations 명령으로 다수의 마이그레이션 파일을 통합할 수 있다.



python manage.py migrate <앱이름>

미적용 <마이그레이션-파일>부터 <최근-마이그레이션-파일>까지 정방향으로 순차적으로 수행

python manage.py migrate <앱이름> <마이그레이션-이름>

지정된 <마이그레이션-이름>이 현재 적용된 마이그레이션보다

**이후라면,** 정방향으로 순차적으로 지정 마이그레이션까지 정방향 수행

**이전이라면,** 역방향으로 순차적으로 지정된 마이그레이션까지 역방향 수행



![image-20200320200746659](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320200746659.png)



**14- 마이그레이션을 통한 데이터베이스 스키마 관리(2)**

* 새로운 필드가 필수필드라면?

makemigrations 명령을 수행할 때, 기존 record들에 어떤 값을 채워넣을 지 묻는다.

(새로운 필드가 null=True, blank=True도 아니고, default값도 없을 때)

선택1) 지금 그 값을 입력하겠다.

선택2) 명령 수행을 중단

![image-20200320202029336](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320202029336.png)



* 협업 Tip

**절대 하지 말아야할 일**

팀원 각자가 마이그레이션 파일을 생성 -> 충돌 발생

**추천) 마이그레이션 파일 생성은 1명이 전담해서 생성**

생성한 마이그레이션 파일을 버전관리에 넣고, 다른 팀원들은 이를 받아서 migrate만 수행

