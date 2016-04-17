#/usr/bin/env python

import boto3

def create_session(region_name, profile_name='myself'):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session
