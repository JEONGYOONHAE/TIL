## Web

- world wide web : 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간

- Static web page (정적 웹페이지)

  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
  - 모든 상황에서 모든 사용자에게 동일한 정보를 표시
  - 일반적으로 HTML, CSS, JavaScript로 작성
  - flat page라고도 함

- Dynamic web page (동적 웹페이지)

  - 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
  - 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
  - 서버 사이드 프로그래밍 언어(python, java, c++ 등)가 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

- Framework

  - 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리의 모임
  - 재사용 할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움

- Web framework

  - __웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적__
  - 데이터베이스 연동, 템플릿 형태의 표준, 코드 재사용 등의 기능을 포함
  - 동적인 웹페이지나, 웹 어플리케이션, 웹 서비스 개발 보조용으로 반들어지는 application framework의 일종

- Framework Architecture

  - MVC Design Pattern (model-view-controller)
  - 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
  - 사용자가 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
  - Django는 MTV Pattern

- MTV Pattern

  - Model
    - 응용프로그램 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  - Template
    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 보여주는데 사용 (presentation)
  - View
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김

  | MVC Pattern | MTV (Django) |
  | :---------: | :----------: |
  |    Model    |    Model     |
  |    View     |   Template   |
  | Controller  |     View     |



## Django 구조

- Project 구조

  - Project는 Application의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
  - init.py : python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시

  - asgi.py (Asynchronous Server Gateway Interface) : 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

  - settings.py : 애플리케이션의 모든 설정 포함

  - urls.py : 사이트 url과 적잘한 views의 연결을 지정

  - wsgi.py (Web Server Gateway Interface) : 장고 어플리케이션이 웹 서버와 연결 및 소통하는 것을 도움

  - manage.py : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

- Application 구조

  - Application 생성 시 이름은 __복수형__으로 하는 것을 권장
  - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
  - 하나의 프로젝트는 여러 앰을 가짐
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

  - admin.py : 관리자용 페이지를 설정하는 곳
  - apps.py : 앱의 정보가 작성된 곳
  - models.py : 앱에서 사용하는 model을 정의하는 곳
  - tests.py : 프로젝트의 테스트 코드를 작성하는 곳
  - views.py : view 함수들이 정의되는 곳

- 앱 등록
  - 프로젝트에서 앱을 사용하기 위해서는 __반드시__ INSTALLED_APPS 리스트에 추가해야 함
  - INSTALLED_APPS : 장고 installaion에 활성화 된 모든 앱을 지정하는 문자열 목록
  - __반드시 생성 후 등록!!__
  - INSTALLED_APPS 에 먼저 작성하고 생성하려면 앱이 생성되지 않음
  - local apps -> third party apps -> django apps 순서를 지키지는 않아도 문제는 없지만, 지키는 것을 권장



## 요청과 응답

- URLs : HTTP요청을 알맞은 view로 전달

  ```PYTHON
  from django.urls import path
  from django.contrib import admin
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
  ]
  ```

- View : HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성

  - Model을 통해 요청에 맞는 필요 데이터에 접근
  - Template에게 HTTP 응답 서식을 맡김

  ``` python
  from django.shortcuts import render
  
  def index(request):
      retrun render(request, 'index.html')
  ```

- Templates : 실제 내용을 보여주는데 사용되는 파일

  - 파일의 구조나 레이아웃을 정리 (ex HTML)
  - Template 파일 경로의 기본값은 __app 폴더 안의 templates 폴더__로 지정되어 있음

- LANGUAGE_CODE : 모든 사용자에게 제공되는 번역을 결정

  - 이 설정이 적옹되려면 USE_I18N이 활성화되어 있어야 함

- TIME_ZONE : 데이터베이스 연결의 시간대를 나타내는 문자열 지정

  - USE_TZ가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, 
    UTC 대신 새로 설정한 시간대의 인식 날짜 & 시간이 반환 됨
  - USE_TZ가 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의

- USE_I18N : 장고의 번역 시스템 활성화 여부 지정
- USE_L10N : 데이터의 지역화 된 형식을 기본적으로 활성화할지 여부 지정
  - True일 경우, 장고는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시
- USE_TZ : datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
  - True일 경우, 장고는 내부적으로 시간대 인식 날짜 / 시간을 사용



## Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

- DTL (Django Template Languate) : built-in template system

  - 조건, 반복, 변수, 치환, 필터 등의 기능을 제공
  - 단순히 python이 HTML에 포함 된 것이 아니며, 프로그래밍 로직이 아니라 __프레젠테이션을 표현하기 위한 것__
  - python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만, 이것이 해당 python 코드로 실행되는 것이 아님

  1. Variable

     - render()을 사용해서 view.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
     - 변수명은 영어, 숫자, 밑줄의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
     - 공백이나 구두점 문자 또한 사용할 수 없음
     - dot(.)를 사용해서 변수 속성에 접근할 수 있음
     - render()의 세번째 인자로 {'key' : value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

  2. Filter

     - 표시할 변수를 수정할 때 사용
     - 60개의 built-in template filters를 제공
     - chained가 가능하며 일부 필터는 인자를 받기도 함

  3. Tag

     - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
     - 일부 태그는 시작과 종료 태그가 필요
     - 약 24개 built-in template tags를 제공

  4. Comment

     - 라인의 주석을 표현하기 위해 사용
     - 한줄 주석에만 사용할 수 있음 (줄 바꿈이 허용되지 않음)
     - 여러 줄 주석은 {% comment %}{% endcomment %} 사이에 입력

  5. 코드 작성 순서

     - urls -> views -> templates

  6.  Template inheritance (템플릿 상속)

     - 템플렛 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

     - 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의 (override) 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음

     - extends : 반드시 최상단에 작성되어야 함 (자식 템플릿이 부모 템플릿을 확장한다는 것을 알림)

     - block :  overridden 할 수 있는 블록을 정의

     - app_name/templates 디렉토리 외 템플릿 추가 경로 설정 : 

       ``` PYTHON
       'DIRS' : [BASE_DIR] / 'tempaltes',
       ```

     - include : 템플릿을 로드하고 현재 페이지로 렌더링

  7. Django template system (Django 설계철학)

     - 표현과 로직(view)을 분리
       - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다. 
       - 즉 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야한다.
     - 중복을 배제



## HTML Form

1. form

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 핵심속성(attribute)
  - action : 입력 데이터가 전송될 URL 지정
  - method : 입력 데이터 전달 방식 지정

2. input

- 사용자로부터 데이터를 입력받기 위해 사용
- type 속성에 따라 동작 방식이 달라짐
- name 
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터로 매핑하는 것
  - GET 방식에서는 URL에서 __?key=value&key=value__ 형식으로 데이터를 전달함
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음

3. label

- 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄
- label을 input 요소와 연결
  - input에 id속성 부여
  - label에는 input의 id와 동일한 값의 for 속성이 필요
  - 시각적인 기능뿐만 아니라 화면 리더기에 label을 읽어 사용자가 입력해야하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점도 있음
  - label을 클릭해서 input에 초점을 맞추거나 활성화 시킬 수 있음

4. for

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어

5. id

- 전체 문성에서 고유해야 하는 식별자를 정의
- 목적 : linking, scripting, styling시 요소를 식별

6. HTTP (HyperText Tranfer Protocol)

- 웹에서 이루어지는 모든 데이터 교환의 기초

- 주어진 리소스가 수행 할 작업을 나타내는 request methods를 정의

- GET, POST, PUT, DELETE, ...

- GET : 서버로부터 __정보__를 __조회__하는데 사용
  - 데이터를 가져올 때만 사용해야 함
  - 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송
  - 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데, 이때 사용하는 요청의 방식이 GET
  
  

## URL Variable Routing

- 웹 애플리케이션은 url을 통한 클라이언트의 요청에서부터 시작됨
- url 주소를 변수로 사용하는 것
- url의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path에 여러 페이지를 연결 시킬 수 있음

![urls](https://user-images.githubusercontent.com/94509971/159160810-d635ad24-4806-481c-b728-10671711d132.PNG)



1. URL Path converters

- str : /을 제외하고 비어 있지 않은 모든 문자열과 매치, 기본값
- int : 0 / 양의 정수와 매치
- slug : ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치

2. include()

- 다른 URLonf(app1/urls.py)들을 참조할 수 있도록 도움
- __django는 명시적 상대경로(from .module import ..)를 권장__ 

3. Naming URL patterns

- path()함수의 name인자를 정의해서 사용
- url 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음