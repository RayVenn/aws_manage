#!/usr/bin/env python

import session
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="define the instance name",
        type=str, required=True, default=1)
args = parser.parse_args()
name = args.name

s = session.create_session()
ec2 = s.resource('ec2')

instances = ec2.create_instances(
        ImageId='ami-d05e75b8',
        InstanceType='t2.micro',
        KeyName = 'myself',
        SecurityGroupIds=['sg-eb8a4a92'],
        MinCount=1, MaxCount=1
        )


for index, instance in enumerate(instances):
    ec2.create_tags(
            Resources=[instance.id],
            Tags=[{'Key':'Name', 'Value':name}]
            )
