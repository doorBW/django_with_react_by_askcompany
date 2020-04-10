# ch08) 비SPA방식으로 장고 Forms/Views를 적극 활용한 인스타그램 St 만들기
**01- Overview**   

* 이번 챕터에서 만들어볼 내용

-> 새로운 프로젝트를 만들어 볼 것!   

회원가입/로그인/프로필 수정 및 암호 수정/포스팅 쓰기 구현/유저 페이지 구현/타임라인   

SPA: Single Page Application -> HTML/CSS/JavaScript의 비중이 커진다.   

   

**02- 프로젝트 생성 및 초기 프로젝트 환경 설정**   

새로운 가상환경세팅   

conda create --name=django-with-react-rev2 python=3.8   

   

장고 환경 구성에 있어서, requirements와 settings를 개발/운영으로 나누어 만들어 두었음.   

이때 settings 변경에 따라 manage.py, asgi.py, wsgi.py 세가지 파일에서 기존의 settings.py 보는 경로를 수정해주어야함.   

   

**03- Bootstrap4를 활용한 기본 레이아웃 구현**   

bootstrap4를 다운받아서 프로젝트 폴더 static에 넣어줌.    

-> bootstrap4를 이용하여 기본 레이아웃(layout.html) 구현.   

   

04- 커스텀 유지 저징 및 회원가입 구현   

05- 회원 가입 환영 이메일 보내기   

06- SendGrid API Key  획득하고 환경변수에 저장하기   

07- 로그인-로그아웃 구현 그리고 회원 가입과 동시에 로그인   

08- django-pydenticon을 활용하여 프로필 디폴트 이미지 구현   

