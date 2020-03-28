# ch06) 장고 Forms
**01- HTML Form.**   

* 언제 쓰나?

HTML Form(클라이언트 측).   

클라이언트에서 사용자에게 입력폼을 제공하고, **이를 서버로 전송하고자 할 때.**   

Django Form(서버 측).   

**클라이언트로부터 전달받은 값들에 대한 유효성 검사를 수행하고, 이를 데이터베이스에 저장하는 등의 처리.**   

HTML Form을 생성하는 기능 제공, 이를 활용하거나 인터페이스만 맞춰서 직접 HTML Form을 코딩해도 됨.   

   

* HTML Form.   

\<form>\</form>태그를 통해 입력폼을 구성한다.   

submit 시에 지정된 action URL로 데이터 전송을 시도한다.   

* HTML \<form> 태그 필수 속성.   

Action: 요청을 보낼 주소.   

Method: 전송 방식.   

​	GET: 주로 데이터 조회 요청 시에 사용, POST: 파괴적인 액션(생성/수정/삭제)에서 사용.   

Enctype: 인코딩 방식.   

​	POST에서만 유효, GET요청에서는 하나의 enctype으로 강제됨.   

   

* 장고 뷰에서의 인자 접근.   

request.GET (GET, POST 모두 사용가능)   

request.POST (POST 에서만 사용 가능)   

request.FILES (POST 에서만 사용 가능)   

   

02- HttpRequest와 HttpResponse

   

03- Form

   

04- Cross Site Request Forgery

   

