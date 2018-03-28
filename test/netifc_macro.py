#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def add_br0(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"add_bridge", "bridge":"br0"}'
    rsp=requests.post(url, data=payload)
    return rsp

def add_br1(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"add_bridge", "bridge":"br1"}'
    rsp=requests.post(url, data=payload)
    return rsp

def add_br0_eth0(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"add_ifc", "bridge":"br0", "ifc":"eth0"}'
    rsp=requests.post(url, data=payload)
    return rsp

def add_br1_eth0_100(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"add_ifc", "bridge":"br1", "ifc":"eth0.100"}'
    rsp=requests.post(url, data=payload)
    return rsp

def add_vlan_eth0_100(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"add_vlan", "ifc":"eth0", "tag":100}'
    rsp=requests.post(url, data=payload)
    return rsp

def http_request(url_prefix):
    rsp = add_br0(url_prefix)
    rsp = add_br1(url_prefix)
    rsp = add_vlan_eth0_100(url_prefix)
    rsp = add_br0_eth0(url_prefix)
    rsp = add_br1_eth0_100(url_prefix)
    return rsp

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    url="http://" + hostname + "/api"
    rsp=http_request(url)

    if rsp.status_code == requests.codes.ok :
        pprint.pprint(rsp.json())
    else :
        print "error" + str(rsp.status_code)
    
