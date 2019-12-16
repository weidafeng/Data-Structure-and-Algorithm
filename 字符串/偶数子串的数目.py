
def count(lst):
    for i in range(len(lst)):
        if int(lst[i]) % 2 == 0 and lst[i] != '0': # 第i个数字是偶数
            for j in range(len(lst)):
                if lst[j] != '0': # 不以0开头
                    print(lst[j:i+1])

lst = '120034'
count(lst)