#!/home/ec2-user/my_app/env/bin/python
index=0
for each_index in list(range(10)):
    ind=each_index
    suma=index+each_index
    print(f'cur_num:{each_index},pre num:{index},sum:{suma}')
    index=each_index
