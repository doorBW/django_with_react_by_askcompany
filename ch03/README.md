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



02- 장고 모델 필드





03- 장고 admin을 통한 데이터 관리





04- 장고가 media 파일을 다루는 방법





05- 장고 쉘





06- 모델을 통한 조회 (기초)





07- Queryset을 통한 간단 검색 구현





08- Queryset의 정렬 및 범위 조건



