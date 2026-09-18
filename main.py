```python
import streamlit as st
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


# ---------------------------------------------------------
# 기본 설정
# ---------------------------------------------------------

st.set_page_config(
    page_title="어제의 박스오피스",
    page_icon="🎬",
    layout="wide",
)

# KOBIS 일일 박스오피스 API 주소
API_URL = (
    "https://www.kobis.or.kr/"
    "kobisopenapi/webservice/rest/boxoffice/"
    "searchDailyBoxOfficeList.json"
)

# 한국 시간대
KST = ZoneInfo("Asia/Seoul")


# ---------------------------------------------------------
# 한국 시간 기준으로 '어제' 날짜 계산
# ---------------------------------------------------------

def get_yesterday():
    """서버의 시간대와 관계없이 한국 시간 기준 어제를 반환합니다."""
    now_kst = datetime.now(KST)
    yesterday = now_kst.date() - timedelta(days=1)

    # KOBIS API가 요구하는 yyyymmdd 형식
    return yesterday.strftime("%Y%m%d")


# ---------------------------------------------------------
# KOBIS API 호출
# ---------------------------------------------------------

@st.cache_data(ttl=3600)
def fetch_boxoffice(target_date):
    """
    지정한 날짜의 박스오피스 데이터를 가져옵니다.

    cache_data의 ttl=3600:
    같은 날짜를 다시 조회하면 약 1시간 동안
    API를 다시 호출하지 않습니다.
    """

    # Streamlit Cloud의 Secrets에서 인증키를 읽습니다.
```
