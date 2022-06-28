## Vue 목록

- [SPA](#SPA)
- [CSR](#CSR)
- [SSR](#SSR)
- [MVVM](#MVVM)
- [Basic syntax](#Basic)
- [Props](#Props)
- [Emit](#Emit)
- [Router](#Router)
- 



## SPA (Single Page Application : 단일 페이지 어플)

​	: 현재 페이지를 __동적__으로 렌더링함으로써 사용자와 소통하는 웹 어플

1. __단일 페이지__로 구성되며 서버로부터 __최초에만 페이지를 다운__로드 하고, 이후에는 동적으로 DOM 구성
   - 처음 페이지를 받은 이후부터는 서버로부터 새로운 전체 페이지를 불러오는 것이 아닌, 현재 페이지 중 __필요한 부분만__ 동적으로 다시 작성
2. 연속되는 페이지 간의 __사용자 경험(UX) 향상__
   - 모바일 사용량이 증가하고 있는 현재 트래픽 감소와 속도, 사용성, 반응성의 향상은 매우 중요
3. 동작 원리의 일부가 __CSR__구조를 따름



## CSR (Client Side Rendering)

​	: 최초 요청시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는__필요한 데이터만 요청해 JS로 DOM을 렌더링__하는 방식

1. 클라이언트에서 화면을 구성
2. 처음엔 뼈대만 받고 브라우저에서 동적으로 DOM을 그림
3. SPA가 사용하는 렌더링 방식
4. 장점
   - 서버와 클라이언트 간 트래픽 감소
     - 필요한 모든 정적 리소스를 최초에 한 번 다운로드 후 필요한 데이터만 갱신
   - 사용자 경험(UX) 향상
     - 전체 페이지를 다시 렌더링 하지 않고 변경되는 부분만을 갱신하기 때문
5. 단점
   - SSR에 비해 전체 페이지 최종 렌더링 시점이 느림
   - SEO(검색 엔진 최적화)에 어려움이 있음 



## SSR (Server Side Rendering)

​	: 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식

1. 장점
   - 초기 구동 속도가 빠름
     - 클라이언트가 빠르게 컨텐츠를 볼 수 있음
   - SEO에 적합
     - DOM에 이미 모든 데이터가 작성되어있기 때문
2. 단점
   - 모든 요청마다 새로운 페이지를 구성하여 전달
     - 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐
     - 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음



## SSR VS CSR

1. 두 방식의 차이는 최종 HTML 생성 주체가 누구인가에 따라 결정
2. 실제 브라우저에 그려질(렌더링) HTML을 서버가 만들면 SSR / 클라이언트가 만들면 CSR
3. 단순 비교하여 어떤 것이 더 좋다가 아니라 적절하게 선택하는 것이 중요



## MVVM Pattern

1. Model
   - __Model__은 JS Object
   - Object === { key : value }
   - Model은 Vue Instance 내부에서 __data__로 존재
   - data가 바뀌면 View(DOM)가 반응
2. View
   - __View__는 DOM(__HTML__)
   - Data의 변화에 따라 바뀌는 대상
3. ViewModel
   - __ViewModel__은 모든 __Vue Instance__
   - View와 Model 사이에서 data와 DOM에 관련된 모든 일을 처리
   - ViewModel을 활용해 data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민



## Basic syntax of Vue

1. Vue Instance ( === Vue Component)

   - 여러 options들을 사용하여 원하는 동작 구현

   - vue 인스턴스를 생성할 때는 __options__ 객체를 전달해야 함

     | options  |                                                              |
     | :------: | ------------------------------------------------------------ |
     |    el    | vue 인스턴스에 연결(마운트)할 기존 DOM 요소가 필요<br/>new를 이용한 인스턴스 생성 때만 사용 |
     |   data   | vue 인스턴스의 데이터 객체, 상태 데이터를 정의하는 곳<br/> vue 객체 내 다른 함수에서 __this__ 키워드를 통해 접근 가능<br/>v-bind, v-on 과 같은 directive에서도 사용 가능 |
     |  method  | vue 인스턴스에 추가할 메서드 <br />directive에서도 사용 가능                  <br />객체 내 다른 함수에서 __this__ 키워드를 통해 접근 가능                  <br />__화살표 함수를 메서드 정의하는데 사용 불가__                  <br />(화살표 함수가 부모 컨텍스트를 바인딩 하기 때문에, this 는 vue 인스턴스가 아님) |
     | computed | 데이터를 기반으로 하는 계산된 속성<br />함수의 형태로 정의하지만 함수가 아닌 __함수의 반환 값이 바인딩 됨__<br />__종속된 데이터가 변경될 때만 함수를 실행__<br />반드시 반환값이 있어야 함 |
     |  watch   | 데이터에 변화가 일어났을 때 실행되는 함수                    |
     |  filter  | interpolation / v-bind를 이용할 때 사용 가능<br />`|` 사용   |

   - computed & methods

     - 최종 결과에 대해 두 가지 접근 방식은 서로 동일
     - computed는 종속 대상을 따라 저장(캐싱)
     - 즉, computed는 종속된 대상이 변경되지 않는 한 computed에 작성된 함수를 여러번 호출해도 계산을 다시 하지 않고 계산되어 있던 결과를 반환
     - methods를 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행

   - computed & watch (사용하는 목적과 상황이 다름)

     - computed (__계산해야 하는 목표 데이터를 정의__)
       - 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
       - 속성은 계산해야 하는 목표 데이터를 정의하는 방식 (선언형 프로그래밍 방식)
       - 특정 값이 변동하면 해당 값을 다시 계산해서 보여줌
     - watch (__데이터가 바뀌면 특정 함수를 실행__)
       - 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
       - 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하는 방식 (명령형 프로그래밍 방식)
       - 특정 값이 변동하면 다른 작업을 함
       - 특정 대상이 변경되었을 때 콜백 함수를 실행시키기 위한 트리거

2. Directive (디렉티브)

   - v- 접두사가 있는 특수 속성

   | directive |                                                              |
   | --------- | ------------------------------------------------------------ |
   | v-text    | 내부적으로 interpolation 문법이 v-text로 컴파일 됨           |
   | v-html    | innerHTML 을 업데이트<br />임의로 사용자로부터 입력 받은 내용은 v-html에 __절대 사용 금지__ |
   | v-show    | 요소는 항상 렌더링 되고 DOM에 남아있음<br />단순히 엘리먼트에 display CSS 속성을 토글하는 것 |
   | v-if      | 표현식이 true일 때만 렌더링                                  |
   | v-for     | __반드시 key 속성을 각 요소에 작성__<br />v-if와 함께 사용하는 경우 __v-for가 우선순위 더 높음__ (동시에 사용하지 말것) |
   | v-on      | 엘리먼트에 이벤트 리스너를 연결                              |
   | v-bind    | HTML 요소의 속성에 Vue 상태 데이터를 값으로 할당<br />Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당 |
   | v-model   | HTML form 요소의 값과 data를 양방향 바인딩                   |

   - v-show vs v-if

   | v-show                                                       | v-if                                                         |
   | :----------------------------------------------------------- | ------------------------------------------------------------ |
   | CSS display 속성을 hidden으로 만들어 토글                    | 전달인자가 false인 경우 렌더링 되지 않음                     |
   | 실제로 렌더링은 되지만 눈에서 보이지 않는 것이기 때문에 딱 한번만 렌더링이 되는 경우라면 v-if에 비해 상대적으로 렌더링 비용이 높음 | 화면에서 보이지 않을 뿐만 아니라 렌더링 자체가 되지 않기 때문에 렌더링 비용이 낮음 |
   | 자주 변경되는 요소라면 한 번 렌더링 된 이후부터는 보여주는지에 대한 여부만 판단하면 되기 때문에 토글 비용이 적음 | 자주 변경되는 요소의 경우 다시 렌더링 해야 하므로 비용이 증가할 수 있음 |




## Props

1. 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

2. 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언 해야함

3. 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음

4. Static Props

   ```vue
   // App.vue
   <about my-message = "message"></about>
   
   // About.vue
   <template>
   <h2>{{ myMessage }}</h2>
   
   <script>
   props : {
   	myMessage: String
   }
   ```

5. Dynamic Props

   ```vue
   // App.vue
   <about :parent-data="parentData">
   
   <script>
   export default {
       data : function() {
           return {
   			parentData : 'this is parent data'
   			}
   		}
       }
   </script>
       
   // About.vue
   <template>
   <h2>{{ parentData }}</h2>
   
   <script>
   props : {
   	parentData: String
   }
   ```

6. 이름 컨벤션

   - 선언 시 : __camelCase__
   - HTML : __kebab-case__

7. 컴포넌트의 __data는 반드시 함수여야 함__

8. Static 구문을 사용하여 숫자를 전달하면 안됨 (문자열로 전달 됨)
   v-bind를 사용해야 숫자로 전달 됨

   ```
   <comp some-prop="1"></comp> 문자열 "1"
   <comp :some-prop="1"></comp> 숫자 1
   ```

9. 모든 props는 하위 속성과 상위 속성 사이의 __단방향__ 바인딩을 형성

10. 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안됨



## Emit (Listening to Child Components Events)

1. $emit(eventName)
   - 현재 인스턴스에서 이벤트를 트리거
   - 추가 인자는 리스너의 콜백 함수로 전달
2. 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 __v-on__을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취 
3. 이름 컨벤션
   - 이벤트는 자동 대소문자 변환을 제공하지 않음
   - v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 __항상 kebab-case를 사용하는 것을 권장__



## Router

1. 위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치

2. `router-link`

   - 목표 경로는 'to' prop으로 지정
   - HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 함
   - a 태그지만 GET 요청을 보내는 이벤트를 제거한 형태로 구성됨

3. `router-view`

   - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
   - router-link를 클릭하면, 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치

4. History mode

   - 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
   - 페이지를 다시 로드하지 않고 URL을 탐색할 수 있음 -> SPA의 단점 중 하나인 URL이 변경되지 않는 점을 해결
   - history 객체는 사용자를 자신의 방문 기록 앞과 뒤로 보내거나, 기록의 특정 지점으로 이동하는 등 유용한 메서드와 속성을 가짐

5. 프로그래밍 방식 네비게이션

   - `router-link to ="..." === $router.push(...)`
   - vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음

   ```vue
   // home으로 이동
   methods :{
   	moveToHome : function () {
   		this.$router.push({ name : 'home' })
   }
   }
   ```

6. 동적 인자 전달

   - `this.$route.params`

7. Components $ Views

   - App.vue
     - 최상위 컴포넌트
   - views/
     - router(index.js)에 매핑되는 컴포넌트를 모아두는 폴더
     - ex) App 컴포넌트 내부에 AboutView & HomeView 컴포넌트 등록
   - components/
     - router에 매핑된 컴포넌트 내부에 작성하는 컴포넌트를 모아두는 폴더
     - ex) Home 컴포넌트 내부에 HelloWorld 컴포넌트 등록







