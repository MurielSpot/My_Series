#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PerpetualCalender(object):
    def __init__(self):
        pass
    
    def show_month_calender(self):
        raise NotImplementedError()
    
    def get_week(self):
        raise NotImplementedError()
    
    def get_month_day(self,year,month):
        if month==2:
            if self.is_leap_year(year):
                return 29
            else:
                return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4,6,9,11]:
            return 30
        else:
            raise ValueError
        return
    
    def is_leap_year(self,year):#判断平瑞年
        if year%4==0 and year%100!=0 or year%400==0:
            return True
        else:
            return False

class PerpetualCalenderAbs(PerpetualCalender):
    def __init__(self):
        self.abs_day_begin={"year":2000,"month":1,"day":1,"week":6}
    
    def show_year_calender(self,abs_day):
        assert abs_day>=0
        raise NotImplementedError()
    
    def show_month_calender(self,abs_day):
        year,month,day=self.get_ymd(abs_day)
        week=self.get_week(abs_day-(day-1))#得1月1号的星期,day输入是从1开始的，程序里都要减一改成0
        month_day=self.get_month_day(year,month)
        print("%d-%d-%d"%(year,month,day))
        print("一\t二\t三\t四\t五\t六\t天\n")
        for i in range(week-1):
            print("\t",end="")
        for i in range(1,month_day+1):
            if week==7:
                if day and i==day:
                    print("[%d]"%(i))#自带换行
                else:
                    print("%d"%(i))
                week=1
            else:
                if day and i==day:
                    print("[%d]\t"%(i),end="")
                else:
                    print("%d\t"%(i),end="")
                week+=1
        print("")
        return
    
    def get_week(self,abs_day):
        assert abs_day>=0
        week=(self.abs_day_begin["week"]+abs_day%7)%7
        if week==0:
            week=7
        return week
    
    def get_y(self,abs_day):
        '''获得年份'''
        assert abs_day>=0
        year=self.abs_day_begin["year"]
        while abs_day>=0:
            if self.is_leap_year(year):
                year_day=366
            else:
                year_day=365
            abs_day-=year_day# 不断减去当前年的日期，年份加1，如果为负说明年份加一前一年是实际年，如果为0，正好加一是当年，所以还要继续减当年日期来退出循环
            year+=1
        remaining_days=abs_day+year_day# 把多减的年份日期加回来，得到目标年份中的天数，0表示1月1日
        year-=1# 多减的年也加回来
        return year,remaining_days
    
    def get_ymd(self,abs_day):
        '''获得年份和月数'''
        assert abs_day>=0
        year,remaining_days=self.get_y(abs_day)
        assert remaining_days>=0
        if self.is_leap_year(year):
            month_day_list=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            month_day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
        month=1
        for pos in range(0,12):
            if remaining_days>=0:
                remaining_days-=month_day_list[pos]
                month+=1
            else:
                remaining_days+=month_day_list[pos-1]#因为剩余天数不为负，所以这里pos必定大于等于1
                month-=1
                break
        assert remaining_days>=0
        day=remaining_days+1
        return year,month,day

class PerpetualCalenderYmd(PerpetualCalender):
    def __init__(self):
        self.abs_day_begin={"year":2000,"month":1,"day":1,"week":6}#这个日期不能随便改，因为还没有代码目前还不能根据这个日期的变化，自动计算出正确的变化结果
    
    def show_month_calender(self,year,month,day=None):
        week=self.get_week(year,month,1)#得1月1日的星期
        month_day=self.get_month_day(year,month)
        if day:
            print("%d-%d-%d"%(year,month,day))
        else:
            print("%d-%d"%(year,month))
        print("一\t二\t三\t四\t五\t六\t天\n")
        for i in range(week-1):
            print("\t",end="")
        for i in range(1,month_day+1):
            if week==7:
                if day and i==day:
                    print("[%d]"%(i))#自带换行
                else:
                    print("%d"%(i))
                week=1
            else:
                if day and i==day:
                    print("[%d]\t"%(i),end="")
                else:
                    print("%d\t"%(i),end="")
                week+=1
        print("")
        return
    
    def get_abs_day(self,year,month,day):
        assert year>=self.abs_day_begin["year"]
        abs_day=0
        for y in range(self.abs_day_begin["year"],year):
            if self.is_leap_year(y):
                abs_day+=366
            else:
                abs_day+=365
        if self.is_leap_year(year):
            month_day_list=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            month_day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
        for m in range(1,month):
            abs_day+=month_day_list[m-1]
        abs_day+=(day-1)#1号应该从0开始计数
        return abs_day
    
    def get_week(self,year,month,day):
        abs_day=self.get_abs_day(year,month,day)
        assert abs_day>=0
        week=(self.abs_day_begin["week"]+abs_day%7)%7
        if week==0:
            week=7
        return week

def test_calender():
    ymd=PerpetualCalenderYmd()
    ymd.show_month_calender(int(input("year:").strip()),int(input("month:").strip()),int(input("day:").strip()))
    
if __name__ == "__main__":
    test_calender()
    pass