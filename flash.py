# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:54:33 2020

@author: mamed
"""

from flask import Flask,jsonify
#import MySQLdb 
from flask_mysqldb import MySQL



app=Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "case"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
@app.route("/list",methods=['GET'])
def liste():
    cursor = mysql.connection.cursor()
    sorgu = '''Select * From car_info'''
    cursor.execute(sorgu)
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route("/extcolor=black")
def liste2():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From car_info Where ext_color='Black'"
    cursor.execute(sorgu)
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route("/brand=BMW/extcolor=black")
def liste3():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From car_info Where ext_color='Black' and models='BMW'"
    cursor.execute(sorgu)
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route("/trans=automatic/brand=Ford/year=2018")
def liste4():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From car_info Where transmisson='Automatic' and models='Ford' and year='2018'"
    cursor.execute(sorgu)
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
if __name__=="__main__":
    app.run()
