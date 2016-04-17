#!/usr/bin/ebv python

import json

def get_config(json_file):
    with open(json_file) as ec2_json:
        ec2_config = json.load(ec2_json)

    return ec2_config
