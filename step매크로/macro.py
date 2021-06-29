# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import  WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import ui
#
# url1 = "https://kb.step.or.kr/main.do"
# # pip install selenium
# # 구글드라이버 다운, 경로설정
# driver = webdriver.Chrome("C:/Users/KB/Desktop/chromedriver")
#
# driver.get(url1)
# # 로그인 후 강의 들어가서 학습하기 버튼이 있는 창에서 아무키나 입력
# input('멈춤')
# link = driver.find_element_by_class_name('btn_learning')
# link.click()
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(5)
#
#
# check = False
# check1 = False
# #  시작 누르기 ( 버튼값이 파이썬,자바,자바스크립트 같은 경우만 가능)
# while not check:
#     try:
#         time.sleep(5)
#         temp = driver.find_element_by_xpath("//iframe[@id='HkmcMainFrame']")
#
#         if temp:
#             time.sleep(5)
#             driver.switch_to.frame(temp)
#             time.sleep(5)
#             link3 = driver.find_element_by_id("pause")
#             time.sleep(3)
#             link3.click()
#             link4 = driver.find_element_by_id("play")
#             time.sleep(3)
#             link4.click()
#             check = True
#             print('found')
#     except:
#         print('Not found')
#
# while True:
#     try:
#         time.sleep(5)
#         driver.switch_to.default_content()
#         time.sleep(5)
#         temp = driver.find_element_by_xpath("//iframe[@id='HkmcMainFrame']")
#         time.sleep(5)
#         if temp:
#             driver.switch_to.frame(temp)
#             time.sleep(5)
#             test1 = driver.find_element_by_xpath("//div[@id='handleBar']")
#             time.sleep(5)
#
#             if test1:
#                 while True:
#                     try:
#                         time.sleep(10)
#
#                         print(test1.get_attribute("style"))
#                         time.sleep(5)
#                         a = test1.get_attribute("style")
#                         print(a)
#                         time.sleep(5)
#                         print('--------')
#                         if test1.get_attribute("style") == "width: 1000px;":
#                             break
#                         if a == test1.get_attribute("style"):
#                             time.sleep(5)
#                             driver.switch_to.default_content()
#                             print('1')
#                             time.sleep(5)
#                             temp1 = driver.find_element_by_xpath("//iframe[@id='HkmcMainFrame']")
#                             time.sleep(6)
#                             print('2')
#                             driver.switch_to.frame(temp1)
#                             print('3')
#                             link41 = driver.find_element_by_id("play")
#                             time.sleep(6)
#                             link41.click()
#                             print('4')
#                             time.sleep(0.5)
#                             link41.click()
#                             time.sleep(0.5)
#                             link41.click()
#                             time.sleep(0.5)
#                             link41.click()
#                             time.sleep(0.5)
#                             link41.click()
#
#                     except:
#                         print('Not found1')
#         driver.switch_to.default_content()
#         time.sleep(5)
#         check1 = False
#         while not check1:
#             try:
#                 link2 = driver.find_element_by_class_name('icon_next_arrow')
#                 if link2:
#                     link2.click()
#                     check1 = True
#             except:
#                 print('Not found1')
#     except:
#         continue

import time
# html용 매크로
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium import webdriver
print("이거 메인 아니다")
check = False
driver = webdriver.Chrome(executable_path="C:/Users/KB/Desktop/chromedriver")

# 나의 학습하기까지 일단 가야함
url1 = "https://kb.step.or.kr/main.do"

driver.get(url1)

input('시작하기')
link = driver.find_element_by_class_name('btn_learning')
link.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

startBtn = False
while True:
    check = False
    check1 = False
    while not check:
        try:
            print('페이지 이동 완료')
            time.sleep(5)
            temp = driver.find_element_by_xpath("//iframe[@id='HkmcMainFrame']")
            if temp:
                driver.switch_to.frame(temp)
                time.sleep(5)
                link3 = driver.find_element_by_xpath("//div[@class ='left']/button")
                time.sleep(5)
                if startBtn == False:
                    link3.click()
                    startBtn=True
                time.sleep(5)
                test1 = driver.find_element_by_xpath("//div[@class='timeLineWrap']/div/div")
                if test1:
                    while True:
                        try:
                            time.sleep(3)
                            print(test1.get_attribute("style"))
                            if test1.get_attribute("style") == "width: 100%;":
                                break
                        except:
                            print('Not found1')

                driver.switch_to.default_content()
                time.sleep(10)
                check = True
                print('found')
        except:
            print('Not found')
        while True:
            try:
                print('다음 버튼 찾는중')
                time.sleep(5)
                link2 = driver.find_element_by_class_name('icon_next_arrow')
                if link2:
                    link2.click()
                    break
            except:
                print('Not found1')

