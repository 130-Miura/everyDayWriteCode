# ウィンドウズ環境で作成したテキストファイルの文字コードがcp932になる場合があるので（今回がそのケース）
# utf-8にエンコードして開く
file = open('txt/number_of_char_appearing.txt', encoding='utf-8')

# pythonという文字が現れる回数をカウントして出力
count = file.read().count('Python')
print(count)
file.close()