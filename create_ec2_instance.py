#!/usr/bin/env python

import argparse
import json
import session


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="define the instance name",
        type=str, required=True)
parser.add_argument("-k", "--key", help="choose a key for this new instance",
        type=str, required=True)

args = parser.parse_args()
name = args.name
key  = args.key

with open('ec2.json') as ec2_json:
    ec2_config = json.load(ec2_json)

s = session.create_session(ec2_config['region'])
ec2 = s.resource('ec2')

instances = ec2.create_instances(
        ImageId=ec2_config['image_id'],
        InstanceType=ec2_config['instance_type'],
        KeyName = key,
        SecurityGroupIds=ec2_config['group_ids'],
        MinCount=1, MaxCount=1
        )


for index, instance in enumerate(instances):
    ec2.create_tags(
            Resources=[instance.id],
            Tags=[{'Key':'Name', 'Value':name}]
            )
