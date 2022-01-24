def fibonacci(month):
    if month == 0 or month == 1:
        return 1
    else:
        return fibonacci(month-1) + fibonacci(month-2)
# 测试经过12个月份后的兔子对数
result = fibonacci(12)
print(result)
