#!/home/ec2-user/my_app/env/bin/python
import os
import datetime
def main():
    path=os.listdir("/home/ec2-user/ansible-environments/aws")
    for eachdir  in path:
        cst_inventory=os.path.join("/home/ec2-user/ansible-environments/aws",eachdir)
        if os.path.isdir(cst_inventory):
           inv_data=os.listdir(cst_inventory) 
           for each_data in inv_data:
               sql_backup_path=os.path.join(cst_inventory,each_data)
               if os.path.isfile(sql_backup_path) and each_data.endswith(".sql"):   
                  file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(sql_backup_path))
                  today=datetime.datetime.now()
                  diff_days=(today-file_cre_date).days
                  if diff_days >= 0 and diff_days < 1:
                     os.remove(sql_backup_path)

if __name__=="__main__":  
    main()
