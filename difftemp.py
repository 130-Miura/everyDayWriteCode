# string カンマ区切りの最高気温,最低気温
# temps = "6, 2"

# 最高気温と最低気温の差を求める
# @temsp string "最高気温,最低気温" 
def difftemp(temps):
    maxtemp, mintemp = map(int, temps.split(','))
    print(maxtemp - mintemp)
    
difftemp(temps)