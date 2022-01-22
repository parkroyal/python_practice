# %%
from datetime import date, timedelta
from typing import List
# %%

from datetime import date, timedelta
from typing import List
# 日期物件
class Date:
    def __init__(self, search_date:date = None) -> None:
        # 最新日報日期
        if search_date:
            self.nowDate = search_date
        else:
            if date.today().isoweekday() == 1:
                self.nowDate = date.today() - timedelta(days = 3)
            elif date.today().isoweekday() == 7:
                self.nowDate = date.today() - timedelta(days = 2)
            else:
                self.nowDate = date.today() - timedelta(days = 1)
    def get_week_date(self, type = "current_week"):
        if type == "current_week":
            # 找禮拜一
            start_date = self.nowDate
            while start_date.isoweekday() != 1:
                start_date -= timedelta(days=1)
            end_date = start_date + timedelta(days=6)
        else:
            start_date = self.nowDate - timedelta(days=7)
            while start_date.isoweekday() != 1:
                start_date -= timedelta(days=1)
            end_date = start_date + timedelta(days=6)

        return start_date, end_date
    def get_month_date(self, type = "current_month"):
        if type == "current_month":
            end_day = self.nowDate.replace(month=self.nowDate.month + 1) - timedelta(days = 1)
            start_day = self.nowDate.replace(day = 1)
        else:
            end_day = self.nowDate.replace(day = 1) - timedelta(days = 1)
            start_day = end_day.replace(day = 1)
        
        return start_day, end_day
