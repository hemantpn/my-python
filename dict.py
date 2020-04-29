#!/home/ec2-user/my_app/env/bin/python
my_dict={}
print(my_dict,type(my_dict))
print(bool(my_dict))


my_dic={'fruit':'apple','animal':'cow','month':'jan'}    #key value should be in format
print(my_dic)

print(my_dic['animal'])
print(my_dic.get('animal'))   #both show same output

'''print(my_dic['three'])'''     #will show a error
print(my_dic.get('three'))  #it'll show none

print(my_dic.keys())
print(my_dic.values())
