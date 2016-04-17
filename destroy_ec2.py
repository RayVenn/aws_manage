#!/usr/bin/env python

import list_ec2
import parse_ec2
import session

instances_list = list_ec2.list_instances()

choose_no = input('Choose an instance to terminate: ')
choose_instance = instances_list[choose_no-1]
choose_id = choose_instance['instance-id']

ec2_config = parse_ec2.get_config('ec2.json')

s = session.create_session(ec2_config['region'])

ec2 = s.client('ec2')
ec2.terminate_instances(InstanceIds=[choose_id])
