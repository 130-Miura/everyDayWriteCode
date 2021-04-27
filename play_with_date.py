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

# タイムゾーン属性がNoneのnaiveなオブジェクトでutcの日時を取得
dt_now_utc_native = datetime.datetime.utcnow()
# print(dt_now_utc_native)

# UTC時間を取得して9時間足した値を取得
now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
# print(now)

# 今日の日付のdateオブジェクトを取得
d_today = datetime.date.today()
# print(d_today)
# print(type(d_today))

# dateオブジェクトはタイムゾーン属性を持たない。
# タイムゾーンを設定したdateオブジェクトを取得したい場合、
# datetimeオブジェクトにタイムゾーンを設定したうえでdateオブジェクトに変換する。
d_tz_jst = dt_now_jst_aware.date()
# print(dir(d_tz_jst))

# awareオブジェクトとnaiveオブジェクト

# awareオブジェクトはタイムゾーン情報を含んでいる。
# そのためほかのdatetimeオブジェクトとの相対関係を特定できる。

# naiveオブジェクトはタイムゾーン情報を含んでいない。
# そのためほかのdatetimeオブジェクトとの相対関係を特定できない。

# datetimeとtimeオブジェクトはタイムゾーン情報の属性（tzinfo）を追加できる。
# tzinfoには抽象クラスtzinfoのサブクラスのインスタンスを設定できる。
# tzinfoオブジェクトはUTC時間からのオフセット（基準時刻との差）やタイムゾーンの名前、
# サマータイムが実施されるかどうかの情報を保持している。

# print(datetime.date(2020, 11, 30))
# print(datetime.date(2020, 11, 30) - datetime.date(2019, 10, 3))
# print(type(datetime.date(2020, 11, 30) - datetime.date(2019, 10, 3)))
# print(datetime.date(2019, 10, 3) - datetime.date(2020, 11, 30))
# print(datetime.date(2019, 10, 3) + datetime.timedelta(days=424))
# print(datetime.date(2019, 10, 3) + datetime.timedelta(hours=24))

