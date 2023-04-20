import pymysql 
from tkinter import *
from tkinter import messagebox

def insertData():
    conn, cur = None, None
    data1, data2, data3, data4 = '', '', '', ''
    sql=""

    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db = 'soloDB', charset='utf8')