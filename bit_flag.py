# フラグ管理
FLAG_A = 1
FLAG_B = 2
FLAG_C = 4
FLAG_D = 8
FLAG_E = 16
FLAG_F= 32
FLAG_G = 64
FLAG_H = 128

# フラグの初期化
man = 0

# Bのフラグを立てる
man |= FLAG_B
# print(man)

# Eのフラグを立てる
man |= FLAG_E
# print(man)

# Aのフラグが立っているかを確認する
if man & FLAG_A:
    print('Aのフラグが立っている')
else:
    print('Aのフラグは立っていない')
# print('AOK') if man & FLAG_A else print('ANG')

# Eのフラグが立っているかを確認する
if man & FLAG_E:
    print('Aのフラグが立っている')
else:
    print('Aのフラグは立っていない')

# BとEのフラグが立っている状態

# Bのフラグを下ろす
man -= man & FLAG_B
if man & FLAG_B:
    print('Bのフラグが立っている')
else:
    print('Bのフラグが立っていない')