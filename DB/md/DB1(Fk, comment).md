# Model Relationship 1

## 1) Foreign key

1. 개념

- 외래 키 (외부 키)
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 데이블에서 속성(필드)에 해당하고, 이는 참조되는 테이블의 기본 키(pk)를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응됨
  - 이 때문에 참조하는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조 할 수 없음
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음



2. 특징

- 키를 사용하여 부모테이블의 유일한 값을 참조 (__참조 무결성__)

- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

  - 참조 무결성

    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
    - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

    

3. ForeignKey field

- A many - to - one relationship
- 2개의 위치 인자가 __반드시__ 필요
  - 참조하는 model class
  - on_delete 옵션
- migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만듦

- 데이터 무결성 [참고]
  - 데이터의 __정확성과 일관성을 유지__하고 보증하는 것을 가리키며, 데이터베이스나 RDBMS 시스템의 중요한 기능
  - 무결성 제한의 유형
    - 개체 무결성 (Entity integrity)
      - pk의 개념과 관련
      - 모든 테이블이 pk를 가져야 하며 pk로 선택된 열은 고유한 값이어야 하고 빈 값은 허용치 않음을 규정
    - 참조 무결성 (Referential integrity)
      - fk의 개념과 관련
      - fk 값이 데이터베이스의 특정 테이블의 pk 값을 참조
    - 범위(도메인) 무결성 (Domain integrity)
      - 정의된 형식(범위)에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정
- 데이터 베이스의 foreignkey 표현
  - 만약 인스턴스를 abcd로 생성 했다면, abcd_id로 만들어짐
  - 하지만 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 바람직함 (1 : N)



4.  1 : N 관계 related manager

- 역참조 ('comment_set')

  - Article(1) -> Comment(N)
  - article.comment 형태로는 사용할 수 없고, article.__comment_set__ manager가 생성됨
  - 게시글에 몇 개의 댓글이 작성 되었는지 Django ORM이 보장할 수 없기 때문
    - article은 comment가 있을 수도 있고, 없을 수도 있음
    - __실제로 Article 클래스에는 Comment 와의 어떠한 관계도 작성되어 있지 않음__

- 참조 ('article')

  - Comment(N) -> Article(1)
  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로, comment.article과 같이 접근할 수 있음
  - 실제 Foreignkey 또한 Comment 클래스에서 작성됨

  

5. on delete : 외래 키가 __참조하는 객체가 사라졌을 때__ 외래 키를 가진 객체를 __어떻게 처리할 지를__ 정의

- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정

- 옵션 값들

  - CASCADE : 부모 객체(참조 __된__ 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  - PROTECT
  - SET_NULL
  - SET_DEFAULT
  - SET()
  - DO_NOTHING
  - RESTRICT

  

6. related_name : 역참조 시 사용할 이름 ('model_set' manager)을 변경할 수 있는 옵션

``` python 
related_name='commnts'
```

- 위와 같이 변경하면 article.comment_set은 더이상 사용할 수 없고, article.comments로 대체됨
- __역참조 시 사용할 이름 수정 후, migration 과정 필요__



7. save()

- save(commit=False)

  - Create, but don't save the new instance
  - 아직 __데이터베이스에 저장되지 않은 인스턴스를 반환__
  - 저장하기 전에 __객체에 대한 사용자 지정 처리를 수행할 때__ 유용하게 사용

  