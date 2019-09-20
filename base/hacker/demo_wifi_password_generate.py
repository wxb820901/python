import itertools
import time
key = '0123456789.qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+-=`~{[}]|\\:;\"\'<,>.?/'#密码包含这些字符
passwords = itertools.product(key, repeat=3)
f = open('password.txt', 'a')
for i in passwords:
    time.sleep(0.01)
    f.write("".join(i))
    f.write('\n')
f.close()