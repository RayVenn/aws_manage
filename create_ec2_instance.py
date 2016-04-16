#!/usr/bin/env python

import session
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="define the instance name",
        type=str, required=True)
parser.add_argument("-k", "--key", help="choose a key for this new instance",
        tyep=str, required=True)

args = parser.parse_args()
name = args.name
key  = args.key

s = session.create_session()
ec2 = s.resource('ec2')

instances = ec2.create_instances(
        ImageId='ami-d05e75b8',
        InstanceType='t2.micro',
        KeyName = key,
        SecurityGroupIds=['sg-eb8a4a92'],
        MinCount=1, MaxCount=1
        )


for index, instance in enumerate(instances):
    ec2.create_tags(
            Resources=[instance.id],
            Tags=[{'Key':'Name', 'Value':name}]
            )
