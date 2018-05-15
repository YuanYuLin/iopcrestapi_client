#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def http_request(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def response_output(out_format, rsp):
    print rsp.status_code
    print rsp.text
    pprint.pprint(rsp.json())

def request_list(hostname, out_format):
    json = '{'
    json += '"name":"vm001", '
    json += '"rootfs":"/vms/vm001/rootfs", '
    json += '"fstab":"/vms/vm001/rootfs/fstab", '
    json += '"nettype":"veth", '
    json += '"nethwlink":"br1", '
    json += '"nethwaddr":"00:20:18:04:04:01", '
    json += '"ipaddress":"192.168.99.1", '
    json += '"gateway":"192.168.99.254"'
    json += '}'
    response_output(out_format, http_request(hostname, 'lxc_1', json))

    json = '{'
    json += '"name":"vm002", '
    json += '"rootfs":"/vms/vm002/rootfs", '
    json += '"fstab":"/vms/vm002/rootfs/fstab", '
    json += '"nettype":"veth", '
    json += '"nethwlink":"br1", '
    json += '"nethwaddr":"00:20:18:04:04:02", '
    json += '"ipaddress":"192.168.99.2", '
    json += '"gateway":"192.168.99.254"'
    json += '}'
    response_output(out_format, http_request(hostname, 'lxc_2', json))

    json = '{'
    json += '"name":"vm003", '
    json += '"rootfs":"/vms/vm003/rootfs", '
    json += '"fstab":"/vms/vm003/rootfs/fstab", '
    json += '"nettype":"veth", '
    json += '"nethwlink":"br1", '
    json += '"nethwaddr":"00:20:18:04:04:03", '
    json += '"ipaddress":"192.168.99.3", '
    json += '"gateway":"192.168.99.254"'
    json += '}'
    response_output(out_format, http_request(hostname, 'lxc_3', json))

    json = '{'
    json += '"name":"vm004", '
    json += '"rootfs":"/vms/vm004/rootfs", '
    json += '"fstab":"/vms/vm004/rootfs/fstab", '
    json += '"nettype":"veth", '
    json += '"nethwlink":"br1", '
    json += '"nethwaddr":"00:20:18:04:04:04", '
    json += '"ipaddress":"192.168.99.4", '
    json += '"gateway":"192.168.99.254"'
    json += '}'
    response_output(out_format, http_request(hostname, 'lxc_4', json))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

