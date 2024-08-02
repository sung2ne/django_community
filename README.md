# 커뮤니티

## 설계서

### 기능정의서

https://docs.google.com/spreadsheets/d/1xMwlDxmaywGRRVoxxf2bHff16j4UEdqjC89XH39eRCY/edit?usp=sharing

### 업무흐름도

https://drive.google.com/file/d/1dSEk7DJ0WyJhBFN6cKgHb4YXRaXPa89S/view?usp=sharing

### 테이블 정의서

https://docs.google.com/spreadsheets/d/1Om3nOSNgWOYZ4eDkAw1gfjCWwQCUZWJOhsFzYw6YHfw/edit?usp=sharing

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

### templates 폴더 만들기

mysite/templates

### 마이그레이션

```bash
mysite> python manage.py makemigrations
mysite> python manage.py migrate
```

## 인증 앱 만들기

### 애플리케이션 만들기

```bash
mysite> python manage.py startapp common
```

### view 만들기

사용할 함수 선언
mysite/common/views.py

### url 만들기

사용할 URL 연결
mysite/common/urls.py
mysite/mysite/urls.py

### 템플릿 만들기

mysite/templates/base.html
mysite/templates/common/main.html
mysite/templates/common/login.html
mysite/templates/common/profile.html
mysite/templates/common/register.html
mysite/templates/common/find_username.html
mysite/templates/common/reset_password.html

### 메인 화면 만들기

mysite/templates/common/main.html

### 로그인 만들기

mysite/tempates/common/login.html
mysite/common/forms.py
mysite/common/views.py

### 로그아웃 만들기

mysite/common/views.py

### 회원가입 만들기

mysite/tempates/common/register.html
mysite/common/forms.py
mysite/common/views.py

### 아이디 찾기 만들기

mysite/tempates/common/find_username.html
mysite/common/forms.py
mysite/common/views.py

### 비밀번호 초기화 만들기

mysite/tempates/common/reset_password.html
mysite/common/forms.py
mysite/common/views.py

## 프로필 만들기

mysite/tempates/common/profile.html
mysite/common/forms.py
mysite/common/views.py

