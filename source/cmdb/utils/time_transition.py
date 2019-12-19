import calendar
import time
import datetime


class TimeFunc(object):
    @classmethod
    def get_date_split(cls, choose_datetime):
        t_year = choose_datetime.year
        t_month = choose_datetime.month
        t_day = choose_datetime.day
        t_week = int(choose_datetime.strftime('%W'))
        return t_year, t_month, t_day, t_week

    @classmethod
    def get_date(cls, choose_datetime):
        return choose_datetime.strftime('%Y%m%d')

    @classmethod
    def get_time(cls, choose_datetime):
        return choose_datetime.strftime('%H:%M:%S')

    # 将时间类型换为时间字符串
    @classmethod
    def time_to_str(cls, time_obj, _type="all"):
        if _type == "all":
            _format = "%Y-%m-%d %H:%M:%S"
        elif _type == "date":
            _format = "%Y-%m-%d"
        elif _type == "hour":
            _format = "%H:%M"
        elif _type == "month":
            _format = "%m-%d"
        elif _type == "year":
            _format = "%Y-%m"
        elif _type == "year_only":
            _format = "%Y"
        elif _type == "full":
            _format = "%Y%m%d%H%M"
        elif _type =="no_year":
            _format = "%m-%d %H:%M:%S"
        elif _type =="time":
            _format = "%H:%M:%S"
        else:
            _format = "%Y-%m-%d %H:%M"
        try:
            time_res = time_obj.strftime(_format)
        except:
            time_res = ""
        return time_res

    # 根据参数时间所在周的开始时间
    def getweekfirstday(self, current_date):
        yearnum = current_date.year
        weeknum = int(current_date.strftime("%W"))
        daynum = int(current_date.weekday()) + 1

        yearstart = datetime.datetime(yearnum, 1, 1)
        yearstartweekday = int(yearstart.weekday())+1
        if yearstartweekday < int (daynum):
            daydelat = (7-int(yearstartweekday))+(int(weeknum))*7
        else:
            daydelat = (7-int(yearstartweekday))+(int(weeknum)-1)*7
        a = yearstart+datetime.timedelta(days=daydelat+1)
        return a

    # 获取当天的开始时间
    @classmethod
    def get_day_start_time(cls):
        now_time = datetime.datetime.now()
        start_time = datetime.datetime(now_time.year,now_time.month,now_time.day)
        return start_time

    # 获取XX天的日期
    @classmethod
    def get_date_list(cls,date_range=7,date_type="day"):
        date_now=datetime.datetime.now()
        date_list = []
        current_month_first_day = 0
        for i in range(date_range):
            if date_type == "day":
                date = date_now-datetime.timedelta(days=i)
                date = date.date()
            else:
                date = cls.get_date_month(date_now,i)
            date_list.append(date)
        date_list.reverse()
        return date_list

    # 获取XX月的月份
    @classmethod
    def get_date_month(cls,date,range_num):
        year = date.year
        month = date.month
        if month - range_num<= 0:
            res_month = 12+(month - range_num)
            res_year = year-1
        else:
            res_month = month-range_num
            res_year = year
        date = "%d-%d"%(res_year,res_month)
        return date

    # 获取xx天的日期
    @classmethod
    def get_assign_date(cls,days=0):
        now_date = datetime.datetime.now()
        assign_date = datetime.datetime(now_date.year,now_date.month,now_date.day)-datetime.timedelta(days=days)
        return assign_date

    # 拼接时间字符串
    @classmethod
    def splice_time(cls,year,month,day,time):
        time = "{year}-{month}-{day} {time}".format(year=year,month=month,day=day,time=cls.time_to_str(time,"time"))
        return time

    # 获取今天的date类型
    @classmethod
    def get_today_date(cls):
        return datetime.date.today()

    # 获取今天的datetime类型
    @classmethod
    def get_today_datetime(cls):
        return datetime.datetime.combine(datetime.datetime.now(), datetime.time.min)

    # 获取两个日期之间的周数差，计算方式为 date2 - date1
    @staticmethod
    def week_difference(date1, date2):
        monday1 = (date1 - datetime.timedelta(date1.weekday()))
        monday2 = (date2 - datetime.timedelta(date2.weekday()))
        return (monday2 - monday1).days / 7

    # 获取两个日期之间的月数差，计算方式为 date2 - date1
    @staticmethod
    def month_difference(date1, date2):
        return (date2.year - date1.year) * 12 + date2.month - date1.month

    # 根据日历星期数获取周开始时间和结束时间
    @classmethod
    def get_week_by_weeknum(cls, year, weeknum, tzinfo=None):
        # 组装1月4日的日期
        day_jan_4th = datetime.date(year, 1, 4)
        # 今年第一个日历星期的开始日期
        first_week_start = day_jan_4th - datetime.timedelta(days=day_jan_4th.isoweekday()-1)
        # 所求星期的开始时间
        week_start = datetime.datetime.combine(
            first_week_start + datetime.timedelta(weeks=weeknum-1),
            datetime.time(),
        )
        week_end = week_start + datetime.timedelta(weeks=1)
        return week_start, week_end

    @staticmethod
    def add_months(source_date, months):
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)
