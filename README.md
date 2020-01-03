# kin-crawler-python
django-crontab과 Firebase Cloud Messaging 을 이용한 네이버 지식인 크롤링 및 푸시 발송 프로그램입니다.

## 사용 기술 스펙
- python3.6, python-django
- django_crontab, rest_framework, selenium, mecab 
- ubuntu18.04

## 서비스 소개
- 네이버 지식인 특정 카테고리에 올라오는 최신 질문을 크롤링
- 앱으로 크롤링한 네이버 질문 푸시알림 전송

## 주요 클래스 소개
- crawler/kincrawler.py: WebDriver를 조작하는 클래스, 자원낭비 방지를 위해 싱글톤으로 구현
- crawler/kin.py: 생성한 WebDriver를 이용하여 최신 질문 체크, 제외키워드 포함 체크 등 크롤링 여부를 판단 
- crawler/cron.py: WebDriver 생성, 네이버 지식인 화면 접근, DB저장, 푸시전송 등 크론탭을 이용해 일정시간마다 실행되는 로직
- crawler/naver.py: 크롤링에 필요한 Element의 Xpath 명시
- crawler/models.py: 지식인 정보 모델, 제외키워드 모델 정의
- push/messaging.py: FCM accessToken 생성, 푸시 메시지 세팅
- push/models.py: 기기토큰 모델 정의

