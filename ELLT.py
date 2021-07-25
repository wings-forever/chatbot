from selenium import webdriver
import csv
driver=webdriver.Chrome("*/chromedriver")
driver.implicitly_wait(1)

driver.get("http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=110904182&siteId=ellt&menuType=T&uId=4&sortChar=A&menuFrame=&linkUrl=4_1.html&mainFrame=right")
            #NOTICE 게시판으로 바로 가는 링크!
driver.implicitly_wait(1)

driver.find_element_by_xpath("//*text()='[졸업]'").click()