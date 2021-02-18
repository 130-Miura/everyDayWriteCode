# ハッシュ化
import hashlib
from random_chars_create import random_str

# password = 'Password123'.encode('utf-8')
password = b'Password123'
# print(hashlib.md5(password).hexdigest())
# print(hashlib.sha256(password).hexdigest())
# print(hashlib.sha512(password).hexdigest())

# 12桁のランダムなソルト文字列を生成しバイト文字列に変換
solt = random_str(12).encode()

# パスワードとソルトを結合
password += solt

# 結合したパスワードをハッシュ化
print(hashlib.md5(password).hexdigest())
print(hashlib.sha256(password).hexdigest())
print(hashlib.sha512(password).hexdigest())

# ランダム生成したソルトをハッシュ化したパスワードと一緒に保管しておけば
# 入力されたパスワードと保持していたソルト文字列を結合して一致確認可能