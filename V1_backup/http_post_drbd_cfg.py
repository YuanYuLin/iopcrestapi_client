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
    drbd_cfg = '{'
    drbd_cfg += '"ipaddress_local":"192.168.155.1", '
    drbd_cfg += '"macaddress_local":"00:20:18:03:13:00", '
    drbd_cfg += '"hostname_local":"qemu1", '
    drbd_cfg += '"drbd_local":"/dev/drbd0", '
    drbd_cfg += '"disk_local":"/dev/sdb", '
    drbd_cfg += '"hostname_remote":"qemu2", '
    drbd_cfg += '"drbd_remote":"/dev/drbd0", '
    drbd_cfg += '"disk_remote":"/dev/sdb", '
    drbd_cfg += '"ipaddress_remote":"192.168.155.2", '
    drbd_cfg += '"macaddress_remote":"00:20:18:03:13:01"'
    drbd_cfg += '}'
    response_output(out_format, http_request(hostname, 'drbd_cfg', drbd_cfg))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

