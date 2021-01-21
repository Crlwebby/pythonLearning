import math
print("请输入三条边的边长，爷帮你算面积")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a + b < c or a + c < b or b + c < a:
    print("爬爬爬，别当爷傻子\n")
else:
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("面积是：%.2f" %S)