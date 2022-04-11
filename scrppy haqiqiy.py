
#***************************************************************
from os import waitpid
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
from dateutil import parser as dtparser
import mysql.connector
from mysql.connector import Error
import pymysql


url = "https://sports.uz/oz/news/boxs"

base_url = "https://sports.uz"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

container = soup.select_one("table.table.table-striped")

products = container.find_all("td", {"class":"article-big h-feed"})

urls = []
for product in products:
    url = product.select_one("a")["href"]
    urls.append(base_url +url.replace("../", ""))
args = []
for url in urls:
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("title").text
    detail = soup.select_one("div.page-content")
    body = detail.find("div", {"class":"post-text"}).text
    add_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # view = soup.select_one("div.view").text
    view = 159
    category = 3
    img_codes = soup.select_one("div.post-image")
    img_links = img_codes.select_one("a")["href"]
    # def save_img(img_links):
    #     filename = img_links.split('/')[-1]
    #     print(filename)
    #     r = requests.get(img_links, allow_redirects=True)
    #     open(('uploads/img/')+filename,"wb").write(r.content)
    # save_img(img_links)
    file = img_links.split('/')[-1]
    file_url = file.replace(file, f"/img/"+file)
    args.append([title, file_url, body, add_time, category, view])
    


#     ######---------------- MYSQL CONNECT---------#####
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='djangodb2',
#                                          user='user',
#                                          password='4926666j')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#     with connection.cursor() as cursor:
#         insert_query = """INSERT INTO news_news 
#               (title, image_image, detail, category_id, post_viewcount) 
#               VALUES (%s, %s, %s, %s, %s)"""
#         # insert_query = "INSERT INTO `news_news` VALUES (title, image_image, detail, post_viewcount, category_id)"
#         cursor.executemany(insert_query, args)
#         connection.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# finally:
#     if connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")
        
    ###### ------SQLITE CONNECNT-------------###
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
insert_query = 'INSERT INTO news_news (title, image_image, detail, add_time, category_id, post_viewcount) VALUES(?, ?, ?, ?, ?, ?)'
# cursor.execute("SELECT title FROM news_news")
# if cursor.fetchone() is None:
cursor.executemany(insert_query, args)
conn.commit()
print("Successfuly!")
# else:
    # print("такая запись уже имеется!")
# conn.commit()
conn.close()
# insert_query = """INSERT INTO news_news 
#                 (title, image_image, detail, category_id, post_viewcount) 
#                 VALUES (%s, %s, %s, %s, %s)"""
# cursor.executemany(insert_query, args)
# conn.commit()

# conn.close()  
#cursor.executemany("INSERT INTO `news_news` VALUES (title, image_image, detail, post_viewcount, category_id)", args)