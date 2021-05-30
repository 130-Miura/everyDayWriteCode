from datetime import datetime as dt
r_path = './for_loading/2020_05/30_jirou.txt'
w_path = './for_writing/2020_05/30_jirou.txt'
hourly_pay = 700
def timedelta_to_int(td):
    m, d = divmod(td, 60)
    h, mi = divmod(m, 60)
    return (h, mi)

def add_info_about_working_hours_and_daily_pay(line):
    d, s, e = line.split()

    # 文字列をdatetime型に変換し、開始時間と終了時間の差（労働時間）を求める
    st = dt.strptime(s, '%H%M')
    et = dt.strptime(e, '%H%M')
    diff_h, diff_mi = timedelta_to_int((et - st).seconds)

    # 労働時間と時給から日給を求める
    dayly_pay = hourly_pay * diff_h
    if diff_mi == 30:
        dayly_pay += int(hourly_pay / 2)

    return f'{d} {s} {e} {format(diff_h, "0>2")}{diff_mi} {dayly_pay}\n'

with open(r_path) as rf, open(w_path, mode='w') as wf:
    for line in rf:
        txt = add_info_about_working_hours_and_daily_pay(line)
        wf.write(txt)


