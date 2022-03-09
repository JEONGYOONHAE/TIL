#### 변수

- 객체 (object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

#### 식별자

- 알파벳, 언더스코어, 숫자로 구성
- 첫글자에 숫자가 올 수 없음
- 길이 제한이 없음
- 대/소문자 구별
- 내장함수나 모듈 등의 이름으로 만들 수 없음

```python
import keyword
print(keyword.kwlist)

>> ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 자료형 분류 (Data Type)

- Boolean Type
  - False : 0, 0.0, (), [], {}, '', None

- Numeric Type : int, float, complex

  1) int

     - long타입 없이 모두 int로 표기

     - 2진수 : 0b, 8진수 : 0o, 16진수 : 0x (box로 암기)

     - 정수 자료형에서 오버플로우가 없음

     - 임의 정밀도 산술 : 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있음

  ```python
  import sys
  max_int = sys.maxsize
  # sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
  ```

  2. float

     - 컴퓨터 지수식 표현 : 314e - 2 

     - 실수의 연산

       ```python
       abs (a - b) <= 1e - 10
       
       import sys
       abs(a - b) <= sys.float_info.epsilon
       
       import math
       math.isclose(a, b)
       ```

- String Type 

  - Immutable : 문자열을 변경 할 수 없음

  - Iterable : 문자열 순회 가능

  - String interpolation

    ```python
    name = 'eco'
    score = 4.5
    
    # %-formatting
    print('%s의 성적은 %f입니다.'%(name, score))
    
    # str.format()
    print('{}의 성적은 {}입니다.'.format(name, score))
    
    # f-string
    print(f'{name}의 성적은 {score}입니다.')
    
    # f-string 의 경우 가능
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
    ```

- None Type : 값이 없음을 표현

#### 컨테이너

- 시퀀스형 : 
  - 리스트, 튜플, 레인지, string, 바이너리
  - 순서가 있음, 특정 위치의 데이터를 가리킬 수 있음
  - 패킹 / 언패킹
    - 모든 시퀀스형(리스트, 튜플 등)은 패킹/언패킹 연산자 * 를 사용하여 객체의 패킹 또는 언패킹이 가능
    - 패킹의 경우, 리스트로 대입
- 비 시퀀스형
  - 세트
    - 순서가 없고 중복된 값이 없음
    - 집합과 동일
    - 중괄호 {} 를 통해서 만듬
    - 객체 삽입, 변경, 삭제 가능 : mutable
    - 빈 세트 만들기는 set() ({}사용 x)
  - 딕셔너리
    - {}을 통해 생성, dict()로 만들 수 있음
    - key 는 변경 불가능 : immutable

#### 형변환 

- 암시적 형변환 (Implicit Typecasting)
  - bool, numeric type
- 명시적 형변환 (Explicit Typecasting)
  - int() : string, float -> int
  - float() : string, int -> float
  - str() : int, float, list, tuple, dictionary -> str
- 컨테이너 형변환
  - range, dictionary는 서로 변환 불가함
  - dictionary의 경우 key만 가능

#### 프로그램 구성단위

- 식별자
- 리터럴
- 표현식
- 문장
  - 특정한 작업을 수행하는 코드 전체의미
  - 파이썬이 실행 가능한 최소한의 코드단위
  - 표현식은 값을 생성하는 일부분이고, 문장은 특정 작업을 수행하는 코드 전체
  - 표현식 ( 문장
- 함수
- 모듈 : 함수/클래스의 모음 or 하나의 프로그램을 구성하는 단위
- 패키지 
  - 프로그램과 모듈의 묶음
  - 프로그램 : 실행하기 위한 것
  - 모듈 : 다른 프로그램에서 불러와서 사용하기 위한 것
- 라이브러리 : 패키지의 모음