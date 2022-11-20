import time
import sys
import os
import calendar
import datetime

class time_module():
    
    def months(yy, mm):
        calendar_months = calendar.month(yy,mm)
        return calendar_months
    
    def now():
        dt = datetime.datetime.now()
        now_time ="""{0}年{1}月{2}日{3}時{4}分{5}秒""" .format(str(dt.year),str(dt.month),str(dt.day),str(dt.hour),str(dt.minute),str(dt.second))
        return now_time    
        
    def years(yy):
        pass
        
        
        
        