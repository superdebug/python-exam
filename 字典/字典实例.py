#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

#--------用dict直接生成, 
name_age=(('xiaoli',33),('xiaowang',20),('xiaozhang',40))
a=dict(name_age)
b=dict(xiaoli=33,xiaowang=20,xiaozhang=40)

#--------如何将两个等长度的list合并成dict
text = 'c++ python shell ruby java javascript c'
code_num = [38599, 100931, 26153, 93142, 84275, 184220, 46843]

text_list=text.split(' ') #通过split转换成list类型
code_dict = dict(zip(text_list,code_num))

#--------key, keys, items, values
code_dict['python']
code_dict.keys() #返回所有关键字
code_dict.values() #返回所有的值
code_dict.items() #返回zip产生元组的list [('c', 46843), ('shell', 26153), ('java', 84275), ('python', 100931), ('javascript', 184220), ('c++', 38599), ('ruby', 93142)]

#--------get
#如果字典中的关键词不存在，则返回为空
a=code_dict.get('fortran',None)
#或者自定义错误类型
a=code_dict.get('fortran','It\'s not in ')
#------- ref and copy
a_ref = code_dict #引用 
a_copy = code_dict.copy() #浅拷贝 只拷贝第一层

#--------update, del, copy, clear
other_code = {'php':78014,'objective-c':34444}
code_dict.update(other_code)
del code_dict['c++']
a_ref
a_copy
a_ref.clear() #清空字典

#--------sort key and value
#列表解析的方式排序
[(k,a_copy[k]) for k in sorted(a_copy.keys())]

#深拷贝
#copy.deepcopy()


