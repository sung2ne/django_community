# 커뮤니티

## 프로젝트 만들기

### 장고 설치

```bash
pip install django
```

### 장고 프로젝 만들기

```bash
django-admin startproject mysite
```

### 설정 바꾸기

mysite/mysite/settings.py

1. 언어
2. 시간
3. 템플릿 디렉터리 설정

### 마이그레이션

```bash
mysite> python manage.py makemigrations
mysite> python manage.py migrate
```

## 인증 앱 만들기

### 애플리케이션 만들기

```bash
mysite> django startapp common
```

### view 만들기

사용할 함수 선언
mysite/common/views.py

### url 만들기

사용할 URL 연결
mysite/common/urls.py
mysite/mysite/urls.py
