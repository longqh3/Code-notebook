#coding=utf-8
import random
import string

digits=string.digits#string_数字
uppercase=string.ascii_uppercase#string_大写字母
lowercase=string.ascii_lowercase#string_小写字母
special_chr='@#$%%^&'#特殊符号

passwd_num=random.sample(digits,1)#随机选择一位数字作为密码中的数字部分
passwd_special_chr=random.sample(special_chr,1)#随机选择一个特殊字符
uppercase_num=random.randint(1,6)#随机选择1~6位字母大写字母
lowercase_num=6-uppercase_num#小写字母个数由大写字母个数决定
password=passwd_num+passwd_special_chr+random.sample(uppercase,uppercase_num)+random.sample(lowercase,lowercase_num)#四部分合成密码内容
random.shuffle(password)#密码内容随机排列
passwd="".join(password)#将随机组合后的密码内容合并为最终密码

