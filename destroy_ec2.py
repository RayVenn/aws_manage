#!/usr/bin/env python

import session
import list_ec2

s = session.create_session()
ec2 = s.client('ec2')

ec2.terminate_instances(InstanceIds=['i-40d109dd'])
