from selenium import webdriver
import time
import pymysql
import pymysql.cursors

driver = webdriver.Chrome("/Users/kimhaneul/Downloads/chromedriver")

driver.get("http://ticket.interpark.com/contents/Ranking/RankList?pType=D&pKind=01003")

time.sleep(5)


concert_num = []
concert_id = []

#image_src_list
image_src_list = []

#concert name list
name_list = []

#concert location list
location_list = []

#concert date list
date_list = []

#concert start date list
start_date_list = []
#concert end date list
end_date_list = []

#concert_ranking_list
ranking_list = []

for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a"
    elem = driver.find_element_by_xpath(url).get_attribute('onclick')
    concert_num.append(elem)

for j in range(0, 28) :
    id = (concert_num[j])[5:12]
    concert_id.append(id)
print(concert_id)


for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a/b"
    elem1 = driver.find_elements_by_xpath(url)
    name_list.append(elem1[0].text)

print(name_list)

for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/a/img"
    elem0 = driver.find_element_by_xpath(url).get_attribute('src')
    image_src_list.append(elem0)

print(image_src_list)

for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a"
    elem2 = driver.find_elements_by_xpath(url)
    location_list.append(elem2[0].text)


#콘서트 이름이랑 장소 자르기 -> 장소 저장
for i in range(0, 28):
    num = location_list[i].find('\n')
    location = location_list[i]
    location_list[i] = location[num+1:]

print(location_list)


for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[2]"
    elem3 = driver.find_elements_by_xpath(url)
    date_list.append(elem3[0].text)



for i in range(0, 28):

    num1 = date_list[i].find('.')
    startdate = (date_list[i])[num1-4:num1+6]
    start_date_list.append(startdate)


    num2 = date_list[i].rfind('.')
    enddate = (date_list[i])[num2-7:num2+3]
    end_date_list.append(enddate)

print(start_date_list)
print(end_date_list)

#concert별 ranking
for i in range(2, 30) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[1]/i"
    elem4 = driver.find_elements_by_xpath(url)
    ranking_list.append(elem4[0].text)

print(ranking_list)

driver.quit()

#mysql 연동
db = pymysql.connect(host='127.0.0.1', user='root', passwd='Rlagksmf2156*', db='mydb', charset='utf8')
print("connect successfull!!!")

try:
    cursor = db.cursor()

    for i in range(0, 28):
        sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_date, concert_main_img, concert_ranking) values('" + concert_id[i] + "', '" + name_list[i] +"', '"+ location_list[i] +"', '"+ start_date_list[i] + "', '" + end_date_list[i] + "', '" + image_src_list[i] + "', '" + ranking_list[i] + "');"
        cursor.execute(sql)
        db.commit()

    print(cursor.lastrowid)
finally:
    db.close()