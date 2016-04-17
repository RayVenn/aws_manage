#!/usr/bin/env python

import subprocess
import session

def list_instances():
    s = session.create_session()
    ec2 = s.resource('ec2')

    instances = ec2.instances.all()
    instances_list = []

    # No., Name, Instance-id, Instance-type, State, DNS, Key
    string_format = '{:5}{:9}{:13}{:15}{:9}{:45}{:10}'

    print string_format.format('No.',
                               'Name',
                               'Instance-id',
                               'Instance-type',
                               'State',
                               'DNS',
                               'Key'
                               )

    for n, i in enumerate(instances):

        i_map = {}
        i_map['name']          = i.tags[0]['Value']
        i_map['instance-id']   = i.instance_id
        i_map['instance-type'] = i.instance_type
        i_map['state']         = i.state['Name']
        i_map['dns']           = i.public_dns_name
        i_map['key']           = i.key_name


        print string_format.format(str(n+1),
                                   i_map['name'],
                                   i_map['instance-id'],
                                   i_map['instance-type'],
                                   i_map['state'],
                                   i_map['dns'],
                                   i_map['key'],
                                   )

        instances_list.append(i_map)

    return instances
