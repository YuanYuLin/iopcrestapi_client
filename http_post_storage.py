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
    key = 'storage_2'
    json = '{'
    json += '"dst":"/hdd/data",'
    json += '"enable":1,'
    json += '"formatable":0,'
    json += '"label":"RAID1",'
    json += '"src":"/dev/sda",'
    json += '"type":"btrfs_raid1",'
    json += '"visable":1'
    json += '}'

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

