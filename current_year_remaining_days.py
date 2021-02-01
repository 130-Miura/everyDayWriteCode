import calendar
from datetime import datetime as dt

# 今年の残り日数を求める（今日を含まない）
def current_year_remaining_days():

    # 今日の日付を取得（形式：yyyy/mm//dd）
    time_str = dt.now().strftime('%Y/%m/%d')

    # 年、月、日をそれぞれ数値化して代入
    year, month, day = map(int, time_str.split('/'))
    result = 0
    for i in range(13 - month):

        # 今月から年末の月までの総日数を加算
        result += int(calendar.monthrange(year, i+1)[1])

    # 今日までの日数を減算
    result -= day

    return result

print(current_year_remaining_days())