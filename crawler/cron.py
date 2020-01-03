import json
import time

import os
from django.utils import timezone

from crawler import kin
from crawler.kincrawler import KinCrawler
from crawler.naver import Naver
from push import messaging
from push.models import Device


def crawling():
    kinCrawler = KinCrawler()
    try:
        if kinCrawler.is_driver_daed():
            kinCrawler.create_driver(os.path.dirname(os.path.abspath(__file__)) +'/chromedriver')
            print('create kincrawler')

        # 크롤링 시작
        naver = Naver('', '')
        kinCrawler.set_url('http://www.naver.com')
        # 크롤링할 카테고리 세팅
        categories = [{'name': '햇살론', 'type': 'sunshineloan'}]

        for category in categories:

            type = category['type']
            name = category['name']

            url = kin.get_latest_url(kinCrawler,naver,type)

            # 이미 크롤링한 지식인이라면 skip
            if kin.is_already_in_use(url, type):
                print('This question is already exists.')
                continue

            text = kin.get_kin_content(kinCrawler, naver, url)

            # 설정한 제외 키워드
            if kin.is_contained_bad_word(text, type):
                print('This question contains bad keyword')
                continue

            # Kin 테이블 저장
            kin.save_kin(url, text, name, type)


            # DB에서 푸시알림 보낼 기기의 토큰 가져오기
            for device in Device.objects.all():
                # Push알림 보내기
                message = messaging._build_message(type, name, text[0:100], url,
                                                   device.fcm_token)  # 메시지 길이는 최대 256바이트
                messaging._send_fcm_message(message)

    except Exception as ex:
        print(ex)
        pass

    # 예외 발생시 드라이버 종료
    finally:
        kinCrawler.finish()