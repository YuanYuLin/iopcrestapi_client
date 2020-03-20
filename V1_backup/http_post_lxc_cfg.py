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
    for idx in [1, 2, 3, 4, 5, 6]:
        key="lxc_%d" % idx
        json = '{'
        json += '"enable":0, '
        json += '"name":"vm%03d", ' % idx
        json += '"rootfs":"/hdd/sdb/vm%03d", ' % idx
        json += '"fstab":"/hdd/sdb/vm%03d.fstab", ' % idx
        json += '"nettype":"veth", '
        json += '"nethwlink":"br0", '
        json += '"nethwaddr":"00:19:82:03:21:%02d", ' % idx
        json += '"ipaddress":"192.168.155.%d", ' % idx
        json += '"gateway":"192.168.155.254"'
        json += '}'
        print key
        print json
        response_output(out_format, http_request(hostname, key, json))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

