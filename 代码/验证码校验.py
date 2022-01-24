#  验证码校验
# 用户登录网站经常需要输入验证码，验证码包含大小写字母和数字，随机出现。
# 用户输入验证码时不区分大小写，只要各字符出现顺序正确即可通过验证。
# 请写一个程序完成验证码的匹配验证，假设当前显示的验证码是'Qs2X'。
# 如果用户输入验证码正确，输出“验证码正确”，输入错误时输出“验证码错误，
# 请重新输入”

str = input()
if str.upper() == 'Qs2X'.upper():
#将用户输入字符串中的字母转为大写，给定字符串中字母转大写，比较二者是否相等
#两个字符串均转为大写 比较两者是否相等即可
    print('验证码正确')
else:
    print('验证码错误，请重新输入')