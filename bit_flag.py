# 2進数を利用したフラグ管理

# フラグが立っているかを確認する
# @target フラグが格納されている変数
# @flag 確認するフラグ
# @return フラグが立っていればTrue、降りていればFalseを返す
def check_flag(target, flag):
    return True if (target & flag) > 0 else False

# フラグが立っていない場合、フラグを立てる
# @return フラグが既に立っていればtargetの値をそのまま返し、立っていなければフラグを立てた値を返す
def up_flag(target, flag):

    # フラグが降りているか確認
    if check_flag(target, flag) == False:

        # フラグが降りている場合、フラグを立てる
        target |= flag
    return target

# フラグが立っていない場合、フラグを降ろす
def down_flag(target, flag):

    # フラグが立っているか確認
    if check_flag(target, flag) == True:

        # フラグが立っている場合、フラグを降ろす
        target -= target & flag
    return target

# 関数のテスト

# フラグの定義
FLAG_A = 1

# フラグの初期化
man = 0

# フラグの確認
assert check_flag(man, FLAG_A) == False

# FLAG_Aを立てる
man = up_flag(man, FLAG_A)

# フラグが立っているか確認
assert check_flag(man, FLAG_A) == True

# FLAG_Aを降ろす
man = down_flag(man, FLAG_A)

# フラグが降りているか確認
assert check_flag(man, FLAG_A) == False
