

# Model Relationship 1

## 2) Customizing authentication in Django 

1. Substituting a custom User model

- user 모델 대체하기

- 일부 프로젝트에서는 django의 __내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음__

  - 예) username 대신 email을 식별 토큰으로 사용하는 것이 더 적합한 사이트

- Django는 User를 참조하는데 사용하는 __AUTH_USER_MODEL__ 값을 제공하여, default user model을 __재정의(override)__ 할 수 있도록 함

- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, __커스텀 유저 모델을 설정하는 것을 강력하게 권장__(highly recommended)

  - 단, __프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함__

  

2. AUTH_USER_MODEL

- User를 나타내는데 사용하는 모델

- 프로젝트가 __진행되는 동안 변경할 수 없음__

- 프로젝트 시작시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함

- 기본값 : 'auth.User' (auth 앱의 User 모델)

- 프로젝트 중간에 AUTH_USER_MODEL 변경이 가능하긴 함

  - 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요
  - 즉, 중간 변경은 권장하지 않으므로 초기에 설정하는 것을 권장

  

3. Custom user & Built-in auth forms

- get_user_model()
  - 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
    - User 모델을 커스터마이징한 상황에서는 Custom User 모델을 반환
  - 이 때문에 Django는 User 클래스를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 참조해야 한다고 강조