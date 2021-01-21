year = float(input("请输入年份:\n"))

logic = year%400==0 or year%100 !=0 and year %4 ==0
judge = {True:'是闰年',False:'不是闰年'}
print("%d年 %s" % (year, str(judge[logic])))