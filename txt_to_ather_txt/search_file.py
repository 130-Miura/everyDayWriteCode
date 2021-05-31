import os, glob

# 指定のパスディレクトリの下に存在するディレクトリのみを抽出する
path = "./for_loading/"
files = os.listdir(path)
folders = [f for f in files if not os.path.isfile(os.path.join(path, f))]

# 抽出されたディレクトリの下のファイルを取得
files = glob.glob(f"./for_loading/{folders[0]}/*")
for file in files:
    print(file)

