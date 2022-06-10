# 选择性排序，线性搜索序列，找到最小值，并移动到第一位；
from pip import main



l1 = [2,1,6,4,5,8,9,5,7]

for i in range(len(l1)):
    x = min(l1[i::]) # 获取列表的最小值
    indX = l1.index(x) # 获取最小值在列表的位置
    print(l1[indX])

# print(l1)


