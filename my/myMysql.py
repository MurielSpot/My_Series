#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
数据库常用命令：
    查看数据库的编码格式：show create database <数据库名>;
    查看数据表的编码格式：show create table <表名>;
    创建数据库时指定数据库的字符集：create database <数据库名> character set utf8;
    创建数据表时指定数据表的编码格式：
        create table tb_books (
        name varchar(45) not null,
        price double not null,
        bookCount int not null,
        author varchar(45) not null ) default charset = utf8;
    插入多行数据：
        INSERT INTO table() VALUES (),(),();
    添加列：
        alter table 表名 add column 列名 varchar(30) not null;
    删除列：
        alter table 表名 drop column 列名;
    添加列，并设置为自增加的主键：
        alter table 表名 add column 列名 bigint not null auto_increment primary key first;
    更新数据：
        update 表名 set 列名=2,列名=200 where 主键名=2;
    修改数据库的编码格式：alter database <数据库名> character set utf8;
    修改数据表格编码格式：alter table <表名> character set utf8;
    修改字段编码格式：alter table <表名> change <字段名> <字段名> <类型> character set utf8;
                    alter table user change username username varchar(20) character set utf8 not null;
    添加外键：alter table tb_product add constraint fk_1 foreign key(factoryid) references tb_factory(factoryid);
            alter table <表名> add constraint <外键名> foreign key<字段名> REFERENCES <外表表名><字段名>;
    删除外键：alter table tb_people drop foreign key fk_1;
            alter table <表名> drop foreign key <外键名>;
'''

import pymysql

config={
    "host":"192.168.10.198",
    "port":3306,
    "user":"",
    "password":"",
    #"database":"tsq",
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