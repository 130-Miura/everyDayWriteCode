# ハッシュ化
import hashlib

# password = 'Password123'.encode('utf-8')
password = b'Password123'
print(password)
print(hashlib.md5(password).hexdigest())
print(hashlib.sha256(password).hexdigest())
print(hashlib.sha512(password).hexdigest())
