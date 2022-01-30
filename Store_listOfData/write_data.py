import boto3
import csv

client = boto3.client('iam')

id= 0

csv_file=open("datarecord.csv","w",newline='')
csv_write=csv.writer(csv_file)
csv_write.writerow(["ID","RoleName",'CreateDate',"Description"])

for each in client.list_roles(MaxItems=19)['Roles']:
    print(id, each['RoleName'],each['CreateDate'],each['Description'])
    csv_write.writerow([id,each['RoleName'],each['CreateDate'],each['Description']])
    id += 1
csv_file.close()