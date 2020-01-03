import time
from urllib.parse import urlparse, parse_qs

# 로그인용 클래스와 지식인 질문 크롤링용 객체를 따로 만들고
# 항상 드라이버 초기화와 quit는 크론탭으로 일괄 진행
from konlpy.tag import Mecab
from crawler.models import BadWord, Kin


def is_already_in_use(url, type):
    try:
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        kin = Kin.objects.filter(d1id= query.get('d1id')[0] , dir_id= query.get('dirId')[0], doc_id= query.get('docId')[0], type=type)
    except Exception as ex:
        print(ex)
        return False
    if kin.count() == 0:
        return False
    else:
        return True

def is_contained_bad_word(text, type):
    # BadWord 테이블에 type 조건으로 키워드 전체 조회
    # konlpy 라이브러리로 체크
    mecab = Mecab()
    mecab_list = mecab.nouns(text)
    # DB에서 제외키워드 조회
    badword_list = BadWord.objects.filter(type=type).values_list('keyword', flat=True)

    for badword in badword_list:
        for mecabword in mecab_list:
            badword_en = badword.encode('utf-8')
            mecabword_en = mecabword.encode('utf-8')
            if badword_en == mecabword_en:
                return True
    # if any (word in BadWord.objects.all().__str__() for word in mecab.nouns(text)):
    #     return True
    return False

def save_kin(url, content, keyword, type):
    # save KI
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    kin = Kin(keyword=keyword,d1id=query.get('d1id')[0],dir_id=query.get('dirId')[0],doc_id=query.get('docId')[0],url=url,content=content,use_yn='N',type=type)
    kin.save()

def get_latest_url(driver,naver,type):
    if type == 'sunshineloan':
        url = 'https://kin.naver.com/qna/list.nhn?dirId=40105'
    elif type == 'move':
        url = 'https://kin.naver.com/qna/list.nhn?dirId=810'
    elif type == 'revival':
        url = 'https://kin.naver.com/qna/list.nhn?dirId=40106'
    else:
        raise Exception('타입이 선정되지 않았습니다.')
    # 키워드 검색
    driver.set_url(url)
    # 최신 질문 url 리턴
    return driver.get_element(naver.get_list_xpath_in_kin_question()).get_attribute('href')

def get_latest_url_about_loan_category(driver, naver):
    loan_url = 'https://kin.naver.com/qna/list.nhn?dirId=40105'

def get_kin_content(driver, naver, url):
    # 최신 질문으로 화면 이동
    driver.check_alert_and_go(url)

    # 타이틀만 있는 질문인지 확인
    if driver.check_exists_by_xpath(naver.get_content_xpath_in_kin_question()):
        title = driver.get_element(naver.get_title_xpath_in_kin_question()).text
        content = driver.get_element(naver.get_content_xpath_in_kin_question()).text
        return title + content
    else:
        return driver.get_element(naver.get_title_xpath_in_kin_question()).text
