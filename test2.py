#测试散列值和密码是否对应
from werkzeug.security import generate_password_hash, check_password_hash
pw_hash = generate_password_hash('dog') # 为密码 dog 生成密码散列值
print(pw_hash) # 查看密码散列值
print(check_password_hash(pw_hash, 'dog')) # 检查散列值是否对应密码 dog
print(check_password_hash(pw_hash, 'cat')) # 检查散列值是否对应密码 cat
