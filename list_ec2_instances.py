#!/usr/bin/env python

import session

s = session.create_session()
ec2 = s.resource('ec2')

instances = ec2.instances.all()

for i in instances:
    print i.tags[0]['Value'], i.instance_id, i.instance_type, i.state['Name'], i.public_dns_name, i.public_ip_address, i.launch_time
