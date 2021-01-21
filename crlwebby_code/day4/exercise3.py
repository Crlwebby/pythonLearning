print("说！想要多少星星，爷给你！")
num = int(input("输入行数："))
i = num
string='*'

while i != 0 :
    print(i * string)
    i -=1

i = num
while i != 0:
    print((i - 1)*' '+ (num - i + 1)*string)
    i -=1

i = num 
while i != 0:
    print((i - 1) * ' ' + (2 * (num - i) - 1) * '*' + (i - 1) * ' ')
    i -=1
