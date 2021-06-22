import requests
from bs4 import BeautifulSoup

pagecontent = requests.get("http://www.dowellcomputer.com/main.jsp")
pagecontent = pagecontent.text.strip()

# HTML 소스코드를 파이썬 BeatifulSoup 객체로 변환합니다.
soup = BeautifulSoup(pagecontent, 'html.parser')

# ==============================================================
# # <a> 태그를 포함하는 요소를 추출합니다.
# links = soup.select('td > a')
#
# # 모든 링크에 하나씩 접근합니다.
# for link in links:
#   # 링크가 href 속성을 가지고 있다면
#   if link.has_attr('href'):
#     # href 속성의 값으로 notice라는 문자가 포함되어 있다면
#     if link.get('href').find('notice') != -1:
#       print(link.text)
# ===============================================================
# <td> 태그를 포함하는 요소를 추출합니다.
tds = soup.select('td')

# 모든 링크에 하나씩 접근합니다.
for td in tds:
  # 링크가 class 속성을 가지고 있다면
    if td.has_attr('class'):
    # class 속성의 값으로 middle라는 문자가 포함되어 있다면
        if td.get('class').find('middle') != -1:
            print(td.text)