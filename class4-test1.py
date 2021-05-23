number_list=[1,2,4,5,6,7,5,8,7,9,0,2,3,4,6,5]
print(number_list)
#增
number_list.insert(2,3)#增加
#删
del number_list[3]#删除
number_list.remove(9)#移除
number_list.clear()#清空
#改
number_list[3]=4.5#改变
#查
print(number_list.index(2))#查询位置
number_list.len#查询长度
number_list.if in#查询是否存在
print(number_list.count(5))#查询出现次数
input("5这个数字在number_list中出现的次数：{}.2出现的次数:{}".format(number_list.count(5),number_list.count(2)))#查询并输出出现次数
#序
number_list.sort()#升序排序
number_list.sort(reverse=True)#降序排序
number_list.reverse#逆序；反转
