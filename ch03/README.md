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





05- 장고 쉘





06- 모델을 통한 조회 (기초)





07- Queryset을 통한 간단 검색 구현





08- Queryset의 정렬 및 범위 조건



