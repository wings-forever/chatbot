from selenium import webdriver
import csv
driver=webdriver.Chrome("*/chromedriver")
driver.implicitly_wait(1)

#go to the login page & login

driver.get("https://everytime.kr/login")
driver.find_element_by_name("userid").send_keys("아이디 입력")
driver.find_element_by_name("password").send_keys("비밀번호 입력")
driver.find_element_by_xpath('//*[@class="submit"]/input').click()
driver.implicitly_wait(1)

results=[]
cnt=0

while True:
    print("Page "+str(cnt))

    if cnt > 1:   #163페이지까지가 2019년도 게시글
        break
    cnt=cnt+1

    driver.get("https://everytime.kr/382452/p/"+str(cnt))
    driver.implicitly_wait(1)

    #get articles link
    posts=driver.find_elements_by_css_selector("article > a.article")
    links=[post.get_attribute("href") for post in posts]

    #get detail article
    for link in links:
        driver.get(link)

        #댓글
        comments=driver.find_elements_by_css_selector("div.comments > article.parent > p.large") #div.comments만 하면 익명,대댓글,공강,쪽지,댓글단 시간 다 나옴;;;

        for comment in comments:
            results.append(comment.text)

with open("에브리타임에타조교크롤링.csv", "w", newline="", encoding="UTF-8-sig") as f:
    writer=csv.writer(f)
    writer.writerow(results)