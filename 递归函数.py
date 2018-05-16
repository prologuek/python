#递归函数的返回值
def calc(n,count):
    print(n,count)
    if count<5:
        return calc(n/2,count+1)
    else:
        return n#最里层以n返回上一层
    
a = calc(9,1)
print(a)
 