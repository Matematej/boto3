import boto3
ec2 = boto3.resource('ec2')

filter_ebs = {"Name":"attachment.delete-on-termination","Values":["true"]}

for each_volume in ec2.volumes.filter(Filters=[filter_ebs]):
	if not each_volume.encrypted:
		#print(dir(each_volume))
		print("Deleting volumes")
		each_volume.delete()
print("volumes delted")

