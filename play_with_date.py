import time
# 現在のUNIX時間（エポック秒）を取得
ut = time.time()
# print(ut)
# print(type(ut))

# 現在日時（日付と時刻）のdatetimeオブジェクトを取得
import datetime
dt_now = datetime.datetime.now()
# print(dt_now)
# print(type(dt_now))

# 取得したdatetimeオブジェクトの表示形式の変更
# print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
# print(dt_now.strftime('%Y/%m/%d %H:%M:%S'))
# print(dt_now.isoformat())
# print(type(dt_now.isoformat()))

# int型で年や月など単位ごとに取得
# print(dt_now.year)
# print(dt_now.month)
# print(dt_now.day)
# print(dt_now.hour)
# print(dt_now.minute)
# print(dt_now.second)
# print(dt_now.microsecond)
# print(type(dt_now.year))

# 初期値はタイムゾーンがNone
# print(dt_now.tzinfo)

# タイムゾーンを設定する
# datetime.now()の引数にタイムゾーンオブジェクトを指定。
# タイムゾーンを考慮されたawareなオブジェクトを取得
# dt_now_timezone_utc = datetime.datetime.now(datetime.timezone.utc)
# print(dt_now_timezone_utc)
# print(dt_now_timezone_utc.tzinfo)

# タイムゾーンをjst(日本標準時)に設定して日時を取得
DIFF_JST_FROM_UTC = 9
dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=DIFF_JST_FROM_UTC)))
# print(dt_now_jst_aware)
# print(dt_now)

# UTC時間を取得して9時間足した値を取得
now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
# print(now)