print("请输入两个正整数，爷帮你算最大公约数和最小公倍数")

a = int(input("请输入a: "))
b = int(input("请输入b："))

gcd = 0;
# greatest common divisor
lcm = 0;
#lowest common multiple

if a > b:
    i = b
else:
    i = a
print(i)
while i != 0:
    if a%i == 0 and b%i ==0:
        gcd = i
        break
    i -= 1

lcm = a * b / gcd
print("%d和%d的最大公约数是：%d\t最小公倍数是%d" %(a, b, gcd, lcm))