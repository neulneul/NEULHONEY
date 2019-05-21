from selenium import webdriver
import time
import pymysql
import pymysql.cursors

driver = webdriver.Chrome("/Users/kimhaneul/Downloads/chromedriver")

driver.get("http://ticket.interpark.com/contents/Ranking/RankList?pType=D&pKind=01003")

time.sleep(5)

#concert group id list ??????? 어케 가져오지.....
concert_num = []
concert_id = []

#concert name list
name_list = []

#concert location list
location_list = []

#concert date list
date_list = []

for i in range(2, 10) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a"
    elem = driver.find_element_by_xpath(url).get_attribute('onclick')
    concert_num.append(elem)

# list(concert_num)
print(concert_num)
#
# for j in range(0, 8) :
#     num = concert_num[j].find("\'")
#
#     id = concert_num[j]
#     concert_id[i] = id[]
#



for i in range(2, 10) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a/b"
    elem1 = driver.find_elements_by_xpath(url)
    name_list.append(elem1[0].text)

print(name_list)


for i in range(2, 10) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a"
    elem2 = driver.find_elements_by_xpath(url)
    location_list.append(elem2[0].text)


#콘서트 이름이랑 장소 자르기 -> 장소 저장
for i in range(0, 8):
    num = location_list[i].find('\n')
    location = location_list[i]
    location_list[i] = location[num+1:]

print(location_list)


for i in range(2, 10) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[2]"
    elem3 = driver.find_elements_by_xpath(url)
    date_list.append(elem3[0].text)


print(date_list)

driver.quit()

#
# sql = [
#             CREATE TABLE concert_rank (
#                     name VARCHAR(30) NOT NULL AUTO_INCREMENT,
#                     location VARCHAR(30) NOT NULL,
#                     date VARCHAR(30) NOT NULL,
#                     PRIMARY KEY(name)
#             );
#     ]
#
# cur.execute(sql)
# conn.commit()
# conn.close()


# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Rlagksmf2156*', db = 'mysql') #utf8mb4???127.0.0.1
# conn = pymysql.connect(host='127.0.0.1', user='root', db='mydb', charset = 'utf8')
# print("connect successfull!!")
#
# cursor = conn.cursor()
#
# sql = "desc ranking;"
# cursor.execute(sql)
#
# data = cursor.fetchall()
#
# for i in data:
#     print(i)
#
#
# conn.close()




# db = pymysql.connect(host='127.0.0.1', user='root', db='mydb', charset = 'utf8')
# print("connect successfull!!")
#
# try:
#     cursor = db.cursor()
#
#     # for i in range(0, 1):
#         # sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_dat) values (‘000’, name_list[" + str(i) + "], location_list[" + str(i) +"], ‘2019.01.01’, ‘2019.01.01’);"
#     sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_dat) values('12345', 'neul2', 'neul2', '2019.01.01', '2019.01.01');"
#
#     cursor.execute(sql)
#
#     db.commit()
#
#     print(cursor.lastrowid)
# finally:
#     db.close()