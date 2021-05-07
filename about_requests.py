import requests

r = requests.get('https://api.github.com')

# レスポンスのステータスコードの確認
print(r.status_code)  # 200

# レスポンスヘッダーの確認
# print(r.headers['content-type']) # 'application/json; charset=utf8'

# レスポンスのエンコードを確認
# print(r.encoding) #  'utf-8'

# レスポンス内容をテキストで取得
# print(r.text)  # '{"type":"User"...'

# レスポンス内容をJSONで取得
# print(r.json()['current_user_url']) # {'private_gists': 419, 'total_private_repos': 77, ...}

# レスポンス内容をバイナリーで取得
# print(r.content) # b'{"type":"User"...'