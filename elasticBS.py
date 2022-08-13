import boto3
elasticbeanstalk = boto3.client('elasticbeanstalk')
autoscaling=boto3.client('autoscaling')
my_list=[]
res1 = elasticbeanstalk.describe_environments()
for i in res1['Environments']:
    res2 = elasticbeanstalk.list_tags_for_resource(ResourceArn=i['EnvironmentArn'])
    for j in res2['ResourceTags']:
        if j['Key'] == 'Environment' and j['Value'] == 'dev':
            for k in res2['ResourceTags']:
                if k['Key'] == 'Name':
                 my_list=[k['Value']]
                 for key in my_list:
                    res3 = elasticbeanstalk.describe_environment_resources(EnvironmentName=key)
                    res4 = autoscaling.update_auto_scaling_group(
                                    AutoScalingGroupName=res3['EnvironmentResources']['AutoScalingGroups'][0]['Name'],
                                    MinSize=0,
                                    MaxSize=0
                                )                    
               
                    
