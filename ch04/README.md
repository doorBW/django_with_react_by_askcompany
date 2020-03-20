# ch04) 장고 Views
**01- 다양한 응답의 함수 기반 뷰(1)**

* View

1개의 HTTP 요청에 대해 1개의 뷰가 호출 됨

urls.py/urlpatterns 리스트에 매핑된 호출 가능한 객체

웹 클라이언트로부터 HTTP 요청을 처리



크게 2가지 형태의 뷰

함수 기반 뷰 (Function Based View): 장고 뷰의 기본

-> 호출 가능한 객체, 그 자체

클래스 기반뷰(Class Based View)

-> 클래스.as_view() 를 통해 호출가능한 객체를 생성/리턴



**View 호출 시, 인자**

HttpRequest 객체 및 URL Captured Values

1번째 인자: HttpRequest 객체

-> 현재 요청에 대한 모든 내역을 담고 있다.

2번째~ 인자: 현재 요청의 URL로부터 Capture된 문자열들

url/re_path를 통한 처리에서는 -> 모든 인자는 str 타입으로 전달

path를 통한 처리에서는 -> 매핑된 Converter의 to_python에 맞게 변환된 값이 인자로 전달



**View 호출에 대한 리턴 값**

- 필히 HttpResponse 객체를 리턴해야 한다.

장고 Middleware에서는 뷰에서 HttpResponse 객체를 리턴하기를 기대함 -> 다른 타입을 리턴하면 Middleware에서 처리 오류

django.shortcut.render 함수는 템플릿 응답을 위한 shortcut함수

- 파일 like 객체 혹은 str/bytes 타입의 응답 지원

str 문자열을 직접 utf8로 인코딩할 필요가 없다.

장고 디폴트 설정에서 str 문자열을 utf8로 인코딩해준다.



![image-20200320213656153](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320213656153.png)



**02- 다양한 응답의 함수 기반 뷰(2)**

- 다양한 타입의 HttpResponse

**Excel 파일 다운로드 응답**

파일객체를 그대로 전달하면 된다.

![image-20200320222153564](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320222153564.png)



**pandas를 통한 CSV 응답 생성**

![image-20200320222301414](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320222301414.png)



**pandas를 통한 엑셀 응답 생성**

![image-20200320222504292](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320222504292.png)



**pillow를 통한 이미지 응답 생성 - 기본**

![image-20200320222620557](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320222620557.png)



**pillow를 통한 이미지 응답 생성 - View**

![image-20200320222819403](C:\Users\beomwoo\AppData\Roaming\Typora\typora-user-images\image-20200320222819403.png)







03- URL Dispatcher와 정규 표현식



04- 클래스 기반 뷰 시작하기



05- 장고 기본 CBV API (Base Views)



06- 장고 기본 CBV API (Generic display views) (1)



07- 장고 기본 CBV API (Generic display views) (2)



08- 장고 기본 CBV API (Generic display views) (3)



09- 뷰 장식자