from selenium import webdriver
import time
import pymysql
import pymysql.cursors

driver = webdriver.Chrome("/Users/kimhaneul/Downloads/chromedriver")

driver.get("http://ticket.interpark.com/contents/Ranking/RankList?pType=D&pKind=01003")

time.sleep(5)


concert_num = []
concert_id = []

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

for i in range(2, 10) :
    url = "/html/body/div[7]/div[" + str(i) + "]/table/tbody/tr/td[1]/div[2]/a"
    elem = driver.find_element_by_xpath(url).get_attribute('onclick')
    concert_num.append(elem)

for j in range(0, 8) :
    id = (concert_num[j])[5:12]
    concert_id.append(id)
print(concert_id)


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



for i in range(0, 8):

    num1 = date_list[i].find('2019')
    startdate = (date_list[i])[num1:num1+10]
    start_date_list.append(startdate)

    num2 = date_list[i].rfind('2019')
    enddate = (date_list[i])[num2:num2+10]
    end_date_list.append(enddate)

print(date_list)
print(start_date_list)
print(end_date_list)

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




db = pymysql.connect(host='127.0.0.1', user='root', db='mydb', charset = 'utf8')
print("connect successfull!!!")

try:
    cursor = db.cursor()

    # for i in range(0, 1):
        # sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_dat) values (‘000’, name_list[" + str(i) + "], location_list[" + str(i) +"], ‘2019.01.01’, ‘2019.01.01’);"
    #sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_dat) values('90005', 'nneul', 'neul2', '2019.01.01', '2019.01.01');"
    for i in range(0, 8):
        sql = "insert into ranking(concert_id, concert_name, concert_place, concert_start_date, concert_end_dat) values('" + concert_id[i] + "', '" + name_list[i] +"', '"+ location_list[i] +"', '"+ start_date_list[i] + "', '" + end_date_list[i] +"');"
        cursor.execute(sql)
        db.commit()



    print(cursor.lastrowid)
finally:
    db.close()