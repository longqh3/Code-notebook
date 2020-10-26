from importlib import reload
import random_passwd
prompt="\nPlease enter your student number:"
while True:#设置while循环，使随机数程序可以连续使用
    message=input(prompt)
    if message=='quit':#设置退出机制
        break
    else:
        reload(random_passwd)
        print("Your password is "+str(random_passwd.passwd))

    
