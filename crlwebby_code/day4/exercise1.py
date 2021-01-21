num = int(input("请输入一个正整数： "))

flag = 0;

for i in range(2, num):
    if num % i == 0:
        flag =1
        break

if flag:
    print("不是素数")
else:
    print("是素数")