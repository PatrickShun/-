# smoking algorithm
# 冒泡序列
# 在一个序列中对比最后两个的数值，对比后把小的移动到前面，否则不动，运行多次后可把序列按顺序排好

l1 = [8,9,5,6,4,3,1,2,7]

def MySmoke():
    for n in range(8): # 循环列表的数值，l1[n]为列表数值；
        p = n+1
        x = l1[n]
        y = l1[p]
        if x < y:
            print("换")
            l1[n],l1[p] = l1[p],l1[n]
        else:
            print("PASS")
    print(l1)
for i in range(len(l1)):
    MySmoke()


# print(l1[9-1])
