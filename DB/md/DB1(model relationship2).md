# Model relationship 2

## 1) User - Article (1 : N)

1. User 모델 참조

- setting.AUTH_USER_MODEL
  - User 모델에 대한 외래 키 또는 다대다 관계를 정의할 때 사용
  - models.py에서 User 모델을 참조할 때 사용
- get_user_model()
  - 현재 활성화(active)된 User 모델을 반환
    - 커스터마이징한 User 모델이 있는 경우는 Custom User모델, 그렇지 않으면 User를 반환
    - User를 직접 참조하지 않는 이유
  - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용