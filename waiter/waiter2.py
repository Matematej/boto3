import boto3
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
waiter = client.get_waiter('instance_running')
Ids_EC2 = []
filter_subnet = {'Name': 'subnet-id', 'Values': ['subnet-b9178f98']}
filter_state = {'Name': 'instance-state-name', 'Values': ['stopped']}
for each in client.describe_instances(Filters=[filter_state])['Reservations']:
    for each2 in each['Instances']:
        Ids_EC2.append(each2['InstanceId'])
    print(Ids_EC2)

print("starting EC2s")        
response = client.start_instances(InstanceIds=Ids_EC2)
waiter.wait(Filters=[filter_subnet], InstanceIds = Ids_EC2)
print("EC2s are runnig")