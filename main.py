def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

try:
    year = int(input("请输入年份: "))
    print(is_leap_year(year))
except ValueError:
    print("输入无效，年份必须是整数。")
