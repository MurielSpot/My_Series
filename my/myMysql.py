#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

config={
    "host":"192.168.10.198",
    "port":3306,
    "user":"",
    "password":"",
    "database":"tsq",
    #"charset":"utf-8"
}
config["user"]=input("输入用户名").strip()
config["password"]=input("输入密码").strip()

def interactive_execute(**config):
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql=input("输入sql,如果为空则结束：").strip()
    while sql:
        try:
            conn.begin()# 开启事务
            cursor.execute(sql)
            print(cursor.fetchall())
            conn.commit()# 提交事务
        except Exception as e:
            conn.rollback()# 若有异常就回滚
            print(type(e),e)
            
        sql=input("输入sql,如果为空则结束：").strip()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    interactive_execute(**config)
    pass