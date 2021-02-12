# open(ファイル名, オプション, 文字エンコード)
# オプション例
# w:書き込み専用、ファイルが存在すれば上書き
# r:読み込み専用
# x:新規ファイル作成、ファイルが存在すればエラー
# a:書き込み専用、ファイルが存在すれば末行に追加
# b:バイナリモードで開く

# f = open('open_test/test.txt', 'w', encoding='utf-8')
# f.write('ファイル作成, 書き込みテスト\n')
# f.close()

# try:
#     f = open('open_test/test.txt', 'x', encoding='utf-8')
#     f.write('新規ファイル作成, ファイル存在する場合のエラー出力テスト\n')
#     f.close()
# except FileExistsError:
#     print('ファイルが存在します。\n新規ファイルが作成できませんでした。\n')

# ファイル名をランダム生成し、ファイルが存在しない場合にファイルを作成する。
# そのファイル名が既に存在する場合はエラーメッセージを返す

import random

r = random.randint(1, 100)

# ファイル名の生成
path = 'open_test/open_func' + str(r) + '.txt'

try:
    # ファイルが存在しない場合、ファイルを作成
    f = open(path, 'x', encoding='utf-8')
    f.close()

# ファイルが存在する場合、エラーメッセージを出力する
except FileExistsError:
    print('ファイルが存在します。\n新規ファイルが作成できませんでした。\n')

