# smoking algorithm
# 冒泡序列
# 在一个序列中对比最后两个的数值，对比后把小的移动到前面，否则不动，运行多次后可把序列按顺序排好

l1 = [8,9,5,6,4,3,1,2,7,0,1,2]

def MySmoke():
    for n in range(len(l1)-1): # 循环列表的数值，l1[n]为列表数值；
        p = n+1 # 用于定位到y的位置，避免在传参时候执行计算发生错误；
        x = l1[n] # 获取对比值
        y = l1[p] # 获取被对比值
        if x >= y: # 如果对比有差异则执行互换位置；
            print("换")
            l1[n],l1[p] = l1[p],l1[n]
        else:
            print("PASS") # 否则跳过
    print(l1) # 遍历一遍后打印一次，用于观察变化；

for i in range(len(l1)): # 此步骤需要重复多次（具体取决于列表的总个数）；
    MySmoke() 


# print(l1[9-1])
