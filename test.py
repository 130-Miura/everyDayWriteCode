# ハッシュ化
import hashlib

password = 'Password123'.encode('utf-8')

print(hashlib.md5(password).hexdigest())
print(hashlib.sha256(password).hexdigest())
print(hashlib.sha512(password).hexdigest())
# 暗号化
# 複合化

