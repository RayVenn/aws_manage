#!/usr/bin/env python

import list_ec2
import subprocess

instances_list = list_ec2.list_instances()

choose_no = input('Choose an instance: ')
choose_instance = instances_list[choose_no-1]

choose_dns = choose_instance['dns']
choose_key = '{}.pem'.format(choose_instance['key'])
login_user = 'ubuntu'


subprocess.call(['ssh', '-i', choose_key, choose_dns, '-l', login_user])
