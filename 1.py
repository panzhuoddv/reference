def judge(list_name):
    list_model=['A','B','C','D']
    for i in list_model:
        if list_name.index(i)<2:
            list_name=list_name[list_name.index(i)+1:]
            if i == 'D':
                return True
        else:
            return False
#用以判断传入的列表是否以list_model的顺序传入，其中任意两个元素以及第一个元素之前可以加入一个未知的元素
