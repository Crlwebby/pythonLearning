import math
r = float(input("请输入圆的半径:\n"))

circumference = 2 * math.pi * r 

area = math.pi * r ** 2

print("圆的周长是：%.3f\n圆的面积是：%.3f" % (circumference,area))