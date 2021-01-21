length = float(input("请输入长度(数字)：\n"))
unit = input("请输入单位(英寸|厘米)：\n")

if unit == '英寸':
    print("%.2f英寸 = %.2f厘米\n"% (length, length * 2.54))
elif unit == '厘米':
    print("%.2f厘米 = %.2f英寸\n"% (length, length / 2.54))
else:
    print("别皮了，输个对的\n")